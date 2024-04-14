# Script file for Terminal Game Project

class Question:
    question_counter = 0

    def __init__(self, question="Question", correct_answer=""):
        self.question = question
        self.correct_answer = ""
        Question.question_counter += 1
        self.question_id = Question.question_counter
    
answered_correctly = False

