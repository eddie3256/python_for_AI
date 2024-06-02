import pyinputplus as pyip
from health import BMI

def main():
    name = pyip.inputStr("請輸入您的姓名: ")
    #print(name) #使用python終端機執行時會自動打上去
    height = pyip.inputInt("請輸入您的身高(cm): ", min=50, max=250)
    #rint(height)
    weight = pyip.inputInt("請輸入您的體重(kg): ", min=0, max=200)
    #print(weight)

    data = BMI(name, height, weight)
    
    print(f"{data.name}, 您的BMI值為 {data.bmi()}")
    print(f"您的體重為 {data.status()}")


if __name__ == "__main__":
    main()