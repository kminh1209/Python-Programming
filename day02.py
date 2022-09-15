"""
    Day2 : print, input
    Version : 1.0
    Created : 2022.9. 15
    Updated : 2022. 9. 15
    Artist : Paul kang
"""

from color import *
# print(RED + '1.Print Test' + END)
cprint('1.print test')

my_name = 'Paul'
# 1. 화면에 Hello + 본인이름을 출력하시오.
print('Hello', my_name)
# 2. Mary's cosmetics
print(RED + "Mary's" + END, "cosmetics")
# 3. 신씨가 "도둑이야"라고 소리쳤다.
print('신씨가 "도둑이야"라고 소리쳤다.')
# 4. a = 'first' b = 'second' 일 때 first second를 출력
a = 'first'
b = 'second'
print(a, b)
print(a + " " + b)

print()
print('한 줄 내리지 않기')
print(a, end='')
print(b)

print()
print('변수들 사이 문자를 |로 바꾸기')
print(a, b, sep = '|')

cprint('2.input test')
a = input()
print("당신이 입력한 값은", a)
b = input('값을 입력하세요 : ')
c = a + b
print('a와 b의 합계는 ', c)
c = int(a) + int(b)
print('a와 b의 합계는 ', c) #input은 문자열로 받기 때문에 숫자로 변환해야 함


