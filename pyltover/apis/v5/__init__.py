from pyltover.base import BasePyltover
from pyltover.apis.errors import translate_error
from pyltover.apis.v5 import schema
from pyltover.apis.v5 import urls


class Pyltover(BasePyltover):
    def __init__(self, server_addr: str, riot_token: str):
        super().__init__(riot_token)
        self.server_addr = server_addr

    async def get_list_of_match_ids_by_puuid(self, puuid: str) -> list[str]:
        url = urls.get_list_of_match_ids_by_puuid.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            raise translate_error(resp.json())

    async def get_match_by_id(self, puuid: str) -> schema.Account:
        url = urls.get_match_by_id.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            account = resp.json()
            return schema.Account(
                gameName=account["gameName"],
                puuid=account["puuid"],
                tagLine=account["tagLine"],
            )
        else:
            raise translate_error(resp.json())

    async def get_match_timeline_by_id(self, puuid: str) -> schema.Account:
        url = urls.get_match_timeline_by_id.format(server_addr=self.server_addr, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            account = resp.json()
            return schema.Account(
                gameName=account["gameName"],
                puuid=account["puuid"],
                tagLine=account["tagLine"],
            )
        else:
            raise translate_error(resp.json())
