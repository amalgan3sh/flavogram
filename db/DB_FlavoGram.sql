/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.28-MariaDB : Database - db_flavogram
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_flavogram` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `db_flavogram`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(30) DEFAULT NULL,
  `description` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `category` */

insert  into `category`(`cat_id`,`cat_name`,`description`) values (6,'chocolate cake','original item'),(5,'Vancho cake','vanila item'),(4,'aa','aa'),(7,'abc','kjdkk'),(8,'cake','chocolate'),(9,'hi','alby sebastian'),(10,'Milk Desserts','desserts'),(11,'al','aa'),(12,'aaa','aaa');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`complaint`,`reply`,`date_time`) values (1,1,'fghjk','Alby Treata','2023-07-28 11:55:20'),(2,1,'fghj1','ok','2023-04-03 00:44:14'),(3,2,'fghjkl','Okay','2023-04-04 21:01:06'),(4,2,'dfghjkl','pending','2023-04-04 21:09:02'),(5,6,'bad','pending','2023-04-08 10:09:38'),(6,2,'I got expired item','pending','2023-09-16 00:02:42'),(7,8,'Thank you','Anytime!!!','2023-09-16 13:14:52'),(8,7,'Nice products. We except to improve more...','pending','2023-09-16 14:20:46'),(9,9,'Nice product... But we except more facilities...','We value your feedback. Thank you !!!','2023-09-16 21:17:30'),(10,10,'Tasty. ','pending','2023-09-17 16:19:04');

/*Table structure for table `favorites` */

DROP TABLE IF EXISTS `favorites`;

CREATE TABLE `favorites` (
  `fav_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`fav_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `favorites` */

insert  into `favorites`(`fav_id`,`product_id`,`user_id`) values (1,2,0),(4,1,0),(3,1,0),(5,2,0),(6,4,0),(7,5,0),(8,5,0),(9,4,0),(10,4,0);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`) values ('admin','admin','admin'),('anu@gmail.com','anu','user'),('riya@gmail.com','riya123','user'),('fathima@gmail.com','fathima123','user'),('clara@gmail.com','clara123','staff'),('tiya@gmail.com','tiya123','user'),('jiya@gmail.com','jiya123','user'),('kiran@gmail.com','kiran123','staff'),('ann@mm.com','ann','staff'),('nn@gg.n','ann','staff'),('christy@gmail.com','christy','user'),('shajan@gmail.com','shajan','user');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` decimal(10,0) DEFAULT NULL,
  `amount` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`order_details_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `order_details` */

insert  into `order_details`(`order_details_id`,`order_master_id`,`product_id`,`quantity`,`amount`) values (1,1,14,1,60),(2,2,19,2,20),(3,3,20,1,210),(4,4,14,5,1000),(5,5,19,2,1800),(6,5,20,1,200),(7,5,14,1,500),(8,6,14,1,500),(9,7,19,2,1800),(10,7,19,2,1000),(11,8,20,2,20),(13,10,20,2,36),(16,11,18,2,12),(15,12,17,2,12),(17,13,17,2,12),(18,14,19,1,780),(21,15,17,2,12),(20,15,18,2,12),(22,16,18,1,6),(23,14,22,2,44),(24,14,18,1,680),(25,14,14,1,34);

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date_time` varchar(30) DEFAULT NULL,
  `total` decimal(10,0) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`user_id`,`date_time`,`total`,`status`) values (1,2,'2023-04-04 15:16:49',60,'paid'),(2,2,'2023-04-04 15:16:49',20,'paid'),(3,3,'2023-04-07 07:17:40',210,'paid'),(4,4,'2023-04-07 09:21:27',1000,'paid'),(5,4,'2023-04-07 21:07:25',2500,'paid'),(6,4,'2023-04-08 08:39:46',500,'pending'),(7,6,'2023-04-08 10:07:33',2800,'paid'),(8,2,'2023-04-11 21:37:16',20,'paid'),(9,2,'2023-04-11 23:03:07',0,'pending'),(10,7,'2023-09-16 12:07:58',36,'paid'),(11,7,'2023-09-16 12:11:36',12,'pending'),(12,8,'2023-09-16 13:10:05',12,'paid'),(13,9,'2023-09-16 21:05:00',12,'paid'),(14,9,'2023-09-16 21:07:37',1538,'pending'),(15,10,'2023-09-17 16:15:51',24,'paid'),(16,10,'2023-09-17 16:18:36',6,'pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `amount` decimal(30,0) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`order_master_id`,`amount`,`date`) values (2,0,70,'1234567'),(3,0,1,'20210404'),(4,0,0,'2023-04-04'),(5,1,60,'2023-04-04'),(6,2,20,'2023-04-04'),(7,3,210,'2023-04-07'),(8,4,1000,'2023-04-07'),(9,5,2500,'2023-04-08'),(10,7,2800,'2023-04-08'),(11,8,20,'2023-04-11'),(12,8,20,'2023-04-11'),(13,10,36,'2023-09-16'),(14,12,12,'2023-09-16'),(15,13,12,'2023-09-16'),(16,15,24,'2023-09-17');

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) DEFAULT NULL,
  `product_name` varchar(30) DEFAULT NULL,
  `product_details` varchar(60) DEFAULT NULL,
  `quantity` decimal(10,0) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `products` */

insert  into `products`(`product_id`,`cat_id`,`product_name`,`product_details`,`quantity`,`price`,`image`,`staff_id`) values (14,8,'Chocolate Berry','asdfghjkl 2',3,34,'static/612295b9-4e4c-4d11-829e-db5f76cc9cfcavatar@2x.png',4),(15,6,'cake','flavoured not orginal 2KG',0,44,'static/e03c973d-4415-4ef1-9d83-dc7aade1a701christmascakeicing_2360_16x9.jpg',NULL),(16,7,'Red velvet','strawberry 1KG',0,240,'static/887e8e1f-0365-4536-be3b-a6e23b33fedbveg1.jpg',NULL),(17,6,'Black Magic','dfghj dfg fghj',0,6,'static/bc9b810f-fd20-4393-9d66-e5a88c87ba81wallpaper2.jpg',7),(18,6,'Black Magic','dfghj dfg fghj',199,680,'static/cc9d47ac-b939-40b5-865f-371c877f2b82wallpaper1.jpeg',7),(19,6,'Black Magic','1KG flavoured wide cake',11,780,NULL,6),(22,6,'cake','ww',86,22,'static/d53478bd-36a7-4c48-8ef5-48145d366d30R.gif',6);

/*Table structure for table `purchase_child` */

DROP TABLE IF EXISTS `purchase_child`;

CREATE TABLE `purchase_child` (
  `cpurchase_id` int(11) NOT NULL AUTO_INCREMENT,
  `mpurchase_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `pur_qty` decimal(10,0) DEFAULT NULL,
  `sub_tot` decimal(10,0) DEFAULT NULL,
  `stockinhand` decimal(10,0) DEFAULT NULL,
  `exp_date` varchar(30) DEFAULT NULL,
  `batch_no` varchar(20) DEFAULT NULL,
  `mfd_date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cpurchase_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `purchase_child` */

insert  into `purchase_child`(`cpurchase_id`,`mpurchase_id`,`item_id`,`pur_qty`,`sub_tot`,`stockinhand`,`exp_date`,`batch_no`,`mfd_date`) values (1,1,2,105,105,72,'2023-04-01','1','2023-03-31'),(2,1,5,20,200,34,'2023-04-08','2','2023-04-20'),(3,1,6,20,900,18,'2024-10-29','3','2021-04-04'),(4,1,6,20,200,38,'2024-04-05','2','2021-04-27'),(5,1,10,20,200,20,'2021-04-07','2','2021-04-16'),(6,1,11,50,100,46,'2021-04-06','2','2021-04-09'),(7,1,6,10,200,48,'2021-04-06','2','2021-04-29'),(8,1,12,20,200,20,'2028-06-28','3','2021-04-05'),(9,1,5,20,200,54,'2021-04-05','5','2021-04-22'),(12,1,13,23456789,12345,23456789,'2020-05-08','34','2019-12-12'),(11,1,14,1,1,0,'2021-05-07','1','2021-03-29');

/*Table structure for table `purchase_master` */

DROP TABLE IF EXISTS `purchase_master`;

CREATE TABLE `purchase_master` (
  `mpurchase_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `purchase_total` decimal(10,0) DEFAULT NULL,
  `purchase_date` varchar(30) DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`mpurchase_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `purchase_master` */

insert  into `purchase_master`(`mpurchase_id`,`staff_id`,`purchase_total`,`purchase_date`,`status`) values (1,1,14651,'2023-04-03 20:28:53','NA');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` varchar(30) DEFAULT NULL,
  `description` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `review` */

insert  into `review`(`review_id`,`product_id`,`description`) values (4,'Food','Gastro Medicine'),(2,'Food','AnimalHHH'),(3,'Session','Beauty Medicine'),(5,'Loreal','Great'),(6,'maybelline','good'),(7,'savlon','ghg');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_name` varchar(30) DEFAULT NULL,
  `details` varchar(150) DEFAULT NULL,
  `location` varchar(60) DEFAULT NULL,
  `staff_pin` varchar(15) DEFAULT NULL,
  `staff_num` varchar(12) DEFAULT NULL,
  `staff_city` varchar(10) DEFAULT NULL,
  `staff_status` varchar(15) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`staff_name`,`details`,`location`,`staff_pin`,`staff_num`,`staff_city`,`staff_status`,`username`) values (4,'q','Food items','1111','687999','9898767654','Kochi',NULL,'clara@gmail.com'),(5,'Kara','tawrtyu sdgh','1993','688111','9807054667','hhhh',NULL,'kiran@gmail.com'),(6,'Home cook','qq',NULL,'688534','1029384756','ert','active','ann@mm.com'),(7,'Home cook 2','sdfgh asdfgh sdfgh',NULL,'688523','1234567899','hhh','active','nn@gg.n');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `users` */

insert  into `users`(`user_id`,`username`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`phone`,`email`) values (1,'ammu','Ammu','Kutty','House Name','kkd','688523','9876543210','fgfg@g.com'),(2,'anu','ammu','anu','thoppilparambil house','chalakudy','680712','3467882908','lab@lab.lab'),(3,'riya@gmail.com','Riya','Rebecca','Eden','Ernakulam','683123','7898789878','riya@gmail.com'),(4,'fathima@gmail.com','Fathima','Noureen','Manadath','Aluva','683101','7896789876','fathima@gmail.com'),(5,'tiya@gmail.com','Tiya','Teddy','Tharam','Ernakulam','683123','6789876545','tiya@gmail.com'),(6,'jiya@gmail.com','jiya','jenny','jar','Ernakulam','683101','6789675677','jiya@gmail.com'),(7,'alby@gmail.com','Alby','Sebastian','Visudhiyil','Vanaswargam','688523','9109109100','alby@gmail.com'),(8,'titta@gmail.com','Ann Titta',' T M','Thottekattu','Aroor','688534','1234567890','titta@gmail.com'),(9,'christy@gmail.com','Christy','Mol','H name','Ernakulam','688111','1230567890','christy@gmail.com'),(10,'shajan@gmail.com','Shajan','V','Visudhiyil','Vanaswargam','688523','0987543211','shajan@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
