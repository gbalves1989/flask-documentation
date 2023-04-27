from typing import List


class GraduationEntity:
    def __init__(self, name: str, description: str, teachers: List):
        self.__name = name
        self.__description = description
        self.__teachers = teachers

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
    def teachers(self) -> List:
        return self.__teachers

    @teachers.setter
    def teachers(self, teachers: List):
        self.__teachers = teachers
