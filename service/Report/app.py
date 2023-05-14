from pprint import pprint
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import status, APIRouter, Request
from starlette.responses import RedirectResponse
from service.Auth.app import SECRET_KEY, ALGORITHM, decode_token


templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/report", response_class=HTMLResponse)
async def reportPage(request: Request):
    if request.cookies.get("access_token"):
        user = decode_token(request.cookies.get("access_token"))
        pprint(user)
        if not user.get("message"):
            return templates.TemplateResponse("report.html", {"request": request})
    else:
        return RedirectResponse(url="/hkleaveapp", status_code=status.HTTP_302_FOUND)
