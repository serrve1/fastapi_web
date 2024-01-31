from fastapi import FastAPI ,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request,name="index.html", context ={"name": "김태뿅"})

# 경로를 바꿉니다.
# 다른 html을 넣어줘야함
#{name}을 경로에 넣어주면 ==> async def name으로 간다.
@app.get('/hello/{name}', response_class=HTMLResponse)

# context 딕셔너리의 키값 "name"이랑 hello.html에 있는 name과 연결되어있는것이다.
async def hello(request: Request, name):
    words = f'당신의 이름은 {name}니까 반가워서 인사'
    return templates.TemplateResponse(request=request,name="hello.html", context ={"name": words})