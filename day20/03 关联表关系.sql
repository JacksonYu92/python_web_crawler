-- 书籍表
# CREATE TABLE book(
# id INT PRIMARY KEY AUTO_INCREMENT,
# title VARCHAR(32),
# price DOUBLE(5,2),
# pub_id INT NOT NULL
# )ENGINE=INNODB CHARSET=utf8;
#

# -- 出版社表
# CREATE TABLE publisher(
# id INT PRIMARY KEY AUTO_INCREMENT,
# name VARCHAR(32),
# email VARCHAR(32),
# addr VARCHAR(32)
# )ENGINE=INNODB CHARSET=utf8;

-- 插入数据
# INSERT INTO publisher(id,name,email,addr) VALUES
# (1,'清华出版社',"123","bj"),
# (2,'北大出版社',"234","bj"),
# (3,'机械工业出版社',"345","nj"),
# (4,'邮电出版社',"456","nj"),
# (5,'电子工业出版社',"567","bj"),
# (6,'人民大学出版社',"678","bj");

# INSERT INTO book(title,price,pub_id) VALUES
# ('西游记',15,1),
# ('三国演义',45,2),
# ('红楼梦',66,3),
# ('水浒传',21,2),
# ('红与黑',67,3),
# ('乱世佳人',44,6),
# ('飘',56,1),
# ('放风筝的人',78,3);

-- 子查询
-- 查询水浒传的出版社的名称和邮箱
select pub_id from book where title="水浒传";
select name,email from publisher where id=2;