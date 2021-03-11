# Author: Diego Saldonid
# Date: 3/4/2021
# Description: Creating database for pdf files 

#create database with three types of puzzles
puzzles_database = {'Easy':[],'Medium':[],"Hard":[]}



import requests 
from bs4 import BeautifulSoup as bs
import json 

#helper function to format puzzles
def format_puzzles(puzzle):
	'''
	input:1-D sudoku puzzle
	returns:2-D sudoku puzzle
	'''

	ret= [] #initialzing our 2-d array
	current_row =[]
	for i in range(len(puzzle)):
		current_row.append(puzzle[i])
		
		#add our row when it is complete 
		if len(current_row) ==9:
			ret.append(current_row)
			current_row =[]

	return ret


#load the webpage
r= requests.get('https://www.nytimes.com/puzzles/sudoku/medium')

#convert to bs4 object
soup = bs(r.text,"html.parser")

#only need the first script tag 
for el in soup.find_all("script",attrs= {"type":"text/javascript"}):
	#the text of this bs el contains puzzle information
	s= el.string
	break

#convert our bs object to a dictionary string to comvert to a dictionary
dict_string = str(s[18:])
puzzle_data = json.loads(dict_string)

print(format_puzzles(puzzle_data['hard']['puzzle_data']['solution']))

#add to our database
puzzles_database['Easy'].append(format_puzzles(puzzle_data['easy']['puzzle_data']['puzzle']))

puzzles_database['Medium'].append(format_puzzles(puzzle_data['medium']['puzzle_data']['puzzle']))

puzzles_database['Hard'].append(format_puzzles(puzzle_data['hard']['puzzle_data']['puzzle']))

# print(puzzles_database['Hard'][0])