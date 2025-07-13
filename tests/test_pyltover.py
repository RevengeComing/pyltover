import pytest
from pyltover import Pyltover
from pyltover.apis.errors import RiotAPIError
from pyltover.servers import RegionalRoutingValues
from pyltover.apis.v1 import schema as schema_v1


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


accounts_puuid = {"SoltanSoren": "ZcIG4rdQ5B70ykqcHAqmTWHBNYnxSEX8z0ZvmJA-Q43iTNYOMG82E_jy3WZxBLTQ4DK-xon4VIyLoQ"}
accounts_game_names = {"SoltanSoren": "SoltanSoren"}
accounts_taglines = {"SoltanSoren": "EUNE"}
accounts_games = {"SoltanSoren": "lor"}
accounts_lol_games = {"SoltanSoren": "lol"}
accounts_active_shard = {"SoltanSoren": "blocked"}
accounts_region = {"SoltanSoren": "euw1"}


arg_to_fixture = {
    "puuid": accounts_puuid,
    "tag_line": accounts_taglines,
    "game_name": accounts_game_names,
    "game": accounts_games,
    "lol_game": accounts_lol_games,
}


def _create_input_args(api_input_args, account_name):
    args = []
    for arg in api_input_args:
        args.append(arg_to_fixture[arg][account_name])
    return args


@pytest.mark.parametrize(
    [
        "server",
        "api_version",
        "api_name",
        "account_name",
        "api_input_args",
        "response_model",
        "checks",
    ],
    [
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_account_by_puuid",
            "SoltanSoren",
            ("puuid",),
            schema_v1.Account,
            {
                "game_name": accounts_game_names["SoltanSoren"],
                "tag_line": accounts_taglines["SoltanSoren"],
                "puuid": accounts_puuid["SoltanSoren"],
            },
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_account_by_riot_id",
            "SoltanSoren",
            ("tag_line", "game_name"),
            schema_v1.Account,
            {
                "game_name": accounts_game_names["SoltanSoren"],
                "tag_line": accounts_taglines["SoltanSoren"],
                "puuid": accounts_puuid["SoltanSoren"],
            },
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_active_shard_for_player",
            "SoltanSoren",
            ("game", "puuid"),
            schema_v1.ActiveShards,
            {
                "game": accounts_games["SoltanSoren"],
                "active_shard": accounts_active_shard["SoltanSoren"],
                "puuid": accounts_puuid["SoltanSoren"],
            },
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_active_region",
            "SoltanSoren",
            ("lol_game", "puuid"),
            schema_v1.ActiveRegion,
            {
                "puuid": accounts_puuid["SoltanSoren"],
                "game": accounts_lol_games["SoltanSoren"],
                "region": accounts_region["SoltanSoren"],
            },
        ),
        pytest.param(
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_account_by_access_token",
            "SoltanSoren",
            (),
            schema_v1.ActiveRegion,
            {
                "puuid": accounts_puuid["SoltanSoren"],
                "game": accounts_lol_games["SoltanSoren"],
                "region": accounts_region["SoltanSoren"],
            },
            marks=pytest.mark.skip("Cannot be tested with dev token"),
        ),
    ],
)
async def test_pyltover_apis_200(
    server,
    api_version,
    api_name,
    riot_api_token,
    account_name,
    api_input_args,
    response_model,
    checks: dict,
):
    pyltover = Pyltover(server, riot_api_token)
    api_input_args_tuple = _create_input_args(api_input_args, account_name)
    response = await getattr(getattr(pyltover, api_version), api_name)(*api_input_args_tuple)
    assert isinstance(response, response_model)
    for key, value in checks.items():
        assert getattr(response, key) == value, (response, key, value)


@pytest.mark.parametrize(
    [
        "server",
        "api_version",
        "api_name",
        "api_input_args",
        "status_code",
        "error_message",
    ],
    [
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_account_by_puuid",
            ("!@invalid puuid!@",),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_account_by_riot_id",
            ("INC", "ORRECT"),
            404,
            "Data not found - No results found for player with riot id ORRECT#INC",
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_active_shard_for_player",
            ("lor", "!@invalid puuid!@"),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_active_region",
            ("lol", "!@invalid puuid!@"),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
    ],
)
async def test_pyltover_apis_errors(
    server,
    api_version,
    api_name,
    riot_api_token,
    api_input_args,
    status_code,
    error_message,
):
    pyltover = Pyltover(server, riot_api_token)
    try:
        _ = await getattr(getattr(pyltover, api_version), api_name)(*api_input_args)
        assert False, "Expecting exception"
    except RiotAPIError as error:
        assert error.error_status.status_code == status_code, (
            status_code,
            error.error_status.message,
        )
        assert error.error_status.message == error_message, error.error_status.message


@pytest.mark.parametrize(
    [
        "server",
        "api_version",
        "api_name",
        "api_input_args",
        "status_code",
        "error_message",
    ],
    [
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_account_by_puuid",
            ("!@invalid puuid!@",),
            401,
            "Forbidden",
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_account_by_riot_id",
            ("INC", "ORRECT"),
            401,
            "Forbidden",
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_active_shard_for_player",
            ("lor", "!@invalid puuid!@"),
            401,
            "Forbidden",
        ),
        (
            RegionalRoutingValues.EUROPE.value,
            "v1",
            "get_active_region",
            ("lol", "!@invalid puuid!@"),
            401,
            "Forbidden",
        ),
    ],
)
async def test_pyltover_apis_unauthorized(
    server,
    api_version,
    api_name,
    unknown_api_token,
    api_input_args,
    status_code,
    error_message,
):
    pyltover = Pyltover(server, unknown_api_token)
    try:
        _ = await getattr(getattr(pyltover, api_version), api_name)(*api_input_args)
        assert False, "Expecting exception"
    except RiotAPIError as error:
        assert error.error_status.status_code == status_code, (
            status_code,
            error.error_status.message,
        )
        assert error.error_status.message == error_message, error.error_status.message
