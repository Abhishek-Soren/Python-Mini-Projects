class QuizBrain:

    def __init__(self, my_list):
        self.question_number = 0
        self.question_list = my_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question} (True/False) : ").lower()
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, my_answer, true_answer):
        if my_answer == true_answer:
            self.score += 1
            print(f"You got it right. Hurrayy!! ")
        else:
            print(f"You got it wrong. Sedd! T_T")
            print(f"The correct answer is {true_answer}")
        print(f"Current Score : {self.score}/{self.question_number}")
        print("\n")
