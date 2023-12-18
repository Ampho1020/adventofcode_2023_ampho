import fileinput

sum_of_ids = 0
max_red = 0
max_green = 0
max_blue = 0

def Valid_ID(stringy):
    #We set up a temporary id number. If the game is impossible, we wimply return 0 and add it nonetheless.
    #impossible_game = False
    power_sum = 0
    min_red = 0
    min_green = 0
    min_blue = 0
    #We parse the line here.
    #First, we find the : , where we need to split the string from Game number and data.
    tmp_stringy = stringy.split(":")
    #We record and trim the "Game X:" from the string
    tmp_id = (int)((tmp_stringy[0].split(" "))[1])
    #Then, we separate the games with the "; ", so we get an array of games played
    game_records = tmp_stringy[1].split("; ")
    #Iterate through the games, and search for the colors and numbers
    for i in range(len(game_records)):
        #This stores the actual iterated game's results. Search one by one for the results, and check with max_colors.
        i_game_results = game_records[i].split(", ")
        #We should split even further, separating with spaces. The first element of the array is the number, for the rest
        # We can use the same tactics as Day 1 
        for j in range(len(i_game_results)):
            #i_game_results.pop(" ")
            i_game_number_of_cubes = i_game_results[j].split(" ")
            if (i_game_number_of_cubes[0] == ""):
                i_game_number_of_cubes.pop(0)
            if (i_game_number_of_cubes[1].find("\n") != -1):
                i_game_number_of_cubes[1] = i_game_number_of_cubes[1].strip("\n")

            if ((int)(i_game_number_of_cubes[0]) > max_red) and i_game_number_of_cubes[1] == "red" and (int)(i_game_number_of_cubes[0]) > min_red:
                #impossible_game = True
                min_red = (int)(i_game_number_of_cubes[0])
            if ((int)(i_game_number_of_cubes[0]) > max_green) and i_game_number_of_cubes[1] == "green" and (int)(i_game_number_of_cubes[0]) > min_green:
                #impossible_game = True
                min_green = (int)(i_game_number_of_cubes[0])
            if ((int)(i_game_number_of_cubes[0]) > max_blue) and i_game_number_of_cubes[1] == "blue" and (int)(i_game_number_of_cubes[0]) > min_blue:
                #impossible_game = True
                min_blue = (int)(i_game_number_of_cubes[0])

    power_sum += min_red * min_green * min_blue
    #...
    #if impossible_game == True:
    #    return 0
    #elif impossible_game == False:
    #    return tmp_id
    return power_sum

for l in fileinput.input(files = "Day2_input.txt"):
    sum_of_ids += Valid_ID(l)

print(sum_of_ids)