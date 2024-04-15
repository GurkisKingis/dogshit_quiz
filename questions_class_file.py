class Question:
    question_counter = 0

    def generate_hint(word):
        new_word = ""
        for i in range(len(word)):
            if word[i] == " ":
                new_word += word[i]
            if i % 2 == 0:
                new_word += word[i]
        if new_word[-1] != word[-1]:
            new_word += word[-1]
        return new_word
    
    def __init__(self, question="Question", answer="Answer"):
        self.question = question
        self.answer = answer
        self.id = Question.question_counter
        Question.question_counter += 1

        questions.append(self.question)
        answers.append(self.answer)
        self.hint = Question.generate_hint(answer)
        hints.append(self.hint)
    
