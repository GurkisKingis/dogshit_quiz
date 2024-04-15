import csv

# Declaring variables and class(es)
round_number = 0
questions = []
answers = []
hints = []

questions_answered_wrongly = []
wrong_user_answers = []
hints_for_wrong_questions = []

number_correct = 0
choose_to_play = True

with open("questions_answers_hints.csv") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        questions.append(row[0])
        answers.append(row[1])
        hints.append(row[2])

print(questions)
print(answers)
print(hints)


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

WELCOME TO THIS DOGSHIT QUIZ!
I HAVE NO IDEA WHAT I'M DOING!

Please try to answer the questions! Hopefully the program doesn't crash!

PLEASE NOTE: Answers are NOT case-sensitive.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
)


play_choice = input("\nWould you like to begin? y/n: ").lower()
while play_choice != "y" and play_choice != "n":
    play_choice = input("Please press y or n: ")
if play_choice == "n":
    choose_to_play = False
    print("Well, you're no fun... :(")
# Start the game while loop
while choose_to_play:
    print("Let's begin!")

    # Set this to zero here so that on repeat it doesn't keep increasing past the last round number
    round_number = 0

    for i in range(len(questions)):
        round_number += 1
        print("\nQUESTION {number} of {total}: {question}".format(number=round_number, total=len(questions), question=questions[i]))
        user_answer = input("Type here: ").lower()
        if user_answer == answers[i].lower():
            number_correct += 1
        else:
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
    
    if number_correct < len(questions):
        print("\nYou answered these questions incorrectly: ")
        for i in range(len(questions_answered_wrongly)):
            print("\n{question}".format(question=questions_answered_wrongly[i]))
            print("You answered: {answer}".format(answer=wrong_user_answers[i]))
            print("Here's a hint: {hint}".format(hint=hints_for_wrong_questions[i]))
        print("\nPlay again if you think you know the answers!")

        play_choice = input("\nWould you like to play again? y/n: ").lower()
        # Make sure not to progress unless user presses y or n
        while play_choice != "y" and play_choice != "n":
            play_choice = input("Please press y or n: ")
        # If no, end the game while loop
        if play_choice == "n":
            choose_to_play = False
            print("\nThanks for playing!")
    else:
        choose_to_play = False
        print("\nYou got every question correct! Well done!")
        print("Thanks for playing!")