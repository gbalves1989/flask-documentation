from pydantic import BaseModel, Field


class GraduationPath(BaseModel):
    graduation_id: int = Field(description='graduation id')


class GraduationBody(BaseModel):
    name: str = Field(min_length=5, max_length=50, description='graduation name')
    description: str = Field(min_length=5, max_length=100, description='graduation description')
    teachers: list[int]


class GraduationQuery(BaseModel):
    page: int = Field(1, description='actual page')
    per_page: int = Field(5, description='registers per page')
