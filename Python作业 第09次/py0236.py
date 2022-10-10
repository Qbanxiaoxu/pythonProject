#3、	随机密码生成。编写程序，在26个字母大小写和10个数字随机生成10个8位密码。
import random
passwordSource="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password=[]
for i in range(0,10):
    password.append("".join(random.sample(passwordSource,8)))
print(password)