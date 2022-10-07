from color import *
import random as rd
import time

# 0. Opening
cprint("운명의 데스티니 게임 [ Start ]")

# Pseudo Code
# 1.1 보물상자 메시지와 사용자가 아무키나 누르기를 기다린다.  -> 수도코드
#   print, input
print('당신은 길을 가다가 ' + YELLOW + '[보물상자]' + END
      + '를 획득하였습니다.')
time.sleep(2)
input('Press Any Key.... to continue ')
print()

# 1.2 보물상자에서 랜덤으로 1개 무기를 획득한다.
#     각 무기는 ['무기이름', 최소공격력, 최대공격력] 을 갖는다.

weapons = [['휴지',1,3],['목검',3,5],['대검',5,10]
           ,['대포',0,50],['에픽검',51,100]]
sel = rd.randint(0,4)
print('[debug]: ', sel)
print()
myWeapon = weapons[sel]
print(myWeapon)
if sel == 0: textcolor = BLACK
elif sel in (1,2): textcolor = GREEN
elif sel == 3: textcolor = YELLOW
elif sel == 4: textcolor = RED

print('당신은 ' + f'{textcolor}' + f'{myWeapon[0]}({myWeapon[1]}-{myWeapon[2]})'
        + END + '를 획득하였습니다.')


# 2.1 길을 가다가 랜덤으로 몬스터를 만난다. (random, list)
print()
mosters = [['늑대',1,3], ['산적',5,10],['드래곤',1,100]]
sel = rd.randint(0, 2)
myMon = mosters[sel]
# print(mymon)

if sel == 0: textcolor = BLACK
elif sel == 1: textcolor = GREEN
elif sel == 2: textcolor = RED

print('당신은 길을 가다가 ' + textcolor + f'{myMon[0]}' + END +
      '을(를) 만났습니다. 큰일났습니다. 싸워야 합니다.')

# 3-1. 초기 양쪽의 에너지는 100이다.
myEnergy = 100
monEnergy = 100

# 3-2. 데미지를 계산하는 함수
def cal_damage(mina=0, maxa=5, cri=50):
    damage = rd.randint(mina, maxa)
    if rd.randint(1,100) <= cri: # 크리티컬 계산
        damage = int(damage * 1.5)
        print(RED + 'Critical Hit!!!!' + END)
    return damage

# 3-3. 에너지 상태를 출력하는 함수
def print_energy(mye, mone):
    #print(f'MyEnergy : {mye}, MonEnergy : {mone}')

    if mye <= 30: textcolor = RED
    else: textcolor = BLACK
    print('MyEnergy : ' + textcolor + f'{mye}' + END, end=' ')

    if mone <= 30: textcolor = RED
    else: textcolor = BLACK
    print('MonEnergy : ' + textcolor + f'{mone}' + END)


# 3-4. 무한 루프로 전투를 한다. 둘 중 하나의 에너지가 0 이하면 끝
while True:
    # 3-5. 사용자로부터 공격(1), 회복(2) 입력 받는다.
    # 사용자 오입력 시 용서 안함
    # user_input = input('행동을 선택하십시오 (1. 공격 2.회복) : ')

    # 사용자 오입력 대용서
    while True:
        user_input = input('행동을 선택하십시오 (1. 공격 2.회복) : ')
        if user_input in ('1','2'):
            break
        print('잘못 입력하셨습니다.')

    if user_input == '1': # 공격
        # 데미지를 계산한다.
        damage = cal_damage(myWeapon[1], myWeapon[2])
        # 몬스터 에너지를 깎는다.
        monEnergy = monEnergy - damage
        print(f'나의 공격으로 {damage}의 피해를 줬다.')
        # 에너지 상태를 출력한다.
        print_energy(myEnergy, monEnergy)
        print()
        # 몬스터 에너지가 0 이하가 되면 탈출한다.
        if monEnergy <= 0:
            break
    elif user_input == '2': # 회복
        # 힐량을 계산한다. (0-30)
        heal = rd.randint(0,30)
        # 에너지를 채운다.
        print(f'{heal}만큼 회복되었습니다.')
        myEnergy = min(myEnergy + heal, 100) # 100이 넘으면 100
        # 에너지 상태를 출력한다.
        print_energy(myEnergy, monEnergy)
        print()

    time.sleep(1)
    #몬스터 차례
    damage = cal_damage(myMon[1],myMon[2], 0)
    print(f'{myMon[0]}의 공격으로 {damage}의 피해를 입었다.')
    myEnergy = myEnergy - damage
    print_energy(myEnergy, monEnergy)
    if myEnergy <= 0:
        break
    time.sleep(1)

#4. 결과를 출력한다.
if myEnergy > 0: #승리
    print('당신은 몬스터에게 승리하였습니다.')
    print('몬스터는 자기보다 강한 자가 2512마리 더 있다고 합니다.')
else:
    print('당신은 몬스터에게 패배하였습니다.')
    print('몬스터가 당신의 명품 가방을 가져갔습니다.')


#5. Ending
cprint('[전설의 레전드 게임 END]')