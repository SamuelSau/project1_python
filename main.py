import argparse

#define data structures
coaches = {}
teams = {}

if  __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Database Design Project 1", description="Print a list of commands to interact with database", add_help=True)
    
    # Optional arguments
    parser.add_argument("--add_coach", type=str, nargs=9, metavar=("ID", "SEASON", "FIRST_NAME", "LAST_NAME", "SEASON_WIN", "SEASON_LOSS", "PLAYOFF_WIN", "PLAYOFF_LOSS", "TEAM"), help="Add new coach data")
    parser.add_argument("--add_team", type=str, nargs=4, metavar=("ID", "LOCATION", "NAME", "LEAGUE"), help="Add a new team")
    parser.add_argument("--print_coaches", action="store_true", help="Print a listing of all coaches")
    parser.add_argument("--print_teams", action="store_true", help="Print a listing of all teams")
    parser.add_argument("--coaches_by_name", type=str, metavar="NAME", help="List info of coaches with the specified name")
    parser.add_argument("--teams_by_city", type=str, metavar="CITY", help="List the teams in the specified city")
    parser.add_argument("--load_coach", type=str, metavar="FILENAME", help="Bulk load of coach info from a file")
    parser.add_argument("--load_team", type=str, metavar="FILENAME", help="Bulk load of team info from a file")
    parser.add_argument("--best_coach", type=str, metavar="SEASON", help="Print the name of the coach with the most netwins in a specified season")
    parser.add_argument("--search_coaches", type=str, metavar="VALUE", help="Print the name of the coach satisfying the specified conditions")
    parser.add_argument("--exit", action="store_true", help="Quit the program")

    #parser.add_argument("coach_data", type=str, nargs=9, help="Coach data (ID, SEASON, FIRST_NAME, LAST_NAME, SEASON_WIN, SEASON_LOSS, PLAYOFF_WIN, PLAYOFF_LOSS, TEAM)")
    args = parser.parse_args()
    
    if args.add_coach:
        coachid = args.add_coach[0]
        season = args.add_coach[1]
        firstname = args.add_coach[2]
        lastname = args.add_coach[3]
        season_win = args.add_coach[4]
        season_loss = args.add_coach[5]
        playoff_win = args.add_coach[6]
        playoff_loss = args.add_coach[7]
        team = args.add_coach[8]

            #check if coachid is valid
        if sum(c.isupper() for c in coachid) > 7 or (not coachid[-2:].isdigit()) or len(coachid) > 9:
            raise ValueError("Coach Id should be less than 7 capital letters and two digits")

        coaches[coachid] = {'Season':season, 'First Name':firstname, 'Last Name':lastname, 'Season Win':season_win, 'Season Loss':season_loss, 'Playoff Win':playoff_win, 'Playoff Loss':playoff_loss, 'Team':team}
        print(coaches)
        print("Coach added to the database") #RUSSEJO01 1946 1 John Russell 22 38 0 0 BOS  
    
    elif args.add_team:

        team_data = args.coach_data
        teamid = team_data[0]
        location = team_data[1]
        name = team_data[2]
        league = team_data[3]

        #check if teamid is valid
        if sum(c.isupper() for c in teamid) > 3 or (not teamid[-2:].isdigit()):
            raise ValueError("Team Id should be less than 3 capital letters and two digits")

        teams[teamid] = {location, name, league}
        print(teams)
        print("Team added to the database")

    # elif args.command == "load_coach":
    #     pass
    # elif args.command == "load_team":
    #     pass
    # elif args.command == "print_coaches":
    #     pass
    # elif args.command == "print_teams":
    #     pass
    # elif args.command == "coaches_by_name":
    #     pass
    # elif args.command == "teams_by_city":
    #     pass
    # elif args.command == "best_coach":
    #     pass
    # elif args.command == "search_coaches":
    #     pass
    # else:
    #     print("Invalid command")