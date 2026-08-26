from pathlib import Path
from fastapi import FastAPI, UploadFile

app = FastAPI()

UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def root():
  return {"message": "hello"}


@app.post("/upload")
async def upload_file(file:UploadFile):
  file_path = UPLOAD_DIR/file.filename

  with open(file_path, "wb") as output:
    output.write(await file.read())

  return{"filename":file.filename}
