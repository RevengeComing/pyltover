import pytest

from pyltover import Pyltover
from pyltover.apis.errors import RiotAPIError
from pyltover.apis.v4 import schema as schema_v4
from tests.conftest import acounts_puuid


async def test_get_summoner_by_puuid(riot_api_token):
    pyltover = Pyltover(riot_api_token)
    summoner = await pyltover.euw1.v4.get_summoner_by_puuid(acounts_puuid["SoltanSoren"])
    assert isinstance(summoner, schema_v4.Summoner)
    assert summoner.puuid == acounts_puuid["SoltanSoren"]
    assert summoner.summoner_level >= 1


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
            "euw1",
            "v4",
            "get_summoner_by_puuid",
            ("!@invalid puuid!@",),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
    ],
)
async def test_pyltover_summoner_apis_errors(
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
