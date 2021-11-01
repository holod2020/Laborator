# from Question import Question # Импорт файла Question и класса question 
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        

question_prompts = [ # Вопрси к викторне 
    'Якого кольру яблуко?\n(a) Червоне/Зелене\n(b) Фіолетове\n(c) Помаранчиве\n\n',
    'Якого кольру Банан?\n(a) Зелений\n(b) Пурпурний\n(c) Жовтий\n\n',
    'Якого кольру полуниця?\n(a) Жовта\n(b) Червона\n(c) Блакитна\n\n',
    'Який місяць коротший за всіх?\n(a) Квітень\n(b) Червень\n(c) Травень\n\n', # Три букви
    'Як зістрибнути з десятиметрових сходів і не розбитися?\n(a) Зістрибнути з першої сходинки\n(b) Зістрибнути з самой верхівки\n(c) Піти до дому\n\n'

]

questions = [ #виставил какие правильные ответи через индекс
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "a")

]

def run_test(questions):
    score = 0 # Счетчик балов пользователя
    for question in questions: # вопрос 
        answer = input(question.prompt)          #ответ пользователя 
        if answer == question.answer:
            score+= 1 
    
    print(' Ти маєш ' + str(score) + ' / ' + str(len(questions)) + ' Балів')

run_test(questions) 



