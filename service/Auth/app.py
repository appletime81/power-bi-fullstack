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
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "eb750ede284955f0ea34e05a0dc364db05535873eec546596e3467d9423ae089"
ALGORITHM = "HS256"

router = APIRouter()

temp_users_info = {
    "users_info": [
        {
            "user_id": 30,
            "username": "frank",
            "hashedpassowrd": "$2b$12$N8jUJ1ZPlNNsXuF6vloy4.SPLXIJlTYcWVTpoHRRcsj.07.xN.dI6",
        }
    ]
}


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def search_user(user_id: int):
    for user in temp_users_info.get("users_info"):
        if user.get("user_id") == user_id:
            return user
    return False


def create_access_token(username: str, user_id: int, expires_delta: timedelta = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = search_user(payload.get("id"))
        if user:
            return user
        else:
            return {"message": "user is not exist"}
    except JWTError:
        return {"message": "JWTError"}


def authenticate_user(username: str, password: str):
    for user in temp_users_info.get("users_info"):
        if user.get("username") == username:
            if user.get("password") == password:
                return user
            else:
                return {"message": "username or password is wrong"}
    return {"message": "username or password is wrong"}


@router.get("/", response_class=HTMLResponse)
async def loginPage(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/")
async def loginFunc(request: Request):
    user_info = await request.json()
    pprint(user_info)
    return user_info


if __name__ == "__main__":
    print(verify_password("123456", "$2b$12$N8jUJ1ZPlNNsXuF6vloy4.SPLXIJlTYcWVTpoHRRcsj.07.xN.dI6"))
