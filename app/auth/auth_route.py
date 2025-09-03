from fastapi import APIRouter, status
from .auth_service import auth_service
from app.schemas.auth_schema import SignupSchema, LoginSchema, VerifyAccount

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def signup_user(user: SignupSchema):
    return await auth_service.signup(user)

@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    summary="Login a user",
)
async def login_user(user: LoginSchema):
    return await auth_service.login(user)

@router.post(
    "/verify-account",
    status_code=status.HTTP_200_OK,
    summary="Verify a user's account with code",
)
async def verify_user(data: VerifyAccount):
    return await auth_service.verify(data.code)