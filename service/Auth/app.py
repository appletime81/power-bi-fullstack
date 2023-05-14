from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException, APIRouter, Request


templates = Jinja2Templates(directory="templates")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "eb750ede284955f0ea34e05a0dc364db05535873eec546596e3467d9423ae089"
ALGORITHM = "HS256"

router = APIRouter()

temp_users_info = {
    "users_info": [
        {
            "user_id": 30,
            "username": "itrimsl8696@gmail.com",
            "hashedpassowrd": "$2b$12$N8jUJ1ZPlNNsXuF6vloy4.SPLXIJlTYcWVTpoHRRcsj.07.xN.dI6",
        }
    ]
}


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def search_user(username: str):
    for user in temp_users_info.get("users_info"):
        if user.get("username") == username:
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
        user = search_user(payload.get("sub"))
        if user:
            return user
        else:
            return {"message": "JWTError"}
    except JWTError:
        return {"message": "JWTError"}


def authenticate_user(username: str, password: str):
    user = search_user(username)
    if not user:
        return False
    if not verify_password(password, user.get("hashedpassowrd")):
        return False
    return user


@router.get("/", response_class=HTMLResponse)
async def loginPage(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/")
async def loginFunc(request: Request):
    user_info = await request.json()
    print(user_info)
    user = authenticate_user(user_info.get("username"), user_info.get("password"))
    print(user)
    if user:
        token_expires = timedelta(minutes=60)
        token = create_access_token(
            user.get("username"), user.get("user_id"), expires_delta=token_expires
        )
        return {"access_token": token}
    else:
        return HTTPException(status_code=403, detail="Incorrect username or password")


if __name__ == "__main__":
    print(
        verify_password(
            "123456", "$2b$12$N8jUJ1ZPlNNsXuF6vloy4.SPLXIJlTYcWVTpoHRRcsj.07.xN.dI6"
        )
    )
