class Game:
    def __init__(self, question_list):
        self.question_num = 1
        self.question = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question]
        player_answer = input(f"Q{self.question_num}: {current_question.question}: ")
        if player_answer == current_question.answer:
            self.score += 1
        self.question += 1
        self.question_num += 1