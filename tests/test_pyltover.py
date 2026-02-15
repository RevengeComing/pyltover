import pytest
from pyltover import Pyltover
from pyltover.apis.errors import RiotAPIError


async def test_ddragon_champions_db(unknown_api_token):
    pyltover = Pyltover(unknown_api_token)
    await pyltover.init_champions_db()
    annie_with_id = Pyltover.champions_db.get_champion_by_id(1)
    annie_with_name = Pyltover.champions_db.get_champion_by_name("Annie")
    assert annie_with_name.name == "Annie"
    assert annie_with_id.name == "Annie"
    assert annie_with_id == annie_with_name


async def test_ddragon_champion_with_details(unknown_api_token):
    pyltover = Pyltover(unknown_api_token)
    annie_details = await pyltover.get_champion_details_by_name("Annie")
    assert annie_details.name == "Annie"
    assert annie_details.lore.startswith("Dangerous, yet disarmingly precocious, Annie is a child mage with")


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
            401,
            "Forbidden",
        ),
        (
            "europe",
            "v1",
            "get_account_by_riot_id",
            ("INC", "ORRECT"),
            401,
            "Forbidden",
        ),
        (
            "europe",
            "v1",
            "get_active_shard_for_player",
            ("lor", "!@invalid puuid!@"),
            401,
            "Forbidden",
        ),
        (
            "europe",
            "v1",
            "get_active_region",
            ("lol", "!@invalid puuid!@"),
            401,
            "Forbidden",
        ),
        (
            "europe",
            "v4",
            "get_all_champion_mastery",
            ("!@invalid puuid!@",),
            401,
            "Forbidden",
        ),
        (
            "europe",
            "v4",
            "get_champion_mastery",
            ("!@invalid puuid!@", "123"),
            401,
            "Forbidden",
        ),
        (
            "europe",
            "v4",
            "get_top_champion_mastery_by_count",
            ("!@invalid puuid!@", 3),
            401,
            "Forbidden",
        ),
        (
            "europe",
            "v4",
            "get_total_champion_mastery_score",
            ("!@invalid puuid!@",),
            401,
            "Forbidden",
        ),
        (
            "euw1",
            "v4",
            "get_summoner_by_puuid",
            ("!@invalid puuid!@",),
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
    pyltover = Pyltover(unknown_api_token)
    try:
        _ = await getattr(getattr(getattr(pyltover, server), api_version), api_name)(*api_input_args)
        assert False, "Expecting exception"
    except RiotAPIError as error:
        assert error.error_status.status_code == status_code, (
            status_code,
            error.error_status.message,
        )
        assert error.error_status.message == error_message, error.error_status.message
