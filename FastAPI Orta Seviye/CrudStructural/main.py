from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Course:
    id : int
    title : str
    instructor : str
    rating : int
    publish_date : int

    def __init__(self, id: int, title: str, instructor: str, rating: int, publish_date: str):
        self.id = id
        self.title = title
        self.instructor = instructor
        self.rating = rating
        self.publish_date = publish_date

class CourseRequest(BaseModel):
    id: Optional[int] = Field(description="The course id",default=None)
    title : str = Field(min_length=3,max_length=100)
    instructor : str = Field(min_length=3)
    rating : int = Field(gt=0,lt=6)
    publish_date : int = Field(gte=1900,lte=2100)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "My course",
                "instructor": "berk",
                "rating": 5,
                "publish_date": 2020 ,
            }
        }
    }


courses_db = [
    Course(1,"Python","Atil",4,2029),
    Course(2, "C#", "Berk", 5, 2026),
    Course(3, "Java", "İsmail", 2, 2023),
    Course(4, "Java", "Berk", 5, 2030),
    Course(5, "C", "İsmail", 1, 2031),
    Course(6, "R", "Rıdvan", 3, 2035),
]

@app.get("/courses",status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses_db

@app.get("/courses/{course_id}",status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

@app.get("/courses/",status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: int = Query(gt=0,lt=6)):
    courses_to_return=[]
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return

@app.get("/courses/publish/",status_code=status.HTTP_200_OK)
async def get_courses_by_publish_date(publish_date: int = Query(gt=2005,lt=2040)):
    courses_to_return=[]
    for course in courses_db:
        if course.publish_date == publish_date:
            courses_to_return.append(course)
    return courses_to_return

@app.post("/create-course",status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.model_dump())
    courses_db.append(find_course_id(new_course))

def find_course_id(course : Course):
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course

@app.put("/courses/update_course",status_code=status.HTTP_204_NO_CONTENT)
async def update_course(course_request: CourseRequest):
    course_updated = False
    for i in range(len(courses_db)):
        if courses_db[i].id == course_request.id:
            courses_db[i] = course_request
            course_updated = True
    if not course_updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

@app.delete("/courses/delete_course/{course_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int = Path(gt=0)):
    course_deleted = False
    for i in range(len(courses_db)):
        if courses_db[i].id == course_id:
            courses_db.pop(i)
            course_deleted = True
            break
    if not course_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")


