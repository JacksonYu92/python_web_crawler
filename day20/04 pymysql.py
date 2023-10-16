import pymysql

# 打开数据库连接

db = pymysql.connect(host='localhost', user='root', passwd='root', port=3307,database="spider10",cursorclass=pymysql.cursors.DictCursor,)
print('连接成功！')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from emp")

# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
data = cursor.fetchall()

print("ret:",data)

# 关闭数据库连接
db.close()