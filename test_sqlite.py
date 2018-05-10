# -*- coding:utf-8 -*-
'''''
代码块的功能是利用sqlit3链接数据库，并且创建用户表。
插入数据，进行查询，然后再利用输入的数字大小的区间，
返回出符合区间之间的姓名、
'''
import os, sqlite3
#os.path.dirname(__file__)  #获取当前运行脚本所在目录
dirname=os.path.dirname(__file__)
#/home/zhubo/workspace/myproject
print(dirname)
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
print(db_file)
#/home/zhubo/workspace/myproject/test.db
if os.path.isfile(db_file):
    os.remove((db_file))



# db_file = 'test.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("create table user(id varchar(20) primary key, name varchar(20), score int)")
cursor.execute(r"insert into user values('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select name from user where score between ? and ? order by score ASC', (low, high))
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    print("55555555555")
    print(records)
    print(len(records))
    for x in records:
        print("3333333333333")
        print(x)
        print("222222")
    names = [x[0] for x in records]
    print(len(names))
    print("aaaaaaaa")
    print(names)
    return names


# debug代码：
print('接下来为调试部分\n')
print('调试开始-----------》\n')
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('调试结束-----------》\n')

res1 = get_score_in(60, 100)
res2 = get_score_in(60, 70)
res3 = get_score_in(70, 80)

print(res1)
print(res2)
print(res3)