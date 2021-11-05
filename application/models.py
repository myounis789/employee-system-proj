from application import db

class Employees(db.Model):
    empNo = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.CHAR(20))
    Subject = db.Column(db.CHAR(20))
    Marks = db.Column(db.Integer)
    Department = db.Column(db.CHAR(30))
    Salary = db.Column(db.Integer)