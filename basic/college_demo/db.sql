# 删除数据库
-- drop database college;

# 创建数据库
create database college_bak default character set utf8;

use college_bak;

# 创建院校表
create table college(
	id int unsigned auto_increment comment '序号',
	area varchar(20) not null default '' comment '地区',
	college_id char(5) not null default '00000' comment '学校代码',
	college_name varchar(20) not null default '' comment '学校名称',
	college_site varchar(128) not null default '' comment '学校网站',
	unique (college_id),
	primary key(id)# 此处不要写',',否则会报错
) engine=InnoDB default charset=utf8 comment '院校表';

# 创建专业科目表
create table major(
	id int unsigned auto_increment comment '序号',
	college_id char(5) not null default '00000' comment '学校代码',
	gradation varchar(10) not null default '' comment '层次',
	classification varchar(128) not null default '' comment '专业名称',
	subject varchar(50) not null default '' comment '科目要求',
	major varchar(128) not null default '' comment '所含专业',
	primary key(id),
	constraint foreign key(college_id) references college(college_id)
) engine=InnoDB default charset=utf8 comment '专业科目表';

