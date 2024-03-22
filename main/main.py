class IdGenerator:
    def __init__(self):
        self.generated_id = 0

    def get_next_id(self):
        self.generated_id += 1
        return self.generated_id


#class TextBox:
    #def __init__(self, text):
        #self.text = text
    #def get_text(self):
        #return self.text

class Questions:
    def __init__(self):
        self.id_generator = IdGenerator()

    def generate_questions(self):
        questions = []
        num_questions = int(input("Введите количество вопросов: "))

        for i in range(num_questions):
            question_text = input(f"Введите текст для вопроса {i + 1}: ")
            question_id = self.id_generator.get_next_id()
            question = {'id': question_id, 'text': question_text}
            questions.append(question)
        return questions

    def write_questions_to_file(self, questions, filename):
        with open(filename, 'a+') as f:
            for question in questions:
                f.write(f'ID: {question['id']}\n')
                f.write(f'Вопрос: {question['text']}\n\n')
        print(f"Вопросы записаны в файл '{filename}'")
        f.close()




class AnswersRadio:
    def __init__(self):
        self.id_generator = IdGenerator()

    def generate_answer(self):
        answers = []
        num_answers = int(input("Введите количество вариантов ответа: "))

        for i in range(num_answers):
            answer_text = input(f"Введите вариант ответа {i + 1}: ")
            answer_id = self.id_generator.get_next_id()
            answer = {'id': answer_id, 'text': answer_text}
            answers.append(answer)
        mark = int(input("Введите номер правильного варианта ответа: "))
        mark -= 1
        answers[mark]['text'] = answers[mark]['text'] + " true"

        return answers


    def write_answers_to_file(self, answers, filename):
        with open(filename, 'a+') as stash:
            for answer in answers:
                stash.write(f'ID: {answer['id']}\n')
                stash.write(f'Ответ: {answer['text']}\n\n')
        print(f"Ответы записаны в файл '{filename}'")
        stash.close()

class AnswerCheckBox:
    def __init__(self):
        self.id_generator = IdGenerator()

    def generate_answer(self):
        answers = []
        num_answers = int(input("Введите количество вариантов ответа: "))

        for i in range(num_answers):
            answer_text = input(f"Введите вариант ответа {i + 1}: ")
            answer_id = self.id_generator.get_next_id()
            answer = {'id': answer_id, 'text': answer_text}
            answers.append(answer)

        marks = []
        mark_count = int(input("Введите количество правильных ответов: "))
        for i in range(mark_count):
            mark = int(input(f"Введите номер правильного ответа {i+1}: "))
            mark -= 1
            marks.append(mark)
        for mark in marks:
            answers[mark]['text'] = answers[mark]['text'] + " true"
        return answers

    def write_answers_to_file(self, answers, filename):
        with open(filename, 'a+') as stash:
            for answer in answers:
                stash.write(f'ID: {answer['id']}\n')
                stash.write(f'Ответ: {answer['text']}\n\n')
        print(f"Ответы записаны в файл '{filename}'")
        stash.close()







question = Questions()
question_list = question.generate_questions()
question.write_questions_to_file(question_list, 'test.txt')

var = int(input("Введите, какие тип ответов нужен:\n 1. Один правильный вариант ответа\n 2. Несколько правильных вариантов ответа\n"))

match var:
    case 1:
        answer = AnswersRadio()
        answer_list = answer.generate_answer()
        answer.write_answers_to_file(answer_list, 'answer.txt')
    case 2:
        answers = AnswerCheckBox()
        answer_list1 = answers.generate_answer()
        answers.write_answers_to_file(answer_list1, 'answers.txt')