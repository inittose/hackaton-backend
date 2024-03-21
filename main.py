from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List, Optional
import uuid
import json
import os

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Test(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    questions: List[dict]
    min_pass_percentage: int

class Question(BaseModel):
    control_type: str
    description: str
    options: Optional[List[str]]
    answer: str

class UserTestResult(BaseModel):
    user_id: uuid.UUID
    test_id: uuid.UUID
    answers: List[str]
    pass_percentage: int

class User(BaseModel):
    id: uuid.UUID
    username: str
    tests: List[UserTestResult]

def authenticate_user(username: str, password: str):
    # Замените эту функцию на проверку пользователя в вашей базе данных
    if username == "admin" and password == "password":
        return User(id=uuid.uuid4(), username=username, tests=[])
    return None

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Замените эту функцию на получение пользователя из вашей базы данных
    username = token.split(":")[0]
    password = token.split(":")[1]
    user = authenticate_user(username, password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

@app.post("/tests")
def create_test(test: Test):
    with open("tests.json", "r") as file:
        tests = json.load(file)
    test.id = uuid.uuid4()
    tests.append(test.dict())
    with open("tests.json", "w") as file:
        json.dump(tests, file)
    return {"message": "Test created successfully"}


@app.get("/tests/{test_id}", response_model=Test)
def get_test(test_id: uuid.UUID):
    with open("tests.json", "r") as file:
        tests = json.load(file)
    for test in tests:
        if test["id"] == test_id:
            return test
    raise HTTPException(status_code=404, detail="Test not found")


def calculate_score(test_id: uuid.UUID, user_answers: List[str]):
    with open("tests.json", "r") as file:
        tests = json.load(file)
    for test in tests:
        if test["id"] == test_id:
            score = 0
            user_answers_dict = {i: answer for i, answer in enumerate(user_answers)}
            for question in test["questions"]:
                if question["control_type"] == "dropdown":
                    if question["answer"] in user_answers_dict[question["id"]]:
                        score += 1
                elif question["control_type"] == "text":
                    if user_answers_dict[question["id"]].strip().lower() == question["answer"].strip().lower():
                        score += 1
                elif question["control_type"] == "number":
                    if question["answer"] == user_answers_dict[question["id"]]:
                        score += 1
                elif question["control_type"] == "date":
                    if user_answers_dict[question["id"]] == question["answer"]:
                        score += 1
            return score


@app.post("/tests/{test_id}/user_results")
def submit_test(test_id: uuid.UUID, user_answers: List[str]):
    with open("tests.json", "r") as file:
        tests = json.load(file)
    for test in tests:
        if test["id"] == test_id:
            score = calculate_score(test_id, user_answers)
            user_result = UserTestResult(
                user_id=uuid.uuid4(),
                test_id=test_id,
                answers=user_answers,
                score=score,
            )
            current_user = get_current_user(oauth2_scheme)
            current_user.tests.append(user_result)
            with open(f"{current_user.id}_results.json", "w") as file:
                json.dump(current_user.tests, file)
            if score / len(test["questions"]) * 100 >= test["min_score"]:
                return {"message": "Test passed", "score": score, "min_score": test["min_score"]}
            else:
                return {"message": "Test failed", "score": score, "min_score": test["min_score"]}

    raise HTTPException(status_code=404, detail="Test not found")
