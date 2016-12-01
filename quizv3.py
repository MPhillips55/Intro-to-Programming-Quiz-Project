#Quiz Game Project
#Michael Phillips

easy_questions = ["A ________ is a pointer to an object.", "_________, or procedures, contain code that is likely to be reused.", 
"______ are passed to a function.", "_______ are returned from a function."]

med_questions = ["A ___ loop will iterate through through an entire list object.", "A _____ loop will run only when certain conditions are met.", 
"3. A ____ is used to hold any number of objects, and can be accesed by using an index.", "_________ is the process of finding and fixing errors in code."]

hard_questions = ["The ___ operator is another way to pass parameters to a function.", "__________ are passed into a function.", 
"____ cases are used to verify code is working as intended.", "Proper ___________ is required for python code to compile."]

easy_answers = ["variable", "functions", "inputs", "outputs"]

med_answers = ["for", "while", "list", "debugging"]

hard_answers = ["dot", "parameters", "test", "indentation"]

easy_sentences = ["A VARIABLE is a pointer to an object.", "FUNCTIONS, or procedures, contain code that is likely to be reused.", 
"INPUTS are passed to a function.", "OUTPUTS are returned from a function."]

med_sentences = ["A FOR loop will iterate through through an entire list object.", "A WHILE loop will run only when certain conditions are met.", 
"A LIST is used to hold any number of objects, and can be accesed by using an index.", "DEBUGGING is the process of finding and fixing errors in code."]
 
hard_sentences = ["The DOT operator is another way to pass parameters to a function.", "PARAMETERS are passed into a function.", 
"TEST cases are used to verify code is working as intended.", "Proper INDENTATION is required for python code to compile."]

#Main game flow, including introduction, leads to user choice on # of guesses, level select, and the question/input function
def game_flow():
	print ""
	print "Hello, welcome to an Introduction to Programming Quiz on Key Topics!"
	print ""
	print "Type in the correct response when prompted to advance further in the quiz."
	guesses_left = num_guesses()
	diff_level = level_select()
	print ""
	print "Type in the correct response when prompted to advance further in the quiz."
	if diff_level == 1:
		ask_question(easy_questions, easy_answers, easy_sentences, guesses_left)
	if diff_level == 2:
		ask_question(med_questions, med_answers, med_sentences, guesses_left)
	if diff_level == 3:
		ask_question(hard_questions, hard_answers, hard_sentences, guesses_left)	

#User chooses how many guesses they will have before they lose.
def num_guesses():
	print ""
	print "How many guesses do you think you need before the game will end?"
	while True:
		try:
			chances = int(raw_input("Enter a number between 1 and 5: "))
			if 1 <= chances <= 5:
				return chances
			print "Please enter a number between 1 and 5."	
		except ValueError:
			print ""
			print "Please enter a number between 1 and 5."	
			print ""

#User picks their difficulty level
def level_select():
	print ""
	print "Level Select: Enter 1 for EASY difficulty, 2 for MEDIUM, or 3 for HARD."
	while True:
		try:
			level_input = int(raw_input("Enter 1, 2, or 3: "))
			if level_input == 1:
				print "You chose Easy!"
				return level_input
			if level_input == 2:
				print "You chose Medium!"
				return level_input
			if level_input == 3:
				print "You chose Hard!"
				return level_input
			print ""
			print "Please enter a number between 1 and 3."	
		except ValueError:
			print ""
			print "Please enter a number between 1 and 3."	

#Checks whether or not the user is out of guesses based on the value they chose. 
def check_guesses(guesses_left):
	total_guesses = guesses_left
	if total_guesses > 1:
		print ""
		print "You have " + str(guesses_left) + " guesses left."
	elif total_guesses == 1:
		print ""
		print "You have " + str(guesses_left) + " guess left."
	elif total_guesses == 0:
		print ""
		print "You lost. Type 1 to play again, or 2 to quit the game."
		print ""
		end_game()
	return

#Asks the user a quiz question, checks the answer. 
def ask_question(list_of_questions, list_of_answers, sentence_list, guesses_left):
	total_questions = len(list_of_questions)
	question_index = 0
	while question_index < total_questions:
		check_guesses(guesses_left)
		print ""
		print list_of_questions[question_index]
		print ""
		user_answer = (raw_input("Type in the answer: ").lower())
		if list_of_answers[question_index] in user_answer:
			print_right_answer(sentence_list, question_index)
			print "Great job!"
			question_index += 1
		else:
			guesses_left -= 1
	print ""
	print "Congrats! You won! To return to level select enter '1'. To quit the game, type '2'"
	print ""
	end_game()

#Prints the complete quiz question if the user enters the answer.
def print_right_answer(sentence_list, question_index):
	print ""
	print sentence_list[question_index]
	print ""
	return

def end_game():
'''User can chose whether to restart the game or to quit the program'''	
	while True:
		try:
			game_end_input = int(raw_input("1 to play again, 2 to quit: "))
			if game_end_input == 1:
				game_flow()
			if game_end_input == 2:
				exit()
			print "Please enter 1 or 2."
		except ValueError:
			print ""
			print "Please enter 1 or 2."
			print ""
	
game_flow()