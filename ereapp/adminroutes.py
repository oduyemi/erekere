from flask import render_template, redirect, flash, session,request


from ereapp import starter

@starter.route('/admin')
def adminhome():
    return 'admin homepage'