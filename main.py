# Import Libraries
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

# Initialize a FastAPI object
app = FastAPI()

class Subjects(BaseModel):
    Maths: Annotated[int, Field(..., description="Marks scored in Mathematics")]
    Physics: Annotated[int, Field(..., description="Marks scored in Physics")]
    computer_science: Annotated[int, Field(..., alias="Computer Science", description="Marks scored in Computer Science")]
    English: Annotated[int, Field(..., description="Marks scored in English")]
    Chemistry: Annotated[int, Field(..., description="Marks scored in Chemistry")]

class Student(BaseModel):
    id: Annotated[str, Field(..., description="ID of the student", examples=["S001"])]
    name: Annotated[str, Field(..., description="Name of the student")]
    age: Annotated[int, Field(..., gt=0, lt=25, description="Age of the student")]
    gender: Annotated[Literal['Male', 'Female'], Field(..., description="Gender of the student")]
    roll_number: Annotated[str, Field(..., description="Roll number of the student", examples=["CS2025000"])]
    subjects: Subjects
    attendance_percentage: Annotated[float, Field(..., description="Attendance Percentage of the student")]

    @computed_field
    @property
    def total_marks(self) -> int:
        s = self.subjects
        return s.Maths + s.Physics + s.computer_science + s.English + s.Chemistry
        return total_marks_add

    @computed_field
    @property
    def average_marks(self) -> float:
        return self.total_marks/5


# Utility Functions
def load_data():
    '''Function to load and return student's data from the JSON file'''
    with open('students.json','r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f)

# Routings and Functions
@app.get("/")
def source_page():
    '''Function to return the content to be displayed on the source page'''
    return {"Key": "Students Management System"}

@app.get("/about")
def about_page():
    '''Function to return the content to be displayed on the about page'''
    return {"key": "This is a student management system where the user can perform the following tasks: 1. View student's information, 2. Create a new student, 3. Modify an existing student, 4. Delete an existing student"}

@app.get("/view_students")
def view_students_page():
    '''Function to return students data for the view_students page'''
    if os.path.exists("students.json"):
        data = load_data()
    else:
        raise HTTPException(404, detail = "Students data does not exist")
    return data

@app.get("/view/{student_id}")
def view_student(student_id: str = Path(..., description= "Provide ID of the student", example = "S001")):
    '''Function to return information of an individual student for the view_student page'''
    data = load_data()
    if student_id not in data:
        raise HTTPException(404, detail= "Student not found")
    else:
        return data[student_id]

@app.get("/sort")
def sort_students_info(sort_on: str = Query(..., description= "Name of the column on which the data needs to be sorted, available options: [attendance_percentage, total_marks]"), sort_by: str = Query('asc', description= "Select valid sorting option")):
    df = load_data()
    if sort_by in ['asc','desc']:
        sort_order = True if sort_by == 'desc' else False
        if sort_on in ['attendance_percentage', 'total_marks']:
            sorted_values = sorted(df.values(), key = lambda x: x.get(sort_on,0), reverse = sort_order)
            return sorted_values
        raise HTTPException(400, detail= "Enter valid column name")
    raise HTTPException(400, detail= "Sorting option can either be asc or desc")

@app.post('/create')
def create_student(student: Student):
    data = load_data()
    if student.id in data:
        raise HTTPException(400, detail="Student already exist")
    else:
        data[student.id] = student.model_dump(exclude=['id'])
        save_data(data)
        return JSONResponse(status_code=201, content={'message':'New student successfully created'})


















