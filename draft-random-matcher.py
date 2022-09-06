import random

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  Below code to define number of teams in the league

def get_number_of_teams() :
    while True :
        try :
            number_of_teams = int(input("\nHow many teams are in the SFFFL?   "))
        except :
            print("\nInvalid input: Input must be a whole number!\n")
            continue
        else :
            return number_of_teams

number_of_teams = get_number_of_teams()

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  Below code to populate list of managers in the league

def get_manager_names() :
    manager_names = []
    i = 1
    while len(manager_names) < number_of_teams :
        manager_names.append(input("Enter the first name and last initial for the manager of Team " + str(i) + ":   "))
        i += 1
    return manager_names

manager_names = get_manager_names()

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  Below code gives the option of adding team names
  #  1) ask if user wants team names 2) if yes, ask for team name one by one for each manager and create list of just team names
  #  3) if no, go to next step 4) if invalid, print message and ask again 5) return teams list and make another list combining managers
  #  with their corresponding team name

team_names = []

def get_team_names() :
    while True :
        teams_y_n = input("\nWould you like to enter each manager's team name?   (Y for yes, N for no)   ")
        if teams_y_n == "Y" :
            i = 0
            while len(team_names) < number_of_teams :
                team_names.append(input("Enter the name of " + manager_names[i] + "'s team:   "))
                i += 1
            return team_names
            break
        elif teams_y_n == "N" :
            print("\nOkay! Let's move to the next step.")
            break
        else :
            print("\nInvalid Input:   Make sure you enter either Y for yes or N for no")
            continue

team_names = get_team_names()
if team_names :
    managers_and_teams = list(zip(manager_names,team_names))

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  Below Code to gather info about match options and create the list for matching

match_options = []

def get_match_options() :
    print("\nYou will need to input " + str(number_of_teams) + " options for teams to be matched with below...")
    i = 1
    while len(match_options) < number_of_teams :
        match_options.append(input("Enter potential match option #" + str(i) + ":   "))
        i += 1
    return match_options

match_options = get_match_options()

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  Below code is used to create the final list
#    if team names were entered, will create list with format (manager, team, random match)
#    if team names were not entered, will create list with format (manager, random match)

random.shuffle(match_options)
final_list = []

if team_names :
    i = 0
    for name_team in managers_and_teams :
        match = name_team + (match_options[i], )
        final_list.append(match)
        i += 1
else :
    i = 0
    for name in manager_names :
        match = (name, match_options[i])
        final_list.append(match)
        i += 1

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  All code is done!! Time to write the code for the final output
  #  dependent upon earlier inputs, print all matches in a polished format

print("\n\nOkay! Time to see who is matched with who...\n\nDrumroll please...\n\n")

if team_names :
    for entry in final_list :
        print(entry[0] + " aka " + entry[1] + "... your draft position will be determined by: " + entry[2] + "!")
else :
    for entry in final_list :
        print(entry[0] + "... your draft position will be determined by: " + entry[1] + "!")

print("\n\nGood luck to everyone!\n")
print("Except for you " + random.choice(manager_names) + "... just cause.\n\nSorry baht it.\n\n")