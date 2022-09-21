from color import *

cprint('3. Operator')
print('(1)산술연산자')
a = 'My name'
b = 'is None'
print(a + ' ' + b)
c = 'I\'ll be '
d = 100
# print(c + d) # 문자열과 숫자의 뎃셈은 불가
print(c + str(d))
print("안녕"*30)
print(10 // 3)
print('10 % 3 ="20"', 10 % 3)

print()
print('(2) 관계 연산자')
print("10 > 10 :", 10 > 10)
print("10>= 10", 10 >= 10)
print("10 < 20", 10 < 20)

a = 30
b = 20
c = a > b
print(c, type(c)) # bool, boolean -> bool 자료형 : True, False 값을 갖는 자료형

print()
print("(3) 논리연산자")
print("10 > 2 and 10 < 20 :", 10 < 2 and 10 < 20)
print("10 != 0 or 10 > 100000 :", 10 != 0 or 10 < 100000)
print("not 10 > 3 :", not 10 > 3)

print()
print("(4) 삼항 연산자")
score = 90
dad1 = (score > 89) and "GOOD" or "어떻게 그런 점수가"
print(dad1)
# 삼항연산자도 중첩이 가능하다.
dad2 = (score > 90) and "A" or ((score > 70) and "B" or "C")
print(dad2)

print()
cprint("str.format")
print("{}은 {}기능 같지만 사실 {}의 기능입니다.".format('format','print','string'))
print("숫자도 되는지 해볼까요? {}".format(1000))
print("괄호보다 더 입력이 많을 때는 {}".format("되네","이것도 되나"))

print(f"Dad1이 말했습니다. \"{dad1}\"")

print()
cprint('if statement')

a = 1
if a > 0:
    print("a는 양수")
#     print("a는 양수2")       # 오류 : 파이썬은 들여쓰기(indendt)가 매우 중요
    print("a는 양수3")
print("a는 양수4")

if a > 0: print('a는 양수5'); print('a는 양수6')
e = -30
if e > 0:
    print('e is positive')
elif e == 0:
    print('e is zero')
else:
    print('e is negative')
