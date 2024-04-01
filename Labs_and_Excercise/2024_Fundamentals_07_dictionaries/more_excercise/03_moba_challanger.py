def pool_refiling():
    player_info = input()
    players_pool = {}
    while True:
        if player_info == 'Season end':
            break
        elif 'vs' in player_info:
            battle_field(player_info, players_pool)
            break
        player_info = player_info.split(' -> ')
        player, position, skill = player_info[0], player_info[1], int(player_info[2])

        if player not in players_pool:
            players_pool[player] = {}
        if position not in players_pool[player]:
            players_pool[player].update({position: 0})
            if players_pool[player][position] < skill:
                players_pool[player].update({position: skill})
        player_info = input()
    return players_pool


def battle_field(user_input, pool):
    while True:
        if user_input == "Season end":
            break
        battle = user_input.split(' vs ')
        first_player, second_player = battle[0], battle[1]
        if first_player in pool and second_player in pool:
            first_player_tot_points = calculate_total_skill_points(pool, first_player)
            second_player_tot_points = calculate_total_skill_points(pool, second_player)
            first_player_data, second_player_data = pool[first_player], pool[second_player]
            for key in first_player_data.keys():
                if key in second_player_data.keys():
                    if first_player_tot_points > second_player_tot_points:
                        del pool[second_player]
                    elif second_player_tot_points > first_player_tot_points:
                        del pool[first_player]

        user_input = input()
    return pool


def calculate_total_skill_points(heroes_data, hero):
    tot_skill_points = 0
    for pretendente in heroes_data:
        if pretendente == hero:
            tot_skill_points = sum(heroes_data[hero].values())
    return tot_skill_points


def sorting_printing_results(dict_to_sort):
    dict_tot_skill = {}
    for hero in dict_to_sort.keys():
        tot_points = calculate_total_skill_points(dict_to_sort, hero)
        dict_tot_skill[hero] = tot_points
    sorted_dict_skill = dict(sorted(dict_tot_skill.items(), key=lambda a: (-int(a[1]), a[0])))
    for player, tot_points in sorted_dict_skill.items():
        dict_one_hero_data = dict_to_sort[player]
        sorted_one_hero_dict = dict(sorted(dict_one_hero_data.items(), key=lambda b: (-int(b[1]), b[0])))
        print(f'{player}: {tot_points} skill')
        for role, points in sorted_one_hero_dict.items():
            print(f'- {role} <::> {points}')


main_tier = pool_refiling()
sorting_printing_results(main_tier)
