from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from pprint import pprint
from datetime import datetime

SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGORITHM = "HS256"

username = "frank"
userid = 30
time_delta = timedelta(seconds=30)


def create_access_token(
    username: str, user_id: int, expires_delta: Optional[timedelta] = None
):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token):
    if token is None:
        return None
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    print(datetime.fromtimestamp(payload.get("exp")))
    pprint(payload)


# encode_token = create_access_token(username, userid, time_delta)
# print(encode_token)
encode_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmcmFuayIsImlkIjozMCwiZXhwIjoxNjg0MDMxNTA3fQ.pWdAn8YPbtm1UmHb8CKelpeuekpZvpT05AA0YpEYwss"

decode_token(encode_token)
