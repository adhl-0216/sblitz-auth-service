from supertokens_python import get_all_cors_headers
from fastapi import FastAPI, Depends, HTTPException
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

from utils import *


app = FastAPI()
settings = get_settings()
supertokens_init(settings)

app.add_middleware(get_middleware())


@app.get("/validate")
async def validate_token(session: SessionContainer = Depends(verify_session())):
    user_id = session.get_user_id()
    return {"user_id": user_id}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.website_domain
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)
