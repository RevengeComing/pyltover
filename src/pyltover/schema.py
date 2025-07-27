from typing import Optional
from pydantic import BaseModel, Field
from decimal import Decimal


class ChampionNotFound(Exception):
    pass


class ChampionInfo(BaseModel):
    attack: int
    defense: int
    magic: int
    difficulty: int


class Image(BaseModel):
    full: str
    sprite: str
    group: str
    x: int
    y: int
    w: int
    h: int


class ChampionStats(BaseModel):
    hp: int
    hpperlevel: int
    mp: int
    mpperlevel: float
    movespeed: int
    armor: int
    armorperlevel: float
    spellblock: int
    spellblockperlevel: float
    attackrange: int
    hpregen: float
    hpregenperlevel: float
    mpregen: float
    mpregenperlevel: float
    crit: int
    critperlevel: int
    attackdamage: int
    attackdamageperlevel: float
    attackspeedperlevel: float
    attackspeed: float


class Champion(BaseModel):
    version: Optional[str] = None
    id: str
    key: Decimal
    name: str
    blurb: str
    info: ChampionInfo
    image: Image
    tags: list[str]
    partype: str
    stats: ChampionStats


class ChampionSkin(BaseModel):
    id: int
    num: int
    name: str
    chromas: bool


class SpellTip(BaseModel):
    label: list[str]
    effect: list[str]


class ChampionSpell(BaseModel):
    id: str
    name: str
    description: str
    tooltip: str
    leveltip: SpellTip
    maxrank: int
    cooldown: list[float]
    cooldown_burn: str = Field(alias="cooldownBurn")
    cost: list[int]
    cost_burn: str = Field(alias="costBurn")  # "60/65/70/75/80"
    datavalues: dict
    effect: list[None | list[int]]
    effect_burn: list[Decimal | None] = Field(alias="effectBurn")
    vars: list
    cost_type: str = Field(alias="costType")
    maxammo: Decimal
    range: list[int]
    range_burn: Decimal = Field(alias="rangeBurn")
    image: Image
    resource: str


class ChampionPassive(Champion):
    name: str
    description: str
    image: Image


class ChampionWithDetails(Champion):
    title: str
    skins: list[ChampionSkin]
    lore: str
    allytips: list[str]
    enemytips: list[str]
    spells: list[ChampionSpell]
    passive: dict
    recommended: list


class ChampionsDB(BaseModel):
    type: str
    format: str
    version: str
    data: dict[str, Champion]
    key_to_champion: Optional[dict[int, Champion]] = None

    def model_post_init(self, _):
        self.key_to_champion = {}
        for _, champion in self.data.items():
            self.key_to_champion[int(champion.key)] = champion

    def get_champion_by_name(self, name: str):
        champ = self.data.get(name)
        if champ:
            return champ

        raise ChampionNotFound(f"Champion {name} not found.")

    def get_champion_by_id(self, id: int):
        champ = self.key_to_champion.get(id)
        if champ:
            return champ

        raise ChampionNotFound(f"Champion {id} not found.")


class ChampionWithDetailsResponse(BaseModel):
    type: str
    format: str
    version: str
    data: dict[str, ChampionWithDetails]
