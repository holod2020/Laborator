class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [  # Вопрси к викторне 
    '1. Компетентнісно орієнтованим навчанням передбачено, що першим етапом планування сучасного навчального заняття є\n(a) формулювання взаємозумовлених мети та результатів\n(b) вибір форм і методів організації діяльності учнів\n(c) аналіз змісту відповідної навчальної літератури\n\n',
    '2. Порушенням академічної доброчесності НЕ є\n(a) свідоме заниження оцінки\n(b) занадто розлоге цитування\n(c) вигадування наукових фактів\n\n',
    '3. На якому етапі уроку відбувається відтворення раніше засвоєних знань учнів, що на них ґрунтується вивчення нового навчального матеріалу, а також їх застосування в новій ситуації?\n(a) актуалізація\n(b) узагальнення\n(c) закріплення\n\n',
    '4. До природно-техногенних небезпек належить\n(a) землетрус\n(b) повінь\n(c) смог\n\n',
    '5. Укажіть прояв негативного впливу будівництва гідроелектростанцій на природні екосистеми.\n(a) радіоактивне забруднення\n(b) загазованість атмосфери\n(c) загазованість атмосфери\n\n'
]

questions = [  #виставил какие правильные ответи через индекс
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c")
]


def run_test(questions):
    score = 0  # Счетчик балов пользователя
    for question in questions:  # вопрос
        answer = input(question.prompt)  #ответ пользователя
        if answer == question.answer:
            score += 1
        if score < 5:
            print(" Вибачте але ви нам не підходите")
        else:
            print("Вітаю ви пройшли тест")

    print(' Вимаете ' + str(score) + ' із ' + str(len(questions)) + ' Балів')


run_test(questions)
