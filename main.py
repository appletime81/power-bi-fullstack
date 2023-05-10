import os
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from service.Auth.app import router as auth_router

app = FastAPI()

ROOT_URL = "/hkleaveapp"
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth_router, prefix=ROOT_URL)
