from fastapi import FastAPI, Depends
from supertokens_python.asyncio import get_user
from supertokens_python.recipe.session.asyncio import get_session
from supertokens_python import get_all_cors_headers
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

from app.utils import *


app = FastAPI()
settings = get_settings()
supertokens_init(settings)

app.add_middleware(get_middleware())


@app.post('/api/auth/get-user-info')
async def get_user_info_api(session: SessionContainer = Depends(verify_session())):
    user_id = session.get_user_id()
    return await get_user(user_id)


@app.get("/api/auth/validate")
async def validate_token(request: Request):
    s_access_token = request.cookies.get("sAccessToken")
    if not s_access_token:
        raise HTTPException(
            status_code=401, detail="Unauthorized: Missing access token"
        )

    try:
        session: SessionContainer = await get_session(request)
        user_id = session.get_user_id()
        return {"userId": user_id}
    except Exception as e:
        print("Error:", e)  # Log the exception for debugging
        raise HTTPException(
            status_code=401, detail="Unauthorized: Invalid session"
        )


@app.get("/api/auth/hello")
async def hello():
    return {"hello": "hola"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)
