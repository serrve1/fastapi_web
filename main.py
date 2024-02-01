from fastapi import FastAPI ,Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request,name="index.html", context ={"name": "김태뿅"})

# 경로를 바꿉니다. path를 parameter 처리한 것, jinja2 문법을 통하여 context 처리
# 다른 html을 넣어줘야함
#{name}을 경로에 넣어주면 ==> async def name으로 간다.
# context 딕셔너리의 키값 "name"이랑 hello.html에 있는 name과 연결되어있는것이다.
# 특이하게 매개변수 타입을 지정할 수 있다.(파이댄틱을 이용)
@app.get('/hello/{name}', response_class=HTMLResponse)
async def hello(request: Request , name ,action, sound: str = "빵빵"):
    print(f'action :{action} 그리고 소리 :{sound} ')
    return templates.TemplateResponse(request=request
                                      ,name="hello.html" 
                                      , context={"name":name 
                                                 , "action":action
                                                 , "sound":sound})

@app.get('/login', response_class=HTMLResponse )
async def get_login(request: Request ):
    return templates.TemplateResponse(request=request, name = 'login.html')


@app.post('/login', response_class=HTMLResponse )
async def login(username: str =Form(...), password:str =Form(...)):
    print(username)
    return "Success"


@app.get('/register', response_class=HTMLResponse )
async def get_login(request: Request ):
    return templates.TemplateResponse(request=request, name = 'register.html')


@app.post('/register', response_class=HTMLResponse )
async def login(username: str =Form(...), 
                email:str =Form(...), 
                phone:str =Form(...), 
                password:str =Form(...)):
    print(username, email, phone, password)
    return email