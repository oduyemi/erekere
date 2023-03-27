import os, random, string
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, flash
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from ereapp import starter, db
from ereapp.models import Admin, Contact, Payment, P_status, Trip, Tour, User
from ereapp.form import LoginForm


from ereapp import starter



def generate_name():
    global filename
    filename = random.sample(string.ascii_lowercase,10) #this will return a list
    return ''.join(filename) #here we join every member of the list "filename"


#             --  ROUTES --





@starter.route('/admin/signup', methods = ["POST", "GET"], strict_slashes = False)
def adminsignup():
    if request.method == "GET":
        return render_template('admin/adminsignup.html', title="Sign Up")
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        username = request.form.get("username")
        password=request.form.get("password")
        hashedpwd = generate_password_hash(password)
    if fname !='' and lname != "" and username !='' and password !='':
        new_admin=Admin(admin_fname = fname, admin_lname = lname, admin_username = username,
        admin_password = hashedpwd)
        db.session.add(new_admin)
        db.session.commit()
        adminid=new_admin.admin_id
        session['admin']=adminid
        flash(f"Account created for {fname}! Please proceed to LOGIN ", "success")
        return redirect(url_for('adminlogin'))
    else:
        flash('You must fill the form correctly to signup', "danger")


@starter.route('/admin/login', methods = ['POST', 'GET'], strict_slashes = False)
def adminlogin():
    form = LoginForm()
    if request.method=='GET':
        return render_template('admin/adminlogin.html', form=form)
    else:
        username=request.form.get('username')
        pwd=request.form.get('password')
        deets = db.session.query(Admin).filter(Admin.admin_username==username).first() 
        if deets !=None:
            pwd_indb = deets.admin_password
            chk = check_password_hash(pwd_indb, pwd)
            if chk:
                id = deets.admin_id
                session['admin'] = id
                return redirect(url_for('adminhome'))
            else:
                flash('Invalid password')
        else:
            return redirect(url_for('adminlogin'))


@starter.route('/admin')
def adminhome():
    id=session.get("admin")
    if id == None:
        return redirect(url_for("adminlogin"))
    else:
        mdeets = db.session.query(Trip).filter(Trip.trip_payment_status==2).all()
        if request.method == 'GET':
            return render_template("admin/admindashboard.html", mdeets=mdeets)
        else:
            return redirect("/admin/adminlogin")


@starter.route("/admin/pending", strict_slashes = False)
def pendingpay():
    if session.get('admin') != None:
        mdeets=db.session.query(Payment).where(Payment.payment_status==1).all()
    return render_template('admin/pending.html',mdeets=mdeets)


@starter.route("/admin/approve/<int:id>", strict_slashes = False)
def approve(id):
    if session.get('admin') != None:
       item=Payment.query.get_or_404(id)
       deets = db.session.query(Payment).filter(Payment.payment_status==3).first() 
       query1=f"UPDATE payment SET payment_status=2 WHERE payment_user=id"
       query2=f"UPDATE trip SET trip_payment_status=2 WHERE trip_user=id"
       db.session.execute(text(query1, query2))
    try:
        db.session.commit()
        return redirect(url_for('adminhome'))
        
    except:
        return redirect(url_for('adminhome'))


@starter.route("/admin/email", strict_slashes = False)
def email():
    if session.get('admin') != None:
        mdeets=db.session.query(Contact).all()
        return render_template('admin/email.html',mdeets=mdeets)


@starter.route("/admin/messages", strict_slashes = False)
def messages():
    if session.get('admin') != None:
        mdeets = db.session.query(Contact).where(Contact.contact_status_id==1).all()
        
        if request.method == 'GET':
            return render_template("admin/inview.html", mdeets=mdeets)


@starter.route("/admin/sort/<msg>", strict_slashes = False)
def sort(msg):
    item=Contact.query.get_or_404(msg)
    if session.get('admin') != None:
        query=f"UPDATE contact SET contact_status_id=3 WHERE contact_id='{msg}'"
        db.session.execute(text(query))
        db.session.commit()
        return redirect("/admin/messages")

@starter.route("/admin/sorted", strict_slashes = False)
def sorted():
    if session.get('admin') != None:
        mdeets=db.session.query(Contact).where(Contact.contact_status_id==3).all()
        return render_template('admin/sorted.html',mdeets=mdeets)


@starter.route("/admin/club", strict_slashes = False)
def club():
    if session.get('admin') != None:
        mdeets=db.session.query(User).all()
        return render_template('admin/club.html',mdeets=mdeets)


@starter.route("/admin/tours", methods=["GET","POST"], strict_slashes = False)
def admintours():
    #id = db.session.query(Tour).filter(Tour.tour_id).first()
    mdeets=db.session.query(Tour).order_by(Tour.tour_id.desc()).all()
    if request.method == "POST":
        if session.get('admin') != None:
            title=request.form.get("title")
            desc=request.form.get("desc")
            price=request.form.get("price")
            start=datetime.strptime(request.form['startdate'], '%Y-%m-%d')
            end=datetime.strptime(request.form['enddate'], '%Y-%m-%d')
            img=request.files['img']
            filename = img.filename 
            filetype = img.mimetype
            allowed= ['.png','.jpg','.jpeg', ".webp", '.pdf'] 
            if filename !="":
                name,ext = os.path.splitext(filename) 
                if ext.lower() in allowed: 
                    newname = generate_name()+ext
                    img.save("ereapp/static/uploads/"+newname) 
                else:
                    return "File not allowed!"
            else:
                flash("Please choose a File")
        #entry = db.session.query(Tour).filter(Tour.tour_name==title, Tour.tour_desc==desc, Tour.tour_price==price, Tour.tour_img==newname)
        query = f"INSERT INTO tour (tour_name, tour_desc, tour_price, tour_img, tour_startdate, tour_enddate) VALUES('{title}','{desc}','{price}','{newname}', '{start}', '{end}')"
        db.session.execute(text(query))
        db.session.commit()
        flash('Trip information successfully completed')
        
    return render_template('admin/tourpost.html', mdeets=mdeets)


@starter.route("/delete/<int:id>", strict_slashes = False)
def delete(id): 
    item=Contact.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('adminhome'))
        
    except:
        return redirect(url_for('adminhome'))


@starter.route("/deletetour/<int:id>", strict_slashes = False)
def deletetour(id): 
    item=Tour.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('admintours'))
        
    except:
        return redirect(url_for('admin'))


@starter.route("/admin/logout", strict_slashes = False)
def adminlogout():
    if session.get("admin") != None:
        session.pop("admin", None)
    return redirect('/admin/login')