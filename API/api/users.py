from fastapi import APIRouter
from scheme.users import User,Maindata,Create,Get,Acsess1,Creds2,Creds
from scheme.users import Question,Answer,Q
from servise.users import user_service
from servise.test import My_test



router = APIRouter()

#регистрация
@router.post("/register", response_model=User | str)
def register_user(data: Creds,data2:Creds2):
    return user_service.register(paylods=data,data=data2)

# #Авторизация
# @router.put(
#     "/avtorize/",
#     response_model=bool
# )
# def avtorize_user(name: str = Query(max_length=50),password: str = Query(max_length=20)):
#     return user_service.avtorizatoin(name=name,password=password)

@router.get(
    "/users",
    status_code=200,
    response_model=list[User]
)
def get_users():
    return user_service.get_users()


@router.post(
    "/create_test/",
    response_model=Maindata|str
)
def create(login:str,password:str,datas: Create):
    return My_test.create(login=login,password=password,data=datas)

@router.get(
    "/get_test_for_use/",
    response_model=list[Maindata],
    status_code=200
)
def get_test():
    return My_test.get_test()

@router.put(
    "/acsess_test/",
    response_model=str
)
def acsess(title:str,owner:str,password:str,creds:Acsess1):
    return My_test.acsess(title=title,login=owner,password=password,creds=creds)

@router.post(
    "/question_test/",
    response_model=Q|str
)
def questoins(title: str,login:str,password:str, question:Question):
    return My_test.add_question(title=title,login=login,password=password,question=question)

@router.get(
    "/show_questions/",
    response_model=list[Question]
)
def show_question(title:str):
    return My_test.show_question(title=title)

@router.post(
    "/testing/",
    response_model=str
)
def testing(title:str,login:str,password:str,question:Answer):
    return My_test.statistic1(title=title,login=login,password=password,question=question)

@router.get(
    "/show_answer/",

)
def show_answer(login:str,password:str,title:str):
    return My_test.show_answer(login=login,password=password,title=title)


@router.get(
    "/statistics_on_question_true/"
)
def statistics_on_question_true(title:str,number_quest:int):
    return My_test.statistics_on_question_true(title=title,number_quest=number_quest)


@router.get(
    "/statistics_on_question_false/"
)
def statistics_on_question_false(title:str,number_quest:int):
    return My_test.statistics_on_question_false(title=title,number_quest=number_quest)


@router.get(
    "/statistics_on_test_true/"
)
def statistics_on_test_true(title:str):
    return My_test.statistics_on_test_true(title=title)

@router.get(
    "/statistics_on_test_false/"
)
def statistics_on_test_false(title:str):
    return My_test.statistics_on_test_false(title=title)

@router.get(
    "/list_of_test/"
)
def list_of_test(user:str,password:str):
    return My_test.list_of_test(user=user,password=password)

