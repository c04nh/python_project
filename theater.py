from restaurunt import Choice_Restaurunt

class Theater:
    def __init__(self):
        self.grand_theater_list = ['광림아트센터 BBCH홀', '디큐브아트센터', '블루스퀘어 신한카드홀', '세종문화회관 대극장', '예술의전당 오페라극장', '예술의전당 CJ 토월극장', '유니버설아트센터', '충무아트센터 대극장', '한전아트센터']
        self.medium_theater_list = ['국립중앙박물관 극장 용', '두산아트센터 연강홀', '두산아트센터 Space111', '명동예술극장', '세종문화회관 M씨어터', '홍익대 대학로 아트센터 대극장']
        self.small_theater_list = ['백암아트홀', '삼일로 창고극장', '성수아트홀', '세븐파이프 홀', '세종문화회관 S씨어터', '신한카드 FAN(판) 스퀘어 라이브홀', '연희예술극장', '이해랑 예술극장', '정동극장', '충무아트센터 중극장 블랙', '홍익대 대학로 아트센터 소극장', 'KT&G 상상마당 대치아트홀']

    def grand_theater(self):
        for index, theater in enumerate(self.grand_theater_list):
            print(f'{index + 1}. ' + theater)
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        theater = input('❤ 공연장을 선택하세요 👉 ')

        restaurunt = Choice_Restaurunt()

        if theater == '1':
            restaurunt.str_광림아트센터()
        elif theater == '2':
            restaurunt.str_디큐브아트센터()
        elif theater == '3':
            restaurunt.str_블루스퀘어()
        elif theater == '4':
            restaurunt.str_세종문화회관()
        elif theater == '5':
            restaurunt.str_예술의전당()
        elif theater == '6':
            restaurunt.str_예술의전당()
        elif theater == '7':
            restaurunt.str_유니버설아트센터()
        elif theater == '8':
            restaurunt.str_충무아트센터()
        elif theater == '9':
            restaurunt.str_한전아트센터()
        else:
            print('처음으로 돌아갑니다')

    def medium_theater(self):
        for index, theater in enumerate(self.medium_theater_list):
            print(f'{index + 1}. ' + theater)
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        theater = input('❤ 공연장을 선택하세요 👉 ')

        restaurunt = Choice_Restaurunt()

        if theater == '1':
            restaurunt.str_극장용()
        elif theater == '2':
            restaurunt.str_두산아트센터()
        elif theater == '3':
            restaurunt.str_두산아트센터()
        elif theater == '4':
            restaurunt.str_명동예술극장()
        elif theater == '5':
            restaurunt.str_세종문화회관()
        elif theater == '6':
            restaurunt.str_홍익대아트센터()
        else:
            print('처음으로 돌아갑니다🏃')

    def small_theater(self):
        for index, theater in enumerate(self.small_theater_list):
            print(f'{index + 1}. ' + theater)
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        theater = input('❤ 공연장을 선택하세요 👉 ')

        restaurunt = Choice_Restaurunt()

        if theater == '1':
            restaurunt.str_백암상상마당()
        elif theater == '2':
            restaurunt.str_삼일로창고극장()
        elif theater == '3':
            restaurunt.str_성수아트홀()
        elif theater == '4':
            restaurunt.str_세븐파이브홀()
        elif theater == '5':
            restaurunt.str_세종문화회관()
        elif theater == '6':
            restaurunt.str_신한카드판()
        elif theater == '7':
            restaurunt.str_연희예술극장()
        elif theater == '8':
            restaurunt.str_이해랑예술극장()
        elif theater == '9':
            pass
        elif theater == '10':
            restaurunt.str_충무아트센터()
        elif theater == '11':
            restaurunt.str_홍익대아트센터()
        elif theater == '12':
            restaurunt.str_백암상상마당()
        else:
            print('처음으로 돌아갑니다🏃')

    def daehakro(self):
        restaurunt = Choice_Restaurunt()
        restaurunt.str_대학로()

