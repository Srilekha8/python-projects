from question_model import Question
from  data import question_data
from quiz_brain import Quizbrain

question_bank= []

correct = True
score = 0

for i in question_data:
    question = Question(i["question"], i["correct_answer"])
    question_bank.append(question)

quiz = Quizbrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("your quiz is completed")
print(f"your final score is {quiz.score}/{quiz.question_num}")

