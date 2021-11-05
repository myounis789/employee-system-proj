from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

application=Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SECRET_KEY'] = os.getenv('secretkey')
db = SQLAlchemy(application)

class Employees(db.Model):
    empNo = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.CHAR(20))
    Subject = db.Column(db.CHAR(20))
    Marks = db.Column(db.Integer)
    Department = db.Column(db.CHAR(30))
    Salary = db.Column(db.Integer)

class AddEmp(FlaskForm):
    emp_name = StringField("empName")
    emp_subject = IntegerField("empSubject", choices=[('Java', 'Java/Javascript'), ('SQL', 'SQL'), ('Python', 'Python'), ('Csharp', 'C++/C#'), ('Html', 'HTML')])
    emp_marks = IntegerField("empMarks")
    emp_dept = SelectField("empDept", choices=[('HR', 'Human Resources'), ('IT', 'Information Technology'), ('Sales', 'Sales'), ('Training', 'Training & Development'), ('DevOps', 'DevOps')])
    emp_salary = SelectField('empSalary')
    submit = SubmitField('Add Employee')

class EditEmp(FlaskForm):
    emp_name = StringField("empName")
    emp_subject = IntegerField("empSubject", choices=[('Java', 'Java/Javascript'), ('SQL', 'SQL'), ('Python', 'Python'), ('Csharp', 'C++/C#'), ('Html', 'HTML')])
    emp_marks = IntegerField("empMarks")
    emp_dept = SelectField("empDept", choices=[('HR', 'Human Resources'), ('IT', 'Information Technology'), ('Sales', 'Sales'), ('Training', 'Training & Development'), ('DevOps', 'DevOps')])
    emp_salary = SelectField('empSalary')
    submit = SubmitField('Update Employee')

db.create_all()

@application.route("/")
def homePage():
    data = Employees.query.all()
    return render_template("homepage.html", records=data)

# @application.route("/addNewRecord")
# def addNewRecord():
    # return render_template("inputForm.html")
# 

@application.route("/saveRecord", methods=["GET","POST"])
def saveRecord():
    form = AddEmp()
    if request.method == 'POST':
        newName=form.emp_name.data
        newSubject=form.emp_subject.data
        newMarks=form.emp_marks.data
        newDept=form.emp_dept.data
        newSalary=form.emp_salary.data

        newEmp = Employees (Name = newName, Subject = newSubject, Marks = newMarks, Department = newDept , Salary = newSalary)
        db.session.add(newEmp)
        db.session.commit()
        return redirect("/")
    
    return render_template("inputForm.html", form=form)

@application.route("/employeeDetails/<int:empno>")
def displayDetails(empno):
    data = Employees.query.filter_by(empNo=empno).first()
    return render_template("personalInformation.html",record=data)

@application.route("/viewAll")
def viewAll():
    data2 = Employees.query.all()
    return render_template("viewAll.html", record1=data2)

@application.route("/deleteRecord/<int:empno>")
def deleteRecord(empno):
    emp = Employees.query.filter_by(empNo=empno).first()
    db.session.delete(emp)
    db.session.commit()
    return redirect("/")

@application.route("/editDetails/<int:empno>")
def editDetails(empno):
    form =EditEmp()
    emp = Employees.query.filter_by(empNo=empno).first()
    if request.method == 'POST':
        emp.Name = form.emp_name.data
        emp.Subject = form.emp_subject.data
        emp.Marks = form.emp_marks.data
        emp.Department = form.emp_dept.data
        emp.Salary = form.emp_salary.data
        db.session.commit()
        return redirect("/")
    return render_template("editForm.html", form=form)

# @application.route("/saveEditedRecord", methods=["POST"])
#def saveEditedRecord():
#    empno=request.form["employeeNum"]
#    name=request.form["employeeNa"]
#    subject = request.form["employeeSbjct"]
#    marks=request.form["employeeMarks"]
#    department=request.form["employeeDept"]
#    salary=request.form["employeeSlry"]
#    emp = Employees.query.filter_by(empNo=empno).first()
#    emp.name = name
#    emp.subject = subject
#    emp.marks = marks
#    emp.department = department
#    emp.salary = salary
# 
#    db.session.commit()
#    return redirect("/")

@application.route("/searchRecord", methods=["POST"])
def searchRecord():
    search_type = request.form["searchby"]
    search_Data = request.form["dataSearch"]
    data1 = eval(f"Employees.query.filter_by({search_type} = '{search_Data}').all()")
    return render_template("searchResults.html", searchRecords = data1)

application.run(debug=True)


