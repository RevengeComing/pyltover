# ChampionMastery-V4
get_all_champion_mastery = "https://{server_addr}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
get_champion_mastery = (
    "https://{server_addr}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
)
get_top_champion_mastery_by_count = (
    "https://{server_addr}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"
)
get_total_champion_mastery_score = "https://{server_addr}/lol/champion-mastery/v4/scores/by-puuid/{puuid}"

# League-Exp-V4
# get_all_the_league_entries = "https://{server_addr}/lol/league-exp/v4/entries/{queue}/{tier}/{division}"

# League-V4
get_the_challenger_league_for_queue = "https://{server_addr}/lol/league/v4/challengerleagues/by-queue/{queue}"
get_league_entries_for_puuid = "https://{server_addr}/lol/league/v4/entries/by-puuid/{puuid}"
get_all_the_league_entries = "https://{server_addr}/lol/league/v4/entries/{queue}/{tier}/{division}"
get_the_grandmaster_league_for_queue = "https://{server_addr}/lol/league/v4/grandmasterleagues/by-queue/{queue}"
get_league_with_id = "https://{server_addr}/lol/league/v4/leagues/{league_id}"
get_the_master_league_for_queue = "https://{server_addr}/lol/league/v4/masterleagues/by-queue/{queue}"
