import pymysql

class Spider(object):

    def __init__(self):
        # 打开数据库连接

        db = pymysql.connect(host='localhost', user='root', passwd='root', port=3307, database="spider10",
                             cursorclass=pymysql.cursors.DictCursor, )
        print('连接成功！')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = db.cursor()

    def foo(self):
        self.cursor.execute("")

    def bar(self):
        self.cursor.execute("")

    def run(self):
        pass

s = Spider()
s.run()