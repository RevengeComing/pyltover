from pydantic import TypeAdapter

from pyltover.apis.errors import translate_error
from pyltover.base import BasePyltover
from pyltover.apis.v4 import urls
from pyltover.apis.v4.schema import ChampionMastery


ChampionMasteries = TypeAdapter(list[ChampionMastery])


class Pyltover(BasePyltover):
    def __init__(self, server_addr: str, riot_token: str):
        super().__init__(riot_token)
        self.server_addr = server_addr

    async def get_all_champion_mastery(self, puuid: str, load_champ: bool = False):
        url = urls.get_all_champion_mastery.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            champion_mastery = ChampionMasteries.validate_json(resp.content)
            if load_champ:
                for mastery in champion_mastery:
                    champion = BasePyltover.champions_db.get_champion_by_id(mastery.champion_id)
                    mastery.set_champion_info(champion)
            return champion_mastery
        else:
            raise translate_error(resp.json())

    async def get_champion_mastery(self, puuid: str, champion_id: str, load_champ: bool = False) -> ChampionMastery:
        url = urls.get_champion_mastery.format(server_addr=self.server_addr, puuid=puuid, champion_id=champion_id)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            champion_mastery = ChampionMastery.model_validate_json(resp.content)
            if load_champ:
                champion = BasePyltover.champions_db.get_champion_by_id(champion_mastery.champion_id)
                champion_mastery.set_champion_info(champion)
            return champion_mastery
        else:
            raise translate_error(resp.json())

    async def get_top_champion_mastery_by_count(self, puuid: str, count: int, load_champ: bool = False):
        url = urls.get_top_champion_mastery_by_count.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url, params={"count": count})
        if resp.status_code == 200:
            champion_mastery = ChampionMasteries.validate_json(resp.content)
            if load_champ:
                for mastery in champion_mastery:
                    champion = BasePyltover.champions_db.get_champion_by_id(mastery.champion_id)
                    mastery.set_champion_info(champion)
            return champion_mastery
        else:
            raise translate_error(resp.json())

    async def get_total_champion_mastery_score(self, puuid: str) -> int:
        url = urls.get_total_champion_mastery_score.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            return int(resp.text)
        else:
            raise translate_error(resp.json())
