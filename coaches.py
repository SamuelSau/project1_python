
def add_coach(coachid, season, firstname, lastname, season_win, season_loss, playoff_win, playoff_loss, team, coaches):

     #check if data is valid
    if sum(c.isupper() for c in coachid) > 7 or (not coachid[-2:].isdigit()) or len(coachid) > 9:
        raise ValueError("Coach Id should be less than 7 capital letters and two digits")
    
    if not (len(season) == 4 and season.isdigit()):
        raise ValueError("Season should be a 4-digit year")
    
    if not (firstname.isalpha() and firstname.replace(' ','').isalpha() and firstname[0].isupper()):
        raise ValueError("Invalid first name")

    if not (lastname.isalpha() and lastname.replace(' ','').isalpha() and lastname[0].isupper()):
        raise ValueError("Invalid last name")

    if not (season_win.isdigit() and int(season_win) >= 0):
        raise ValueError("Season wins should be a non-negative integer")

    if not (season_loss.isdigit() and int(season_loss) >= 0):
        raise ValueError("Season losses should be a non-negative integer")

    if not (playoff_win.isdigit() and int(playoff_win) >= 0):
        raise ValueError("Playoff wins should be a non-negative integer")

    if not (playoff_loss.isdigit() and int(playoff_loss) >= 0):
        raise ValueError("Playoff losses should be a non-negative integer")

    if not (team.isalnum() and team.isupper() and len(team) == 3):
        raise ValueError("Team should be capital letters and/or digits")

    #store most recent into dictionary
    coaches[coachid] = {season, firstname, lastname, season_win, season_loss, playoff_win, playoff_loss, team}
    
    print("Coach added to the database")
    return coaches

def load_coaches():
    with open("coaches.txt", 'r') as f:
        for line in f:
            line = line.strip().split(',')
            add_coach(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])

def print_coaches(coaches):
    
    print(coaches)
    
    return

def coaches_by_name():
    pass

def best_coach():
    pass

def search_coaches():
    pass