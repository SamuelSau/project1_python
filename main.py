import sys

'''
By: Samuel Sau

This program is a database of coaches and teams in the NBA. 
It can add coaches and teams to the database, load coaches and teams from a file, print coaches and teams, 
print coaches and teams by name or city, print the best coach in a season, and search for coaches by name, city, or team.

Use 'python3 main.py' to run python program
Use 'help' to see usage
Use 'exit' to exit program
'''

#initialize list data structure
coaches = []
teams = []

#importing functions from coaches.py and teams.py
from coaches import add_coach
from coaches import load_coaches
from coaches import print_coaches
from coaches import coaches_by_name
from coaches import best_coach
from coaches import search_coaches

from teams import add_team
from teams import load_teams
from teams import print_teams
from teams import teams_by_city

def main_loop():
    print('The mini-DB of NBA coaches and teams')
    print('Please enter a command.  Enter "help" for a list of commands.')

    while True:
        command = input("Enter command: ")
        sys.argv = command.split()

        if sys.argv[0] == 'help' and len(sys.argv) == 1:
            print("Usage: <command> <arguments>")
            print("Commands:                      Arguments:")
            print("add_coach                      ID SEASON FIRST_NAME LAST_NAME SEASON_WIN SEASON_LOSS PLAYOFF_WIN PLAYOFF_LOSS TEAM")
            print("add_team                       ID LOCATION NAME LEAGUE")
            print("load_coaches                   FILENAME")
            print("load_teams                     FILENAME")
            print("print_coaches")
            print("print_teams")
            print("coaches_by_name                LAST_NAME")
            print("teams_by_city                  CITY_NAME")
            print("best_coach")
            print("search_coaches                 field=value1, field=value2, ...")
            sys.exit(1)
 
        elif sys.argv[0] == 'exit' and len(sys.argv) == 1:
            print("Exiting... goodbye!")
            sys.exit(1)

        elif sys.argv[0] == 'add_coach':
            #if command line arguments are not 10, then print usage and exit
            if len(sys.argv) != 10:
                print("Usage: add_coach ID SEASON FIRST_NAME LAST_NAME SEASON_WIN SEASON_LOSS PLAYOFF_WIN PLAYOFF_LOSS TEAM")
                sys.exit(1)
            
            add_coach(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], coaches)
            
        elif sys.argv[0] == 'add_team':
            
            if len(sys.argv) != 5:
                print("Usage: add_team ID LOCATION NAME LEAGUE")
                sys.exit(1)

            add_team(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], teams)
            
        elif sys.argv[0] == 'load_coaches':

            if len(sys.argv) != 2:
                print("Usage: load_coaches FILENAME")
                sys.exit(1)

            load_coaches(sys.argv[1], coaches)

        elif sys.argv[0] == 'load_teams':
            
            if len(sys.argv) != 2:
                print("Usage: load_teams FILENAME")
                sys.exit(1)

            load_teams(sys.argv[1], teams)

        elif sys.argv[0] == 'print_coaches':

            if len(sys.argv) != 1:
                print("Usage: print_coaches")
                sys.exit(1)

            print_coaches(coaches)

        elif sys.argv[0] == 'print_teams':

            if len(sys.argv) != 1:
                print("Usage: print_teams")
                sys.exit(1)

            print_teams(teams)

        elif sys.argv[0] == 'coaches_by_name':

            if len(sys.argv) < 2 or len(sys.argv) > 3:
                print("Usage: coaches_by_name LASTNAME")
                sys.exit(1)
            
            #last name can be 1 or 2 words, so we need to check if there are 2 words
            if len(sys.argv) == 2:
                lastname = sys.argv[1]
            else:
                lastname = sys.argv[1] + " " + sys.argv[2]
            
            coaches_by_name(lastname, coaches)

        elif sys.argv[0] == 'teams_by_city':

            if len(sys.argv) != 2:
                print("Usage: teams_by_city CITYNAME")
                sys.exit(1)

            teams_by_city(sys.argv[1], coaches, teams)

        elif sys.argv[0] == 'best_coach':

            if len(sys.argv) != 2:
                print("Usage: best_coach SEASON")
                sys.exit(1)

            best_coach(sys.argv[1], coaches)

        elif sys.argv[0] == 'search_coaches':

            if len(sys.argv) < 2:
                print("Usage: search_coaches field1=value1 field2=value2 ...")
                sys.exit(1)
            else:
                fields = {}
                for arg in sys.argv[1:]:
                    field, value = arg.split("=")
                    fields[field] = value
                search_coaches(coaches, **fields)

        else:
            print("Invalid command. Use help to see usage")
            sys.exit(1)

if __name__ == '__main__':
    main_loop()