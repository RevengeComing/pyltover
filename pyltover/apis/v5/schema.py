from typing import Optional
from pydantic import BaseModel, Field


class MatchMetadata(BaseModel):
    data_version: str = Field(alias="dataVersion")
    match_id: str = Field(alias="matchId")
    participants: list[str]


class Challenges(BaseModel):
    twelve_assist_streak_count: Optional[int] = Field(None, alias="12AssistStreakCount")
    baron_buff_gold_advantage_over_threshold: Optional[int] = Field(None, alias="baronBuffGoldAdvantageOverThreshold")
    control_ward_time_coverage_in_river_or_enemy_half: Optional[float] = Field(
        None, alias="controlWardTimeCoverageInRiverOrEnemyHalf"
    )
    earliest_baron: Optional[float] = Field(None, alias="earliestBaron")
    earliest_dragon_takedown: Optional[float] = Field(None, alias="earliestDragonTakedown")
    earliest_elder_dragon: Optional[float] = Field(None, alias="earliestElderDragon")
    early_laning_phase_gold_exp_advantage: Optional[int] = Field(None, alias="earlyLaningPhaseGoldExpAdvantage")
    faster_support_quest_completion: Optional[int] = Field(None, alias="fasterSupportQuestCompletion")
    fastest_legendary: Optional[float] = Field(None, alias="fastestLegendary")
    had_afk_teammate: Optional[int] = Field(None, alias="hadAfkTeammate")
    highest_champion_damage: Optional[int] = Field(None, alias="highestChampionDamage")
    highest_crowd_control_score: Optional[int] = Field(None, alias="highestCrowdControlScore")
    highestWardKills: Optional[int] = Field(None, alias="highestWardKills")
    jungler_kills_early_jungle: Optional[int] = Field(None, alias="junglerKillsEarlyJungle")
    kills_on_laners_early_jungle_as_jungler: Optional[int] = Field(None, alias="killsOnLanersEarlyJungleAsJungler")
    laning_phase_gold_exp_advantage: Optional[int] = Field(None, alias="laningPhaseGoldExpAdvantage")
    legendary_count: Optional[int] = Field(None, alias="legendaryCount")
    max_cs_advantage_on_lane_opponent: Optional[float] = Field(None, alias="maxCsAdvantageOnLaneOpponent")
    max_level_lead_lane_opponent: Optional[int] = Field(None, alias="maxLevelLeadLaneOpponent")
    most_wards_destroyed_one_sweeper: Optional[int] = Field(None, alias="mostWardsDestroyedOneSweeper")
    mythic_item_used: Optional[int] = Field(None, alias="mythicItemUsed")
    played_champ_select_position: Optional[int] = Field(None, alias="playedChampSelectPosition")
    solo_turrets_lategame: Optional[int] = Field(None, alias="soloTurretsLategame")
    takedowns_first25_minutes: Optional[int] = Field(None, alias="takedownsFirst25Minutes")
    teleport_takedowns: Optional[int] = Field(None, alias="teleportTakedowns")
    third_inhibitor_destroyed_time: Optional[int] = Field(None, alias="thirdInhibitorDestroyedTime")
    three_wards_one_sweeper_count: Optional[int] = Field(None, alias="threeWardsOneSweeperCount")
    vision_score_advantage_lane_opponent: Optional[float] = Field(None, alias="visionScoreAdvantageLaneOpponent")
    infernal_scale_pickup: Optional[int] = Field(None, alias="InfernalScalePickup")
    fist_bump_participation: Optional[int] = Field(None, alias="fistBumpParticipation")
    void_monster_kill: Optional[int] = Field(None, alias="voidMonsterKill")
    ability_uses: Optional[int] = Field(None, alias="abilityUses")
    aces_before15_minutes: Optional[int] = Field(None, alias="acesBefore15Minutes")
    allied_jungle_monster_kills: Optional[float] = Field(None, alias="alliedJungleMonsterKills")
    baron_takedowns: Optional[int] = Field(None, alias="baronTakedowns")
    blast_cone_opposite_opponent_count: Optional[int] = Field(None, alias="blastConeOppositeOpponentCount")
    bounty_gold: Optional[float] = Field(None, alias="bountyGold")
    buffs_stolen: Optional[int] = Field(None, alias="buffsStolen")
    complete_support_quest_in_time: Optional[int] = Field(None, alias="completeSupportQuestInTime")
    control_wards_placed: Optional[int] = Field(None, alias="controlWardsPlaced")
    damage_per_minute: Optional[float] = Field(None, alias="damagePerMinute")
    damage_taken_on_team_percentage: Optional[float] = Field(None, alias="damageTakenOnTeamPercentage")
    danced_with_rift_herald: Optional[int] = Field(None, alias="dancedWithRiftHerald")
    deaths_by_enemy_champs: Optional[int] = Field(None, alias="deathsByEnemyChamps")
    dodge_skill_shots_small_window: Optional[int] = Field(None, alias="dodgeSkillShotsSmallWindow")
    double_aces: Optional[int] = Field(None, alias="doubleAces")
    dragon_takedowns: Optional[int] = Field(None, alias="dragonTakedowns")
    legendary_item_used: Optional[list[int]] = Field(None, alias="legendaryItemUsed")
    effective_heal_and_shielding: Optional[float] = Field(None, alias="effectiveHealAndShielding")
    elder_dragon_kills_with_opposing_soul: Optional[int] = Field(None, alias="elderDragonKillsWithOpposingSoul")
    elder_dragon_multikills: Optional[int] = Field(None, alias="elderDragonMultikills")
    enemy_champion_immobilizations: Optional[int] = Field(None, alias="enemyChampionImmobilizations")
    enemy_jungle_monster_kills: Optional[float] = Field(None, alias="enemyJungleMonsterKills")
    epic_monster_kills_near_enemy_jungler: Optional[int] = Field(None, alias="epicMonsterKillsNearEnemyJungler")
    epic_monster_kills_within30_seconds_of_spawn: Optional[int] = Field(
        None, alias="epicMonsterKillsWithin30SecondsOfSpawn"
    )
    epic_monster_steals: Optional[int] = Field(None, alias="epicMonsterSteals")
    epic_monster_stolen_without_smite: Optional[int] = Field(None, alias="epicMonsterStolenWithoutSmite")
    first_turret_killed: Optional[int] = Field(None, alias="firstTurretKilled")
    first_turret_killed_time: Optional[float] = Field(None, alias="firstTurretKilledTime")
    flawless_aces: Optional[int] = Field(None, alias="flawlessAces")
    full_team_takedown: Optional[int] = Field(None, alias="fullTeamTakedown")
    game_length: Optional[float] = Field(None, alias="gameLength")
    get_takedowns_in_all_lanes_early_jungle_as_laner: Optional[int] = Field(
        None, alias="getTakedownsInAllLanesEarlyJungleAsLaner"
    )
    gold_per_minute: Optional[float] = Field(None, alias="goldPerMinute")
    had_open_nexus: Optional[int] = Field(None, alias="hadOpenNexus")
    immobilize_and_kill_with_ally: Optional[int] = Field(None, alias="immobilizeAndKillWithAlly")
    initial_buff_count: Optional[int] = Field(None, alias="initialBuffCount")
    initial_crab_count: Optional[int] = Field(None, alias="initialCrabCount")
    jungle_cs_before10_minutes: Optional[float] = Field(None, alias="jungleCsBefore10Minutes")
    jungler_takedowns_near_damaged_epic_monster: Optional[int] = Field(
        None, alias="junglerTakedownsNearDamagedEpicMonster"
    )
    kda: Optional[float]
    kill_after_hidden_with_ally: Optional[int] = Field(None, alias="killAfterHiddenWithAlly")
    killed_champ_took_full_team_damage_survived: Optional[int] = Field(
        None, alias="killedChampTookFullTeamDamageSurvived"
    )
    killing_sprees: Optional[int] = Field(None, alias="killingSprees")
    kill_participation: Optional[float] = Field(None, alias="killParticipation")
    kills_near_enemy_turret: Optional[int] = Field(None, alias="killsNearEnemyTurret")
    kills_on_other_lanes_early_jungle_as_laner: Optional[int] = Field(None, alias="killsOnOtherLanesEarlyJungleAsLaner")
    kills_on_recently_healed_by_aram_pack: Optional[int] = Field(None, alias="killsOnRecentlyHealedByAramPack")
    kills_under_own_turret: Optional[int] = Field(None, alias="killsUnderOwnTurret")
    kills_with_help_from_epic_monster: Optional[int] = Field(None, alias="killsWithHelpFromEpicMonster")
    knock_enemy_into_team_and_kill: Optional[int] = Field(None, alias="knockEnemyIntoTeamAndKill")
    k_turrets_destroyed_before_plates_fall: Optional[int] = Field(None, alias="kTurretsDestroyedBeforePlatesFall")
    land_skill_shots_early_game: Optional[int] = Field(None, alias="landSkillShotsEarlyGame")
    lane_minions_first10_minutes: Optional[int] = Field(None, alias="laneMinionsFirst10Minutes")
    lost_an_inhibitor: Optional[int] = Field(None, alias="lostAnInhibitor")
    max_kill_deficit: Optional[int] = Field(None, alias="maxKillDeficit")
    mejais_full_stack_in_time: Optional[int] = Field(None, alias="mejaisFullStackInTime")
    more_enemy_jungle_than_opponent: Optional[float] = Field(None, alias="moreEnemyJungleThanOpponent")
    # This is an offshoot of the OneStone challenge. The code checks if a spell with the same instance ID does the final
    #  point of damage to at least 2 Champions. It doesn't matter if they're enemies, but you cannot hurt your friends.
    multi_kill_one_spell: Optional[int] = Field(None, alias="multiKillOneSpell")
    multikills: Optional[int]
    multikills_after_aggressive_flash: Optional[int] = Field(None, alias="multikillsAfterAggressiveFlash")
    multi_turret_rift_herald_count: Optional[int] = Field(None, alias="multiTurretRiftHeraldCount")
    outer_turret_executes_before10_minutes: Optional[int] = Field(None, alias="outerTurretExecutesBefore10Minutes")
    outnumbered_kills: Optional[int] = Field(None, alias="outnumberedKills")
    outnumbered_nexus_kill: Optional[int] = Field(None, alias="outnumberedNexusKill")
    perfect_dragon_souls_taken: Optional[int] = Field(None, alias="perfectDragonSoulsTaken")
    perfect_game: Optional[int] = Field(None, alias="perfectGame")
    pick_kill_with_ally: Optional[int] = Field(None, alias="pickKillWithAlly")
    poro_explosions: Optional[int] = Field(None, alias="poroExplosions")
    quick_cleanse: Optional[int] = Field(None, alias="quickCleanse")
    quick_first_turret: Optional[int] = Field(None, alias="quickFirstTurret")
    quick_solo_kills: Optional[int] = Field(None, alias="quickSoloKills")
    rift_herald_takedowns: Optional[int] = Field(None, alias="riftHeraldTakedowns")
    save_ally_from_death: Optional[int] = Field(None, alias="saveAllyFromDeath")
    scuttle_crab_kills: Optional[int] = Field(None, alias="scuttleCrabKills")
    shortest_time_to_ace_from_first_takedown: Optional[float] = Field(None, alias="shortestTimeToAceFromFirstTakedown")
    skillshots_dodged: Optional[int] = Field(None, alias="skillshotsDodged")
    skillshots_hit: Optional[int] = Field(None, alias="skillshotsHit")
    snowballs_hit: Optional[int] = Field(None, alias="snowballsHit")
    solo_baron_kills: Optional[int] = Field(None, alias="soloBaronKills")
    swarm_defeat_aatrox: Optional[int] = Field(None, alias="SWARM_DefeatAatrox")
    swarm_defeat_briar: Optional[int] = Field(None, alias="SWARM_DefeatBriar")
    swarm_defeat_mini_bosses: Optional[int] = Field(None, alias="SWARM_DefeatMiniBosses")
    swarm_evolve_weapon: Optional[int] = Field(None, alias="SWARM_EvolveWeapon")
    swarm_have3_passives: Optional[int] = Field(None, alias="SWARM_Have3Passives")
    swarm_kill_enemy: Optional[int] = Field(None, alias="SWARM_KillEnemy")
    swarm_pickup_gold: Optional[float] = Field(None, alias="SWARM_PickupGold")
    swarm_reach_level50: Optional[int] = Field(None, alias="SWARM_ReachLevel50")
    swarm_survive15_min: Optional[int] = Field(None, alias="SWARM_Survive15Min")
    swarm_win_with5_evolved_weapons: Optional[int] = Field(None, alias="SWARM_WinWith5EvolvedWeapons")
    solo_kills: Optional[int] = Field(None, alias="soloKills")
    stealth_wards_placed: Optional[int] = Field(None, alias="stealthWardsPlaced")
    survived_single_digit_hp_count: Optional[int] = Field(None, alias="survivedSingleDigitHpCount")
    survived_three_immobilizes_in_fight: Optional[int] = Field(None, alias="survivedThreeImmobilizesInFight")
    takedown_on_first_turret: Optional[int] = Field(None, alias="takedownOnFirstTurret")
    takedowns: Optional[int]
    takedowns_after_gaining_level_advantage: Optional[int] = Field(None, alias="takedownsAfterGainingLevelAdvantage")
    takedowns_before_jungle_minion_spawn: Optional[int] = Field(None, alias="takedownsBeforeJungleMinionSpawn")
    takedowns_first_x_minutes: Optional[int] = Field(None, alias="takedownsFirstXMinutes")
    takedowns_in_alcove: Optional[int] = Field(None, alias="takedownsInAlcove")
    takedowns_in_enemy_fountain: Optional[int] = Field(None, alias="takedownsInEnemyFountain")
    team_baron_kills: Optional[int] = Field(None, alias="teamBaronKills")
    team_damage_percentage: Optional[float] = Field(None, alias="teamDamagePercentage")
    team_elder_dragon_kills: Optional[int] = Field(None, alias="teamElderDragonKills")
    team_rift_herald_kills: Optional[int] = Field(None, alias="teamRiftHeraldKills")
    took_large_damage_survived: Optional[int] = Field(None, alias="tookLargeDamageSurvived")
    turret_plates_taken: Optional[int] = Field(None, alias="turretPlatesTaken")
    # Any player who damages a tower that is destroyed within 30 seconds of a Rift Herald charge will receive credit.
    # A player who does not damage the tower will not receive credit.
    turrets_taken_with_rift_herald: Optional[int] = Field(None, alias="turretsTakenWithRiftHerald")
    turret_takedowns: Optional[int] = Field(None, alias="turretTakedowns")
    twenty_minions_in3_seconds_count: Optional[int] = Field(None, alias="twentyMinionsIn3SecondsCount")
    two_wards_one_sweeper_count: Optional[int] = Field(None, alias="twoWardsOneSweeperCount")
    unseen_recalls: Optional[int] = Field(None, alias="unseenRecalls")
    vision_score_per_minute: Optional[float] = Field(None, alias="visionScorePerMinute")
    wards_guarded: Optional[int] = Field(None, alias="wardsGuarded")
    ward_takedowns: Optional[int] = Field(None, alias="wardTakedowns")
    ward_takedowns_before20m: Optional[int] = Field(None, alias="wardTakedownsBefore20M")


class Missions(BaseModel):
    player_score0: int = Field(alias="playerScore0")
    player_score1: int = Field(alias="playerScore1")
    player_score2: int = Field(alias="playerScore2")
    player_score3: int = Field(alias="playerScore3")
    player_score4: int = Field(alias="playerScore4")
    player_score5: int = Field(alias="playerScore5")
    player_score6: int = Field(alias="playerScore6")
    player_score7: int = Field(alias="playerScore7")
    player_score8: int = Field(alias="playerScore8")
    player_score9: int = Field(alias="playerScore9")
    player_score10: int = Field(alias="playerScore10")
    player_score11: int = Field(alias="playerScore11")


class PerkStats(BaseModel):
    defense: int
    flex: int
    offense: int


class PerkStyleSelection(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class PerkStyle(BaseModel):
    description: str
    selections: list[PerkStyleSelection]
    style: int


class Perks(BaseModel):
    statPerks: PerkStats
    styles: list[PerkStyle]


class Participant(BaseModel):
    all_in_pings: int = Field(alias="allInPings")  # Yellow crossed swords
    assist_me_pings: int = Field(alias="assistMePings")  # Green flag
    assists: int
    baron_kills: int = Field(alias="baronKills")
    bounty_level: Optional[int] = Field(None, alias="bountyLevel")
    champ_experience: int = Field(alias="champExperience")
    champ_level: int = Field(alias="champLevel")
    # Prior to patch 11.4, on Feb 18th, 2021, this field returned invalid championIds. We recommend determining the
    # champion based on the championName field for matches played prior to patch 11.4.
    champion_id: int = Field(alias="championId")
    champion_name: str = Field(alias="championName")  # Blue generic ping (ALT+click)
    command_pings: int = Field(alias="commandPings")
    # This field is currently only utilized for Kayn's transformations. (Legal values: 0 - None, 1 - Slayer, 2 - Assassin)
    champion_transform: int = Field(alias="championTransform")
    consumables_purchased: int = Field(alias="consumablesPurchased")
    challenges: Challenges = []
    damage_dealt_to_buildings: int = Field(alias="damageDealtToBuildings")
    damage_dealt_to_objectives: int = Field(alias="damageDealtToObjectives")
    damage_dealt_to_turrets: int = Field(alias="damageDealtToTurrets")
    damage_self_mitigated: int = Field(alias="damageSelfMitigated")
    deaths: int
    detector_wards_placed: int = Field(alias="detectorWardsPlaced")
    double_kills: int = Field(alias="doubleKills")
    dragon_kills: int = Field(alias="dragonKills")
    eligible_for_progression: bool = Field(alias="eligibleForProgression")
    # Yellow questionmark
    enemy_missing_pings: int = Field(alias="enemyMissingPings")
    # Red eyeball
    enemy_vision_pings: int = Field(alias="enemyVisionPings")
    first_blood_assist: bool = Field(alias="firstBloodAssist")
    first_blood_kill: bool = Field(alias="firstBloodKill")
    first_tower_assist: bool = Field(alias="firstTowerAssist")
    first_tower_kill: bool = Field(alias="firstTowerKill")
    # This is an offshoot of the OneStone challenge. The code checks if a spell with the same instance ID does the
    # final point of damage to at least 2 Champions. It doesn't matter if they're enemies, but you cannot hurt your friends.
    game_ended_in_early_surrender: bool = Field(alias="gameEndedInEarlySurrender")
    game_ended_in_surrender: bool = Field(alias="gameEndedInSurrender")
    hold_pings: int = Field(alias="holdPings")
    get_back_pings: int = Field(alias="getBackPings")  # Yellow circle with horizontal line
    gold_earned: int = Field(alias="goldEarned")
    gold_spent: int = Field(alias="goldSpent")
    # Both individualPosition and teamPosition are computed by the game server and are different versions of the most
    # likely position played by a player. The individualPosition is the best guess for which position the player
    # actually played in isolation of anything else. The teamPosition is the best guess for which position the player
    # actually played if we add the constraint that each team must have one top player, one jungle, one middle, etc.
    # Generally the recommendation is to use the teamPosition field over the individualPosition field.
    individual_position: str = Field(alias="individualPosition")
    inhibitor_kills: int = Field(alias="inhibitorKills")
    inhibitor_takedowns: int = Field(alias="inhibitorTakedowns")
    inhibitors_lost: int = Field(alias="inhibitorsLost")
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    items_purchased: int = Field(alias="itemsPurchased")
    killing_sprees: int = Field(alias="killingSprees")
    kills: int
    lane: str
    largest_critical_strike: int = Field(alias="largestCriticalStrike")
    largest_killing_spree: int = Field(alias="largestKillingSpree")
    largest_multi_kill: int = Field(alias="largestMultiKill")
    longest_time_spent_living: int = Field(alias="longestTimeSpentLiving")
    magic_damage_dealt: int = Field(alias="magicDamageDealt")
    magic_damage_dealt_to_champions: int = Field(alias="magicDamageDealtToChampions")
    magic_damage_taken: int = Field(alias="magicDamageTaken")
    missions: Missions
    # neutralMinionsKilled = mNeutralMinionsKilled, which is incremented on kills of kPet and kJungleMonster
    neutral_minions_killed: int = Field(alias="neutralMinionsKilled")
    need_vision_pings: int = Field(alias="needVisionPings")  # Green ward
    nexus_kills: int = Field(alias="nexusKills")
    nexus_takedowns: int = Field(alias="nexusTakedowns")
    nexus_lost: int = Field(alias="nexusLost")
    objectives_stolen: int = Field(alias="objectivesStolen")
    objectives_stolen_assists: int = Field(alias="objectivesStolenAssists")
    on_my_way_pings: int = Field(alias="onMyWayPings")  # Blue arrow pointing at ground
    participant_id: int = Field(alias="participantId")
    player_score0: Optional[int] = Field(None, alias="playerScore0")
    player_score1: Optional[int] = Field(None, alias="playerScore1")
    player_score2: Optional[int] = Field(None, alias="playerScore2")
    player_score3: Optional[int] = Field(None, alias="playerScore3")
    player_score4: Optional[int] = Field(None, alias="playerScore4")
    player_score5: Optional[int] = Field(None, alias="playerScore5")
    player_score6: Optional[int] = Field(None, alias="playerScore6")
    player_score7: Optional[int] = Field(None, alias="playerScore7")
    player_score8: Optional[int] = Field(None, alias="playerScore8")
    player_score9: Optional[int] = Field(None, alias="playerScore9")
    player_score10: Optional[int] = Field(None, alias="playerScore10")
    player_score11: Optional[int] = Field(None, alias="playerScore11")
    penta_kills: int = Field(alias="pentaKills")
    perks: Perks
    physical_damage_dealt: int = Field(alias="physicalDamageDealt")
    physical_damage_dealt_to_champions: int = Field(alias="physicalDamageDealtToChampions")
    physical_damage_taken: int = Field(alias="physicalDamageTaken")
    placement: int
    player_augment1: int = Field(alias="playerAugment1")
    player_augment2: int = Field(alias="playerAugment2")
    player_augment3: int = Field(alias="playerAugment3")
    player_augment4: int = Field(alias="playerAugment4")
    player_subteam_id: int = Field(alias="playerSubteamId")
    push_pings: int = Field(alias="pushPings")  # Green minion
    profile_icon: int = Field(alias="profileIcon")
    puuid: str
    quadra_kills: int = Field(alias="quadraKills")
    riot_id_game_name: str = Field(alias="riotIdGameName")
    riot_id_tagline: str = Field(alias="riotIdTagline")
    role: str
    sight_wards_bought_in_game: int = Field(alias="sightWardsBoughtInGame")
    spell1_casts: int = Field(alias="spell1Casts")
    spell2_casts: int = Field(alias="spell2Casts")
    spell3_casts: int = Field(alias="spell3Casts")
    spell4_casts: int = Field(alias="spell4Casts")
    subteam_placement: int = Field(alias="subteamPlacement")
    summoner1_casts: int = Field(alias="summoner1Casts")
    summoner1_id: int = Field(alias="summoner1Id")
    summoner2_casts: int = Field(alias="summoner2Casts")
    summoner2_id: int = Field(alias="summoner2Id")
    summoner_id: str = Field(alias="summonerId")
    summoner_level: int = Field(alias="summonerLevel")
    summoner_name: str = Field(alias="summonerName")
    team_early_surrendered: bool = Field(alias="teamEarlySurrendered")
    team_id: int = Field(alias="teamId")
    # Both individualPosition and teamPosition are computed by the game server and are different versions of the most
    # likely position played by a player. The individualPosition is the best guess for which position the player
    # actually played in isolation of anything else. The teamPosition is the best guess for which position the player
    # actually played if we add the constraint that each team must have one top player, one jungle, one middle, etc.
    # Generally the recommendation is to use the teamPosition field over the individualPosition field.
    team_position: str = Field(alias="teamPosition")
    time_c_cing_others: int = Field(alias="timeCCingOthers")
    time_played: int = Field(alias="timePlayed")
    total_ally_jungle_minions_killed: int = Field(alias="totalAllyJungleMinionsKilled")
    total_damage_dealt: int = Field(alias="totalDamageDealt")
    total_damage_dealt_to_champions: int = Field(alias="totalDamageDealtToChampions")
    total_damage_shielded_on_teammates: int = Field(alias="totalDamageShieldedOnTeammates")
    total_damage_taken: int = Field(alias="totalDamageTaken")
    total_enemy_jungle_minions_killed: int = Field(alias="totalEnemyJungleMinionsKilled")
    # Whenever positive health is applied (which translates to all heals in the game but not things like regeneration),
    # totalHeal is incremented by the amount of health received. This includes healing enemies, jungle monsters, yourself, etc
    total_heal: int = Field(alias="totalHeal")
    # Whenever positive health is applied (which translates to all heals in the game but not things like regeneration),
    # totalHealsOnTeammates is incremented by the amount of health received. This is post modified, so if you heal
    # someone missing 5 health for 100 you will get +5 totalHealsOnTeammates
    total_heals_on_teammates: int = Field(alias="totalHealsOnTeammates")
    # totalMillionsKilled = mMinionsKilled, which is only incremented on kills of kTeamMinion, kMeleeLaneMinion,
    # kSuperLaneMinion, kRangedLaneMinion and kSiegeLaneMinion
    total_minions_killed: int = Field(alias="totalMinionsKilled")
    total_time_cc_dealt: int = Field(alias="totalTimeCCDealt")
    total_time_spent_dead: int = Field(alias="totalTimeSpentDead")
    total_units_healed: int = Field(alias="totalUnitsHealed")
    triple_kills: int = Field(alias="tripleKills")
    true_damage_dealt: int = Field(alias="trueDamageDealt")
    true_damage_dealt_to_champions: int = Field(alias="trueDamageDealtToChampions")
    true_damage_taken: int = Field(alias="trueDamageTaken")
    turret_kills: int = Field(alias="turretKills")
    turret_takedowns: int = Field(alias="turretTakedowns")
    turrets_lost: int = Field(alias="turretsLost")
    unreal_kills: int = Field(alias="unrealKills")
    vision_score: int = Field(alias="visionScore")
    vision_cleared_pings: int = Field(alias="visionClearedPings")
    vision_wards_bought_in_game: int = Field(alias="visionWardsBoughtInGame")
    wards_killed: int = Field(alias="wardsKilled")
    wards_placed: int = Field(alias="wardsPlaced")
    win: bool


class MatchBan(BaseModel):
    champion_id: int = Field(alias="championId")
    pick_turn: int = Field(alias="pickTurn")


class Objective(BaseModel):
    first: bool
    kills: int


class MatchObjectives(BaseModel):
    baron: Objective
    champion: Objective
    dragon: Objective
    horde: Objective
    inhibitor: Objective
    riftHerald: Objective
    tower: Objective


class MatchTeam(BaseModel):
    bans: list[MatchBan]
    objectives: MatchObjectives
    team_id: int = Field(alias="teamId")
    win: bool


class MatchInfo(BaseModel):
    end_of_game_result: str = Field(alias="endOfGameResult")
    game_creation: int = Field(alias="gameCreation")
    game_duration: int = Field(alias="gameDuration")
    game_end_timestamp: int = Field(alias="gameEndTimestamp")
    game_id: int = Field(alias="gameId")
    game_mode: str = Field(alias="gameMode")
    game_name: str = Field(alias="gameName")
    game_start_timestamp: int = Field(alias="gameStartTimestamp")
    game_type: str = Field(alias="gameType")
    game_version: str = Field(alias="gameVersion")
    map_id: int = Field(alias="mapId")
    participants: list[Participant]
    platform_id: str = Field(alias="platformId")
    queue_id: int = Field(alias="queueId")
    teams: list[MatchTeam]
    tournament_code: str = Field(alias="tournamentCode")


class Match(BaseModel):
    metadata: MatchMetadata
    info: MatchInfo


class MatchTimeline(BaseModel):
    pass
