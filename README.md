# pyltover

Python wrapper around riot games developer api.

## Installation

The package is uploaded into pypi and you can install it using pip or uv.

`$ pip install pyltover`

## Supported APIs

* Account
    * v1
        - [x] Get Account by puuid
        - [x] Get Account by riot id
        - [x] Get active shard for a player
        - [x] Get active region (lol and tft)
        - [ ] Get account by access token - Not possible with development key
* Champion Mastery
    * v4
        - [x] Get all champion mastery entries sorted by number of champion points descending.
        - [x] Get a champion mastery by puuid and champion ID.
        - [x] Get specified number of top champion mastery entries sorted by number of champion points descending.
        - [x] Get a player's total champion mastery score, which is the sum of individual champion mastery levels.
* Champion
    * v3
        - [x] Returns champion rotations, including free-to-play and low-level free-to-play rotations (REST)
* Clash
    * v1
        - [ ] Get players by puuid
        - [ ] Get team by ID.
        - [ ] Get all active or upcoming tournaments.
        - [ ] Get tournament by team ID.
        - [ ] Get tournament by ID.
* League
    * v4
        - [x] Get the challenger league for given queue.
        - [x] Get league entries in all queues for a given puuid
        - [x] Get all the league entries.
        - [x] Get the grandmaster league of a specific queue.
        - [x] Get league with given ID, including inactive entries.
        - [x] Get the master league for given queue.
* Summoner
    * v4
        - [x] Get a summoner by encrypted PUUID.
* Challenges
    * v1
        - [ ] List of all basic challenge configuration information (includes all translations for names and descriptions)
        - [ ] Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it
        - [ ] Get challenge configuration (REST)
        - [ ] Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER.
        - [ ] Map of level to percentile of players who have achieved it
        - [ ] Returns player information with list of all progressed challenges (REST)
* Match
    * v5
        - [x] Get a list of match ids by puuid
        - [x] Get a match by match id
        - [ ] Get a match timeline by match id

## How to use?

Get your token from  [Riot games developer website](https://developer.riotgames.com/).

```python
import asyncio
from pyltover import Pyltover


async def main():
    pyltover = Pyltover("your token")
    champion_mastery_score = await pyltover.euw1.v4.get_total_champion_mastery_score("puuid")
    print(champion_mastery_score)

    account_details = await pyltover.europe.v1.get_account_by_puuid("puuid")
    print(account_details)

    champion_rotation = await pyltover.euw1.v3.get_champion_rotaions("puuid")
    print(champion_rotation)

asyncio.run(main())
```

Servers are listed as properties under pyltover root object, e.g. `pytlover.euw` or `pyltover.na`. The API versions are listed under each server, e.g. `pyltover.euw.v1` or `pyltover.euw.v4`.

The response objects are Pydantic model objects.
