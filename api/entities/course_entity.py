from ..models.graduation_model import GraduationModel


class CourseEntity:
    def __init__(self, name: str, description: str, published_at: str, graduation: GraduationModel):
        self.__name = name
        self.__description = description
        self.__published_at = published_at
        self.__graduation = graduation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def published_at(self) -> str:
        return self.__published_at

    @published_at.setter
    def published_at(self, published_at: str):
        self.__published_at = published_at

    @property
    def graduation(self) -> GraduationModel:
        return self.__graduation

    @graduation.setter
    def graduation(self, graduation: GraduationModel):
        self.__graduation = graduation
