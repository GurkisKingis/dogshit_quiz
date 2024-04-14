# variables and class(es)
round_number = 0
questions = []
answers = []
hints = []

questions_answered_wrongly = []
wrong_user_answers = []
hints_for_wrong_questions = []

number_correct = 0
choose_to_play = True

def generate_hint(word):
    new_word = ""
    for i in range(len(word)):
        if word[i] == " ":
            new_word += word[i]
        if i % 2 == 0:
            new_word += word[i]
        else:
            new_word += "_"
    if new_word[-1] != word[-1]:
        new_word += word[-1]
    return new_word


class Question:
    question_counter = 0

    def __init__(self, question="Question", answer="Answer"):
        self.question = question
        self.answer = answer
        self.id = Question.question_counter
        Question.question_counter += 1

        questions.append(self.question)
        answers.append(self.answer)
        self.hint = generate_hint(answer)
        hints.append(self.hint)



# Creating the questions
qs1 = Question("What is the name of the protagonist in the mainline HALO video games?", "Master Chief")
qs2 = Question("What is the title of the second book in the A SONG OF ICE AND FIRE series of novels?", "A Clash of Kings")
qs3 = Question("Who composed the music for the video game THE ELDER SCROLLS: SKYRIM?", "Jeremy Soule")
qs4 = Question("The English, Norwegian, and Dutch languages are part of what language family?", "Germanic")
qs5 = Question("In Physics, what is the name of the force that causes attraction between objects that have mass?", "Gravity")
qs6 = Question("What is the capital of Sweden?", "Stockholm")
qs7 = Question("In the video game DEEP ROCK GALACTIC, what is the name of the dwarves' robotic companion on solo missions?", "Bosco")
qs8 = Question("What is the surname of the character Dominic in the video game GEARS OF WAR?", "Santiago")
qs9 = Question("In the original HALO video games, what is the name of the parasitic threat that aims to consume all life in the galaxy?", "The Flood")
qs10 = Question("What is the name of the protagonist in the TOMB RAIDER video games?", "Lara Croft")



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
        print("\nQUESTION {number}: {question}".format(number=round_number, question=questions[i]))
        print("What is your answer?")
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
            print("\nHere's a hint: {hint}".format(hint=hints_for_wrong_questions[i]))
        print("\nPlay again if you think you know the answers!")
    else:
        print("\nYou got every question correct! Well done!")
    
    play_choice = input("Would you like to play again? y/n: ").lower()
    # Make sure not to progress unless user presses y or n
    while play_choice != "y" and play_choice != "n":
        play_choice = input("Please press y or n: ")
    # If no, end the game while loop
    if play_choice == "n":
        choose_to_play = False







