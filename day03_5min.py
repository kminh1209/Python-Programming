from color import *

cprint("Day3 5min Challenge")

#1. 사용자로부터 숫자 입력을 하나 받는다.


num = input("숫자를 하나 입력하세요 : ")
num = int(num)

if num == 0:
    print("입력하신 수는 0 입니다.")

elif num > 0:
    print(GREEN + "입력하신 숫자는 양수 입니다." + END)

else:
    print(RED + "입력하신 숫자는 음수 입니다." + END)