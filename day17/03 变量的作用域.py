age = 35 # 全局

def update_age():
    global age
    age = 18
    print("age:", age)

update_age()
print(age)