from typing import Optional
from pydantic import BaseModel, Field

from pyltover.schema import Champion, ChampionWithDetails


class ChampionRotation(BaseModel):
    free_champion_ids: list[int] = Field(alias="freeChampionIds")
    free_champion_ids_for_new_players: list[int] = Field(alias="freeChampionIdsForNewPlayers")

    free_champions: Optional[list[Champion]] = None
    free_champions_for_new_players: Optional[list[ChampionWithDetails]] = None

    def set_free_champions(self, champions: list[Champion]):
        self.free_champions = champions

    def set_free_champions_for_new_players(self, champions: list[Champion]):
        self.free_champions_for_new_players = champions
