import random_gen

def over(game) : # check kardan inke bazi be etmam reside ya na. agar tamam nashode 0 bargardan
                 # dar gheir in soorat shomare bazikon barande ra bargardan.
                 # va agar bazi mosavi shode va digar nemitavan harkati kard -1 bargardan
    if (game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] != 0) : # ghotri
        return game[0][0]
    if (game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[2][0] != 0) :
        return game[2][0]
    t = 3
    while (t > 0) : # check amoodi
        t -= 1
        if (game[0][t] == game[1][t] and game[1][t] == game[2][t] and game[2][t] != 0) :
            return game[2][t]
    t = 3
    while (t > 0) : # check ofoghi
        t -= 1
        if (game[t][0] == game[t][1] and game[t][1] == game[t][2] and game[t][0] != 0) :
            return game[t][2]
    
    cnt = 0 # tedad khane khali
    t = 0
    while (t < 3) : # shomaresh tedad khane haye khali
        k = 0
        while (k < 3) :
            if (game[t][k] == 0) :
                cnt += 1
            k += 1
        t += 1
    
    if (cnt == 0) : # agar hich khane ee khali namande ast -1 bargardan
        return -1
    
    return 0


def print_game(game) : # print kardan safhe bazi
    t = 0
    while (t < 3) :
        k = 0
        s = ""
        while (k < 3) :
            if (game[t][k] == 0) :
                s += " "
            elif (game[t][k] == 1) :
                s += "X"
            elif (game[t][k] == 2) :
                s += "O"
            s += "|"
            k += 1
        print(s[0:-1])
        if (t != 2) :
            print("-+-+-")
        t += 1
    
    print("\n")

    
game = [[0, 0, 0],[0, 0, 0], [0, 0, 0]] # meghdar dahi avalie safhe bazi

rnd = random_gen.rand()

mode = input("(1) : PvP\n(2) : PvC\n(1 / 2) : ") # entekhab halat bazi

if (mode != "1" and mode != "2") :
    raise Exception("vorudi eshtebah")

print_game(game)

while (True) :
    x, y = input("X - (x, y) : ").replace(",", " ").split() # vorudi x va y
    x = int(x) - 1
    y = int(y) - 1
    while (x < 0 or y < 0 or y > 2 or x > 2 or game[x][y] != 0) : # ta zamani ke eshtebah bood vorudi begir
        x, y = input("Invalid input.\n(x, y) : ").replace(",", " ").split()
        x = int(x) - 1
        y = int(y) - 1
    
    
    game[x][y] = 1 # dar an khane x bezar
    print_game(game)
    
    
    if (mode == '2') : # agar bazi tamam shode bud peygham monaseb ra chap kon ba tavajoh be noe bazi
        if (over(game) == -1) : 
            print("Game Over. tie")
            break
        elif (over(game) == 1) :
            print("You won!")
            break
        elif (over(game) == 2) :
            print("Game Over. You lost")
            break
    else :
        if (over(game) == -1) :
            print("Game Over. tie")
            break
        elif (over(game) == 1) :
            print("Game Over. X wins")
            break
        elif (over(game) == 2) :
            print("Game Over. O wins")
            break
    
    x = 0
    y = 0
    
    if (mode == '1') : # agar pvp ast dobare vorudi begir ta zamani ke dorost vared konand
        x, y = input("O - (x, y) : ").replace(",", " ").split()
        x = int(x) - 1
        y = int(y) - 1
        while (x < 0 or y < 0 or y > 2 or x > 2 or game[x][y] != 0) :
            x, y = input("Invalid input.\n(x, y) : ").replace(",", " ").split()
            x = int(x) - 1
            y = int(y) - 1
    else : # va agar ba computer bod yek mokhtasat entekhab kon ta vaghti ke ghabel ghabul shavad
        x = rnd.rand_int(0, 2)
        y = rnd.rand_int(0, 2)
        while (x < 0 or y < 0 or y > 2 or x > 2 or game[x][y] != 0) :
            x = rnd.rand_int(0, 2)
            y = rnd.rand_int(0, 2)
    
    
    game[x][y] = 2 # dar an khane O begozar va print kon
    print_game(game)
    
    
    if (mode == '2') : # agar bazi tamam shode bud peygham monaseb ra chap kon ba tavajoh be noe bazi
        if (over(game) == -1) : 
            print("Game Over. tie")
            break
        elif (over(game) == 1) :
            print("You won!")
            break
        elif (over(game) == 2) :
            print("Game Over. You lost")
            break
    else :
        if (over(game) == -1) :
            print("Game Over. tie")
            break
        elif (over(game) == 1) :
            print("Game Over. X wins")
            break
        elif (over(game) == 2) :
            print("Game Over. O wins")
            break
    
    