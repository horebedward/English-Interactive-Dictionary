import mysql.connector
from difflib import get_close_matches

def translate():
	while True:
		word = input("Enter a word in English and press Enter: ")
		word = word.lower()
		con = mysql.connector.connect(
	    user="ardit700_student", 
	    password = "ardit700_student", 
	    host="108.167.140.122", 
	    database = "ardit700_pm1database"
		)
		cursor = con.cursor()
		query = cursor.execute("SELECT * FROM Dictionary")
		results1 = cursor.fetchall()
		index = dict()
		[index [t[0]].append(t [1]) if t [0] in list(index.keys()) else index.update({t[0]:[t[1]]}) for t in results1]
		
		if word in index:
			return index[word]
		elif word.title() in index:
			return index[word.title()]
		elif word.upper in index:
			return index[word.upper()]
		elif len(get_close_matches(word,index.keys(),cutoff = 0.6)) > 0:
			user_in = input(f'Did you mean {get_close_matches(word,index.keys(),cutoff = 0.6)[0]} instead ? type y if Yes or n No: ')
			if user_in.lower() == 'y':
				return index[get_close_matches(word,index.keys(),cutoff = 0.6)[0]]
			elif user_in.lower() == 'n':
				print("The word doesn't exist.Please double check it ")
				continue
			else:
				return "You type wrong option."

		else:
			return "The word doesn't exist.Please double check it "

output = translate()

if type(output) == list:
	for i in output:
		print(i)
else:
	print(output)


