from pydantic import BaseModel, Field


class UserBody(BaseModel):
    name: str = Field(min_length=5, max_length=50, description='user name')
    email: str = Field(min_length=5, max_length=100, description='user email')
    password: str = Field(min_length=5, max_length=255, description='user password')


class LoginBody(BaseModel):
    email: str = Field(min_length=5, max_length=100, description='user email')
    password: str = Field(min_length=5, max_length=255, description='user password')


class AuthorizationQuery(BaseModel):
    authorization: str = Field('Bearer token', description='user email')
