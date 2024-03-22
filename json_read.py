import json

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/uploadjson/")
async def create_upload_json(file: UploadFile):
    file_content = await file.read()
    file_as_dict = json.loads(file_content)
    return {"filename": file.filename, "file_content": file_as_dict}
