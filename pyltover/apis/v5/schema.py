from pydantic import BaseModel, Field


class MatchMetadata(BaseModel):
    data_version: str = Field(alias="dataVersion")
    match_id: str = Field(alias="matchId")
    participants: list[str]


class MatchParticipant(BaseModel):
    pass


class MatchBan(BaseModel):
    champion_id: int = Field(alias="championId")
    pick_turn: int = Field(alias="pickTurn")


class MatchObjectives(BaseModel):
    first: bool
    kills: int


class MatchTeam(BaseModel):
    bans: list[MatchBan]
    objectives: MatchObjectives
    team_id: int = Field(alias="teamId")
    win: bool


class MatchInfo(BaseModel):
    end_of_game_result: str = Field(alias="endOfGameResult")
    game_creation: int = Field(alias="gameCreation")
    game_duration: int = Field(alias="gameDuration")
    game_end_timestamp: int = Field(alias="gameEndTimestamp")
    game_id: int = Field(alias="gameId")
    game_mode: str = Field(alias="gameMode")
    game_name: str = Field(alias="gameName")
    game_start_timestamp: int = Field(alias="gameStartTimestamp")
    game_type: str = Field(alias="gameType")
    game_version: str = Field(alias="gameVersion")
    map_id: int = Field(alias="mapId")
    participants: list[MatchParticipant]
    platform_id: str = Field(alias="platformId")
    queue_id: int = Field(alias="queueId")
    teams: list[MatchTeam]
    tournament_code: str = Field(alias="tournamentCode")


class Match(BaseModel):
    metadata: MatchMetadata
    info: MatchInfo
