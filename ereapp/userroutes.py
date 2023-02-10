from flask import render_template

from ereapp import starter

@starter.route('/')
def homepage():
    return render_template('user/index.html')


@starter.route('/contact')
def contactpage():
    return render_template('user/contact.html')

@starter.route('/about')
def aboutpage():
    return render_template('user/about.html')

@starter.route('/login')
def loginpage():
    return render_template('user/login.html')

@starter.route('/media')
def mediapage():
    return render_template('user/media.html')

@starter.route('/account')
def accountpage():
    return render_template('user/myaccount.html')

@starter.route('/tours')
def tourspage():
    return render_template('user/tours.html')

@starter.route('/trip')
def trippage():
    return render_template('user/trip.html')

@starter.route('/privacy-policy')
def privacypolicypage():
    return render_template('user/privacy-policy.html')

@starter.route('/site-requirements')
def siterequirementspage():
    return render_template('user/site-requirements.html')

@starter.route('/terms-conditions')
def termsandconditionpage():
    return render_template('user/terms.html')

@starter.route('/signup')
def signupage():
    return render_template('user/signup.html')