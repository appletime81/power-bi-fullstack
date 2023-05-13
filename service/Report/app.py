from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pprint import pprint
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, APIRouter, Request, Response, Form
from starlette.responses import RedirectResponse
from ..Auth.app import router as auth_router


templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/report", response_class=HTMLResponse)
async def reportPage(request: Request):
    return templates.TemplateResponse("report.html", {"request": request})
