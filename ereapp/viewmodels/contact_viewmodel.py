import flask
from flask import render_template, request, redirect, url_for, session, flash
from ereapp import starter, db
from ereapp.models import User, Contact


class ContactViewModel():
    def __init__(self):
        """Create the ViewModel with the form data from the request """
        request = flask.request
        self.name = request.form.get("c_name")
        self.phone = request.form.get("phone")
        self.email = request.form.get("email")
        self.gender=request.form.get("gender")
        self.method=request.form.get("method")
        self.message=request.form.get("message")
        self.error = None
    
    def validate(self):
        """Form validation """
        if not self.name or not self.name.strip():
            error = "This field cannot be blank. Please provide a valid name"
        if not self.email or not self.email.strip():
            error = "This field cannot be blank. Please provide a valid email address"
        if not self.phone or not self.phone.strip():
            error = "This field cannot be blank. Please provide a valid phone number"
        if not self.gender or not self.gender.strip():
            error = "This field cannot be blank. Please choose your gender"
        if not self.method or not self.method.strip():
            error = "This field cannot be blank. Please tell us how you would like to be contacted"
        if not self.message or not self.message.strip():
            error = "This field cannot be blank. Please drop a message"

       
    def __str__(self):
        """Create a readable output for the data
        """
        return f"{self.name} {self.email} {self.phone} {self.gender} [{self.method}]: {self.message}"

    def to_dict(self):
        """ Turn this object into a dictionary"""
        return self.__dict__