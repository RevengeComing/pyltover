from typing import Optional
from pydantic import BaseModel
from decimal import Decimal


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
    mpperlevel: int
    movespeed: int
    armor: int
    armorperlevel: float
    spellblock: int
    spellblockperlevel: float
    attackrange: int
    hpregen: int
    hpregenperlevel: float
    mpregen: int
    mpregenperlevel: int
    crit: int
    critperlevel: int
    attackdamage: int
    attackdamageperlevel: int
    attackspeedperlevel: float
    attackspeed: float


class Champion(BaseModel):
    version: Optional[str]
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
    cooldown: list[int]
    cooldownBurn: int
    cost: list[int]
    costBurn: str  # "60/65/70/75/80"
    datavalues: dict
    effect: list[None | list[int]]
    effectBurn: list[Decimal | None]
    vars: list
    costType: str
    maxammo: Decimal
    range: list[int]
    rangeBurn: Decimal
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


class ChampionResponse(BaseModel):
    type: str
    format: str
    version: str
    data: dict[str, Champion]


class ChampionWithDetailsResponse(BaseModel):
    type: str
    format: str
    version: str
    data: dict[str, ChampionWithDetails]
