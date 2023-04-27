from pydantic import BaseModel, Field


class GraduationCoursesResponse(BaseModel):
    id: int = Field(0, description='course id')
    name: str = Field('test', description='name of course')


class GraduationTeachersResponse(BaseModel):
    id: int = Field(0, description='teacher id')
    name: str = Field('test', description='name of teacher')


class GraduationResponse(BaseModel):
    id: int = Field(0, description='graduation id')
    name: str = Field('test', description='name of graduation')
    description: str = Field('test description', description='description of graduation')
    courses: list[GraduationCoursesResponse]
    teachers: list[GraduationTeachersResponse]


class GraduationListResponse(BaseModel):
    total: int = Field(1, description='total of graduation')
    pages: int = Field(1, description='number of pages')
    next: int = Field(1, description='next page')
    prev: int = Field(1, description='preview page')
    results: list[GraduationResponse]
