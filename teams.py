teams = {}

def add_team(teamid, location, name, league):

    #check if data is valid
    if sum(c.isupper() for c in teamid) > 3 or (not teamid[-2:].isdigit()):
        raise ValueError("Team Id should be less than 3 capital letters and two digits")
    
    if not (location.isalpha() and location.replace(' ','').isalpha()):
        raise ValueError("Invalid location")
    
    if not (name.isalpha() and name.replace(' ','').isalpha()):
        raise ValueError("Invalid name")
    
    if not (league.isalpha() and len(league) == 1 and league.isupper()):
        raise ValueError("Invalid league")

    teams[teamid] = {'Location': location, 'Name': name, 'League': league}
    print(teams)
    print("Team added to the database")
    return None

def load_teams():
    pass

def print_teams():
    pass

def teams_by_city():
    pass

