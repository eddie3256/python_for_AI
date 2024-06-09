from pprint import pprint
import csv
from pyinputplus import *
from random import *

with open("個股日成交資訊.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    sells:list[dict] = list(reader)

num = inputInt("請輸入要隨機顯示的資料數(1~20): ", min=1, max=20)
sells2 = choices(sells, k=num)

pprint(sells2) 