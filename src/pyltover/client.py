import httpx

from pyltover import servers
from pyltover.apis import v1
from pyltover.base import BasePyltover


class Pyltover(BasePyltover):
    def __init__(self, server_addr: servers.ServerAddress, riot_token: str):
        super().__init__(
            server_addr,
            riot_token,
            httpx.AsyncClient(headers={"X-Riot-Token": riot_token}),
        )
        self.v1 = v1.Pyltover(self.server_addr, self.riot_token, self.async_client)
        # self.v2 = v2.Pyltover(self.server_addr, self.riot_token, self.async_client)
        # self.v3 = v3.Pyltover(self.server_addr, self.riot_token)
        # self.v4 = v4.Pyltover(self.server_addr, self.riot_token)
        # self.v5 = v5.Pyltover(self.server_addr, self.riot_token)
