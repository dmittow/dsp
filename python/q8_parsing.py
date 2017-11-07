# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import csv

with open('football.csv','r') as f: 
    f_reader = csv.reader(f)
    next(f_reader)
    teams = []
    for line in f_reader:
        teams.append([line[0],int(line[5])-int(line[6])])
    print(sorted(teams, key=lambda t:t[1])[0][0])

