from pyltover import Pyltover


async def test_get_all_champion_mastery(riot_api_token):
    pyltover = Pyltover(riot_api_token)
    await Pyltover.init_champions_db()
    champion_masteries = await pyltover.euw1.v3.get_champion_rotaions()
    assert len(champion_masteries.free_champion_ids) > 1
    assert len(champion_masteries.free_champion_ids_for_new_players) > 1

    champion_rotations_with_info = await pyltover.euw1.v3.get_champion_rotaions(load_champ=True)
    assert len(champion_rotations_with_info.free_champion_ids) > 1
    assert len(champion_rotations_with_info.free_champion_ids_for_new_players) > 1
    assert len(champion_rotations_with_info.free_champions) > 1
    assert len(champion_rotations_with_info.free_champions_for_new_players) > 1
