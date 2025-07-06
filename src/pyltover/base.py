import httpx

from pyltover import servers


class BasePyltover:
    def __init__(
        self,
        server_addr: servers.ServerAddress,
        riot_token: str,
        async_client: httpx.AsyncClient = None,
    ):
        self.riot_token = riot_token
        self.server_addr = server_addr

        self.async_client = async_client

        self.ddragon_version = "15.13.1"

    async def init(self):
        _ = await self._fetch_ddragon_champion_json(
            f"https://ddragon.leagueoflegends.com/cdn/{self.ddragon_version}/data/en_US/champion.json"
        )

    async def _fetch_ddragon_champion_json(self):
        pass
