from game import Game
from questions import question_bank

print('Quiz game')
print('Answer the following questions by typing true or false')

num_of_question = 0
game = Game(question_bank)
while num_of_question < len(question_bank):
    game.next_question()
    print(f"Score: {game.score}")
print(f"You got {game.score} questions correct")
