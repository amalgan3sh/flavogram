from flask import Blueprint,request,render_template,request,session,redirect,url_for,flash
from database import*
from datetime import*
import uuid

admin=Blueprint('admin',__name__)

@admin.route("/admin_home")
def admin_home():
	if session.get("unamess"):
		return render_template("admin_home.html")
	else:
		return redirect(url_for("public.login"))


@admin.route("/admin_view_order_payment_report",methods=['get','post'])
def admin_view_order_report():
	if session.get("unamess"):
		data={}
		if 'submit' in request.form:
			d1=request.form['d1']
			d2=request.form['d2']
			q="SELECT *,order_details.`amount` as a,order_details.`quantity` as oq from order_master inner join payment using(order_master_id) inner join order_details using(order_master_id) inner join products using(product_id) inner join users using(user_id) WHERE date_time BETWEEN '%s' AND '%s'"%(d1,d2)
			res=select(q)
			if res:
				data['view']=res
			else:
				flash("Orders not availble on this duration")
		return render_template("admin_view_order_report.html",data=data)
	else:
		return redirect(url_for("public.login"))


@admin.route("/admin_manage_homecook",methods=['get','post'])
def admin_manage_staff():
	if session.get("unamess"):
		data={}
		q="select * from staff"
		data['view']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=='delete':
			q="delete from login where username='%s'"%(id)
			delete(q)
			q="delete from staff where username='%s'"%(id)
			delete(q)
			flash("Removed")
			return redirect(url_for('admin.admin_manage_staff'))

		if action=='update':
			q="select * from staff where username='%s'"%(id)
			data['update_view']=select(q)

		if 'update_submit' in request.form:
			staff_name=request.form['staff_name']
			staff_num=request.form['staff_num']
			details=request.form['details']		
			staff_city=request.form['staff_city']
			staff_pin=request.form['staff_pin']

			q="UPDATE`staff` set `staff_name`='%s',`staff_num`='%s',`details`='%s',`staff_city`='%s',`staff_pin`='%s' where username='%s'"%(staff_name,staff_num,details,staff_city,staff_pin,id)
			update(q)
			flash("Changes Saved!")
			return redirect(url_for('admin.admin_manage_staff'))

		if 'submit' in request.form:
			staff_name=request.form['staff_name']
			staff_num=request.form['staff_num']
			details=request.form['details']
			staff_city=request.form['staff_city']
			staff_pin=request.form['staff_pin']
			email=request.form['username']
			passs=request.form['psw']

			q="select * from login where username='%s'"%(email)
			res=select(q)
			if res:
				flash("Email already Exist. Try Another One...")
			else:
				q1="insert into login(username,password,usertype)values('%s','%s','staff')"%(email,passs)
				insert(q1)
				q="INSERT INTO `staff` (`username`,`staff_name`,`staff_num`,`details`,`staff_city`,`staff_pin`,staff_status)VALUES('%s','%s','%s','%s','%s','%s','active')"%(email,staff_name,staff_num,details,staff_city,staff_pin)
				insert(q)
				flash("Successfully Registered!")
				return redirect(url_for('admin.admin_manage_staff'))
		return render_template("admin_manage_staff.html",data=data)
	else:
		return redirect(url_for("public.login"))


@admin.route("/admin_manage_category",methods=['get','post'])
def admin_manage_category():
	if session.get("unamess"):
		data={}
		if 'action' in request.args:
			action=request.args['action']
			cid=request.args['cid']
		else:
			action=None

		if action=='update':
			q="select * from category where cat_id='%s'"%(cid)
			res=select(q)
			data['updates']=res

		if action=='remove':
			q="delete from category where cat_id='%s'"%(cid)
			res=delete(q)
			flash("Removed")
			return redirect(url_for("admin.admin_manage_category"))

		if 'submit_update' in request.form:
			catname=request.form['catname']
			desc=request.form['desc']
			q="update category set cat_name='%s',description='%s' where cat_id='%s'"%(catname,desc,cid)
			update(q)
			flash("Changes Saved")
			return redirect(url_for('admin.admin_manage_category'))

		if 'submit' in request.form:
			catname=request.form['catname']
			desc=request.form['desc']
			q="select * from category where cat_name='%s'"%(catname)
			res=select(q)
			if res:
				flash("This Category Already Exist!!!")
			else:
				q="INSERT INTO category(cat_name,description)VALUES('%s','%s')"%(catname,desc)
				insert(q)
				flash("Saved")
				return redirect(url_for('admin.admin_manage_category'))

		q1="select *from category"
		res=select(q1)
		data['cat']=res
		return render_template("admin_manage_category.html",data=data)
	else:
		return redirect(url_for("public.login"))
			

@admin.route("/admin_manage_products",methods=['get','post'])
def admin_manage_products():
	print("sdf",session.get("unamess"))
	# if session.get("unamess"):

	data={}
	q="select * from products"
	data['view']=select(q)
	q="select * from staff"
	data['staff']=select(q)
	q="select * from category"
	data['cat']=select(q)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='remove':
		q="delete from products where product_id='%s'"%(id)
		delete(q)
		flash("Product Removed")
		return redirect(url_for('admin.admin_manage_products'))
	if action=='update':
		q="select * from products inner join category using(cat_id) where product_id='%s'"%(id)
		data['updated_view']=select(q)
# update_submit
	if 'update_submit' in request.form:
		product_name=request.form['pdt_name']
		# brand_id=request.form['brand_id']
		cat_id=request.form['cat_id']
		qty=request.form['qty']
		details=request.form['det']
		price=request.form['price']
		
		q="UPDATE products set cat_id='%s',`product_name`='%s',`product_details`='%s',`price`='%s',`quantity`='%s' where product_id='%s'"%(cat_id,product_name,details,price,qty,id)
		print(q)
		update(q)
		flash("Changes Saved")
		return redirect(url_for("admin.admin_manage_products"))

	if 'submit' in request.form:
		product_name=request.form['pdt_name']
		# brand_id=request.form['brand_id']
		cat_id=request.form['cat_id']
		# vendor_id=request.form['cmp']
		details=request.form['det']
		price=request.form['price']
		img=request.files['images']
		path="static/"+str(uuid.uuid4())+img.filename
		img.save(path)
		q="INSERT INTO products (`cat_id`,`product_name`,`product_details`,quantity,`price`,image) VALUES('%s','%s','%s','0','%s','%s')"%(cat_id,product_name,details,price,path)
		insert(q)
		flash("Products Added")
		return redirect(url_for("admin.admin_manage_products"))
	return render_template("admin_manage_products.html",data=data)
	# else:
	# 	# pass
	# 	return redirect(url_for("public.login"))


@admin.route('/admin_view_customers',methods=['get','post'])
def admin_view_customers():
	if not session.get("unamess") is None:
		data={}
		q="select *,concat(first_name,' ',last_name) as urname from users"
		data['view']=select(q)
		return render_template("admin_view_customers.html",data=data)
	else:
		return redirect(url_for("public.login"))


@admin.route("/admin_view_complaints_and_send_reply",methods=['get','post'])
def admin_view_complaints_and_send_reply():
	if session.get("unamess"):
		data={}
		q="SELECT *,CONCAT(first_name,' ',last_name) AS urname FROM complaints INNER JOIN users USING(user_id)"
		data['msgs']=select(q)
		i=1
		for row in data['msgs']:
			if 'submit'+str(i) in request.form:
				reply=request.form['reply'+str(i)]
				q="update complaints set reply='%s',date_time=NOW() where complaint_id='%s'"%(reply,row['complaint_id'])
				update(q)
				flash("Replied")
				return redirect(url_for("admin.admin_view_complaints_and_send_reply"))
			i=i+1
		return render_template("admin_view_complaints_and_send_reply.html",data=data)
	else:
		return redirect(url_for("public.login"))

@admin.route("/admin_make_purchase",methods=['get','post'])
def admin_make_purchase():
	if session.get("unamess"):
		data={}
		item_id=request.args['pid']
		q="select * from products where product_id='%s'"%(item_id)
		data['pdt']=select(q)
		q="select * from staff"
		data['staff']=select(q)
		if 'submit' in request.form:
			staff_id=request.form['staff_id']
			vendor=request.form['cmp']
			qty=request.form['qty']
			price=request.form['price']
			ex=request.form['ex']
			mfg=request.form['mfg']
			bno=request.form['bno']
			today = date.today()
			print(mfg)

			# dd/mm/YY
			d1 = today.strftime("%Y-%m-%d") 
			print(d1)
			if mfg<ex and mfg<d1 and ex>d1:
				q="select * from purchase_master where staff_id='%s' and status='NA'" %(staff_id)
				res=select(q)
				if res:
					id=res[0]['mpurchase_id']
				else:
					q="INSERT INTO `purchase_master` (`staff_id`,`purchase_total`,`purchase_date`,status)VALUES('%s','0',NOW(),'NA')"%(staff_id)
					id=insert(q)
				q="select * from products where product_id='%s'"%(item_id)
				result=select(q)
				q="select * from purchase_child where item_id='%s' and mpurchase_id='%s' and exp_date='%s' and batch_no='%s' and mfd_date='%s'"%(item_id,id,ex,bno,mfg)
				check=select(q)
				if check:
					check1=check[0]['cpurchase_id']
					q1="UPDATE purchase_child set pur_qty=pur_qty+'%s',sub_tot=sub_tot+'%s' where cpurchase_id='%s'"%(qty,price,check1)
					update(q1)
				else:
					q1="INSERT INTO purchase_child (`mpurchase_id`,`item_id`,`pur_qty`,`sub_tot`,`stockinhand`,`exp_date`,`batch_no`,`mfd_date`) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" %(id,item_id,qty,price,result[0]['quantity'],ex,bno,mfg)
					check1=insert(q1)
				q2="update purchase_master set purchase_total=purchase_total+'%s' where mpurchase_id='%s'" %(price,id)
				update(q2)
				q3="UPDATE purchase_child set stockinhand=stockinhand+'%s' where item_id='%s' and cpurchase_id='%s'"%(qty,item_id,check1)
				update(q3)
				q4="update products set quantity=quantity+'%s',vendor_id='%s' where product_id='%s'"%(qty,vendor,item_id)
				update(q4)
				flash("Product Added")
				return redirect(url_for("admin.admin_make_purchase",pid=item_id))
			else:
				flash("Manufacturing Date or Expiry Date is Not Valid")
		return render_template("admin_make_purchase.html",data=data)
	else:
		return redirect(url_for("public.login"))

@admin.route("/admin_view_products",methods=['get','post'])#treata dbt
def admin_view_products():
	if session.get("unamess"):
		data={}
		q="select * from category"
		data['cat']=select(q)
		
		# change
		q="select * from products"
		data['view']=select(q)
		return render_template("admin_view_products.html",data=data)
	else:
		return redirect(url_for("public.login"))

@admin.route("/admin_view_staff_report",methods=['get','post'])
def admin_view_staff_report():
	if session.get("unamess"):
		data={}
		q="select * from staff"
		res=select(q)
		data['staff']=select(q)
		return render_template('admin_view_staff_report.html',data=data)
	else:
		return redirect(url_for("public.login"))
