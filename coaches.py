coaches = {}

def add_coach(coachid, season, firstname, lastname, season_win, season_loss, playoff_win, playoff_loss, team):
    
     #check if data is valid
    if sum(c.isupper() for c in coachid) > 7 or (not coachid[-2:].isdigit()) or len(coachid) > 9:
        raise ValueError("Coach Id should be less than 7 capital letters and two digits")
    
    if not (len(season) == 4 and season.isdigit()):
        raise ValueError("Season should be a 4-digit year")

    if not (firstname.isalpha() and firstname.replace(' ','').isalpha()):
        raise ValueError("Invalid first name")

    if not (lastname.isalpha() and lastname.replace(' ','').isalpha()):
        raise ValueError("Invalid last name")

    if not (season_win.isdigit() and int(season_win) >= 0):
        raise ValueError("Season wins should be a non-negative integer")

    if not (season_loss.isdigit() and int(season_loss) >= 0):
        raise ValueError("Season losses should be a non-negative integer")

    if not (playoff_win.isdigit() and int(playoff_win) >= 0):
        raise ValueError("Playoff wins should be a non-negative integer")

    if not (playoff_loss.isdigit() and int(playoff_loss) >= 0):
        raise ValueError("Playoff losses should be a non-negative integer")

    if not (team.isalnum() and team.isupper()):
        raise ValueError("Team should be capital letters and/or digits")

    coaches[coachid] = {'Season':season, 'First Name':firstname, 'Last Name':lastname, 'Season Win':season_win, 'Season Loss':season_loss, 'Playoff Win':playoff_win, 'Playoff Loss':playoff_loss, 'Team':team}
    print(coaches)
    print("Coach added to the database")
    return None

def load_coaches():
    

def print_coaches():
    pass

def coaches_by_name():
    pass

def best_coach():
    pass

def search_coaches():
    pass