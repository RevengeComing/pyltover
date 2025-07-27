import pytest
from pyltover import Pyltover
from pyltover.apis.errors import RiotAPIError
from pyltover.servers import PlatformRoutingValues
from tests.conftest import acounts_puuid


async def test_get_all_champion_mastery(riot_api_token):
    pyltover = Pyltover(PlatformRoutingValues.EUW1.value, riot_api_token)
    await pyltover.init_champions_db()
    champion_masteries = await pyltover.v4.get_all_champion_mastery(acounts_puuid["SoltanSoren"])
    for index, mastery in enumerate(champion_masteries):
        if mastery.champion_id == 64:
            break

    assert champion_masteries[index].champion is None
    assert champion_masteries[index].champion_id == 64

    champion_masteries = await pyltover.v4.get_all_champion_mastery(acounts_puuid["SoltanSoren"], True)
    assert champion_masteries[index].champion.name == "Lee Sin"
    assert champion_masteries[index].champion_id == 64


async def test_get_champion_mastery(riot_api_token):
    pyltover = Pyltover(PlatformRoutingValues.EUW1.value, riot_api_token)
    await pyltover.init_champions_db()
    champion_mastery = await pyltover.v4.get_champion_mastery(acounts_puuid["SoltanSoren"], "64")
    assert champion_mastery.champion is None
    assert champion_mastery.champion_id == 64

    champion_mastery = await pyltover.v4.get_champion_mastery(acounts_puuid["SoltanSoren"], "64", True)
    assert champion_mastery.champion.name == "Lee Sin"
    assert champion_mastery.champion_id == 64


async def test_get_top_champion_mastery_by_count(riot_api_token):
    pyltover = Pyltover(PlatformRoutingValues.EUW1.value, riot_api_token)
    await pyltover.init_champions_db()
    champion_mastery = await pyltover.v4.get_top_champion_mastery_by_count(acounts_puuid["SoltanSoren"], 1)
    assert champion_mastery[0].champion is None
    assert champion_mastery[0].champion_id == 64


async def test_get_total_champion_mastery_score(riot_api_token):
    pyltover = Pyltover(PlatformRoutingValues.EUW1.value, riot_api_token)
    champion_mastery_score = await pyltover.v4.get_total_champion_mastery_score(acounts_puuid["SoltanSoren"])
    assert isinstance(champion_mastery_score, int)
    assert champion_mastery_score > 600


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
            PlatformRoutingValues.EUW1.value,
            "v4",
            "get_all_champion_mastery",
            ("!@invalid puuid!@",),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
        (
            PlatformRoutingValues.EUW1.value,
            "v4",
            "get_champion_mastery",
            ("!@invalid puuid!@", "123"),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
        (
            PlatformRoutingValues.EUW1.value,
            "v4",
            "get_top_champion_mastery_by_count",
            ("!@invalid puuid!@", 3),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
        (
            PlatformRoutingValues.EUW1.value,
            "v4",
            "get_total_champion_mastery_score",
            ("!@invalid puuid!@",),
            400,
            "Bad Request - Exception decrypting !@invalid puuid!@",
        ),
    ],
)
async def test_pyltover_champion_mastery_apis_errors(
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
