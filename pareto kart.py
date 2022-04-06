characters = [[0,5,5], [2,5,4], [4,4,3], [5,3,3], [6,2,2], [8,1,1], [7,1,2], [9,1,1], [10,0,0]]
karts = [[3,4,4], [1,6,6], [2,5,5], [5,1,1], [0,7,7], [4,3,3]]
wheels = [[2,4,3], [0,6,6], [3,2,2], [4,1,0], [1,5,5], [3,3,1]]
gliders = [[1,1,1], [0,2,2]]

combos = {}


def make_combo(char, kart, wheel, glider):
    combo = [0, 0, 0]

    for i in range(3):
        combo[i] = char[i] + kart[i] + wheel[i] + glider[i]
    
    return combo


def check_pareto(new_combo):
    false_paretos = []

    for key, combo in combos.items():
        if combo == new_combo:
            return True, []
        
        check = [False] * len(combo)
        for i in range(len(combo)):
            check[i] = combo[i] >= new_combo[i]
        
        if sum(check) == len(combo):
            return False, []
        
        if sum(check) == 0:
            false_paretos.append(key)
    
    return True, false_paretos


for i in range(len(characters)):
    for j in range(len(karts)):
        for k in range(len(wheels)):
            for l in range(len(gliders)):
                combo = make_combo(characters[i], karts[j], wheels[k], gliders[l])

                combo_result, remove_options = check_pareto(combo)

                if combo_result:
                    combo_string = str(i) + str(j) + str(k) + str(l)
                    combos[combo_string] = combo

                    if len(remove_options) > 0:
                        for removal in remove_options:
                            del combos[removal]

for key, value in combos.items():
    print(f"{key}: ", value, f"; Sum: {sum(value)}")