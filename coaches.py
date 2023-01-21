import csv

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

    #store most recent into a list using tuple and explicitly convert to int
    coaches.append((coachid, int(season), firstname, lastname, int(season_win), int(season_loss), int(playoff_win), int(playoff_loss), team))
    print("Coach added to the database")
    return coaches

def load_coaches(filename, coaches):

    #check if filename is valid
    # if filename != 'coaches_season.txt':
    #     raise ValueError('Invalid filename. Expected coaches_season.txt')

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) #skip first line
        for row in reader:
            coachid, year, _, firstname, lastname, season_win, season_loss, playoff_win, playoff_loss, team = [item.strip() for item in row]
            coaches.append((coachid, int(year), firstname, lastname, int(season_win), int(season_loss), int(playoff_win), int(playoff_loss), team))
    
    return coaches

def print_coaches(coaches):
    
    # for i in range(len(coaches)):
    #     print(coaches[i])
    for coach in coaches:
        print("{:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}".format(coach[0], coach[1], coach[2], coach[3], coach[4], coach[5], coach[6], coach[7], coach[8]))
    return None

def coaches_by_name(lastname, coaches, teams):
    #FIND COACHES BY LAST NAME IN COACHES
    for coach in coaches:
        #handle test cases where coach's last name has a + in it
        coach_lastname = lastname.replace('+', ' ')
        if coach_lastname == coach[3]:
            
            team_id = coach[8]
            team = [t for t in teams if t[0] == team_id][0]
            location = team[1]
            team_name = team[2]
            print(coach[0], coach[1], coach[2], coach[3], coach[4], coach[5], coach[6], coach[7], coach[8], location, team_name)
    
    return None

def best_coach(season, coaches):
    best_coach = ""
    max_net_wins = float("-inf")
    for coach in coaches:
        if str(coach[1]) == season:
            net_wins = (int(coach[4]) - int(coach[5])) + (int(coach[6]) - int(coach[7]))
            if net_wins > max_net_wins:
                max_net_wins = net_wins
                best_coach = coach[2] + " " + coach[3]
    print(best_coach)
    return None

def search_coaches(coaches, **fields):
    matching_coaches = []
    for coach in coaches: 
        match = True
        for field, value in fields.items(): 
            if field == 'coach_id':
                if coach[0] != value:
                    match = False
    
            if field == 'season':
                if coach[1] != value:
                    match = False
                    
            if field == 'firstname': 
                if coach[2] != value: 
                    match = False
                    
            if field == 'lastname':
                if coach[3] != value:
                    match = False
                    
            if field == 'season_wins':
                if coach[4] != value:
                    match = False
                    
            if field == 'season_losses':
                if coach[5] != value:
                    match = False
                    
            if field == 'playoff_wins':
                if coach[6] != value:
                    match = False
                    
            if field == 'playoff_losses':
                if coach[7] != value:
                    match = False
                    
            if field == 'team':
                if coach[8] != value:
                    match = False
            
        if match:
            matching_coaches.append(coach)

    for coach in matching_coaches:
        print(coach)
    
    return None