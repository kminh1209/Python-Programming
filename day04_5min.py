"""
    1. '이름을 입력하세요 : '를 출력하고 입력을 받는다.
    2. '최대 숫자를 입력하세요 : '를 출력하고 입력을 받는다.
    3. 1부터 입력한 최대 숫자 사이의 임의의 수를 만든다.
    4. 숫자 입력을 받아 임의의 수와 같은지 맞추는 게임을 한다.
       정답은 몇일까요? 를 출력하고 입력을 받는다.
       임의의 수와 입력한 수가 일치하면 종료
       5번까지 못맞추면 종료
    5. 한 번에 정답을 맞추면 '***님 대단하십니다'
       세 번 이내에 정답을 맞추면 '***님 우수한 성적이십니다'
       다섯 번 이내에 정답을 맞추면 '***님 좀 심하십니다'
       다섯 번까지도 못 맞추면 '정답은 *입니다. 님 사람 맞음?'
"""
from color import *
import random

# 0. Opening
#여러분들이 하심

# 1
name = input('이름을 입력하세요 : ')
print(f'{name}님이 로그인하셨습니다.')

while True:
    if input('게임을 시작하시겠습니까(Y/N) : ') in ['Y','y']:
        break


#2.
while True:
    num = input('최대 숫자를 입력하세요 : ')
    if num.isdigit():
        break
    print('잘못 입력하셨습니다.')


# 랜덤으로 1과 입력받은 최대숫자 사이의 숫자를 가져온다.
answer = random.randrange(1,int(num))
print(answer)

count = 1
while True:
    guess = input("정답은 몇번일까요? : ")
    if guess.isdigit():
        if answer == int(guess):
            print("정답!")
            break
        else:
            print('오답!')
            count = count + 1
            if count == 6:
                break
    else:
        print('숫자를 입력하세요!!')

if count == 1:
    print("{}님 대단하십니다.".format(name))

elif count <= 3:
    print("{}님 우수한 성적이십니다.".format(name))

elif count <= 5:
    print("{}님 좀 심하십니다.".format(name))

else:
    print('정답은 {}입니다. 님 사람 맞음?'.format(answer))







