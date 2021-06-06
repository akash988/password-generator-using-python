import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
symbol="{}[]()!@#$%^&*:;"

all=lower+upper+number+symbol
length=10
password="".join(random.sample(all,length))
print(password)

my_list=["ggx","frfe","htgg"]
print(random.choice(my_list))