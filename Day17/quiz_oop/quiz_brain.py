class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list 
        self.score = 0
    
    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ").capitalize()
        self.check_answer(user_answer, curr_question.answer)
    
    def still_has_question(self):
        total_questions = len(self.question_list)
        return self.question_number < total_questions
        
    def check_answer(self, user_answer, correct_answer):

        if (user_answer.lower() == correct_answer.lower()):
            print("\tYou got it right")
            self.score += 1
        else:
            print("\tThat's wrong. ")

        print(f"\tYour current score is: {self.score}/{self.question_number}")
        print(f"\tThe correct answer was: {correct_answer}\n")


        

