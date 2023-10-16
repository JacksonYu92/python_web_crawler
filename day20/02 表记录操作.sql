-- 插入表记录
# insert into user (name, age, salary) values ("jackson", 23, 5000);

-- 批量插入记录
# insert into user(name, age, salary) values
#                                     ("jack", 23, 5000),
#                                     ("andy", 23, 5000),
#                                     ("tom", 23, 5000);

# CREATE TABLE emp(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(20),
#     gender ENUM("male", "female", "other"),
#     age TINYINT,
#     dep VARCHAR(20),
#     city VARCHAR(20),
#     salary DOUBLE(7,2)
# ) character set=utf8;

# INSERT INTO emp (name,gender,age,dep,city,salary) VALUES
#                 ("yuan","male",24,"教学部","河北省",8000),
#                 ("eric","male",34,"销售部","山东省",8000),
#                 ("rain","male",28,"销售部","山东省",10000),
#                 ("alvin","female",22,"教学部","北京",9000),
#                 ("George", "male",24,"教学部","河北省",6000),
#                 ("danae", "male",32,"运营部","北京",12000),
#                 ("Sera", "male",38,"运营部","河北省",7000),
#                 ("Echo", "male",19,"运营部","河北省",9000),
#                 ("Abel", "female",24,"销售部","北京",9000);

--                     表记录查询
# select * from emp;

# select name,age from emp;

# select name,age from emp where age > 30;

# select name,age from emp where age between 20 and 25;

# select name,age from emp where age = 22 or age = 24;

# select name,age from emp where age in(22,24,32);

# select name,age from emp where name like "%a%";

# select name,age from emp where name like "a%";

# select name,age from emp where name like "%a";

# select name,age from emp where name like "_a%";

# select * from emp order by age;

# select * from emp order by age desc;

# select * from emp order by age desc, salary desc;

# select * from emp where age> 22 limit 3;
# select * from emp limit 3;
# select * from emp limit 3,3;
# select * from emp limit 6,3;

--                     表记录删除

# delete from emp where name="Abel";


--                     表记录更新
select * from emp where age>30;
# update emp set salary=2000 where age>30;