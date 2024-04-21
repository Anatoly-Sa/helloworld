board = list(range(1,10))

wins_cord = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def draw_board():
    print('.............')
    for i in range (3):
        print('|', board[0 + i*3], '|', board[1 + i*3],'|', board[2 + i*3],'|')
    print('.............')

def take_input(player_token):
    while True:
        value = input('Выберите место на поле для : ' +player_token + ' . ')
        if not (value in '123456789'):
            print('Поле выбрано не правильно')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Это поле уже занято! Выберите другое.')
            continue
        board[value - 1] = player_token
        break

def check_win():
    for each in wins_cord:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1]-1]
    else:
        return False
        
def main():
    counter = 0
    while True:
        draw_board()
        if counter %2 == 0:
            take_input('X')
        else:
            take_input('0')
        if counter >3:
            winner  = check_win()
            if winner:
                draw_board()
                print(winner, 'Победа !!!')
                break
        counter +=1
        if counter >8:
            draw_board()
            print('Ничья !!!')
            break
main()