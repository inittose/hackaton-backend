from scheme.users import Create,Maindata,Acsess1,Question,Answer,Q
import os

class Test:
    # Авторизация
    def avtorization(self, name: str, password: str) -> bool:
        file = open("Base_Data.txt", "r")
        useri = file.readlines()
        for item in useri:
            k = item.split()
            if k[1] == name and k[2] == password:
                return True
        return False
    def create(self,login:str,password:str,data:Create) -> Maindata|str:
        creds = {
            "title": data.title,
            "owner": data.owner,
            "description": data.description,
            "acsess": data.acsess,
        }
        if not self.avtorization(name=login,password=password):
            return f'неверное имя пользователя или пароль'
        if creds["owner"] != login:
            return f'Введите свой логин в строке owner'
        if not os.path.isdir("Acsess_Test"):
            os.mkdir("Acsess_Test")
        p = f'{creds["title"]}'
        for i in os.listdir("Acsess_Test"):
            if i == p:
                return f'Невозможно создать тест, такое название уже существует'
        file = open(f'{p}',"a+")
        for key, value in creds.items():
            file.write(f'{value}-' )
        file.write(f'\n')
        file.close()
        if os.path.isdir("Acsess_Test"):
            os.makedirs("Acsess_Test/"f'{p}')
            os.replace(f'{p}',"Acsess_Test/"f'{p}/'f'{p}')
        return Maindata(
            title=creds["title"],
            description=creds["description"]
        )

    def get_test(self)->list[Maindata]:
        items1 = []
        for folder in os.listdir("Acsess_Test"):
            if os.path.isdir('Acsess_Test'+'\\'+folder):
                os.listdir('Acsess_Test'+'\\'+folder)
                if os.path.isfile('Acsess_Test'+'\\'+folder+'\\'+f'{folder}'):
                    file = open('Acsess_Test'+'\\'+folder+'\\'+f'{folder}',"r")
                    test = file.readlines()
                    for i in test:
                        k = i.split("-")
                        if k[3] == "True":
                            items1.append(
                                Maindata(
                                    title=k[0],
                                    description=k[2]
                                )
                            )
        return items1

    def acsess(self,title:str,login:str,password:str,creds:Acsess1)->str:
        for folder in os.listdir("Acsess_Test"):
            if os.path.isdir('Acsess_Test'+'\\'+folder):
                os.listdir('Acsess_Test'+'\\'+folder)
                if os.path.isfile('Acsess_Test'+'\\'+folder+'\\'+f'{folder}'):
                    file = open('Acsess_Test'+'\\'+folder+'\\'+f'{folder}',"r")
                    test = file.readlines()
                    for i in test:
                        k = i.split("-")
                        if k[0] == title:
                            if not self.avtorization(name=login,password=password):
                                return "неверное имя пользователя или пароль"
                            if creds == Acsess1.Yes:
                                new_data = i.replace(f'{k[3]}',"True")
                                f = open('Acsess_Test'+'\\'+folder+'\\'+f'{folder}','w')
                                f.write(new_data)
                                k[3] = "True"
                                return f'доступ изменен на {k[3]}'
                            else:
                                new_data = i.replace(f'{k[3]}', "False")
                                f = open('Acsess_Test' + '\\' + folder + '\\' + f'{folder}', 'w')
                                f.write(new_data)
                                k[3] = "False"
                                return f'доступ изменен на {k[3]}'
    def add_question(self,title:str,login:str,password:str,question:Question) ->Q|str:
        creds = {
            "number": question.number,
            "question": question.question,
        }
        cnt = creds["number"]
        if not os.path.isdir("Acsess_Test"):
            os.mkdir("Acsess_Test")

        if not os.path.isdir("Acsess_Test/"f'{title}'):
            return f'Теста {title} нет'

        if not self.avtorization(name=login,password=password):
            return "Неверное имя пользователя или пароль"


        if not os.path.isdir("Acsess_Test/"f'{title}/'"questions"):
            os.makedirs("Acsess_Test/"f'{title}/'"questions")
        file = open(f'questions_{cnt}','w')
        for key, value in creds.items():
            file.write(f'{value}-')
        file.write(f'\n')
        file.close()
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                for fil in os.listdir("Acsess_Test"+'\\'+folder+'\\'+f'questions'):
                    if fil == f'questions_{cnt}':
                        return f'Вопрос №{cnt} уже существует'
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                if os.path.isfile('Acsess_Test'+'\\'+folder+'\\'+f'{folder}'):
                    file1 = open('Acsess_Test'+'\\'+folder+'\\'+f'{folder}',"r")
                    test = file1.readlines()
                    for i in test:
                        k = i.split("-")
                        if k[0] == title:
                            if k[1] == login:
                                os.replace(f'questions_{cnt}', "Acsess_Test/"f'{title}/'"questions/"f'questions_{cnt}')
                                file1.close()
                                return Q(
                                    question=creds["question"],
                                )
                            return "Введено неверное имя хозяина теста"



    #получение вопросов
    def show_question(self,title:str)->list[Question]:
        items = []
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                if os.path.isdir('Acsess_Test' + '\\' + folder):
                    os.listdir('Acsess_Test' + '\\' + folder)
                    if os.path.isdir('Acsess_Test'+'\\'+folder+'\\'+"questions"):
                        os.listdir('Acsess_Test'+'\\'+folder+'\\'+"questions")
                        for fil in os.listdir('Acsess_Test'+'\\'+folder+'\\'+"questions"):
                            if os.path.isfile('Acsess_Test'+'\\'+folder+'\\'+"questions"+'\\'f'{fil}'):
                                file = open('Acsess_Test'+'\\'+folder+'\\'+"questions"+'\\'f'{fil}',"r")
                                passing = file.readlines()
                                for i in passing:
                                    k = i.split("-")
                                    items.append(
                                        Question(
                                            number=k[0],
                                            question=k[1]
                                        )
                                    )
        return items


    #СЧЕТИЕТ КОЛИЧЕСТВО ВОПРОСОВ
    def solve(self,title:str)->int:

        cnt = 0
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                if os.path.isdir('Acsess_Test' + '\\' + folder):
                    os.listdir('Acsess_Test' + '\\' + folder)
                    if os.path.isdir('Acsess_Test'+'\\'+folder+'\\'+"questions"):
                        os.listdir('Acsess_Test'+'\\'+folder+'\\'+"questions")
                        for fil in os.listdir('Acsess_Test'+'\\'+folder+'\\'+"questions"):
                            os.path.isfile('Acsess_Test' + '\\' + folder + '\\' + "questions" + '\\'f'{fil}')
                            cnt += 1
                        return cnt


    def statistic1(self,title:str,login:str,password:str,question:Answer)->str:
        data = {
            "number":question.number,
            "answer":question.answer
        }
        if self.avtorization(name=login,password=password) == False:
            return f'Неверный логин или пароль'
        if question.number > self.solve(title=title):
            return f'В тесте нет такого вопроса'
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                if not os.path.isdir("Acsess_Test/"f'{title}/'"answer"):
                    os.mkdir("Acsess_Test/"f'{title}/'"answer")
                if os.path.isdir("Acsess_Test/"f'{title}/'"answer"):
                    if os.path.isdir("Acsess_Test/"f'{title}/'"answer/"):
                        if not os.path.isfile("Acsess_Test/"f'{title}/'"answer/"f'{login}'):
                            file = open("Acsess_Test/"f'{title}/'"answer/"f'{login}', "w+")
                        else:
                            file = open("Acsess_Test/"f'{title}/'"answer/"f'{login}', "r+")
                        fil = file.readlines()
                        for i in fil:
                            if i[0] == f'{data["number"]}':
                                return "Вы уже ответили на этот вопрос"
                        for key, value in data.items():
                            file.write(f'{value}-')
                        file.write(f'\n')
                        if question.number == self.solve(title=title):
                            return "Тест окончен"
                        file.close()
                        return f'Ответ записан'

    def show_answer(self,login:str,password:str,title:str):
        items = []
        if not self.avtorization(name=login,password=password):
            return f'Неверное имя пользователя или пароль'
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                if os.path.isdir('Acsess_Test' + '\\' + folder):
                    os.listdir('Acsess_Test' + '\\' + folder)
                    if os.path.isdir('Acsess_Test'+'\\'+folder+'\\'+"answer"):
                        os.listdir('Acsess_Test'+'\\'+folder+'\\'+"answer")
                        for fil in os.listdir('Acsess_Test'+'\\'+folder+'\\'+"answer"):
                            if fil == login:
                                if os.path.isfile('Acsess_Test'+'\\'+folder+'\\'+"answer"+'\\'f'{fil}'):
                                    file = open('Acsess_Test' + '\\' + folder + '\\' + "answer" + '\\'f'{fil}', "r")
                                    passing = file.readlines()
                                    for i in passing:
                                        k = i.split("-")
                                        p = k[1]
                                        t = p.split(".")
                                        items.append(
                                            Answer(
                                                number=k[0],
                                                answer=t[1]
                                            )
                                        )
        return items

    #список userов ответивших да по конкретному вопросу
    def statistics_on_question1(self,title:str,number_quest:int):
        stat_yes = []
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                for ans in os.listdir('Acsess_Test' + '\\' + folder + "\\"+ "answer"):
                    file = open('Acsess_Test' + '\\' + folder + "\\"+ "answer"+ "\\" + f'{ans}',"r")
                    s = file.readlines()
                    for i in s:
                        k = i.split("-")
                        p = k[1]
                        t = p.split(".")
                        if f'{number_quest}' == k[0]:
                            if t[1] == "Yes":
                                stat_yes.append(ans)
        return stat_yes
    #список userов ответивших нет по конкретному вопросу
    def statistics_on_question2(self,title:str,number_quest:int):
        stat_no = []
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                for ans in os.listdir('Acsess_Test' + '\\' + folder + "\\" + "answer"):
                    file = open('Acsess_Test' + '\\' + folder + "\\" + "answer" + "\\" + f'{ans}', "r")
                    s = file.readlines()
                    for i in s:
                        k = i.split("-")
                        p = k[1]
                        t = p.split(".")
                        if f'{number_quest}' == k[0]:
                            if t[1] == "No":
                                stat_no.append(ans)
        return stat_no
    #количество ответов да по конкретному вопросу
    def cnt_true(self,title:str,number_quest:int):
        cnt = 0
        for folder in self.statistics_on_question1(title=title,number_quest=number_quest):
            cnt += 1
        return cnt
    #количество ответов нет по конкретному вопросу
    def cnt_false(self,title:str,number_quest:int):
        cnt = 0
        for folder in self.statistics_on_question2(title=title,number_quest=number_quest):
            cnt += 1
        return cnt

    #статистика ответов да по конкретному вопросу
    def statistics_on_question_true(self,title:str,number_quest:int):
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                cnt = self.cnt_true(title=title,number_quest=number_quest)
                if number_quest > self.solve(title=title):
                    return f'В тесте нет такого вопроса'

                stati = (cnt*100)/(self.cnt_true(title=title,number_quest=number_quest)+self.cnt_false(title=title,number_quest=number_quest))
                return f'{stati}%'
        return f'Теста не существует'


    #статистика ответов нет по конкретному вопросу
    def statistics_on_question_false(self,title:str,number_quest:int):
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                cnt = self.cnt_false(title=title,number_quest=number_quest)
                if number_quest > self.solve(title=title):
                    return f'В тесте нет такого вопроса'

                stati = (cnt*100)/(self.cnt_true(title=title,number_quest=number_quest)+self.cnt_false(title=title,number_quest=number_quest))
                return f'{stati}%'
        return f'Теста не существует'

    def for_stat1(self,title:str):
        answer_yes = []
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                for fil in os.listdir("Acsess_Test"+'\\'+ title +'\\' + 'answer'):
                    file = open("Acsess_Test"+'\\'+ title +'\\' + "answer" + '\\' + f'{fil}')
                    k = file.readlines()
                    for i in k:
                        k = i.split("-")
                        p = k[1]
                        t = p.split(".")
                        if t[1] == "Yes":
                            answer_yes.append(fil)
        return answer_yes

    def for_stat2(self,title:str):
        answer_no = []
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                for fil in os.listdir("Acsess_Test"+'\\'+ title +'\\' + 'answer'):
                    file = open("Acsess_Test"+'\\'+ title +'\\' + "answer" + '\\' + f'{fil}')
                    k = file.readlines()
                    for i in k:
                        k = i.split("-")
                        p = k[1]
                        t = p.split(".")
                        if t[1] == "No":
                            answer_no.append(fil)
        return answer_no

    def cnt_true_test(self,title:str):
        cnt = 0
        for folder in self.for_stat1(title=title):
            cnt += 1
        return cnt

    def cnt_true_false(self,title:str):
        cnt = 0
        for folder in self.for_stat2(title=title):
            cnt += 1
        return cnt

    def statistics_on_test_true(self,title:str):
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                cnt = self.cnt_true_test(title=title)
                stati = (cnt*100)/(self.cnt_true_test(title=title)+self.cnt_true_false(title=title))
                return f'{stati}%'
        return f'Теста не существует'


    def statistics_on_test_false(self,title:str):
        for folder in os.listdir("Acsess_Test"):
            if folder == title:
                cnt = self.cnt_true_false(title=title)
                stati = (cnt*100)/(self.cnt_true_test(title=title)+self.cnt_true_false(title=title))
                return f'{stati}%'
        return f'Теста не существует'

    def list_of_test(self,user:str,password:str):
        list1 = []
        if not self.avtorization(name=user,password=password):
            return "Неверное имя пользователя или пароль"
        for folder in os.listdir("Acsess_Test"):
            for fil in os.listdir("Acsess_Test"+'\\'+f'{folder}'+'\\'+"answer"):
                if fil == user:
                    file = open("Acsess_Test"+'\\'+f'{folder}'+'\\'+"answer"+'\\'+f'{fil}',"r")
                    f = file.readlines()
                    for s in f:
                        if s[0] == f'{self.solve(title=folder)}':
                            list1.append(folder)
        return list1




My_test: Test = Test()