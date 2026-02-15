from pyltover.base import BasePyltover
from pyltover.apis.v3.schema import ChampionRotation
from pyltover.apis.v3 import urls


class Pyltover(BasePyltover):
    def __init__(self, server_addr: str, riot_token: str):
        super().__init__(riot_token)
        self.server_addr = server_addr

    async def get_champion_rotaions(self, load_champ: bool = False):
        url = urls.get_champion_rotaions.format(server_addr=self.server_addr)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            champion_rotation = self._model_validate_json(
                ChampionRotation, resp.content, "v3.get_champion_rotaions", resp
            )
            if load_champ:
                free_champions = []
                for champion_id in champion_rotation.free_champion_ids:
                    champion = BasePyltover.champions_db.get_champion_by_id(champion_id)
                    free_champions.append(champion)
                champion_rotation.set_free_champions(free_champions)

                free_champions_for_new_players = []
                for champion_id in champion_rotation.free_champion_ids_for_new_players:
                    champion = BasePyltover.champions_db.get_champion_by_id(champion_id)
                    free_champions_for_new_players.append(champion)
                champion_rotation.set_free_champions_for_new_players(free_champions)
            return champion_rotation
        else:
            self._raise_riot_api_error(resp, "v3.get_champion_rotaions")
