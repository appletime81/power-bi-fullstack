from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pprint import pprint
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, APIRouter, Request, Response, Form

SECRET_KEY = "eb750ede284955f0ea34e05a0dc364db05535873eec546596e3467d9423ae089"
ALGORITHM = "HS256"

templates = Jinja2Templates(directory="templates")


router = APIRouter()


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return bcrypt_context.hash(password)


@router.get("/", response_class=HTMLResponse)
async def loginPage(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/")
async def loginFunc(request: Request):
    user_info = await request.json()

    return {"h": "h"}
