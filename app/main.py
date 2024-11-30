from supertokens_python import get_all_cors_headers
from fastapi import FastAPI, Depends, HTTPException, Response
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

from app.utils import *


app = FastAPI()
settings = get_settings()
supertokens_init(settings)

app.add_middleware(get_middleware())


@app.get("/api/auth/validate")
async def validate_token(response: Response, session: SessionContainer = Depends(verify_session())):
    try:
        return {"userId": session.get_user_id()}
    except Exception as e:
        raise HTTPException(
            status_code=401, detail="Unauthorized: Invalid session")


@app.get("/api/auth/hello")
async def hello():
    return {"hello": "hola"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.website_domain,
        settings.api_domain
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)
