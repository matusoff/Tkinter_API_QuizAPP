from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

#once the code hits the line below, it is going to create a new object from the QuizInterface class 
# and hits the __init__ method
#so the quiz created in QiuzBrain will pass into QuizInterface and to catch it we have to add another parameter
#in ui.py __init__(self) --> __init__(self, quiz_brain)
#and then create a property self.quiz = quiz_brain
quiz_ui = QuizInterface(quiz)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
