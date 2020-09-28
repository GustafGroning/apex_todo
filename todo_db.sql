create database todo;
use todo;


drop table items;
CREATE TABLE items (
name VARCHAR(100),
category VARCHAR(50),
estimated_time int,
priority ENUM ("1", "2", "3", "4", "5")
);
select * from items;
delete from items where name= "plugga";

insert into items (name, category, estimated_time, priority) values ("städa köket", "hemma", 30, 5);
insert into items (name, category, estimated_time, priority) values ("köp kryddor", "hemma", 15, 1);
insert into items (name, category, estimated_time, priority) values ("Packa inför Stockholm", "hemma", 60, 3);
insert into items (name, category, estimated_time, priority) values ("laga middag", "hemma", 45, 2);
insert into items (name, category, estimated_time, priority) values ("gör uppgift", "skola", 45, 2);
insert into items (name, category, estimated_time, priority) values ("gör uppgift", "test", 45, 2);
DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `category` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `estimated_time` int(11) DEFAULT NULL,
  `priority` enum('1','2','3','4','5') COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `items` VALUES ('simonis','hemma','10','1'),
('conroygutkowski','hemma','74','3'),
('waters','hemma','67','2'),
('franecki','hemma','33','3'),
('goyettemurphy','hemma','32','3'),
('runolfsson','hemma','69','2'),
('krajcik','hemma','13','4'),
('faheymayer','hemma','79','1'),
('wehnerfranecki','hemma','17','1'),
('thompson','hemma','75','4'),
('bechtelar','hemma','109','4'),
('berge','hemma','109','1'),
('halvorson','hemma','54','2'),
('mcglynn','hemma','17','1'),
('hermann','hemma','93','2'),
('larson','hemma','60','2'),
('bechtelar','hemma','106','3'),
('trompritchie','hemma','51','5'),
('cremin','hemma','79','3'),
('jacobsdach','hemma','91','4'),
('mccluretrantow','hemma','12','2'),
('howell','hemma','63','3'),
('stroman','hemma','40','5'),
('gloverschmidt','hemma','44','2'),
('ryandavis','hemma','88','2'),
('schumm','hemma','74','1'),
('strackemuller','hemma','105','5'),
('bauch','hemma','28','4'),
('kuphalhahn','hemma','73','5'),
('kris','hemma','19','1'),
('crona','hemma','105','5'),
('koelpinkub','hemma','80','3'),
('wymanwillms','hemma','50','3'),
('simonismorar','hemma','62','5'),
('jacobi','hemma','119','3'),
('rolfson','hemma','84','2'),
('yundtkoelpin','hemma','53','1'),
('kutch','hemma','29','3'),
('schamberger','hemma','69','3'),
('prosacco','hemma','58','5'),
('price','hemma','61','4'),
('predovicwehner','hemma','11','1'),
('daniel','hemma','109','2'),
('okunevastiedemann','hemma','29','2'),
('homenick','hemma','71','5'),
('hermann','hemma','50','4'),
('considine','hemma','81','3'),
('mohr','hemma','76','2'),
('smitham','hemma','11','4'),
('dare','hemma','39','3'); 

# select * from items WHERE estimated_time <= %s (timeEst)
select * from items WHERE priority = 5 AND estimated_time <= 65;

UPDATE mysql.user SET authentication_string=PASSWORD("gurkan") WHERE User='root';
