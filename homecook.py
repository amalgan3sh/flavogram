from flask import Blueprint,request,render_template,request,session,redirect,url_for,flash
from database import*
from datetime import*
import uuid

homecook=Blueprint('homecook',__name__)

@homecook.route("/staff_home")
def staff_home():
	if session.get("unamess"):
		return render_template("staff_home.html")
	else:
		return redirect(url_for("public.login"))

@homecook.route("/staff_view_purchased_products")
def staff_view_purchased_products():
	if session.get("unamess"):
		data={}
		q="SELECT * FROM `purchase_master` INNER JOIN `purchase_child` USING(mpurchase_id) INNER JOIN products ON purchase_child.`item_id`=products.`product_id` inner join vendors using(vendor_id) where staff_id='%s' order by exp_date asc"%(session['sid'])
		data['view']=select(q)
		today = date.today()
		d1 = today.strftime("%Y-%m-%d") 
		if 'expire_id' in request.args:
			expire_id=request.args['expire_id']
			q="SELECT * FROM purchase_child WHERE cpurchase_id='%s'"%(expire_id)
			res=select(q)
			q="UPDATE purchase_master SET purchase_total=purchase_total-'%s' WHERE mpurchase_id='%s'"%(res[0]['sub_tot'],res[0]['mpurchase_id'])
			update(q)
			q="UPDATE products SET quantity=quantity-'%s' WHERE product_id='%s'"%(res[0]['stockinhand'],res[0]['item_id'])
			update(q)
			q="DELETE FROM purchase_child WHERE cpurchase_id='%s'"%(expire_id)
			delete(q)
			flash("Products removed from stock")
			return redirect(url_for("homecook.staff_view_purchased_products"))
		return render_template("staff_view_purchased_products.html",data=data,d1=d1)
	else:
		return redirect(url_for("public.login"))


@homecook.route("/staff_manage_brand",methods=['get','post'])
def staff_manage_brand():
	if session.get("unamess"):
		data={}
		if 'action' in request.args:
			action=request.args['action']
			cid=request.args['cid']
		else:
			action=None
		if action=='update':
			q="select * from brand where brand_id='%s'"%(cid)
			res=select(q)
			data['updates']=res

		if action=='remove':
			q="delete from brand where brand_id='%s'"%(cid)
			res=delete(q)
			flash("Removed")
			return redirect(url_for("homecook.staff_manage_brand"))

		if 'submit_update' in request.form:
			catname=request.form['catname']
			desc=request.form['desc']
			q="update brand set brand_name='%s',brand_description='%s' where brand_id='%s'"%(catname,desc,cid)
			update(q)
			flash("Changes Saved")
			return redirect(url_for('homecook.staff_manage_brand'))

		if 'submit' in request.form:
			catname=request.form['catname']
			desc=request.form['desc']
			q="INSERT INTO brand(brand_name,brand_description)VALUES('%s','%s')"%(catname,desc)
			insert(q)
			flash("Saved")
			return redirect(url_for('homecook.staff_manage_brand'))

		q1="select *from brand"
		res=select(q1)
		data['cat']=res
		return render_template("staff_manage_brand.html",data=data)
	else:
		return redirect(url_for("public.login"))

@homecook.route("/staff_manage_products",methods=['get','post'])
def staff_manage_products():
	if session.get("unamess"):
		data={}
		staff_username=session.get("unamess")
		m="select staff_id from staff where username='%s'"%(staff_username)
		data['staff_id']=select(m)
		q="select * from category"
		data['cat']=select(q)		
		q="select * from products inner join staff using(staff_id) inner join category using(cat_id)"
		data['view']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='remove':
			q="delete from products where product_id='%s'"%(id)
			delete(q)
			flash("Product Removed")
			return redirect(url_for('homecook.staff_manage_products'))
		if action=='update':
			q="select * from products inner join staff using(staff_id) inner join category using(cat_id) where product_id='%s'"%(id)
			data['updated_view']=select(q)
# update_submit
		if 'update_submit' in request.form:
			product_name=request.form['pdt_name']
			cat_id=request.form['cat_id']
			qty=request.form['qty']
			details=request.form['det']
			price=request.form['price']
			img=request.files['images']		
			path="static/"+str(uuid.uuid4())+img.filename
			img.save(path)
			q="UPDATE products set cat_id='%s',`product_name`='%s',`product_details`='%s',`quantity`='%s',`price`='%s' where product_id='%s'"%(cat_id,product_name,details,qty,price,id)
			print(q)
			update(q)
			flash("Changes Saved")
			return redirect(url_for("homecook.staff_manage_products"))

		if 'submit' in request.form:
			product_name=request.form['pdt_name']
			# brand_id=request.form['brand_id']
			cat_id=request.form['cat_id']
			qty=request.form['qty']
			img=request.files['images']		
			path="static/"+str(uuid.uuid4())+img.filename
			img.save(path)
			details=request.form['det']
			price=request.form['price']
			q="INSERT INTO products (`cat_id`,`staff_id`,`product_name`,`product_details`,`quantity`,`price`,image) VALUES('%s','%s','%s','%s','%s','%s','%s')"%(cat_id,data['staff_id'][0]['staff_id'],product_name,details,qty,price,path)
			insert(q)
			flash("Products Added")
			return redirect(url_for("homecook.staff_manage_products"))
		return render_template("staff_manage_products.html",data=data)
	else:
		return redirect(url_for("public.login"))

@homecook.route("/staff_manage_subcategory",methods=['get','post'])
def staff_manage_subcategory():
	if session.get("unamess"):
		data={}
		q="select * from category"
		data['dd']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			cid=request.args['cid']
		else:
			action=None

		if action=='update':
			q="select * from subcategory inner join category using(cat_id) where subcat_id='%s'"%(cid)
			res=select(q)
			data['updates']=res

		if action=='remove':
			q="delete from subcategory where subcat_id='%s'"%(cid)
			res=delete(q)
			flash("Removed")
			return redirect(url_for("homecook.staff_manage_subcategory"))

		if 'submit_update' in request.form:
			cat_id=request.form['cat_id']
			catname=request.form['catname']
			desc=request.form['desc']
			q="update subcategory set cat_id='%s',subcat_name='%s',subcat_description='%s' where subcat_id='%s'"%(cat_id,catname,desc,cid)
			update(q)
			flash("Changes Saved")
			return redirect(url_for('homecook.staff_manage_subcategory'))

		if 'submit' in request.form:
			cat_id=request.form['cat_id']
			catname=request.form['catname']
			desc=request.form['desc']
			q="INSERT INTO subcategory(cat_id,subcat_name,subcat_description)VALUES('%s','%s','%s')"%(cat_id,catname,desc)
			insert(q)
			flash("Saved")
			return redirect(url_for('homecook.staff_manage_subcategory'))

		q1="select *from subcategory inner join category using(cat_id)"
		res=select(q1)
		data['cat']=res
		return render_template("staff_manage_subcategory.html",data=data)
	else:
		return redirect(url_for("public.login"))

@homecook.route("/staff_manage_vendors",methods=['get','post'])
def staff_manage_vendors():
	if session.get("unamess"):
		data={}
		q="select * from vendors"
		data['vend']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			vid=request.args['vid']
		else:
			action=None

		if action=='remove':
			q="delete from vendors where vendor_id='%s'"%(vid)
			res=delete(q)
			flash("Removed")
			return redirect(url_for('homecook.staff_manage_vendors'))

		if action=='update':
			q="select * from vendors where vendor_id='%s'"%(vid)
			res=select(q)
			data['updates']=res
			if res:
				if 'update_submit' in request.form:
					cmp_name=request.form['cmp']
					det=request.form['det']
					estyear=request.form['estyear']
					q="update `vendors` set `company_name`='%s',`details`='%s',`est_year`='%s' where vendor_id='%s'"%(cmp_name,det,estyear,vid)
					update(q)
					flash("Changes Saved")
					return redirect(url_for('homecook.staff_manage_vendors'))
		if 'submit' in request.form:
			cmp_name=request.form['cmp']
			det=request.form['det']
			estyear=request.form['estyear']
			q="INSERT INTO `vendors` (`company_name`,`details`,`est_year`) VALUES('%s','%s','%s')"%(cmp_name,det,estyear)
			insert(q)
			flash("Registered")
			return redirect(url_for("homecook.staff_manage_vendors"))
		return render_template("staff_manage_vendors.html",data=data)
	else:
		return redirect(url_for("public.login"))

@homecook.route("/staff_view_online_orders",methods=['get','post'])
def staff_view_online_orders():
	if session.get("unamess"):
		data={}
		q="SELECT *,CONCAT(first_name,' ',last_name)AS ename FROM order_master INNER JOIN users USING(user_id)"
		data['view']=select(q)
		return render_template("staff_view_online_orders.html",data=data)
	else:
		return redirect(url_for("public.login"))

@homecook.route("/staff_view_online_orders_details",methods=['get','post'])
def staff_view_online_orders_details():
	if session.get("unamess"):
		data={}
		omid=request.args['omid']
		q="SELECT *,CONCAT(first_name,'',last_name)AS ename from order_details inner join products using(product_id) inner join order_master using(order_master_id) INNER JOIN users USING(user_id) where order_master.order_master_id='%s'"%(omid)
		data['view']=select(q)
		if 'o_mid' in request.args:
			o_mid=request.args['o_mid']
			q="select* from payment inner join order_master using(order_master_id) inner join order_details inner join products using(product_id) where payment.order_master_id='%s' and order_details.order_details_id='%s'"%(omid,o_mid)
			data['pay']=select(q)
		return render_template("staff_view_online_orders_details.html",data=data)
	else:
		return redirect(url_for("public.login"))

@homecook.route("/staff_manage_vendors_products",methods=['get','post'])
def staff_manage_vendors_products():
	if session.get("unamess"):
		return render_template("staff_manage_vendors_products.html")
	else:
		return redirect(url_for("public.login"))

# @homecook.route("/staff_manage_vendors_products",methods=['get','post'])
# def staff_manage_vendors_products():
# 	if session.get("uname"):
# 		return render_template("staff_manage_vendors_products.html")
# 	else:
# 		return redirect(url_for("public.login"))

@homecook.route("/staff_make_purchase",methods=['get','post'])
def staff_make_purchase():
	if session.get("unamess"):
		data={}
		item_id=request.args['pid']
		q="select * from products where product_id='%s'"%(item_id)
		data['pdt']=select(q)
		q="select * from vendors"
		data['vendor']=select(q)
		q="select * from staff"
		data['staff']=select(q)
		if 'submit' in request.form:
			qty=request.form['qty']
			vendor=request.form['cmp']
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
				q="select * from purchase_master where staff_id='%s' and status='NA'" %(session['sid'])
				res=select(q)
				if res:
					id=res[0]['mpurchase_id']
				else:
					q="INSERT INTO `purchase_master` (`staff_id`,`purchase_total`,`purchase_date`,status)VALUES('%s','0',NOW(),'NA')"%(session['sid'])
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
				return redirect(url_for("homecook.staff_make_purchase",pid=item_id))
			else:
				flash("Manufacturing Date or Expiry Date is Not Valid")
		return render_template("staff_make_purchase.html",data=data)
	else:
		return redirect(url_for("public.login"))


@homecook.route("/staff_manage_category",methods=['get','post'])
def staff_manage_category():
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
			return redirect(url_for("homecook.staff_manage_category"))

		if 'submit_update' in request.form:
			catname=request.form['catname']
			desc=request.form['desc']
			q="update category set cat_name='%s',description='%s' where cat_id='%s'"%(catname,desc,cid)
			update(q)
			flash("Changes Saved")
			return redirect(url_for('homecook.staff_manage_category'))

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
				return redirect(url_for('homecook.staff_manage_category'))

		q1="select *from category"
		res=select(q1)
		data['cat']=res
		return render_template("staff_manage_category.html",data=data)
	else:
		return redirect(url_for("public.login"))