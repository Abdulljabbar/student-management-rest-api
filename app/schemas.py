
from pydantic import BaseModel, Field, ConfigDict


class StudentCreate(BaseModel):

    name: str = Field(min_length=1, max_length=100)

    rollNo: str = Field(min_length=1, max_length=20)

    department: str = Field(min_length=1, max_length=100)

    semester: int = Field(ge=1, le=8)


class StudentUpdate(StudentCreate):
    pass


class StudentResponse(StudentCreate):

    id: int

    model_config = ConfigDict(from_attributes=True)
