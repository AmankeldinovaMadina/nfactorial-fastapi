from fastapi import Depends, HTTPException, status
from pydantic import BaseModel

from ..service import Service, get_service
from . import router


class UpdateUserRequest(BaseModel):
    email: str
    password: str


class UpdateUserResponse(BaseModel):
    email: str


@router.patch(
    "/users", status_code=status.HTTP_201_CREATED, response_model=UpdateUserResponse
)
def update_user(
    input: UpdateUserRequest,
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    if svc.repository.get_user_by_email(input.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already taken.",
        )

    svc.repository.create_user(input.dict())

    return UpdateUserResponse(email=input.email)
