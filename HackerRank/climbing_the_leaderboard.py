def climbingLeaderboard(ranked, player):
    res = []
    scores_unique = []
    for i in range(len(ranked)):
        if i == 0 or ranked[i] != ranked[i - 1]:
            scores_unique.append(ranked[i])

    ranked_pointer = 0
    player_pointer = len(player) - 1

    while player_pointer >= 0 and ranked_pointer < len(scores_unique):
        if player[player_pointer] >= scores_unique[ranked_pointer]:
            res.append(ranked_pointer + 1)
            player_pointer -= 1
        elif ranked_pointer == len(scores_unique) - 1:
            res.append(len(scores_unique) + 1)
            player_pointer -= 1
        else:
            ranked_pointer += 1

    res_reversed = []
    for i in range(len(res) - 1, -1, -1):
        res_reversed.append(res[i])

    return res_reversed