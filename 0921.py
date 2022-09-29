# 목표: 사용자를 통해 글자를 입력 받고 그 글자를 원하는 색으로 출력할 수 있게끔 함

from color import *

# 사용자로부터 글자를 입력 받는다.
word = input("글자를 눌러 주세요 : ")
# 입력한 글자를 확인 받는다.
confirm = input("입력하신 글자가 {}가 맞나요? ".format(word))

# 사용자가 입력한 글자를 확인하고 원하는 색으로 색칠해준다.
if confirm == "yes":
    print("Okay, 원하는 색을 골라 주시면 그 색으로 글을 색칠해 드리겠습니다.")
    w_color = input("OPTION: GREEN, RED (default = 무색) ")

    #원하는 색으로 색칠
    if w_color == "GREEN":
        print(GREEN + word + END)
    elif w_color == "RED":
        print(RED + word + END)
    else:
        print(word)

else:
    print("프로그램을 처음부터 실행합니다.")






