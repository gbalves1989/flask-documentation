from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: int = Field(0, description='user id')
    name: str = Field('test', description='name of user')
    email: str = Field('test email', description='email of user')
    password: str = Field('test password', description='password of user')


class LoginResponse(BaseModel):
    access_token: str = Field(description='token access')
    refresh_token: str = Field(description='token refresh')
    message: str = Field(description='message to return')


class RefreshResponse(BaseModel):
    access_token: str = Field(description='token access')
    refresh_token: str = Field(description='token refresh')
