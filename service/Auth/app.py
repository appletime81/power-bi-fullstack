from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pprint import pprint
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, APIRouter, Request, Response, Form
from starlette.responses import RedirectResponse


templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def loginPage(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/")
async def loginFunc(request: Request):
    user_info = await request.json()
    pprint(user_info)
    return user_info

@router.get("/report", response_class=HTMLResponse)
async def reportPage(request: Request):
    return templates.TemplateResponse("report.html", {"request": request})
