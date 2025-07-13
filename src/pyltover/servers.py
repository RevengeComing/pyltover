from enum import StrEnum
from typing import Literal, Union


class Region(StrEnum):
    BR1 = "BR1"
    EUN1 = "EUN1"
    EUW1 = "EUW1"
    JP1 = "JP1"
    KR = "KR"
    LA1 = "LA1"
    LA2 = "LA2"
    ME1 = "ME1"
    NA1 = "NA1"
    OC1 = "OC1"
    RU = "RU"
    SG2 = "SG2"
    TR1 = "TR1"
    TW2 = "TW2"
    VN2 = "VN2"


class PlatformRoutingValues(StrEnum):
    BR1 = "br1.api.riotgames.com"
    EUN1 = "eun1.api.riotgames.com"
    EUW1 = "euw1.api.riotgames.com"
    JP1 = "jp1.api.riotgames.com"
    KR = "kr.api.riotgames.com"
    LA1 = "la1.api.riotgames.com"
    LA2 = "la2.api.riotgames.com"
    NA1 = "na1.api.riotgames.com"
    OC1 = "oc1.api.riotgames.com"
    TR1 = "tr1.api.riotgames.com"
    RU = "ru.api.riotgames.com"
    PH2 = "ph2.api.riotgames.com"
    SG2 = "sg2.api.riotgames.com"
    TH2 = "th2.api.riotgames.com"
    TW2 = "tw2.api.riotgames.com"
    VN2 = "vn2.api.riotgames.com"


class RegionalRoutingValues(StrEnum):
    AMERICAS = "americas.api.riotgames.com"
    ASIA = "asia.api.riotgames.com"
    EUROPE = "europe.api.riotgames.com"
    SEA = "sea.api.riotgames.com"


esports_server = "esports.api.riotgames.com"

ServerAddress = Union[PlatformRoutingValues, RegionalRoutingValues, Literal["esports.api.riotgames.com"]]
