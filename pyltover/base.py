import json
import logging
from typing import Any, NoReturn

import httpx
from pydantic import BaseModel as PydanticBaseModel, TypeAdapter, ValidationError

from pyltover.apis.errors import translate_error
from pyltover.schema import ChampionWithDetails, ChampionWithDetailsResponse, ChampionsDB


logger = logging.getLogger(__name__)


class BasePyltover:
    ddragon_version = "15.15.1"
    champions_db = None
    async_client = None
    ddragon_cdn_address = "ddragon.leagueoflegends.com"

    def __init__(
        self,
        riot_token: str,
    ):
        self.riot_token = riot_token

        BasePyltover.async_client = httpx.AsyncClient(headers={"X-Riot-Token": self.riot_token})
        BasePyltover.champion_details_db = {"by_id": {}, "by_name": {}}

    @classmethod
    async def init_champions_db(cls):
        """preloads champions data"""
        BasePyltover.champions_db = await cls._fetch_ddragon_champions_json()

    async def get_champion_details(self, id: int) -> ChampionWithDetails:
        if not self.champion_details_db["by_id"].get(id):
            name = self.champions_db.get_champion_by_id(id).name
            champion_details = await self._fetch_ddragon_champion_details(name)
            self.champion_details_db["by_id"][id] = champion_details
            self.champion_details_db["by_name"][name] = champion_details
        return self.champion_details_db["by_id"][id]

    async def get_champion_details_by_name(self, name: str) -> ChampionWithDetails:
        if not self.champion_details_db["by_id"].get(name):
            champion_details = await self._fetch_ddragon_champion_details(name)
            self.champion_details_db["by_name"][name] = champion_details
            self.champion_details_db["by_id"][champion_details.id] = champion_details
        return self.champion_details_db["by_name"][name]

    @classmethod
    async def _fetch_ddragon_champions_json(cls) -> ChampionsDB:
        url = f"https://{BasePyltover.ddragon_cdn_address}/cdn/{cls.ddragon_version}/data/en_US/champion.json"
        resp = await BasePyltover.async_client.get(url)
        return cls._model_validate_json(ChampionsDB, resp.content, "ddragon._fetch_ddragon_champions_json", resp)

    @classmethod
    async def _fetch_ddragon_champion_details(cls, name: str) -> ChampionWithDetails:
        url = f"https://{BasePyltover.ddragon_cdn_address}/cdn/{cls.ddragon_version}/data/en_US/champion/{name}.json"
        resp = await cls.async_client.get(url)
        champion_response = cls._model_validate_json(
            ChampionWithDetailsResponse, resp.content, "ddragon._fetch_ddragon_champion_details", resp
        )
        return champion_response.data[name]

    @staticmethod
    def _response_json(resp: httpx.Response, api_name: str) -> dict:
        try:
            return resp.json()
        except json.decoder.JSONDecodeError:
            logger.exception(
                "JSON decode error in %s (status=%s, url=%s). Response content: %r",
                api_name,
                resp.status_code,
                resp.url,
                resp.text,
            )
            raise

    def _raise_riot_api_error(self, resp: httpx.Response, api_name: str) -> NoReturn:
        raise translate_error(self._response_json(resp, api_name))

    @staticmethod
    def _is_json_decode_validation_error(error: ValidationError) -> bool:
        return any(err.get("type") == "json_invalid" for err in error.errors())

    @staticmethod
    def _model_validate_json(
        model: type[PydanticBaseModel], content: bytes | str, api_name: str, resp: httpx.Response | None = None
    ) -> Any:
        try:
            return model.model_validate_json(content)
        except ValidationError as error:
            if BasePyltover._is_json_decode_validation_error(error):
                status_code = resp.status_code if resp else "n/a"
                url = resp.url if resp else "n/a"
                body = resp.text if resp else content
                logger.exception(
                    "JSON decode error in %s (status=%s, url=%s). Response content: %r",
                    api_name,
                    status_code,
                    url,
                    body,
                )
            raise

    @staticmethod
    def _adapter_validate_json(
        adapter: TypeAdapter, content: bytes | str, api_name: str, resp: httpx.Response | None = None
    ) -> Any:
        try:
            return adapter.validate_json(content)
        except ValidationError as error:
            if BasePyltover._is_json_decode_validation_error(error):
                status_code = resp.status_code if resp else "n/a"
                url = resp.url if resp else "n/a"
                body = resp.text if resp else content
                logger.exception(
                    "JSON decode error in %s (status=%s, url=%s). Response content: %r",
                    api_name,
                    status_code,
                    url,
                    body,
                )
            raise
