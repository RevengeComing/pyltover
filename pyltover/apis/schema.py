from enum import StrEnum


class Game(StrEnum):
    LOL = "lor"
    VALURANT = "val"


class Tier(StrEnum):
    IRON = "IRON"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"
    EMERALD = "EMERALD"
    DIAMOND = "DIAMOND"


class Division(StrEnum):
    I = "I"  # noqa: E741
    II = "II"
    III = "III"
    IV = "IV"


class QueueTypes(StrEnum):
    RANKED_SOLO_5x5 = "RANKED_SOLO_5x5"
    RANKED_FLEX_SR = "RANKED_FLEX_SR"
    RANKED_FLEX_TT = "RANKED_FLEX_TT"
