import random

con = 'y'

while con == 'y':
    num_list = [i+1 for i in range(10)]
    number = random.choice(num_list)

    print('1과 10 사이의 숫자를 하나 정했습니다.\n이 숫자는 무엇일까요?')

    while 1:
        x = int(input('예상 숫자: '))
        if x not in num_list: print(f'{x}는 1과 10 사이의 숫자가 아닙니다.\n1과 10 사이의 숫자를 입력하세요.')
        elif x == number: print('정답입니다!'); break
        else: print('너무 큽니다. 다시 입력하세요.') if x > number else print('너무 작습니다. 다시 입력하세요.')

    con = input('게임을 다시 하시겠습니까? (y/n): ')

print('게임을 종료합니다. 즐거우셨나요? 또 만나요!')
