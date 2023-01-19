import sys
from coaches import add_coach
from coaches import load_coaches
from teams import add_team

'''
By: Samuel Sau

This program is a database of coaches and teams in the NBA. 
It can add coaches and teams to the database, load coaches and teams from a file, print coaches and teams, 
print coaches and teams by name or city, print the best coach in a season, and search for coaches by name, city, or team.

Use python3 main.py help to see usage
'''

#check for command line arguments

if sys.argv[1] == 'help':
    print("Usage: python3 get.py <command> <arguments>")
    print("Commands:                      Arguments:")
    print("add_coach                      ID SEASON FIRST_NAME LAST_NAME SEASON_WIN SEASON_LOSS PLAYOFF_WIN PLAYOFF_LOSS TEAM")
    print("add_team                       ID LOCATION NAME LEAGUE")
    print("load_coaches")
    print("load_team")
    print("print_coaches")
    print("print_teams")
    print("coaches_by_name                LAST_NAME")
    print("teams_by_city                  CITY_NAME")
    print("best_coach")
    print("search_coaches                 field=VALUE")
    
if sys.argv[1] == 'add_coach':
    #if command line arguments are not 9, then print usage and exit
    if len(sys.argv) != 12:
        print("Usage: python3 get.py add_coach coachid season firstname lastname season_win season_loss playoff_win playoff_loss team")
        sys.exit(1)
    add_coach(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])

elif sys.argv[1] == 'add_team':
    
    if len(sys.argv) != 6:
        print("Usage: python3 get.py add_team teamid location name league")
        sys.exit(1)
    add_team(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

elif sys.argv[1] == 'load_coach':
    if len(sys.argv) != 3:
        print("Usage: python3 get.py load_coach filename")
        sys.exit(1)
    load_coaches()

elif sys.argv[1] == 'load_team':
    pass