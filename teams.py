import csv

def add_team(teamid, location, name, league, teams):

    print(teamid)

    #check if data is valid
    if len(teamid) != 3 or (not teamid.isupper() and any(c.isalpha() for c in teamid)):
        raise ValueError("Team Id should be less than 3 capital letters and two digits")
    
    if not (location.isalpha() and location.replace(' ','').isalpha()):
        raise ValueError("Invalid location")
    
    if not (name.isalpha() and name.replace(' ','').isalpha()):
        raise ValueError("Invalid name")
    
    if not (league.isalpha() and len(league) == 1 and league.isupper()):
        raise ValueError("Invalid league")

    #store into tuple
    teams.append((teamid, location, name, league))

    print("Team added to the database")
    return teams

def load_teams(filename, teams):

    # if filename != 'teams.txt':
    #     raise ValueError('Invalid filename. Expected teams.txt')

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) #skip first line
        for row in reader:
            teamid, location, name, league = [item.strip() for item in row]
            teams.append((teamid, location, name, league))
    return teams

def print_teams(teams): 
    for team in teams:
        print("{:<4} {:<4} {:<4} {:<4}".format(team[0], team[1], team[2], team[3]))
    return None

def teams_by_city(cityname, coaches, teams):
    
    matching_teams = []
    for team in teams:
        if team[1] == cityname:
            matching_teams.append(team)
    for team in matching_teams:
        team_id = team[0]
        matching_coaches = {coach[3] for coach in coaches if coach[8] == team_id}
        for coach in matching_coaches:
            print(team[0], team[1], team[2], team[3], coach)
    return None
