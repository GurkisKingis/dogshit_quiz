# variables and class(es)
round = 0
questions = []
answers = []

answered_correctly = False

class Question:
    question_counter = 0

    def __init__(self, question="Question", answer="Answer"):
        self.question = question
        self.answer = answer
        Question.question_counter += 1
        self.question_id = Question.question_counter

        questions.append(self.question)
        answers.append(self.answer)

    
    def print_question(self):
        pass
    

# Creating my questions here
q1 = Question("What is my name?", "Matt")
q2 = Question("How old am I?", "30")
q3 = Question("Which country do I want to move to?")


# Program starts here
print(
    """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WELCOME TO THIS DOGSHIT QUIZ!
I HAVE NO IDEA WHAT I'M DOING!

Please try to answer the questions without judging me!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
)

if input("Would you like to begin? y/n: ").lower() == "y":
    print("Let's begin!")

# print(questions)
# print(answers)