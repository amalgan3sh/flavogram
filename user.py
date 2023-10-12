from flask import Blueprint,request,render_template,request,session,redirect,url_for,flash
from database import*
import uuid

user=Blueprint('user',__name__)

@user.route("/user_home")
def user_home():
	if session.get("unamess"):
		return render_template("user_home.html")
	else:
		return redirect(url_for("public.login"))

@user.route("/user_view_nearby_cook",methods=['get','post'])
def user_view_nearby_cook():
	if session.get("unamess"):
		data={}
		q="select * from users where user_id='%s'"%(session['uid'])
		data['users']=select(q)
		q="select * from products inner join staff using(staff_id) where staff_pin='%s'"%(data['users'][0]['pincode'])
		data['view']=select(q)
		return render_template("user_view_nearby_cook.html",data=data)
	else:
		return redirect(url_for("public.login"))

@user.route("/user_view_cook_products",methods=['get','post'])
def user_view_cook_products():
	if session.get("unamess"):
		data={}
		staff_id=request.args['id']
		q="select * from staff where staff_id='%s'"%(staff_id)
		data['staff']=select(q)
		q="select * from products where staff_id='%s'"%(staff_id)
		data['view']=select(q)
		return render_template("user_view_cook_products.html",data=data)
	else:
		return redirect(url_for("public.login"))

@user.route("/user_view_cook",methods=['get','post'])
def user_view_cook():
	if session.get("unamess"):		
		data={}
		username=session.get("unamess")
		m="select user_id from users where username='%s'"%(username)
		data['user_id']=select(m)
		q="select * from staff"
		data['view']=select(q)
		if 'staff_id' in request.args:
			staff_id=request.args['staff_id'] # needed to change
			q="update staff set status='%s' where staff_id='%s'"%(data['user_id'][0]['user_id'],staff_id)
			w=update(q)
			flash("Added to Favourite")
		return render_template("user_view_cook.html",data=data)
	else:
		return redirect(url_for("public.login"))

@user.route("/user_order_products",methods=['get','post'])
def user_order_products():
	if session.get("unamess"):
		data={}
		q="SELECT *,order_details.`quantity` AS oqty FROM order_master INNER JOIN order_details USING(order_master_id) INNER JOIN products USING(product_id) WHERE user_id='%s' order by status DESC"%(session['uid'])
		data['view']=select(q)
		return render_template("user_order_products.html",data=data)
	else:
		return redirect(url_for("public.login"))
#treata alby
@user.route("/user_view_my_cart",methods=['get','post'])
def user_view_my_cart():
	if session.get("unamess"):
		data={}
		q1="SELECT *,order_details.`quantity` AS oqty FROM order_master INNER JOIN order_details USING(order_master_id) INNER JOIN products USING(product_id) WHERE user_id='%s' and status='pending'"%(session['uid'])
		res=select(q1)
		data['NA']=res
		if 'remove_id' in request.args:
			remove_id=request.args['remove_id']
			q="select * from order_details where order_details_id='%s'"%(remove_id)
			res=select(q)
			q="update order_master set total=total-'%s' where order_master_id='%s'"%(res[0]['amount'],res[0]['order_master_id'])
			update(q)
			q="update products set quantity=quantity+'%s' where product_id='%s'"%(res[0]['quantity'],res[0]['product_id'])
			update(q)
			q="update purchase_child set stockinhand=stockinhand+'%s' where item_id='%s'"%(res[0]['quantity'],res[0]['product_id'])
			update(q)
			q="delete from order_details where order_details_id='%s'"%(remove_id)
			delete(q)
			flash("Item Removed")
			return redirect(url_for("user.user_view_my_cart"))
		return render_template("user_view_my_cart.html",data=data)
	else:
		return redirect(url_for("public.login"))

@user.route("/user_view_order_history",methods=['get','post'])
def user_view_order_history():
	if session.get("unamess"):
		data={}
		q="select *,order_details.`amount` as a,order_details.`quantity` as oq from order_master inner join payment using(order_master_id) inner join order_details using(order_master_id) inner join products using(product_id) where order_master.user_id='%s'"%(session['uid'])
		data['view']=select(q)
		return render_template("user_view_order_history.html",data=data)
	else:
		return redirect(url_for("public.login"))

@user.route("/user_view_products",methods=['get','post'])
def user_view_products():
	if session.get("unamess"):
		data={}
		if 'ser' in request.form:
			se='%'+request.form['se']+'%'
			q="SELECT *,products.price as sprice FROM products inner join category using(cat_id) WHERE product_name LIKE '%s' ORDER BY quantity DESC"%(se)
			# q="SELECT *,products.price as sprice FROM products inner join brand using(brand_id) inner join purchase_child on item_id=products.product_id WHERE product_name LIKE '%s' ORDER BY quantity DESC"%(se)
		else:
			q="SELECT *,products.price as sprice FROM products inner join category using(cat_id) ORDER BY quantity DESC"
			# q="SELECT *,products.price as sprice FROM products inner join brand using(brand_id) inner join purchase_child on item_id=products.product_id ORDER BY quantity DESC"
		data['view']=select(q)
		print(q)
		return render_template("user_view_products.html",data=data)
	else:
		return redirect(url_for("public.login"))

@user.route("/user_buy_products",methods=['get','post'])
def user_buy_products():
	if session.get("unamess"):
		data={}
		pid=request.args['pid']

		if 'submit' in request.form:
			oq=request.form['order_quantity']
			a=request.form['amount']

			q="select * from order_master where user_id='%s' and status='pending'" %(session['uid'])
			res=select(q)
			if res:
				id=res[0]['order_master_id']
			else:
				q="INSERT INTO order_master (`user_id`,`date_time`,`total`,`status`) VALUES('%s',NOW(),'0','pending')" %(session['uid'])
				id=insert(q)
			q="SELECT * FROM order_details WHERE order_master_id='%s' and product_id='%s'"%(id,pid)
			check=select(q)
			if check:
				w="UPDATE order_details set quantity=quantity+'%s',amount=amount+'%s' where order_master_id='%s' and product_id='%s'"%(oq,a,id,pid)
				update(w)
			else:
				q1="INSERT INTO `order_details` (`order_master_id`,`product_id`,`quantity`,`amount`) VALUES('%s','%s','%s','%s')" %(id,pid,oq,a)
				insert(q1)
			q2="update order_master set total=total+'%s' where order_master_id='%s'" %(a,id)
			update(q2)
			q="UPDATE products set quantity=quantity-'%s' where product_id='%s'"%(oq,pid)
			update(q)
			q="UPDATE purchase_child set stockinhand=stockinhand-'%s' where item_id='%s'"%(oq,pid)
			update(q)
			flash("Added to cart")
			# change direction
			return redirect(url_for("user.user_view_my_cart"))
		q="select * from products where product_id='%s'" %(pid)
		res=select(q)
		data['addtocarts']=res
		return render_template("user_buy_products.html",data=data)
	else:
		return redirect(url_for("public.login"))

#treata alby
@user.route("/user_payment",methods=['get','post'])
def user_payment():
	if session.get("unamess"):
		data={}
		omid=request.args['id']
		if 'pay' in request.form:
			q="update order_master set status='paid' where order_master_id='%s'"%(omid)
			update(q)
			q="SELECT * FROM order_master INNER JOIN order_details USING(order_master_id) where user_id='%s' and order_master_id='%s'"%(session['uid'],omid)
			res=select(q)
			w="INSERT INTO payment(`order_master_id`,`amount`,`date`) VALUES('%s','%s',CURDATE())"%(omid,res[0]['total'])
			insert(w)
			flash("Payment Successfully")
			return redirect(url_for("user.user_home"))
		else:
			q1="SELECT *,order_details.`quantity` AS oqty FROM order_master INNER JOIN order_details USING(order_master_id) INNER JOIN products USING(product_id) WHERE user_id='%s' and order_master_id='%s'"%(session['uid'],omid)
			print(q1)
			data['view']=select(q1)
		return render_template("user_payment.html",data=data)
	else:
		return redirect(url_for("public.login"))


@user.route("/user_complaints_and_reply",methods=['get','post'])
def user_complaints_and_reply():
	if session.get("unamess"):
		data={}
		q="SELECT * FROM complaints WHERE user_id='%s'"%(session['uid'])
		data['complaints']=select(q)
		if 'submit' in request.form:
			msg=request.form['msg']
			q="INSERT INTO complaints VALUES(NULL,'%s','%s','pending',NOW())"%(session['uid'],msg)
			insert(q)
			flash("Feedback Submitted")
			return redirect(url_for("user.user_complaints_and_reply"))
		return render_template("user_complaints_and_reply.html",data=data)
	else:
		return redirect(url_for("public.login"))


# user_payment

# @user.route("/user_view_products",methods=['get','post'])
# def user_view_products():
# 	if session.get("uname"):
# 		return render_template("user_view_products.html")
# 	else:
# 		return redirect(url_for("public.login"))