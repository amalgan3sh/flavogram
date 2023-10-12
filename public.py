from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from database import *

public=Blueprint("public",__name__)

@public.route("/")
def home():
	session.clear()
	return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if 'submit' in request.form:
		uname=request.form['uname']
		passs=request.form['passs']
		q="select * from login where username='%s' and password='%s'" %(uname,passs)
		print(q)
		res=select(q)
		if res:
			session['unamess']=res[0]['username']
			if res[0]['usertype']=="admin":
				flash("Logging in")			
				return redirect(url_for("admin.admin_home"))

			elif res[0]['usertype']=="staff":
				q="select * from staff where username='%s'"%(session['unamess'])
				res1=select(q)
				if res1:
					session['sid']=res1[0]['staff_id']
					flash("Logging in")
					return redirect(url_for("homecook.staff_home"))

			elif res[0]['usertype']=="user":
				q="select * from users where username='%s'"%(session['unamess'])
				res1=select(q)
				if res1:
					session['uid']=res1[0]['user_id']
					flash("Logging in")
					return redirect(url_for("user.user_home"))
			else:
				flash("Registration Under Process")
		flash("You are Not Registered")
	return render_template("login.html")

@public.route('/reg',methods=['get','post'])
def user_registration():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']		
		place=request.form['place']
		pincode=request.form['pincode']
		email=request.form['email']
		phone=request.form['phone']
		passs=request.form['passs']

		q="select * from login where username='%s'"%(email)
		res=select(q)
		if res:
			flash("Email already Exist. Try Another One...")
		else:
			q1="insert into login(username,password,usertype)values('%s','%s','user')"%(email,passs)
			insert(q1)
			q="INSERT INTO `users` (`username`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`email`,`phone`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%(email,fname,lname,hname,place,pincode,email,phone)
			print(q)
			insert(q)
			flash("Successfully Registered. Login Now!")
			return redirect(url_for('public.login'))		

	return render_template("user_registration.html")