from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from ereapp import db




class Admin(db.Model):
    admin_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_fname=db.Column(db.String(100),nullable=True)
    admin_lname=db.Column(db.String(100),nullable=True)
    admin_username=db.Column(db.String(100),nullable=True, unique=True)
    admin_password=db.Column(db.String(200),nullable=True)
    admin_regdate = db.Column(db.DateTime(), default=datetime.utcnow)

class User(db.Model):
    user_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_fullname=db.Column(db.String(100),nullable=True)
    user_phone=db.Column(db.String(100),nullable=True)
    user_username=db.Column(db.String(100),nullable=True, unique=True)
    user_password=db.Column(db.String(200),nullable=True)
    user_question = db.Column(db.Integer, db.ForeignKey('question.question_id'))
    user_secret = db.Column(db.String(255),nullable=True)
    user_regdate = db.Column(db.DateTime(), default=datetime.utcnow)
    #Relationship
    userdeets = db.relationship("Question", backref="questdeets")


class Question(db.Model):
    question_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    question_name=db.Column(db.String(255),nullable=True)

    #Relationship
    #questdeets = db.relationship("User", backpopulates="userdeets")


class Contact_status(db.Model):
    status_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    statusname=db.Column(db.String(120),nullable=False)

class P_status(db.Model):
    p_status_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    p_status_status = db.Column(db.String(120),nullable=False)


class Contact(db.Model):
    contact_id=db.Column(db.Integer, autoincrement=True,primary_key=True) 
    contact_name=db.Column(db.String(150),nullable=False)   
    contact_email=db.Column(db.String(100),nullable=False)
    contact_phone=db.Column(db.String(40),nullable=False)
    contact_gender=db.Column(db.String(100),nullable=False)
    contact_method=db.Column(db.String(100),nullable=False)
    contact_content=db.Column(db.Text(),nullable=False)
    contact_date = db.Column(db.DateTime(), default=datetime.utcnow)
    contact_status_id=db.Column(db.Integer, db.ForeignKey('contact_status.status_id'))
    contact_admin_id=db.Column(db.Text(),nullable=True)


class Payment(db.Model):
    payment_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    payment_userfname = db.Column(db.String(200),nullable=True)   
    payment_user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    payment_amount = db.Column(db.Float(),nullable=True)
    payment_trip = db.Column(db.Integer, db.ForeignKey('tour.tour_id'))
    payment_date = db.Column(db.DateTime(), default=datetime.utcnow)
    payment_status = db.Column(db.Integer, db.ForeignKey('p_status.p_status_id')) 

    #Relationship
    paydeets = db.relationship("P_status", backref="pdeets")  


class Trip(db.Model):
    trip_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    trip_tour = db.Column(db.Integer, db.ForeignKey('tour.tour_id'))
    trip_user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    trip_receipt = db.Column(db.String(120),nullable=True) 
    trip_payment_status = db.Column(db.Integer, db.ForeignKey('p_status.p_status_id'))

    #Relationship
    tripdeets = db.relationship("Tour", backref="tourdeets")
    tripuserdeets = db.relationship("User", backref="user_deets")
    tripp_deets = db.relationship("P_status", backref="pee_deets")

class Tour(db.Model):
    tour_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    tour_name = db.Column(db.String(200),nullable=False)
    tour_desc = db.Column(db.Text(), nullable=True)
    tour_price = db.Column(db.String(200),nullable=False)
    tour_img = db.Column(db.String(200), nullable=False)
    tour_startdate = db.Column(db.DateTime(), nullable=True)
    tour_enddate = db.Column(db.DateTime(), nullable=True)


