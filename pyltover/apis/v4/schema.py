from typing import Optional
from pydantic import BaseModel, Field
from pyltover.schema import Champion, ChampionWithDetails


class NextSeasonMilestone(BaseModel):
    require_grade_counts: dict = Field(alias="requireGradeCounts")
    reward_marks: int = Field(alias="rewardMarks")
    bonus: bool
    total_games_requires: int = Field(alias="totalGamesRequires")


class ChampionMastery(BaseModel):
    puuid: str
    champion_id: int = Field(alias="championId")
    champion_level: int = Field(alias="championLevel")
    champion_points: int = Field(alias="championPoints")
    last_play_time: int = Field(alias="lastPlayTime")
    champion_points_since_last_level: int = Field(alias="championPointsSinceLastLevel")
    champion_points_until_next_level: int = Field(alias="championPointsUntilNextLevel")
    mark_required_for_next_level: int = Field(alias="markRequiredForNextLevel")
    tokens_earned: int = Field(alias="tokensEarned")
    champion_season_milestone: int = Field(alias="championSeasonMilestone")
    milestone_grades: list[str] = Field(None, alias="milestoneGrades")
    next_season_milestone: NextSeasonMilestone = Field(alias="nextSeasonMilestone")

    champion: Optional[Champion] = None
    champion_with_details: Optional[ChampionWithDetails] = None

    def set_champion_info(self, champion: Champion):
        self.champion = champion

    def set_champion_details(self, champion_with_details: ChampionWithDetails):
        self.champion_with_details = champion_with_details


class MiniSeries(BaseModel):
    losses: int
    progress: str
    target: int
    wins: int


class LeagueItem(BaseModel):
    fresh_blood: bool = Field(alias="freshBlood")
    wins: int  # Winning team on Summoners Rift.
    mini_series: Optional[MiniSeries] = Field(None, alias="miniSeries")
    inactive: bool
    veteran: bool
    hot_streak: bool = Field(alias="hotStreak")
    rank: str
    league_points: int = Field(alias="leaguePoints")
    losses: int  # Losing team on Summoners Rift.
    puuid: str


class League(BaseModel):
    league_id: str = Field(alias="leagueId")
    entries: list[LeagueItem]
    tier: str
    name: str
    queue: str


class LeagueEntry(BaseModel):
    league_id: str = Field(alias="leagueId")
    puuid: str  # Player's encrypted puuid.
    queue_type: str = Field(alias="queueType")
    tier: str
    rank: str  # The player's division within a tier.
    league_points: int = Field(alias="leaguePoints")
    wins: int  # Winning team on Summoners Rift.
    losses: int  # Losing team on Summoners Rift.
    hot_streak: bool = Field(alias="hotStreak")
    veteran: bool
    fresh_blood: bool = Field(alias="freshBlood")
    inactive: bool
    mini_series: Optional[MiniSeries] = Field(None, alias="miniSeries")
