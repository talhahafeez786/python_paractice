from unicodedata import name
from webbrowser import get
from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


students = {
    1 : {
        "name" : "Talha",
        "age" : "20",
        "Degree" : "BSIT"
    },
    2: {
        "name" : "Talha1111",
        "age" : "20",
        "Degree" : "BSIT"
    }
}

class student(BaseModel):
    name : str
    age : int
    Degree : str

class updatestudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    Degree : Optional[str] = None

@app.get('/')
def get_all_students():
    return students

@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(None, description="The id of the student you want to view", gt=0)):
    return students [student_id]

@app.get("/get-by-name")
def get_student(name : str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return{"Data" : "not Found"}

@app.post("/create-student{student_id}")
def create_student(student_id : int , student : student):
    if student_id in students:
        return {"Error" : "Student Exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student{student_id}")
def update_student(student_id : int, student : updatestudent):
    if student_id not in students:
        return {"Error" : "Student does not exists"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.Degree != None:
        students[student_id].Degree = student.Degree

    return  students[student_id]   

@app.delete("/delete-student{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "student does not exists"}

    del students[student_id]
    return {"Student" : "Deleted"} 
    