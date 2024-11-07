from supertokens_python import get_all_cors_headers
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware

from utils import *


app = FastAPI()
settings = get_settings()
supertokens_init(settings)

app.add_middleware(get_middleware())

# TODO: Add APIs


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)
