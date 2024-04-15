import csv

# Declaring variables and class(es)
choose_to_play = True

# Program starts
print(
    """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$$\      $$\  $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$\  $$$$$$\        $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$$\        $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$$\ 
$$$\    $$$ |$$  __$$\\__$$  __|\__$$  __|$  |$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |\_$$  _|\__$$  __|      $$  __$$\ $$ |  $$ |\_$$  _|\____$$  |
$$$$\  $$$$ |$$ /  $$ |  $$ |      $$ |   \_/ $$ /  \__|      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  \__|$$ |  $$ |  $$ |     $$ |         $$ /  $$ |$$ |  $$ |  $$ |      $$  / 
$$\$$\$$ $$ |$$$$$$$$ |  $$ |      $$ |       \$$$$$$\        $$ |  $$ |$$ |  $$ |$$ |$$$$\ \$$$$$$\  $$$$$$$$ |  $$ |     $$ |         $$ |  $$ |$$ |  $$ |  $$ |     $$  /  
$$ \$$$  $$ |$$  __$$ |  $$ |      $$ |        \____$$\       $$ |  $$ |$$ |  $$ |$$ |\_$$ | \____$$\ $$  __$$ |  $$ |     $$ |         $$ |  $$ |$$ |  $$ |  $$ |    $$  /   
$$ |\$  /$$ |$$ |  $$ |  $$ |      $$ |       $$\   $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |$$ |  $$ |  $$ |     $$ |         $$ $$\$$ |$$ |  $$ |  $$ |   $$  /    
$$ | \_/ $$ |$$ |  $$ |  $$ |      $$ |       \$$$$$$  |      $$$$$$$  | $$$$$$  |\$$$$$$  |\$$$$$$  |$$ |  $$ |$$$$$$\    $$ |         \$$$$$$ / \$$$$$$  |$$$$$$\ $$$$$$$$\ 
\__|     \__|\__|  \__|  \__|      \__|        \______/       \_______/  \______/  \______/  \______/ \__|  \__|\______|   \__|          \___$$$\  \______/ \______|\________|
                                                                                                                                             \___|

WELCOME TO THE QUIZ!
Try to answer the questions!
NOTE: Answers are NOT case-sensitive.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
)

play_choice = input("Would you like to begin? y/n: ").lower()
while play_choice != "y" and play_choice != "n":
    play_choice = input("Please press y or n: ")
if play_choice == "n":
    choose_to_play = False
    print("Well, you're no fun...")

# Start the main game while loop
while choose_to_play:
    print("Let's begin!")

    # Set these to zero here so that on repeat they don't keep increasing
    round_number = 0
    questions = []
    answers = []
    hints = []
    questions_answered_wrongly = []
    wrong_user_answers = []
    hints_for_wrong_questions = []
    number_correct = 0

    # Let the user choose which set of questions to answer
    # Update to compare input to a list of strings based on how many csv files there are?
    chosen_set = input("Which set of questions would you like to try? Type 1, 2, or 3: ")
    while chosen_set != "1" and chosen_set != "2" and chosen_set != "3":
        chosen_set = input("Please type 1, 2, or 3: ")
    chosen_set.strip('"')

    # Take questions, answers, hints from CSV file and append to respective lists
    with open("set{set_number}.csv".format(set_number=chosen_set)) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            questions.append(row[0])
            answers.append(row[1])
            hints.append(row[2])

    for i in range(len(questions)):
        round_number += 1
        print("\nQUESTION {number} of {total}: {question}".format(number=round_number, total=len(questions), question=questions[i]))
        user_answer = input("Type here: ").lower()
        if user_answer == answers[i].lower():
            number_correct += 1
        else: # Add incorrect question, answer, hint to "incorrect" lists for post-game summary
            questions_answered_wrongly.append(questions[i])
            wrong_user_answers.append(user_answer)
            hints_for_wrong_questions.append(hints[i])

    
    print(
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
YOU'VE REACHED THE END OF THE QUIZ!      
You got {number} of {total} questions correct!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""".format(number=number_correct, total=len(questions)))
    
    # If there were any incorrect answers:
    if number_correct < len(questions):
        print("You answered these questions incorrectly: ")
        for i in range(len(questions_answered_wrongly)):
            print("\n{question}".format(question=questions_answered_wrongly[i]))
            print("You answered: {answer}".format(answer=wrong_user_answers[i]))
            print("Here's a hint: {hint}".format(hint=hints_for_wrong_questions[i]))
        print("\nPlay again if you think you know the answers!")

        play_choice = input("Would you like to play again? y/n: ").lower()
        # Make sure not to progress unless user presses y or n
        while play_choice != "y" and play_choice != "n":
            play_choice = input("Please press y or n: ")
        # If no, end the game while loop
        if play_choice == "n":
            choose_to_play = False
            print("\nThanks for playing!")
    # If every answer was correct:
    else:
        print("You got every question correct! Well done!")
        play_choice = input("Would you like to play again? y/n: ").lower()
        # Make sure not to progress unless user presses y or n
        while play_choice != "y" and play_choice != "n":
            play_choice = input("Please press y or n: ")
        # If no, end the game while loop
        if play_choice == "n":
            choose_to_play = False
            print("\nThanks for playing!")