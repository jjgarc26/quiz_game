from question_model import Question
questions_to_ask = [
    {'text': 'Seahorses have stomachs for the absorption of nutrients from food.', 'answer': 'false'},
    {'text': 'The letter H is between letters G and J on a keyboard', 'answer': 'true'},
    {'text': 'Camels have three sets of eyelashes', 'answer': 'true'},
    {'text': 'There are five zeros in one hundred thousand', 'answer': 'true'},
    {'text': 'There are stars and zigzags on the flag of America', 'answer': 'false'},
    {'text': 'If you add the two numbers on the opposite sides of dice, the answer is always 7', 'answer': 'true'},
    {'text': 'Scallops don\'t have good vision', 'answer': 'false'},
    {'text': 'Your hand has a built in snuff box', 'answer': 'true'},
    {'text': 'The moon is just 50 percent of the mass of Earth.', 'answer': 'false'},
    {'text': 'Nearly three percent of the ice in Antarctic glaciers is penguin urine.', 'answer': 'true'},
    {'text': 'Apes cant laugh.', 'answer': 'false'}]

question_bank = []
for question in questions_to_ask:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)