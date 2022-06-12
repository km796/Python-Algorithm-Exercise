

def solution(character, monsters):

    character = character.split(" ")
    c_hp = int(character[0])
    c_att = int(character[1])
    c_df = int(character[2])

    max_exp = 0
    answer = None

    for mon in monsters:
        mon = mon.split(" ")
        name = mon[0]
        exp = int(mon[1])
        hp = int(mon[2])
        att = int(mon[3])
        df = int(mon[4])
        round = 1

        while True:
            dmg = c_att - df
            if dmg <= 0:
                break
            hp -= dmg

            if hp <= 0:
                if exp/round > max_exp:
                    max_exp = exp/round
                    answer = name
                break

            mon_dmg = att - c_df
            if mon_dmg >= c_hp:
                break
            round += 1
    return answer

print(solution("10 5 2", ["K 3 10 10 3", "W 5 10 15 1", "B 1 1 15 1"]))




