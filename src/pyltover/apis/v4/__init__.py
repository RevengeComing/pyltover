from typing import Literal, Union
from pyltover.base import BasePyltover
from pyltover import servers

Union[
    servers.PlatformRoutingValues,
    servers.RegionalRoutingValues,
    Literal[servers.esports_server],
]


class Pyltover(BasePyltover):
    async def get_all_champion_mastery(self, puuid: str, mode: Literal["basic", "partial", "full"] = "basic"):
        pass

    async def get_champion_mastery(
        self,
        puuid: str,
        champion_id,
        mode: Literal["basic", "partial", "full"] = "basic",
    ):
        pass

    async def get_top_champion_mastery_by_count(self, puuid: str, mode: Literal["basic", "partial", "full"] = "basic"):
        pass

    async def get_total_champion_mastery_score(self, puuid: str, mode: Literal["basic", "partial", "full"] = "basic"):
        pass
