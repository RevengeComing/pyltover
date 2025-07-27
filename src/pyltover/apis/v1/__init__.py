from typing import Literal, Union
from pyltover.base import BasePyltover
from pyltover import servers
from pyltover.apis.errors import translate_error
from pyltover.apis.v1 import schema
from pyltover.apis.v1 import urls

Union[
    servers.PlatformRoutingValues,
    servers.RegionalRoutingValues,
    Literal[servers.esports_server],
]


class Pyltover(BasePyltover):
    def __init__(self, server_addr: str, riot_token: str):
        super().__init__(riot_token)
        self.server_addr = server_addr

    async def get_account_by_puuid(self, puuid: str) -> schema.Account:
        url = urls.get_account_by_puuid.format(server_addr=self.server_addr, puuid=puuid)
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

    async def get_account_by_riot_id(self, tag_line: str, game_name: str) -> schema.Account:
        url = urls.get_account_by_riot_id.format(server_addr=self.server_addr, tag_line=tag_line, game_name=game_name)
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

    async def get_active_shard_for_player(self, game: str, puuid: str) -> schema.ActiveShards:
        url = urls.get_active_shard_for_player.format(server_addr=self.server_addr, game=game, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            active_shard = resp.json()
            return schema.ActiveShards(
                puuid=active_shard["puuid"],
                game=active_shard["game"],
                activeShard=active_shard["activeShard"],
            )
        else:
            raise translate_error(resp.json())

    async def get_active_region(self, game: str, puuid: str) -> schema.ActiveRegion:
        url = urls.get_active_region.format(server_addr=self.server_addr, game=game, puuid=puuid)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            account = resp.json()
            return schema.ActiveRegion(game=account["game"], puuid=account["puuid"], region=account["region"])
        else:
            raise translate_error(resp.json())

    async def get_account_by_access_token(self) -> schema.Account:
        url = urls.get_account_by_access_token.format(server_addr=self.server_addr)
        resp = await Pyltover.async_client.get(url)
        if resp.status_code == 200:
            account = resp.json()
            return schema.ActiveRegion(game=account["game"], puuid=account["puuid"], region=account["region"])
        else:
            raise translate_error(resp.json())
