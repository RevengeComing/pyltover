import httpx

from pyltover.schema import ChampionWithDetails, ChampionWithDetailsResponse, ChampionsDB


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
        return ChampionsDB.model_validate_json(resp.content)

    @classmethod
    async def _fetch_ddragon_champion_details(cls, name: str) -> ChampionWithDetails:
        url = f"https://{BasePyltover.ddragon_cdn_address}/cdn/{cls.ddragon_version}/data/en_US/champion/{name}.json"
        resp = await cls.async_client.get(url)
        return ChampionWithDetailsResponse.model_validate_json(resp.content).data[name]
