from pydantic import BaseModel, Field


class TeacherPath(BaseModel):
    teacher_id: int = Field(description='teacher id')


class TeacherBody(BaseModel):
    name: str = Field(min_length=5, max_length=50, description='teacher name')
    age: int = Field(1, description='age of teacher')


class TeacherQuery(BaseModel):
    page: int = Field(1, description='actual page')
    per_page: int = Field(5, description='registers per page')
    