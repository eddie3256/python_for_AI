from random import *
from pyinputplus import *

min:int = 1
max:int = 100
target:int = randint(min, max) #x:int  type.hint(不強制轉型)
count:int = 0

print("===========猜數字遊戲===========\n")
while True:
    count += 1
    keyin:int = inputInt(f"猜數字(範圍{min}~{max}): ", min=min, max=max)
    print(keyin)
    if keyin == target:
        print(f"答對了~答案是{keyin}")
        print(f"你共猜了 {count} 次")
        break
    elif keyin > target:
        print("再小一點~")
        max = keyin - 1
        print(f"你已經猜了 {count} 次")
    else:
        print("再大一點~")
        min = keyin + 1
        print(f"你已經猜了 {count} 次")

print("遊戲結束")