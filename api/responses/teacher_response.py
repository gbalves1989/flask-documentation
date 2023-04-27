from pydantic import BaseModel, Field


class TeacherResponse(BaseModel):
    id: int = Field(0, description='teacher id')
    name: str = Field('test', description='name of teacher')
    age: int = Field(1, description='age of teacher')


class TeacherListResponse(BaseModel):
    total: int = Field(1, description='total of graduation')
    pages: int = Field(1, description='number of pages')
    next: int = Field(1, description='next page')
    prev: int = Field(1, description='preview page')
    results: list[TeacherResponse]
    