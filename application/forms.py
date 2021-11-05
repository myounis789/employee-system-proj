from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

class AddEmp(FlaskForm):
    emp_name = StringField("empName")
    emp_subject = SelectField("empSubject", choices=[('Java', 'Java/Javascript'), ('SQL', 'SQL'), ('Python', 'Python'), ('Csharp', 'C++/C#'), ('Html', 'HTML')])
    emp_marks = IntegerField("empMarks")
    emp_dept = SelectField("empDept", choices=[('HR', 'Human Resources'), ('IT', 'Information Technology'), ('Sales', 'Sales'), ('Training', 'Training & Development'), ('DevOps', 'DevOps')])
    emp_salary = IntegerField('empSalary')
    submit = SubmitField('Add Employee')

class EditEmp(FlaskForm):
    emp_name = StringField("empName")
    emp_subject = SelectField("empSubject", choices=[('Java', 'Java/Javascript'), ('SQL', 'SQL'), ('Python', 'Python'), ('Csharp', 'C++/C#'), ('Html', 'HTML')])
    emp_marks = IntegerField("empMarks")
    emp_dept = SelectField("empDept", choices=[('HR', 'Human Resources'), ('IT', 'Information Technology'), ('Sales', 'Sales'), ('Training', 'Training & Development'), ('DevOps', 'DevOps')])
    emp_salary = IntegerField('empSalary')
    submit = SubmitField('Update Employee')