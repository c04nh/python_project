from theater import Theater

def print_menu():
    print('1. 대극장')
    print('2. 중극장')
    print('3. 소극장')
    print('4. 대학로')
    print('5. 종료')
    menu = input('❤ 공연장 규모를 선택하세요 👉 ')
    return menu


def main():
    theater = Theater()
    while True:
        menu = print_menu()
        if menu == '1':
            # 대극장
            theater.grand_theater()
        elif menu == '2':
            # 중극장
            theater.medium_theater()
        elif menu == '3':
            # 소극장
            theater.small_theater()
        elif menu == '4':
            # 대학로
            theater.daehakro()
        elif menu == '5':
            break
        else:
            print('다시 입력하세요.')


if __name__ == '__main__':
    main()