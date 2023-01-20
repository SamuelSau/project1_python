teams = {}

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

    #store into dictionary
    teams[teamid] = {location, name, league}
    
    print("Team added to the database")
    return teams

def load_teams():
    with open("teams.txt", 'r') as f:
        for line in f:
            line = line.strip().split(',')
            add_team(line[0], line[1], line[2], line[3])
def print_teams(teams):

    print(teams)
    
    return

def teams_by_city(cityname, coaches, teams):
    
    #check if cityname is valid 
    
    
    #access location in teams dictionary (cityname == location)
    #access coaches dictionary
    #query and print the information of teams in that city
    #query and print the information of coaches of teams in that city (each coach in each line)
    #e.g. cityname = Baltimore
    #Bob Leonard, BAL,Baltimore,Bullets,N
    #...
    #Buddy,Jeannette,BA1,Baltimore,Bullets,N
    pass
