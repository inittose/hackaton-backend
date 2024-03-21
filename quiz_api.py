from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel
import uvicorn
from pathlib import Path
import datetime
import json

app = FastAPI()

class Quiz(BaseModel):
    name: str
    list_control: list
    text_field: str
    number_field: int
    date_field: datetime.date
    fs_data: str

class FileSystem:
    def save_json(self, data: dict, filename: str):
        filepath = Path.cwd() / filename
        data_json = json.dumps(data)
        with filepath.open(mode='w') as fp:
            fp.write(data_json)

    def load_json(self, filename: str):
        filepath = Path.cwd() / filename
        data_json = filepath.read_text()
        data = json.loads(data_json)
        return data

fs = FileSystem()

@app.post('/create_quiz/')
async def create_quiz(
    name: str = Form(...),
    list_control: list = Form(...),
    text_field: str = Form(...),
    number_field: int = Form(...),
    date_field: datetime.date = Form(...),
    file: bytes = File(...),
):
    quiz_data = {
        'Название': name,
        'Выпадающий список': list_control,
        'Тестовое поле': text,
        "Поле с Цифрой": number_field,
        "Поле с датой": date_field,
        "Поле с датой": file,
    }
    quiz_dict = quiz_data.__dict__
    fs_data_dict = json.loads(quiz_dict['fs_data'])
    quiz_dict['fs_data'] = fs_data_dict
    quiz = Quiz(**quiz_dict)
    fs.save_json(quiz.dict(), quiz.name + '.json')
    return {'message': 'Тест создан'}


# if __name__ == '__main__':
#     uvicorn.run(quiz_api, host='127.0.0.1', port=8000)