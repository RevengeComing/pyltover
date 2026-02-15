import pytest


@pytest.fixture
def unknown_api_token():
    return "unknown-api-token"


@pytest.fixture
def riot_api_token():
    import os

    token = os.getenv("DEV_RIOT_API_TOKEN")
    if token:
        return token

    try:
        with open(".devkey", mode="r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("Please create a file with name .devkey with your token inside it.")


acounts_puuid = {"SoltanSoren": "iyPYkvZg9bA-vnOKhE1ADcmkT6Z89VwQuxm_t9lHJZg-8PDDHqa1ASGzmiobXJ7Pu8wD3ZbqMuHcsw"}
acounts_game_names = {"SoltanSoren": "SoltanSoren"}
acounts_taglines = {"SoltanSoren": "RPS"}
acounts_games = {"SoltanSoren": "lor"}
acounts_lol_games = {"SoltanSoren": "lol"}
acounts_active_shard = {"SoltanSoren": "blocked"}
acounts_region = {"SoltanSoren": "euw1"}


arg_to_fixture = {
    "puuid": acounts_puuid,
    "tag_line": acounts_taglines,
    "game_name": acounts_game_names,
    "game": acounts_games,
    "lol_game": acounts_lol_games,
}


def create_input_args(api_input_args, account_name):
    args = []
    for arg in api_input_args:
        args.append(arg_to_fixture[arg][account_name])
    return args
