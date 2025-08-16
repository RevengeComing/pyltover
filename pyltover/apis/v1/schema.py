from pydantic import BaseModel, Field


__all__ = ("Account", "ActiveShards", "ActiveRegion")


class Account(BaseModel):
    puuid: str
    game_name: str = Field(alias="gameName")
    tag_line: str = Field(alias="tagLine")

    def __repr__(self):
        return f"[Account details: <puuid: {self.puuid}, game_name: {self.game_name}, tag_line: {self.tag_line}>]"


class ActiveShards(BaseModel):
    puuid: str
    game: str
    active_shard: str = Field(alias="activeShard")


class ActiveRegion(BaseModel):
    puuid: str
    game: str
    region: str
