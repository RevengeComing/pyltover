import pytest
from pyltover import Pyltover
from pyltover.apis.errors import RiotAPIError
from pyltover.apis.v1 import schema as schema_v1

from tests.conftest import (
    acounts_game_names,
    acounts_taglines,
    acounts_puuid,
    acounts_lol_games,
    acounts_region,
    create_input_args,
)


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
            "europe",
            "v1",
            "get_account_by_puuid",
            "SoltanSoren",
            ("puuid",),
            schema_v1.Account,
            {
                "game_name": acounts_game_names["SoltanSoren"],
                "tag_line": acounts_taglines["SoltanSoren"],
                "puuid": "SoltanSoren",
            },
        ),
        (
            "europe",
            "v1",
            "get_account_by_riot_id",
            "SoltanSoren",
            ("tag_line", "game_name"),
            schema_v1.Account,
            {
                "game_name": acounts_game_names["SoltanSoren"],
                "tag_line": acounts_taglines["SoltanSoren"],
                "puuid": "SoltanSoren",
            },
        ),
        (
            "europe",
            "v1",
            "get_active_region",
            "SoltanSoren",
            ("lol_game", "puuid"),
            schema_v1.ActiveRegion,
            {
                "puuid": "SoltanSoren",
                "game": acounts_lol_games["SoltanSoren"],
                "region": acounts_region["SoltanSoren"],
            },
        ),
        pytest.param(
            "europe",
            "v1",
            "get_account_by_access_token",
            "SoltanSoren",
            (),
            schema_v1.ActiveRegion,
            {
                "puuid": "SoltanSoren",
                "game": acounts_lol_games["SoltanSoren"],
                "region": acounts_region["SoltanSoren"],
            },
            marks=pytest.mark.skip("Cannot be tested with dev token"),
        ),
    ],
)
async def test_pyltover_acount_apis_200(
    server,
    api_version,
    api_name,
    riot_api_token,
    account_name,
    api_input_args,
    response_model,
    checks: dict,
):
    pyltover = Pyltover(riot_api_token)
    api_input_args_tuple = create_input_args(api_input_args, account_name)
    response = await getattr(getattr(getattr(pyltover, server), api_version), api_name)(*api_input_args_tuple)
    assert isinstance(response, response_model)
    for key, value in checks.items():
        if key == "puuid":
            assert getattr(response, key) == acounts_puuid[value], (response, key, value)
        else:
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
            "europe",
            "v1",
            "get_account_by_puuid",
            ("!@invalid puuid!@",),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
        (
            "europe",
            "v1",
            "get_account_by_riot_id",
            ("INC", "ORRECT"),
            404,
            "Data not found - No results found for player with riot id ORRECT#INC",
        ),
        (
            "europe",
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
    pyltover = Pyltover(riot_api_token)
    try:
        _ = await getattr(getattr(getattr(pyltover, server), api_version), api_name)(*api_input_args)
        assert False, "Expecting exception"
    except RiotAPIError as error:
        assert error.error_status.status_code == status_code, (
            status_code,
            error.error_status.message,
        )
        assert error.error_status.message == error_message, error.error_status.message
