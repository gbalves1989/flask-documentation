from pydantic import BaseModel, Field


class CoursePath(BaseModel):
    course_id: int = Field(description='course id')


class CourseBody(BaseModel):
    name: str = Field(min_length=5, max_length=50, description='course name')
    description: str = Field(min_length=5, max_length=100, description='course description')
    published_at: str = Field(description='Example: 2023-04-23')
    graduation: str = Field(description='graduation related')


class CourseQuery(BaseModel):
    page: int = Field(1, description='actual page')
    per_page: int = Field(5, description='registers per page')
