from color import *

# cprint('while statement')
# print('노가다')
# print('1번 출력')
# print('2번 출력')
# print('3번 출력')
# print('4번 출력')
# print('5번 출력')
# print('6번 출력')
# print('7번 출력')
# print('8번 출력')
# print('9번 출력')
# print('10번 출력')
# print()

# i = 1
# while i < 11:
#     print('{}번 출력'.format(i))
#     i = i + 1
#
#
# print()
# print('Infinite Loop')
# while True:
#     print(i)
#     i = i + 1


# while True:
#     num = input('1에서부터 10까지의 숫자를 입력해주세요 : ')
#     if num.isdigit():
#         #num이 숫자인지 물어보는 함수
#         if 1 <= int(num) <= 10:
#             break
#         else:
#             print('숫자는 맞으시나 눈이 침침하신 듯')
#     else:
#         print('{}는 숫자 아니잖아 이걸 확'.format(num))


cprint('for statement')
print('1. 문자열')
for c in '문자열집합':
    if c == '문':
        print(RED + c + END)
    else:
        print(c)

print()
print('2.list')
for lst in ['strike','double','turkey','fourth']:
    print(lst)

print()
print('3. tuple')
s4 = ('Spring','Summer','Fall','Winter')
for season in s4:
    print(season)


print()
print('4. set')
s4 = {'Spring','Summer','Fall','Winter'}
for season in s4:
    print(season)

print()
print('5. range') # 0, 1, 2, 3, 4
for i in range(5):
    print(i)

#게릴라 문제
print()
print('게릴라 문제')
for i in range(1,100,2):
    print(i,end=',')
print()

print('6.dict')
music = {'artist':'Chopin', 'title':'Nocturn'}
for item in music:
    print(item)
    print(music[item])
    print(music.get(item))
    #print(item + ':' + music.get(item))

print()
for key in music.keys():
    print('key값 :', key)

print()
for value in music.values():
    print('value :', value)

print()
for key, value in music.items():
    print('key :', key, ' value :', value)

for item in music.items():
    print(item)


print()
print('[]와 .get의 차이')
print(music['artist']) # Chopin
#print(music['musician']) # 없음 오류를 발생시킴
print(music.get('musician'))
print(music.get('musician','대체 글자')) # 값이 없으면 대체
