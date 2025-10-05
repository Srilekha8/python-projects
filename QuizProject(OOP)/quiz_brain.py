class Quizbrain:

    def __init__(self, qlist):
        self.question_num = 0
        self.score = 0
        self.question_list = qlist


    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q.{self.question_num}:{question.text} (True/False) : ")
        self.check_answer(user_ans, question.answer)


    def check_answer(self, userAns, actAns):
        if userAns.lower() == actAns.lower():
            print("You got it right")
            self.score+=1
        else:
            print("your got it wrong")
        print(f"Your current score is {self.score}/{self.question_num}")
        print("\n")

    def still_has_question(self):
        return self.question_num<len(self.question_list)
