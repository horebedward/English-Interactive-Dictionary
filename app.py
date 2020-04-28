import re
from difflib import SequenceMatcher,get_close_matches
data = open('data.json','r').read()
dic = eval(data)



def translate():
	
	while True:
		user = input('Enter a word: ')
		user = user.lower()
		if user in dic:
			return dic[user]
		elif user.title() in dic:
			return dic[user.title()]
		elif user.upper in dic:
			return dic[user.upper()]
		elif len(get_close_matches(user,dic.keys())) > 0:
			user_in = input(f'Did you mean {get_close_matches(user,dic.keys())[0]} instead ? type y if Yes or n No: ')
				
			if user_in.lower() == 'y':
				return dic[get_close_matches(user,dic.keys())[0]]
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

