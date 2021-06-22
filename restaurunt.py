class Restaurunt:
    def __init__(self, name):
        # 식당 이름
        self.name = name
        # 메뉴
        self.menu = {}
        # 주소
        self.location = ''
        # 후기
        self.review = ''
        # 별점
        self.star = ''


class Choice_Restaurunt:
    def __init__(self):
        self.대학로_list = []
        self.광림아트센터_list = []
        self.디큐브아트센터_list = []
        self.블루스퀘어_list = []
        self.세종문화회관_list = []
        self.예술의전당_list = []
        self.유니버설아트센터_list = []
        self.충무아트센터_list = []
        self.한전아트센터_list = []
        self.극장용_list = []
        self.두산아트센터_list = []
        self.명동예술극장_list = []
        self.홍익대아트센터_list = []
        self.백암상상마당_list = []
        self.삼일로창고극장_list = []
        self.성수아트홀_list = []
        self.세븐파이브홀_list = []
        self.신한카드판_list = []
        self.연희예술극장_list = []
        self.이해랑예술극장_list = []
        self.정동극장_list = []
        self.대학로()
        self.광림아트센터()
        self.디큐브아트센터()
        self.블루스퀘어()
        self.세종문화회관()
        self.예술의전당()
        self.유니버설아트센터()
        self.충무아트센터()
        self.한전아트센터()
        self.극장용()
        self.두산아트센터()
        self.명동예술극장()
        self.홍익대아트센터()
        self.백암상상마당()
        self.삼일로창고극장()
        self.성수아트홀()
        self.세븐파이브홀()
        self.신한카드판()
        self.연희예술극장()
        self.이해랑예술극장()
        self.정동극장()


    def 대학로(self):
        # 한식
        혜화칼국수 = Restaurunt('혜화칼국수')
        혜화칼국수.menu = {'국시': '9000원', '녹두빈대떡': '12000원', '문어 (소)': '16000원'}
        혜화칼국수.location = '서울 종로구 창경궁로35길 13'
        self.대학로_list.append(혜화칼국수)

        순대실록 = Restaurunt('순대실록')
        순대실록.menu = {'전통 순댓국(보통)': '8000원', '살코기 순댓국': '9000원', '시래기 순댓국': '9000원'}
        순대실록.location = '서울 종로구 동숭길 127 우성빌딩'
        self.대학로_list.append(순대실록)

        대포찜닭 = Restaurunt('대포찜닭 대학로점')
        대포찜닭.menu = {'대포찜닭(2인)': '22000원', '대포찜닭(3인)': '33000원', '대포찜닭(4인)': '44000원'}
        대포찜닭.location = '서울 종로구 대학로9길 18 1층'
        self.대학로_list.append(대포찜닭)

        # 중식
        만리성 = Restaurunt('만리성')
        만리성.menu = {'만 코스': '20000원', '리 코스': '25000원', '성 코스': '40000원'}
        만리성.location = '서울 종로구 대학로12길 61 계우빌딩'
        self.대학로_list.append(만리성)

        탕화쿵푸마라탕 = Restaurunt('탕화쿵푸마라탕 대학로점')
        탕화쿵푸마라탕.menu = {'마라탕100g': '1500원', '마라향궈100g': '3000원', '꿔보로우': '15000원'}
        탕화쿵푸마라탕.location = '서울 종로구 창경궁로 258-15 2층'
        self.대학로_list.append(탕화쿵푸마라탕)

        진아춘 = Restaurunt('진아춘')
        진아춘.menu = {'짜장면': '6500원', '삼선짜장': '9000원','짬뽕': '7500원'}
        진아춘.location = '서울 종로구 대명1길 18'
        self.대학로_list.append(진아춘)

        #일식
        정돈 = Restaurunt('정돈 대학로본점')
        정돈.menu = {'등심 돈카츠(220g)': '13000원', '안심 돈가츠(220g)': '14000원', '등심+안심 돈카츠': '18000원'}
        정돈.location = '서울 종로구 대학로9길 12'
        self.대학로_list.append(정돈)

        호호식당 = Restaurunt('호호식당 대학로점')
        호호식당.menu = {'사케동': '14000원', '가츠나베정식': '14000원', '돈가츠정식': '13000원'}
        호호식당.location = '서울 종로구 대학로9길 35'
        self.대학로_list.append(호호식당)

        겐로쿠우동 = Restaurunt('겐로쿠우동 대학로점')
        겐로쿠우동.menu = {'지도리우동': '8000원', '니꾸우동': '8000원', '키즈네우동': '7000원'}
        겐로쿠우동.location = '서울 종로구 대학로 129-9'
        self.대학로_list.append(겐로쿠우동)

        #양식
        더키친 = Restaurunt('더 키친 750')
        더키친.menu = {'크림 포테이토 피자': '15900원', '크림 쉬림프 피자': '16900원', '리코타 피자': '16900원'}
        더키친.location = '서울 종로구 대학로8가길 80'
        self.대학로_list.append(더키친)

        버거파크 = Restaurunt('버거파크')
        버거파크.menu = {'베이컨치즈버거': '6900원', '아보카도치즈버거': '7900원', '치즈버거': '5900원'}
        버거파크.location = '서울 종로구 대학로11길 5 1층 버거파크'
        self.대학로_list.append(버거파크)

        핏제리아오 = Restaurunt('핏제리아오')
        핏제리아오.menu = {'마르게리따': '12000원', '오핏자': '19500원', '스텔라': '29000원'}
        핏제리아오.location = '서울 종로구 동숭길 48'
        self.대학로_list.append(핏제리아오)

        # 기타
        이스탄불 = Restaurunt('이스탄불')
        이스탄불.menu = {'케밥샌드위치(버거)': '5800원', '피데(터키 피자)(치킨)': '13000원', '타스 케밥(더키식 덮밥)(소고기)': '8000원'}
        이스탄불.location = '서울 종로구 대학로11길 20 우리빌딩 1층'
        self.대학로_list.append(이스탄불)

        뎁짜이 = Restaurunt('뎁짜이')
        뎁짜이.menu = {'하노이 쌀국수': '9000원', '반미 샌드위치': '7000원', '하노이 고급쌀국수': '12000원'}
        뎁짜이.location = '서울 종로구 대학로11길 41-4'
        self.대학로_list.append(뎁짜이)

        깔리 = Restaurunt('깔리')
        깔리.menu = {'탄두리 치킨': '17000원', '양고기 반딜루': '12000원', '야채/달 타드카': '9000원'}
        깔리.location = '서울 종로구 대학로11길 43 명륜4가 171번지 2층'
        self.대학로_list.append(깔리)

       # 디저트
        일월일일 = Restaurunt('일월일일')
        일월일일.menu = {'단호박라떼': '6500원', '아이스모찌케이크': '5000원', '아메리카노': '5000원'}
        일월일일.location = '서울 종로구 창경궁로 231 2층 일월일일'
        self.대학로_list.append(일월일일)

        알티프로젝트 = Restaurunt('알티프로젝트')
        알티프로젝트.menu = {'아메리카노': '3500원', '카페라떼': '4000원', '오곡라떼': '5000원'}
        알티프로젝트.location = '서울 종로구 동숭3길 26-1'
        self.대학로_list.append(알티프로젝트)

        카페다오 = Restaurunt('카페다오')
        카페다오.menu = {'티라미수': '8000원', '흑임자크림라떼': '6500원', '갸또쇼콜라': '7000원'}
        카페다오.location = '서울 종로구 대학로14길 19'
        self.대학로_list.append(카페다오)


    def str_대학로(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
                print(f'이름: {self.대학로_list[i].name}\n위치: {self.대학로_list[i].location}\n메뉴: {self.대학로_list[i].menu}\n별점: {self.대학로_list[i].star}\n후기: {self.대학로_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_대학로()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
                print(f'이름: {self.대학로_list[i].name}\n위치: {self.대학로_list[i].location}\n메뉴: {self.대학로_list[i].menu}\n별점: {self.대학로_list[i].star}\n후기: {self.대학로_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_대학로()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
                print(f'이름: {self.대학로_list[i].name}\n위치: {self.대학로_list[i].location}\n메뉴: {self.대학로_list[i].menu}\n별점: {self.대학로_list[i].star}\n후기: {self.대학로_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_대학로()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
                print(f'이름: {self.대학로_list[i].name}\n위치: {self.대학로_list[i].location}\n메뉴: {self.대학로_list[i].menu}\n별점: {self.대학로_list[i].star}\n후기: {self.대학로_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_대학로()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
                print(f'이름: {self.대학로_list[i].name}\n위치: {self.대학로_list[i].location}\n메뉴: {self.대학로_list[i].menu}\n별점: {self.대학로_list[i].star}\n후기: {self.대학로_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_대학로()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
                print(f'이름: {self.대학로_list[i].name}\n위치: {self.대학로_list[i].location}\n메뉴: {self.대학로_list[i].menu}\n별점: {self.대학로_list[i].star}\n후기: {self.대학로_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_대학로()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_대학로(self):
        for i in range(18):
            print(f'{i + 1}. {self.대학로_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.대학로_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.대학로_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.대학로_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.대학로_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.대학로_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.대학로_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.대학로_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.대학로_list[int(restaurunt_num) - 1].name}\n위치: {self.대학로_list[int(restaurunt_num) - 1].location}\n메뉴: {self.대학로_list[int(restaurunt_num) - 1].menu}\n별점: {self.대학로_list[int(restaurunt_num) - 1].star}\n후기: {self.대학로_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.대학로_list[int(restaurunt_num) - 1].name}\n위치: {self.대학로_list[int(restaurunt_num) - 1].location}\n메뉴: {self.대학로_list[int(restaurunt_num) - 1].menu}\n별점: {self.대학로_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_대학로()


    def 광림아트센터(self):
        # 한식
        청담미역 = Restaurunt('청담미역 압구정점')
        청담미역.menu = {'가자미미역국': '11000원', '전복가자미미역국': '16000원', '조개미역국': '11000원'}
        청담미역.location = '서울 강남구 압구정로20길 15'
        self.광림아트센터_list.append(청담미역)

        담미온 = Restaurunt('담미온 압구정점')
        담미온.menu = {'수육국밥(보통)': '8000원', '순대국밥(보통)': '8000원', '얼큰국밥(보통)': '9000원'}
        담미온.location = '서울 강남구 압구정로28길 42'
        self.광림아트센터_list.append(담미온)

        시골밥상 = Restaurunt('시골밥상')
        시골밥상.menu = {'갈치조림정식': '9000원', '시골밥상': '8000원', '불고기': '12000원'}
        시골밥상.location = '서울 강남구 논현로175길 68'
        self.광림아트센터_list.append(시골밥상)

        # 중식
        대가방 = Restaurunt('대가방 압구정동점')
        대가방.menu = {'탕수육': '27000원', '라조기': '40000원', '게살볶음밥': '9500원'}
        대가방.location = '서울 강남구 논현로175길 64'
        self.광림아트센터_list.append(대가방)

        종쓰부 = Restaurunt('종쓰부')
        종쓰부.menu = {'유니짜장': '6000원', '꿔바로우': '20000원', '해물누룽지밥': '8000원'}
        종쓰부.location = '서울 강남구 논현로161길 12 1F'
        self.광림아트센터_list.append(종쓰부)

        명궁 = Restaurunt('명궁')
        명궁.menu = {'짜장면': '7000원', '짬뽕': '8000원','간짜장': '8000원'}
        명궁.location = '서울 강남구 논현로157길 10'
        self.광림아트센터_list.append(명궁)

        #일식
        온기정 = Restaurunt('온기정')
        온기정.menu = {'텐동': '11000원', '붓카케우동': '11000원', '카이센동': '13000원'}
        온기정.location = '서울 강남구 압구정로4길 13-9 1층 온기정'
        self.광림아트센터_list.append(온기정)

        기꾸 = Restaurunt('기꾸1984')
        기꾸.menu = {'런치스시': '25000원', '런치스페셜스시': '55000원', '디너스시': '60000원'}
        기꾸.location = '서울 강남구 압구정로20길 19'
        self.광림아트센터_list.append(기꾸)

        토모 = Restaurunt('토모')
        토모.menu = {'모듬꼬치구이 5종': '18500원', '닭안심튀김과 케이준샐러드': '24000원', '토모 안심 까츠': '26500원'}
        토모.location = '서울 강남구 압구정로28길 25 엑시'
        self.광림아트센터_list.append(토모)

        #양식
        스파게티스토리 = Restaurunt('스파게티스토리')
        스파게티스토리.menu = {'미트소스 스파게티': '4500원', '토마토소스 스파게티': '4500원', '크림 양송이 스파게티': '5800원'}
        스파게티스토리.location = '서울 강남구 압구정로18길 12'
        self.광림아트센터_list.append(스파게티스토리)

        키친랩 = Restaurunt('키친랩 가로수길점')
        키친랩.menu = {'(홈메이드)리코타+피자샐러드': '18900원', '부채살 팬 스테이크': '23900원', '키조개 관자 크림 리조또': '15900원'}
        키친랩.location = '서울 강남구 압구정로10길 30-1 키친랩 지하 1층~지상 3층'
        self.광림아트센터_list.append(키친랩)

        엘이베리코 = Restaurunt('엘이베리코 압구정점')
        엘이베리코.menu = {'이베리코 목살 (150g)': '15000원', '이베리코 시크릿 (150g)': '18000원', '이베리코 늑간살 (150g)': '15000원'}
        엘이베리코.location = '서울 강남구 압구정로28길 22-7'
        self.광림아트센터_list.append(엘이베리코)

        # 기타
        낭만국수 = Restaurunt('낭만국수')
        낭만국수.menu = {'낭만이면': '8000원', '낭만탕면': '9000원', '낭만쌀면': '9000원'}
        낭만국수.location = '서울 강남구 논현로175길 40'
        self.광림아트센터_list.append(낭만국수)

        꿍탈레 = Restaurunt('꿍탈레')
        꿍탈레.menu = {'똠양쌀국수': '12000원', '팟타이': '13000원', '팟끄라파오무쌉': '14000원'}
        꿍탈레.location = '서울 강남구 압구정로10길 14 2층'
        self.광림아트센터_list.append(꿍탈레)

        감성타코 = Restaurunt('감성타코 신사점')
        감성타코.menu = {'까르니따스 치즈 타코': '9000원', '감성 그릴드 파히타': '38000원', '파인애플 베르데 살사 타코': '9000원'}
        감성타코.location = '서울 강남구 강남대로162길 31'
        self.광림아트센터_list.append(감성타코)

       # 디저트
        자미당 = Restaurunt('자미당 압구정점')
        자미당.menu = {'꽈배기(3개)': '2000원', '찹쌀도넛츠(3개)': '2000원', '핫도그': '1500원'}
        자미당.location = '서울 강남구 논현로 851 1층 자미당'
        self.광림아트센터_list.append(자미당)

        퍼플어니언 = Restaurunt('퍼플어니언 본점')
        퍼플어니언.menu = {'에스프레소': '2500원', '싱글샷 아메리카노': '2500원', '더블샷 아메리카노': '2800원'}
        퍼플어니언.location = '서울 강남구 압구정로28길 49 유림아트홀'
        self.광림아트센터_list.append(퍼플어니언)

        소나 = Restaurunt('소나')
        소나.menu = {'3코스 디저트와 음료세트': '24000원', '쁘티푸와 음료 세트': '26000원', '샴페인슈가볼': '13000원'}
        소나.location = '서울 강남구 강남대로162길 40 2층 SONA'
        self.광림아트센터_list.append(소나)


    def str_광림아트센터(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
                print(
                    f'이름: {self.광림아트센터_list[i].name}\n위치: {self.광림아트센터_list[i].location}\n메뉴: {self.광림아트센터_list[i].menu}\n별점: {self.광림아트센터_list[i].star}\n후기: {self.광림아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_광림아트센터()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
                print(
                    f'이름: {self.광림아트센터_list[i].name}\n위치: {self.광림아트센터_list[i].location}\n메뉴: {self.광림아트센터_list[i].menu}\n별점: {self.광림아트센터_list[i].star}\n후기: {self.광림아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_광림아트센터()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
                print(
                    f'이름: {self.광림아트센터_list[i].name}\n위치: {self.광림아트센터_list[i].location}\n메뉴: {self.광림아트센터_list[i].menu}\n별점: {self.광림아트센터_list[i].star}\n후기: {self.광림아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_광림아트센터()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
                print(
                    f'이름: {self.광림아트센터_list[i].name}\n위치: {self.광림아트센터_list[i].location}\n메뉴: {self.광림아트센터_list[i].menu}\n별점: {self.광림아트센터_list[i].star}\n후기: {self.광림아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_광림아트센터()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
                print(
                    f'이름: {self.광림아트센터_list[i].name}\n위치: {self.광림아트센터_list[i].location}\n메뉴: {self.광림아트센터_list[i].menu}\n별점: {self.광림아트센터_list[i].star}\n후기: {self.광림아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_광림아트센터()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
                print(
                    f'이름: {self.광림아트센터_list[i].name}\n위치: {self.광림아트센터_list[i].location}\n메뉴: {self.광림아트센터_list[i].menu}\n별점: {self.광림아트센터_list[i].star}\n후기: {self.광림아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_광림아트센터()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_광림아트센터(self):
        for i in range(18):
            print(f'{i + 1}. {self.광림아트센터_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.광림아트센터_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.광림아트센터_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.광림아트센터_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.광림아트센터_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.광림아트센터_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.광림아트센터_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.광림아트센터_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.광림아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.광림아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.광림아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.광림아트센터_list[int(restaurunt_num) - 1].star}\n후기: {self.광림아트센터_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.광림아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.광림아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.광림아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.광림아트센터_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_광림아트센터()


    def 디큐브아트센터(self):
        # 한식
        사월에보리밥과쭈꾸미 = Restaurunt('사월에보리밥과쭈꾸미 현대디큐브신도림점')
        사월에보리밥과쭈꾸미.menu = {'쭈꾸미정식': '12000원', '쭈꾸미한상': '14000원', '보리밥고등어정식': '13000원'}
        사월에보리밥과쭈꾸미.location = '서울 구로구 경인로 661 디큐브시티 6층'
        self.디큐브아트센터_list.append(사월에보리밥과쭈꾸미)

        경복궁 = Restaurunt('경복궁 디큐브점')
        경복궁.menu = {'영양갈비찜한정식(평일/점심특선)': '29000원', '한우불고기 점심한상': '21000원', '숯불갈비살한정식 (평일/점심특선)': '23000원'}
        경복궁.location = '서울 구로구 경인로 662 디큐브시티 현대백화점 6층'
        self.디큐브아트센터_list.append(경복궁)

        그믐족발 = Restaurunt('그믐족발 본점')
        그믐족발.menu = {'꽈리튀김족발': '35000원', '그믐족발(앞다리)': '33000원', '그믐족발(뒷다리)': '29000원'}
        그믐족발.location = '서울 영등포구 경인로 79길 21 1층'
        self.디큐브아트센터_list.append(그믐족발)

        # 중식
        충칭 = Restaurunt('충칭 마라탕 샤브샤브')
        충칭.menu = {'무한리필': '15000원/8000원 (대인/소인)', '마라탕(100g)': '1600원', '마라샹궈(100g)': '3000원'}
        충칭.location = '서울 구로구 경인로 661 2층 226호'
        self.디큐브아트센터_list.append(충칭)

        신미양꼬치 = Restaurunt('신미양꼬치')
        신미양꼬치.menu = {'양꼬치': '12000원', '고추소고기볶음': '18000원', '마라샹궈': '20000원'}
        신미양꼬치.location = '서울 구로구 새말로16길 21'
        self.디큐브아트센터_list.append(신미양꼬치)

        신승반점 = Restaurunt('신승반점 현대백화점 디큐브시티점')
        신승반점.menu = {'유니짜장면': '9000원', '짬뽕': '9000원','볶음밥': '8000원'}
        신승반점.location = '서울 구로구 경인로 662 현대백화점 디큐브시티 B2 신승반점'
        self.디큐브아트센터_list.append(신승반점)

        #일식
        후와후와 = Restaurunt('후와후와 현대백화점 디큐브시티점')
        후와후와.menu = {'아보카도 연어덮밥': '14000원', '아보카도 명란덮밥': '12800원', '프리미엄 장어 솥밥': '18800원'}
        후와후와.location = '서울 구로구 경인로 662 현대백화점 디큐브시티 5층'
        self.디큐브아트센터_list.append(후와후와)

        켄비멘 = Restaurunt('켄비멘 신도림점')
        켄비멘.menu = {'시오라멘': '9000원', '매운라멘': '10000원', '소유라멘': '9000원'}
        켄비멘.location = '서울 구로구 경인로 662'
        self.디큐브아트센터_list.append(켄비멘)

        스시웨이 = Restaurunt('스시웨이 신도림점')
        스시웨이.menu = {'특초밥 A(12pcs)': '19000원', '특초밥 B(12pcs)': '22000원', '스페셜초밥 (15pcs)': '27000원'}
        스시웨이.location = '서울 강남구 압구정로28길 25 엑시'
        self.디큐브아트센터_list.append(스시웨이)

        #양식
        라그릴리아 = Restaurunt('라그릴리아 신도림디큐브시티점')
        라그릴리아.menu = {'로얄까르보나라 파스타': '14800원', '프레쉬 그리너리 플랫피자': '15200원', '스테이크 트러플 크림 파스타': '18600원'}
        라그릴리아.location = '서울 구로구 경인로 662 디큐브시티 2층'
        self.디큐브아트센터_list.append(라그릴리아)

        키친브로망스 = Restaurunt('키친브로망스')
        키친브로망스.menu = {'리코타 명란피자': '17500원', '루꼴라 프로슈토피자': '17000원', '마르게리타 피자': '16000원'}
        키친브로망스.location = '서울 구로구 새말로16길 16 지하1층'
        self.디큐브아트센터_list.append(키친브로망스)

        양키수산 = Restaurunt('양키수산')
        양키수산.menu = {'양키스메인 플레이트': '33000원', '루이지애나 씨푸드 파스타': '18000원', '씨푸드 그린커리 with 바스마티': '18000원'}
        양키수산.location = '서울 영등포구 도림로 139길 11-1 양키수산'
        self.디큐브아트센터_list.append(양키수산)

        # 기타
        이스트 = Restaurunt('이스트바이게이트 신도림점')
        이스트.menu = {'태국쌀국수': '11000원', '포크라이스': '13000원', '뿌팟봉커리': '28000원'}
        이스트.location = '서울시 구로구 경인로 661 디큐브시티'
        self.디큐브아트센터_list.append(이스트)

        온더보더 = Restaurunt('온더보더 현대디큐브시티점')
        온더보더.menu = {'시를링 화이타 샐러드': '27500원', '더블스텍클럽 퀘사디아': '27900원', '얼티밋 화이타': '38900원'}
        온더보더.location = '서울 구로구 경인로 662 디큐브시티 별관 4층'
        self.디큐브아트센터_list.append(온더보더)

        퍼틴 = Restaurunt('퍼틴 현대백화점 디큐브시티점')
        퍼틴.menu = {'프리미엄쌀국수': '11000원', '퍼틴쌀국수': '10000원', '하노이': '9500원'}
        퍼틴.location = '서울 구로구 경인로 662 지하 2층'
        self.디큐브아트센터_list.append(퍼틴)

        # 디저트
        빈브라더스 = Restaurunt('빈브라더스 현대백화점 디큐브시티점')
        빈브라더스.menu = {'아메리카노': '5000원', '오들리 라떼': '6000원', '자몽 허니부쉬티': '6000원'}
        빈브라더스.location = '서울 구로구 경인로 662 디큐브시티'
        self.디큐브아트센터_list.append(빈브라더스)

        밀탑 = Restaurunt('밀탑 현대백화점 디큐브시티점')
        밀탑.menu = {'밀크빙수': '10000원', '과일빙수': '10000원', '오곡빙수': '10000원'}
        밀탑.location = '서울 구로구 경인로 662 디큐브시티'
        self.디큐브아트센터_list.append(밀탑)

        띵크커피 = Restaurunt('띵크커피 디큐브시티점')
        띵크커피.menu = {'띵크커피 L': '4800원', '아메리카노 L': '5300원', '라떼 L': '5800원'}
        띵크커피.location = '서울 구로구 경인로 662 현대백화점디큐브시티점 지하 1층'
        self.디큐브아트센터_list.append(띵크커피)


    def str_디큐브아트센터(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
                print(
                    f'이름: {self.디큐브아트센터_list[i].name}\n위치: {self.디큐브아트센터_list[i].location}\n메뉴: {self.디큐브아트센터_list[i].menu}\n별점: {self.디큐브아트센터_list[i].star}\n후기: {self.디큐브아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_디큐브아트센터()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
                print(
                    f'이름: {self.디큐브아트센터_list[i].name}\n위치: {self.디큐브아트센터_list[i].location}\n메뉴: {self.디큐브아트센터_list[i].menu}\n별점: {self.디큐브아트센터_list[i].star}\n후기: {self.디큐브아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_디큐브아트센터()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
                print(
                    f'이름: {self.디큐브아트센터_list[i].name}\n위치: {self.디큐브아트센터_list[i].location}\n메뉴: {self.디큐브아트센터_list[i].menu}\n별점: {self.디큐브아트센터_list[i].star}\n후기: {self.디큐브아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_디큐브아트센터()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
                print(
                    f'이름: {self.디큐브아트센터_list[i].name}\n위치: {self.디큐브아트센터_list[i].location}\n메뉴: {self.디큐브아트센터_list[i].menu}\n별점: {self.디큐브아트센터_list[i].star}\n후기: {self.디큐브아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_디큐브아트센터()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
                print(
                    f'이름: {self.디큐브아트센터_list[i].name}\n위치: {self.디큐브아트센터_list[i].location}\n메뉴: {self.디큐브아트센터_list[i].menu}\n별점: {self.디큐브아트센터_list[i].star}\n후기: {self.디큐브아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_디큐브아트센터()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
                print(
                    f'이름: {self.디큐브아트센터_list[i].name}\n위치: {self.디큐브아트센터_list[i].location}\n메뉴: {self.디큐브아트센터_list[i].menu}\n별점: {self.디큐브아트센터_list[i].star}\n후기: {self.디큐브아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_디큐브아트센터()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_디큐브아트센터(self):
        for i in range(18):
            print(f'{i + 1}. {self.디큐브아트센터_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.디큐브아트센터_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.디큐브아트센터_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.디큐브아트센터_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.디큐브아트센터_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.디큐브아트센터_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.디큐브아트센터_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.디큐브아트센터_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(f'이름: {self.디큐브아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.디큐브아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.디큐브아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.디큐브아트센터_list[int(restaurunt_num) - 1].star}\n후기: {self.디큐브아트센터_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(f'이름: {self.디큐브아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.디큐브아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.디큐브아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.디큐브아트센터_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_디큐브아트센터()


    def 블루스퀘어(self):
        # 한식
        Gongi = Restaurunt('Gongi')
        Gongi.menu = {'채끝등심구이': '32000원', '가지새우강정': '20000원', '송화고 강정': '17000원'}
        Gongi.location = '서울 용산구 이태원로45길 4 1,2층'
        self.블루스퀘어_list.append(Gongi)

        일호식 = Restaurunt('일호식 사운즈한남점')
        일호식.menu = {'일호식 점심 소반': '15500원', '고기 김치전': '12000원', '일호식 왕갈비찜': '39000원'}
        일호식.location = '서울 용산구 대사관로 35'
        self.블루스퀘어_list.append(일호식)

        시화담 = Restaurunt('시화담 파인다이닝')
        시화담.menu = {'해물을 듬뿍 얹은 동래 파전': '25000원', '감칠맛 나는 장모님의 닭튀김': '20000원', '(코스)한줄의 시(런치)': '45000원'}
        시화담.location = '서울 용산구 이태원로 254 3층'
        self.블루스퀘어_list.append(시화담)

        # 중식
        청 = Restaurunt('중식당 청 한남점')
        청.menu = {'해삼탕(소)': '45000원', '왕새우(소)': '12000원', '삼선 자장면': '9000원'}
        청.location = '서울 용산구 한남대로20길 47-24 리플레이스 D동 2층'
        self.블루스퀘어_list.append(청)

        JARI = Restaurunt('JARI')
        JARI.menu = {'철판어향새우가지': '26000원', '목화솜 탕수육': '21000원', 'JARI’s짬뽕': '12000원'}
        JARI.location = '서울 용산구 이태원로 54길 5-5'
        self.블루스퀘어_list.append(JARI)

        마라 = Restaurunt('마라')
        마라.menu = {'마라샹궈 대': '53000원', '수안라탕면': '8000원', '마파두부덮밥': '12000원'}
        마라.location = '서울 용산구 이태원로 4층'
        self.블루스퀘어_list.append(마라)

        # 일식
        오복수산 = Restaurunt('오복수산')
        오복수산.menu = {'카이센동': '18000원', '우니이쿠라카이센동': '27000원', '도로우니동': '30000원'}
        오복수산.location = '서울 용산구 이태원로54길 26'
        self.블루스퀘어_list.append(오복수산)

        라멘81번옥 = Restaurunt('라멘81번옥 이태원점')
        라멘81번옥.menu = {'돈코츠라멘': '9000원', '사케동': '12000원', '소유라멘': '8000원'}
        라멘81번옥.location = '서울 용산구 이태원로 258'
        self.블루스퀘어_list.append(라멘81번옥)

        엔소쿠 = Restaurunt('엔소쿠')
        엔소쿠.menu = {'어묵우동': '4500원', '비빔우동': '6000원', '카레우동': '6000원'}
        엔소쿠.location = '서울 용산구 이태원로54길 8 지1층'
        self.블루스퀘어_list.append(엔소쿠)

        # 양식
        리틀넥 = Restaurunt('리틀넥 한남')
        리틀넥.menu = {'살몬 포케': '12000원', '머쉬룸 리조또': '20000원', '명란 크림 파스타': '18000원'}
        리틀넥.location = '서울 용산구 한남대로27길 66 1층'
        self.블루스퀘어_list.append(리틀넥)

        파이프그라운드 = Restaurunt('파이프그라운드')
        파이프그라운드.menu = {'리가토니 화이트 라구': '20000원', '옥수수피자': '20000원', '로메인시저': '8000원'}
        파이프그라운드.location = '서울 용산구 한남대로27길 66 지하1층'
        self.블루스퀘어_list.append(파이프그라운드)

        summer = Restaurunt('Summer Lane')
        summer.menu = {'크로아상프렌치토스트': '16000원', '(베이컨/연어)와플에그베네딕트': '17000원', '스매쉬드 아보카도': '17000원'}
        summer.location = '서울 용산구 이태원로55가길 49 1층 summerlane'
        self.블루스퀘어_list.append(summer)

        # 기타
        어메이징타이 = Restaurunt('어메이징타이')
        어메이징타이.menu = {'팟 타이 꿍': '14000원', '톰 양 꿍': '14000원', '팟 타이 까이': '13000원'}
        어메이징타이.location = '서울 용산구 이태원로 238'
        self.블루스퀘어_list.append(어메이징타이)

        WangThai = Restaurunt('WangThai')
        WangThai.menu = {'똠양꿍': '17000원', '팟타이 가이': '13000원', '얌운센': '16000원'}
        WangThai.location = '서울 용산구 이태원로 1511'
        self.블루스퀘어_list.append(WangThai)

        플러스84 = Restaurunt('플러스84')
        플러스84.menu = {'Special 반미': '8000원', '스프링롤': '8000원', '쇠고기 쌀국수': '9000원'}
        플러스84.location = '서울 용산구 보광로59길 56 2층'
        self.블루스퀘어_list.append(플러스84)

        # 디저트
        카페드블루 = Restaurunt('카페드블루 블루스퀘어점')
        카페드블루.menu = {'아메리카노': '4000원', '카페라떼/카푸치노': '4500원', '밀크티/초코라떼': '4700원'}
        카페드블루.location = '서울 용산구 한남동 727-35 카페드블루'
        self.블루스퀘어_list.append(카페드블루)

        패션5 = Restaurunt('패션5 라뜰리에')
        패션5.menu = {'클럽샌드위치브런치': '23000원', '레몬치킨&아보카도 샐러드': '17000원', '갈릭소스 비프 버거 플레이트': '24000원'}
        패션5.location = '서울 용산구 이태원로 272 2층'
        self.블루스퀘어_list.append(패션5)

        키에리 = Restaurunt('키에리')
        키에리.menu = {'아메리카노': '4900원', '카페라떼/카페모카/카라멜마끼아또': '5500원', '콘크럼블치즈케이크': '9500원'}
        키에리.location = '서울 용산구 이태원로26길 16-8 1층'
        self.블루스퀘어_list.append(키에리)


    def str_블루스퀘어(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.블루스퀘어_list[i].name}\n위치: {self.블루스퀘어_list[i].location}\n메뉴: {self.블루스퀘어_list[i].menu}\n별점: {self.블루스퀘어_list[i].star}\n후기: {self.블루스퀘어_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_블루스퀘어()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.블루스퀘어_list[i].name}\n위치: {self.블루스퀘어_list[i].location}\n메뉴: {self.블루스퀘어_list[i].menu}\n별점: {self.블루스퀘어_list[i].star}\n후기: {self.블루스퀘어_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_블루스퀘어()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.블루스퀘어_list[i].name}\n위치: {self.블루스퀘어_list[i].location}\n메뉴: {self.블루스퀘어_list[i].menu}\n별점: {self.블루스퀘어_list[i].star}\n후기: {self.블루스퀘어_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_블루스퀘어()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.블루스퀘어_list[i].name}\n위치: {self.블루스퀘어_list[i].location}\n메뉴: {self.블루스퀘어_list[i].menu}\n별점: {self.블루스퀘어_list[i].star}\n후기: {self.블루스퀘어_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_블루스퀘어()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.블루스퀘어_list[i].name}\n위치: {self.블루스퀘어_list[i].location}\n메뉴: {self.블루스퀘어_list[i].menu}\n별점: {self.블루스퀘어_list[i].star}\n후기: {self.블루스퀘어_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_블루스퀘어()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.블루스퀘어_list[i].name}\n위치: {self.블루스퀘어_list[i].location}\n메뉴: {self.블루스퀘어_list[i].menu}\n별점: {self.블루스퀘어_list[i].star}\n후기: {self.블루스퀘어_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_블루스퀘어()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_블루스퀘어(self):
        for i in range(18):
            print(f'{i + 1}. {self.블루스퀘어_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.블루스퀘어_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.블루스퀘어_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.블루스퀘어_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.블루스퀘어_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.블루스퀘어_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.블루스퀘어_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.블루스퀘어_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.블루스퀘어_list[int(restaurunt_num) - 1].name}\n위치: {self.블루스퀘어_list[int(restaurunt_num) - 1].location}\n메뉴: {self.블루스퀘어_list[int(restaurunt_num) - 1].menu}\n별점: {self.블루스퀘어_list[int(restaurunt_num) - 1].star}\n후기: {self.블루스퀘어_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.블루스퀘어_list[int(restaurunt_num) - 1].name}\n위치: {self.블루스퀘어_list[int(restaurunt_num) - 1].location}\n메뉴: {self.블루스퀘어_list[int(restaurunt_num) - 1].menu}\n별점: {self.블루스퀘어_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_블루스퀘어()


    def 세종문화회관(self):
        # 한식
        설가온 = Restaurunt('설가온')
        설가온.menu = {'점심특선': '30000원', '오찬': '35000원', '궁 코스': '40000원'}
        설가온.location = '서울 종로구 세종대로 175 세종문화회관 지하1층 설가온'
        self.세종문화회관_list.append(설가온)

        반상 = Restaurunt('반상')
        반상.menu = {'김치전골': '13000원', '김치등찜': '35000원', '김치찜': '13000원'}
        반상.location = '서울 종로구 세종대로 175 세종문화회관 지하1층'
        self.세종문화회관_list.append(반상)

        광화문한옥집 = Restaurunt('광화문한옥집')
        광화문한옥집.menu = {'대왕 소갈비 도시락': '30000원', '떡갈비 도시락': '19000원', '낙지볶음 반상': '19000원'}
        광화문한옥집.location = '서울 종로구 새문안로5가길 7 B1층'
        self.세종문화회관_list.append(광화문한옥집)

        # 중식
        동성각 = Restaurunt('동성각')
        동성각.menu = {'짜장면': '6000원', '짬뽕': '7000원', '탕수육': '20000원'}
        동성각.location = '서울 종로구 새문안로9길 29-2 당주빌딩'
        self.세종문화회관_list.append(동성각)

        가봉루 = Restaurunt('가봉루')
        가봉루.menu = {'삼선짬뽕': '8000원', '삼선짜장': '8000원', '짬뽕': '6000원'}
        가봉루.location = '서울 종로구 세종대로23길 3 2층 가봉루'
        self.세종문화회관_list.append(가봉루)

        동천홍 = Restaurunt('동천홍 광화문점')
        동천홍.menu = {'오품냉채': '55000원', '오향장육': '20000원', '매생이샥스핀스프': '10000원'}
        동천홍.location = '서울 종로구 새문안로9길 23'
        self.세종문화회관_list.append(동천홍)

        # 일식
        오가와 = Restaurunt('오가와')
        오가와.menu = {'오마카세(런치)': '50000원', '오마카세(디너코스)': '80000원', '포장 도시락': '40000원'}
        오가와.location = '서울 종로구 새문안로5길 19'
        self.세종문화회관_list.append(오가와)

        사보텐 = Restaurunt('사보텐 광화문점')
        사보텐.menu = {'제주흑돈카츠(히레)': '17000원', '더블업 모차렐라 카츠': '15500원', '시그니처카츠': '17000원'}
        사보텐.location = '서울 종로구 새문안로 103 2층'
        self.세종문화회관_list.append(사보텐)

        동경우동 = Restaurunt('동경우동')
        동경우동.menu = {'동경우동': '6000원', '오뎅우동': '7000원', '회덮밥': '8000원'}
        동경우동.location = '서울 종로구 새문안로9길 28'
        self.세종문화회관_list.append(동경우동)

        # 양식
        뽐모도로 = Restaurunt('뽐모도로 광화문지점')
        뽐모도로.menu = {'Spaghetti all\' Amatriciana': '16500원', 'Spaghetti Con gamberi all Aglio Dolce': '18000원', 'Spaghetti alle Vongole Veraei': '18000원'}
        뽐모도로.location = '서울 종로구 새문안로9길 19-1'
        self.세종문화회관_list.append(뽐모도로)

        루뽀 = Restaurunt('루뽀')
        루뽀.menu = {'더 램(1.2kg/2~3인분)': '67000원', '깻잎페스토치킨파스타': '20000원', '토마호크(1.4kg)': '158000원'}
        루뽀.location = '서울 종로구 새문안로5길 31 센터포인트 빌딩 2층'
        self.세종문화회관_list.append(루뽀)

        매드포갈릭 = Restaurunt('매드포갈릭 광화문D타워')
        매드포갈릭.menu = {'Caesar Salad': '17900원', 'Garlicpeno Pasta': '22800원', 'Garlic Sizzling Rice': '25200원'}
        매드포갈릭.location = '서울 종로구 종로3길 17 D타워 리플레이스 광화문 3층'
        self.세종문화회관_list.append(매드포갈릭)

        # 기타
        반포식스 = Restaurunt('반포식스 광화문점')
        반포식스.menu = {'쌀국수': '9500원', '볶음밥, 볶음면': '12000원', '스프링롤': '5000원'}
        반포식스.location = '서울 종로구 새문안로 97'
        self.세종문화회관_list.append(반포식스)

        팻누들 = Restaurunt('팻누들 디타워점')
        팻누들.menu = {'포 닥 비엣': '11900원', '포타이': '12900원', '분 팃 느엉': '13900원'}
        팻누들.location = '서울 종로구 종로3길 17'
        self.세종문화회관_list.append(팻누들)

        미미쌀국수 = Restaurunt('미미쌀국수')
        미미쌀국수.menu = {'미미 쌀국수': '6900원', '얼큰 쌀국수': '7900원', '소곱창 쌀국수': '9900원'}
        미미쌀국수.location = '서울 종로구 새문안로3길 36 용비어천가 101호'
        self.세종문화회관_list.append(미미쌀국수)

        # 디저트
        모란커피 = Restaurunt('모란커피')
        모란커피.menu = {'아메리카노': '2800원', '헤이즐넛라떼': '4000원', '카페모카': '4500원'}
        모란커피.location = '서울 종로구 새문안로5길 13 변호사회관 지하 1층'
        self.세종문화회관_list.append(모란커피)

        플로리안커피 = Restaurunt('플로리안커피')
        플로리안커피.menu = {'에스프레소 핫': '2500원', '아메리카노 핫': '2500원', '비엔나커피 핫': '3000원'}
        플로리안커피.location = '서울 종로구 새문안로5길 7-1'
        self.세종문화회관_list.append(플로리안커피)

        카페자스 = Restaurunt('카페자스 광화문점')
        카페자스.menu = {'에그타르트': '2500원', '바닐라라떼': '3800원', '아메리카노': '2800원'}
        카페자스.location = '서울 종로구 새문안로5가길 3-1 영진빌딩 1층'
        self.세종문화회관_list.append(카페자스)


    def str_세종문화회관(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.세종문화회관_list[i].name}\n위치: {self.세종문화회관_list[i].location}\n메뉴: {self.세종문화회관_list[i].menu}\n별점: {self.세종문화회관_list[i].star}\n후기: {self.세종문화회관_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세종문화회관()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.세종문화회관_list[i].name}\n위치: {self.세종문화회관_list[i].location}\n메뉴: {self.세종문화회관_list[i].menu}\n별점: {self.세종문화회관_list[i].star}\n후기: {self.세종문화회관_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세종문화회관()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.세종문화회관_list[i].name}\n위치: {self.세종문화회관_list[i].location}\n메뉴: {self.세종문화회관_list[i].menu}\n별점: {self.세종문화회관_list[i].star}\n후기: {self.세종문화회관_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세종문화회관()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.세종문화회관_list[i].name}\n위치: {self.세종문화회관_list[i].location}\n메뉴: {self.세종문화회관_list[i].menu}\n별점: {self.세종문화회관_list[i].star}\n후기: {self.세종문화회관_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세종문화회관()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.세종문화회관_list[i].name}\n위치: {self.세종문화회관_list[i].location}\n메뉴: {self.세종문화회관_list[i].menu}\n별점: {self.세종문화회관_list[i].star}\n후기: {self.세종문화회관_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세종문화회관()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.세종문화회관_list[i].name}\n위치: {self.세종문화회관_list[i].location}\n메뉴: {self.세종문화회관_list[i].menu}\n별점: {self.세종문화회관_list[i].star}\n후기: {self.세종문화회관_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세종문화회관()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_세종문화회관(self):
        for i in range(18):
            print(f'{i + 1}. {self.세종문화회관_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.세종문화회관_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.세종문화회관_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.세종문화회관_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.세종문화회관_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.세종문화회관_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.세종문화회관_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.세종문화회관_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.세종문화회관_list[int(restaurunt_num) - 1].name}\n위치: {self.세종문화회관_list[int(restaurunt_num) - 1].location}\n메뉴: {self.세종문화회관_list[int(restaurunt_num) - 1].menu}\n별점: {self.세종문화회관_list[int(restaurunt_num) - 1].star}\n후기: {self.세종문화회관_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.세종문화회관_list[int(restaurunt_num) - 1].name}\n위치: {self.세종문화회관_list[int(restaurunt_num) - 1].location}\n메뉴: {self.세종문화회관_list[int(restaurunt_num) - 1].menu}\n별점: {self.세종문화회관_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_세종문화회관()


    def 예술의전당(self):
        # 한식
        바다양푼이동태탕 = Restaurunt('바다양푼이동태탕 서초점')
        바다양푼이동태탕.menu = {'생태탕': '13000원', '섞어탕': '9000원', '알곤이탕': '9000원'}
        바다양푼이동태탕.location = '서울 서초구 반포대로 12 1층'
        self.예술의전당_list.append(바다양푼이동태탕)

        앵콜칼국수 = Restaurunt('앵콜칼국수')
        앵콜칼국수.menu = {'옛날손칼국수': '8000원', '얼큰칼국수': '8500원', '팥칼국수': '10000원'}
        앵콜칼국수.location = '서울 서초구 효령로52길 69'
        self.예술의전당_list.append(앵콜칼국수)

        백년옥 = Restaurunt('백년옥')
        백년옥.menu = {'자연식 순두부': '10000원', '뚝배기 순두부': '10000원', '팥동지죽': '10000원'}
        백년옥.location = '서울 서초구 남부순환로 2407'
        self.예술의전당_list.append(백년옥)

        # 중식
        차이나비스트로 = Restaurunt('차이나비스트로')
        차이나비스트로.menu = {'탕수육, 간풍기': '18000원', '양장피, 간풍기, 탕수육': '26000원', '양장피, 간풍기, 탕수육, 고추잡채': '34000원'}
        차이나비스트로.location = '서울 서초구 반포대로3길 20'
        self.예술의전당_list.append(차이나비스트로)

        공리 = Restaurunt('공리 중국집')
        공리.menu = {'차돌짬뽕': '9500원', '관자해물짬뽕': '9500원', '오징어삼겹짬뽕': '9000원'}
        공리.location = '서울 서초구 반포대로7길 7 동양빌딩'
        self.예술의전당_list.append(공리)

        부라문 = Restaurunt('부라문')
        부라문.menu = {'짜장면+계란후라이': '7000원', '우육탕면': '9000원', '차돌짬뽕': '10000원'}
        부라문.location = '서울 서초구 남부순환로325길 9'
        self.예술의전당_list.append(부라문)

        # 일식
        동경도 = Restaurunt('동경도')
        동경도.menu = {'부타동(제육덮밥)': '6000원', '규동(소고기 덮밥)': '7000원', '코이 돈코츠라멘': '8000원'}
        동경도.location = '서울 서초구 남부순환로317길 18-3'
        self.예술의전당_list.append(동경도)

        허수아비돈까스 = Restaurunt('허수아비돈까스 본점')
        허수아비돈까스.menu = {'로스까스': '9000원', '코돈브루': '12500원', '히레까스': '9500원'}
        허수아비돈까스.location = '서울 서초구 반포대로 16 지하1층'
        self.예술의전당_list.append(허수아비돈까스)

        연어로만 = Restaurunt('연어로만 서초점')
        연어로만.menu = {'생연어야채롤': '10800원', '생연어덮밥': '9900원', '연어구이크림파스타': '12900원'}
        연어로만.location = '서울 서초구 반포대로9길 3 삼현빌딩'
        self.예술의전당_list.append(연어로만)

        # 양식
        비노인빌라 = Restaurunt('비노인빌라 Vino in Villa')
        비노인빌라.menu = {'알리오올리오(Alio e olio)': '15000원', '페투치니(Fettucine)': '21000원', '봉골레(Vongole)': '19000원'}
        비노인빌라.location = '서울 서초구 남부순환로319길 14 제이큐브데이터빌딩1층'
        self.예술의전당_list.append(비노인빌라)

        플람스 = Restaurunt('플람스 비스트로')
        플람스.menu = {'플람스': '12000원', '굴라쉬와 슈페츨레': '20000원', '슈페츨레': '17000원'}
        플람스.location = '서울 서초구 남부순환로317길 41 1층'
        self.예술의전당_list.append(플람스)

        노트르비 = Restaurunt('노트르비')
        노트르비.menu = {'고다 시그니처 버거': '11800원', '푸타네스카': '13500원', '새우 비스큐 크림': '14500원'}
        노트르비.location = '서울 서초구 효령로40길 25 1층'
        self.예술의전당_list.append(노트르비)

        # 기타
        바노이 = Restaurunt('바노이')
        바노이.menu = {'분짜': '16000원', '양지 쌀국수': '9000원', '분보남보': '10000원'}
        바노이.location = '서울 서초구 반포대로 10 신원빌딩 1층'
        self.예술의전당_list.append(바노이)

        포호아 = Restaurunt('포호아 예술의전당점')
        포호아.menu = {'K1 안심 쌀국수(M)': '11000원', 'K2 양지 쌀국수(M)': '9500원', 'K3 양지, 힘줄쌀국수(M)': '10000원'}
        포호아.location = '서울 서초구 남부순환로323길 1 다모성갤러리'
        self.예술의전당_list.append(포호아)

        마실 = Restaurunt('마실')
        마실.menu = {'마실 오뎅 쌀국수 탕면': '8000원', '매콤한 쌀국수 탕면': '7000원', '달콤한 쌀국수 볶음면': '7000원'}
        마실.location = '서울 서초구 명달로 58'
        self.예술의전당_list.append(마실)

        # 디저트
        커피라운지55 = Restaurunt('커피라운지55')
        커피라운지55.menu = {'아메리카노': '3000원', '스페셜 아메리카노': '4000원', '디 카페인 아메리카노': '4500원'}
        커피라운지55.location = '서울 서초구 반포대로 9 1층'
        self.예술의전당_list.append(커피라운지55)

        decen = Restaurunt('cafe de cen')
        decen.menu = {'리얼자몽주스': '5500원', '리얼딸기주스': '2500원', '아메리카노(핫)': '2500원'}
        decen.location = '서울 서초구 반포대로 13 아이티센빌딩 1층'
        self.예술의전당_list.append(decen)

        프리퍼 = Restaurunt('프리퍼')
        프리퍼.menu = {'크림 드 코코': '5000원', '인절미 티라미수': '5500원', '토피넛 라떼': '5000원'}
        프리퍼.location = '서울 서초구 반포대로5길 4 성원빌딩 1층'
        self.예술의전당_list.append(프리퍼)


    def str_예술의전당(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.예술의전당_list[i].name}\n위치: {self.예술의전당_list[i].location}\n메뉴: {self.예술의전당_list[i].menu}\n별점: {self.예술의전당_list[i].star}\n후기: {self.예술의전당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_예술의전당()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.예술의전당_list[i].name}\n위치: {self.예술의전당_list[i].location}\n메뉴: {self.예술의전당_list[i].menu}\n별점: {self.예술의전당_list[i].star}\n후기: {self.예술의전당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_예술의전당()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.예술의전당_list[i].name}\n위치: {self.예술의전당_list[i].location}\n메뉴: {self.예술의전당_list[i].menu}\n별점: {self.예술의전당_list[i].star}\n후기: {self.예술의전당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_예술의전당()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.예술의전당_list[i].name}\n위치: {self.예술의전당_list[i].location}\n메뉴: {self.예술의전당_list[i].menu}\n별점: {self.예술의전당_list[i].star}\n후기: {self.예술의전당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_예술의전당()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.예술의전당_list[i].name}\n위치: {self.예술의전당_list[i].location}\n메뉴: {self.예술의전당_list[i].menu}\n별점: {self.예술의전당_list[i].star}\n후기: {self.예술의전당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_예술의전당()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.예술의전당_list[i].name}\n위치: {self.예술의전당_list[i].location}\n메뉴: {self.예술의전당_list[i].menu}\n별점: {self.예술의전당_list[i].star}\n후기: {self.예술의전당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_예술의전당()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_예술의전당(self):
        for i in range(18):
            print(f'{i + 1}. {self.예술의전당_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.예술의전당_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.예술의전당_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.예술의전당_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.예술의전당_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.예술의전당_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.예술의전당_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.예술의전당_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.예술의전당_list[int(restaurunt_num) - 1].name}\n위치: {self.예술의전당_list[int(restaurunt_num) - 1].location}\n메뉴: {self.예술의전당_list[int(restaurunt_num) - 1].menu}\n별점: {self.예술의전당_list[int(restaurunt_num) - 1].star}\n후기: {self.예술의전당_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.예술의전당_list[int(restaurunt_num) - 1].name}\n위치: {self.예술의전당_list[int(restaurunt_num) - 1].location}\n메뉴: {self.예술의전당_list[int(restaurunt_num) - 1].menu}\n별점: {self.예술의전당_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_예술의전당()


    def 유니버설아트센터(self):
        # 한식
        다래나무 = Restaurunt('다래나무')
        다래나무.menu = {'영광보리굴비정식': '22000원', '토종닭 녹두백숙(3~4인분)': '65000원', '오리 녹두백숙(3~4인분)': '60000원'}
        다래나무.location = '서울 광진구 천호대로124길 24'
        self.유니버설아트센터_list.append(다래나무)

        정선곤드레메밀집 = Restaurunt('정선곤드레메밀집')
        정선곤드레메밀집.menu = {'정선황기보쌈': '27000원', '촌두부김치': '15000원', '메밀싹쌈': '13000원'}
        정선곤드레메밀집.location = '서울 광진구 능동로36길 186'
        self.유니버설아트센터_list.append(정선곤드레메밀집)

        손씨네 = Restaurunt('손씨네 부대찌개')
        손씨네.menu = {'손씨네 부대찌개': '7500원', '손씨네 솥밥 부대찌개': '8500원', '손씨네 돝솦밥 부대찌개': '9500원'}
        손씨네.location = '서울 광진구 자양로43길 28'
        self.유니버설아트센터_list.append(손씨네)

        # 중식
        짬뽕지존 = Restaurunt('짬뽕지존 아차산역점')
        짬뽕지존.menu = {'게살볶음밥': '8500원', '새우볶음밥': '8500원', '지존짜장': '7500원'}
        짬뽕지존.location = '서울 광진구 천호대로 682'
        self.유니버설아트센터_list.append(짬뽕지존)

        전설의짬뽕 = Restaurunt('전설의짬뽕 아차산점')
        전설의짬뽕.menu = {'찹쌀탕수육': '13000원', '홍합해물짬뽕': '7000원', '소고기짬뽕': '9000원'}
        전설의짬뽕.location = '서울 광진구 자양로43길 42'
        self.유니버설아트센터_list.append(전설의짬뽕)

        무명반점 = Restaurunt('무명반점')
        무명반점.menu = {'짜장면': '6000원', '해물짬뽕': '9000원', '유산슬': '29000원'}
        무명반점.location = '서울 광진구 천호대로127길 19'
        self.유니버설아트센터_list.append(무명반점)

        # 일식
        가야초밥 = Restaurunt('가야초밥')
        가야초밥.menu = {'모듬초밥': '10000원', '생선초밥': '15000원', '광어초밥': '18000원'}
        가야초밥.location = '서울 광진구 자양로41길 7'
        self.유니버설아트센터_list.append(가야초밥)

        소바쿠 = Restaurunt('소바쿠')
        소바쿠.menu = {'냉소바': '7000원', '자루소바': '7000원', '토리카라': '6000원'}
        소바쿠.location = '서울 광진구 천호대로 650'
        self.유니버설아트센터_list.append(소바쿠)

        토라스시 = Restaurunt('토라스시')
        토라스시.menu = {'혼술사시미': '19000원', '혼술연어사시미(15p)': '21000원', '연어사시미(21p)': '32000원'}
        토라스시.location = '서울 광진구 자양로43길 57'
        self.유니버설아트센터_list.append(토라스시)

        # 양식
        아스토리아 = Restaurunt('아스토리아')
        아스토리아.menu = {'소고기 수비드 스테이크 (등심)': '39000원', '새우 버터 스파게티': '16000원', '양고기 프렌치 렉': '43000원'}
        아스토리아.location = '서울 광진구 능동로36길 182 1층 아스토리아'
        self.유니버설아트센터_list.append(아스토리아)

        라비올리 = Restaurunt('라비올리')
        라비올리.menu = {'해산물마리나라': '6500원', '까르보나라': '6500원', '해산물알프레도': '6500원'}
        라비올리.location = '서울 광진구 천호대로129길 16'
        self.유니버설아트센터_list.append(라비올리)

        아마노 = Restaurunt('아마노')
        아마노.menu = {'아마노': '16000원', '파파델레': '13000원', '마르게리따': '13000원'}
        아마노.location = '서울 광진구 자양로39길 20'
        self.유니버설아트센터_list.append(아마노)

        # 기타
        멕시칼리 = Restaurunt('멕시칼리')
        멕시칼리.menu = {'피쉬 타코 2개': '8800원', '소고기 께사디야': '10800원', '과꽈몰레 나초': '7800원'}
        멕시칼리.location = '서울 광진구 능동로36길 181 1층'
        self.유니버설아트센터_list.append(멕시칼리)

        미스사이공 = Restaurunt('미스사이공 아차산점')
        미스사이공.menu = {'소고기 쌀국수': '4500원', '닭고기 쌀국수': '4500원', '사이공 볶음면': '4500원'}
        미스사이공.location = '서울 광진구 자양로43길 47'
        self.유니버설아트센터_list.append(미스사이공)

        리틀하노이 = Restaurunt('리틀하노이 군자역점')
        리틀하노이.menu = {'best 분팃사오(분짜)': '10900원', 'best 양지쌀국수(보통)': '6500원', 'best 매운양지쌀국수(보통)': '7500원'}
        리틀하노이.location = '서울 광진구 천호대로112길 10'
        self.유니버설아트센터_list.append(리틀하노이)

        # 디저트
        산풀잎 = Restaurunt('카페 산풀잎')
        산풀잎.menu = {'쌍화차': '7000원', '소리차': '7000원', '산풀잎 차': '6000원'}
        산풀잎.location = '서울 광진구 천호대로124길 28 2층'
        self.유니버설아트센터_list.append(산풀잎)

        블레이크커피 = Restaurunt('블레이크커피')
        블레이크커피.menu = {'에스프레소': '4500원', '아메리카노': '4500원', '카푸치노': '5000원'}
        블레이크커피.location = '서울 광진구 천호대로124길 20'
        self.유니버설아트센터_list.append(블레이크커피)

        안다즈커피 = Restaurunt('안다즈커피')
        안다즈커피.menu = {'아메리카노': '4500원', '카페라떼': '5500원', '타이밀크티525': '6000원'}
        안다즈커피.location = '서울 광진구 천호대로132길 10'
        self.유니버설아트센터_list.append(안다즈커피)


    def str_유니버설아트센터(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.유니버설아트센터_list[i].name}\n위치: {self.유니버설아트센터_list[i].location}\n메뉴: {self.유니버설아트센터_list[i].menu}\n별점: {self.유니버설아트센터_list[i].star}\n후기: {self.유니버설아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_유니버설아트센터()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.유니버설아트센터_list[i].name}\n위치: {self.유니버설아트센터_list[i].location}\n메뉴: {self.유니버설아트센터_list[i].menu}\n별점: {self.유니버설아트센터_list[i].star}\n후기: {self.유니버설아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_유니버설아트센터()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.유니버설아트센터_list[i].name}\n위치: {self.유니버설아트센터_list[i].location}\n메뉴: {self.유니버설아트센터_list[i].menu}\n별점: {self.유니버설아트센터_list[i].star}\n후기: {self.유니버설아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_유니버설아트센터()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.유니버설아트센터_list[i].name}\n위치: {self.유니버설아트센터_list[i].location}\n메뉴: {self.유니버설아트센터_list[i].menu}\n별점: {self.유니버설아트센터_list[i].star}\n후기: {self.유니버설아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_유니버설아트센터()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.유니버설아트센터_list[i].name}\n위치: {self.유니버설아트센터_list[i].location}\n메뉴: {self.유니버설아트센터_list[i].menu}\n별점: {self.유니버설아트센터_list[i].star}\n후기: {self.유니버설아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_유니버설아트센터()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.유니버설아트센터_list[i].name}\n위치: {self.유니버설아트센터_list[i].location}\n메뉴: {self.유니버설아트센터_list[i].menu}\n별점: {self.유니버설아트센터_list[i].star}\n후기: {self.유니버설아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_유니버설아트센터()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_유니버설아트센터(self):
        for i in range(18):
            print(f'{i + 1}. {self.유니버설아트센터_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.유니버설아트센터_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.유니버설아트센터_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.유니버설아트센터_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.유니버설아트센터_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.유니버설아트센터_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.유니버설아트센터_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.유니버설아트센터_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.유니버설아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.유니버설아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.유니버설아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.유니버설아트센터_list[int(restaurunt_num) - 1].star}\n후기: {self.유니버설아트센터_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.유니버설아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.유니버설아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.유니버설아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.유니버설아트센터_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_유니버설아트센터()


    def 충무아트센터(self):
        # 한식
        불꽃닭발 = Restaurunt('불꽃닭발')
        불꽃닭발.menu = {'불꽃 오돌뼈': '16000원', '불꽃 닭발': '16000원', '불꽃 똥집': '16000원'}
        불꽃닭발.location = '서울 중구 퇴계로73길 54-67'
        self.충무아트센터_list.append(불꽃닭발)

        나주곰탕 = Restaurunt('나주곰탕신당본점')
        나주곰탕.menu = {'나주곰탕': '8000원', '얼큰곰탕': '9000원', '얼큰곰탕': '7000원'}
        나주곰탕.location = '서울 중구 퇴계로 386'
        self.충무아트센터_list.append(나주곰탕)

        전원식당 = Restaurunt('전원식당')
        전원식당.menu = {'생목살 김치찌개': '7000원', '된장찌개': '7000원', '갈치조림': '9000원'}
        전원식당.location = '서울 중구 퇴계로 397'
        self.충무아트센터_list.append(전원식당)

        # 중식
        차이나문 = Restaurunt('차이나문')
        차이나문.menu = {'짜장면': '6000원', '짬뽕': '7000원', '간짜장': '7000원'}
        차이나문.location = '서울 중구 퇴계로 384'
        self.충무아트센터_list.append(차이나문)

        텐미미 = Restaurunt('텐미미')
        텐미미.menu = {'자장면': '5000원', '삼선간자장': '8000원', '고추간자장': '7000원'}
        텐미미.location = '서울 중구 다산로47길 27'
        self.충무아트센터_list.append(텐미미)

        고향정도삭면 = Restaurunt('고향정도삭면')
        고향정도삭면.menu = {'대표도삭면招牌刀削面': '7000원', '충유면葱油面': '7000원', '비빔면凉拌面': '7000원'}
        고향정도삭면.location = '서울 중구 퇴계로 386-1'
        self.충무아트센터_list.append(고향정도삭면)

        # 일식
        산들바다 = Restaurunt('The 92 산들바다')
        산들바다.menu = {'등심까스': '7500원', '김치나베': '8500원', '어묵우동': '7500원'}
        산들바다.location = '서울 중구 퇴계로 398 1층'
        self.충무아트센터_list.append(산들바다)

        키라키라윤 = Restaurunt('키라키라윤 신당점')
        키라키라윤.menu = {'버터명란구이': '15000원', '연어사시미': '19000원', '스키야끼(2~3인분)': '20000원'}
        키라키라윤.location = '서울 중구 다산로39길 20'
        self.충무아트센터_list.append(키라키라윤)

        우미회전초밥 = Restaurunt('우미회전초밥')
        우미회전초밥.menu = {'빨간접시': '3000원', '초록접시': '2000원', '우동,메밀소바': '3000원'}
        우미회전초밥.location = '서울 중구 퇴계로 397 1층'
        self.충무아트센터_list.append(우미회전초밥)

        # 양식
        루레스토랑 = Restaurunt('루레스토랑')
        루레스토랑.menu = {'새우, 관자 크림 파스타': '17000원', '가지 라구 파스타': '17000원', '고르곤졸라': '16500원'}
        루레스토랑.location = '서울 중구 퇴계로 387 충무아트홀 1층 루레스토랑'
        self.충무아트센터_list.append(루레스토랑)

        오차드1974 = Restaurunt('오차드1974')
        오차드1974.menu = {'엔쵸비 오일 파스타': '16500원', '모듬 버섯 스테이크 샐러드': '20500원', '스테이크 크림 리조또': '18500원'}
        오차드1974.location = '서울 중구 퇴계로 373-1'
        self.충무아트센터_list.append(오차드1974)

        올댓피자 = Restaurunt('올댓피자')
        올댓피자.menu = {'올댓버거피자(11인치)': '28000원', '어벤져스(11인치)': '25000원', '올댓 쉬림프(11인치)': '24000원'}
        올댓피자.location = '서울 중구 다산로40길 15'
        self.충무아트센터_list.append(올댓피자)

        # 기타
        포그린 = Restaurunt('포그린 pho green')
        포그린.menu = {'반쎼오': '16000원', '세숫대야월남쌈': '36000원', '양지쌀국수(S)': '10000원'}
        포그린.location = '서울 중구 다산로35길 11'
        self.충무아트센터_list.append(포그린)

        또르띠 = Restaurunt('또르띠')
        또르띠.menu = {'CHICKEN 치킨브리또': '9000원', 'VEGAN 비건브리또': '7000원', 'BEEF 비프브리또': '10500원'}
        또르띠.location = '서울 중구 다산로36길 15 1층또르띠'
        self.충무아트센터_list.append(또르띠)

        하노이별 = Restaurunt('하노이별')
        하노이별.menu = {'쌀국수(홍두깨,양지차돌,우목심)': '8000원', '하노이국밥': '8500원', '참숯돼지파인덮밥': '8500원'}
        하노이별.location = '서울 중구 다산로40길 18 1층 하노이별'
        self.충무아트센터_list.append(하노이별)

        # 디저트
        배우세상 = Restaurunt('Cafe배우세상')
        배우세상.menu = {'에스프레소': '3500원', '청포도스무디': '6400원', '핑크레몬에이드': '5400원'}
        배우세상.location = '서울 중구 퇴계로75길 11'
        self.충무아트센터_list.append(배우세상)

        북해빙수 = Restaurunt('북해빙수')
        북해빙수.menu = {'눈꽃우유빙수': '6500원', '카페드사이공': '5500원', '커피빙수': '7000원'}
        북해빙수.location = '서울 중구 다산로47길 28'
        self.충무아트센터_list.append(북해빙수)

        카페우드 = Restaurunt('카페우드')
        카페우드.menu = {'아메리카노 HOT': '2500원', '카페라떼 HOT': '3000원', '카페모카 HOT': '3200원'}
        카페우드.location = '서울 중구 퇴계로 373-3 1층 카페우드'
        self.충무아트센터_list.append(카페우드)


    def str_충무아트센터(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.충무아트센터_list[i].name}\n위치: {self.충무아트센터_list[i].location}\n메뉴: {self.충무아트센터_list[i].menu}\n별점: {self.충무아트센터_list[i].star}\n후기: {self.충무아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_충무아트센터()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.충무아트센터_list[i].name}\n위치: {self.충무아트센터_list[i].location}\n메뉴: {self.충무아트센터_list[i].menu}\n별점: {self.충무아트센터_list[i].star}\n후기: {self.충무아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_충무아트센터()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.충무아트센터_list[i].name}\n위치: {self.충무아트센터_list[i].location}\n메뉴: {self.충무아트센터_list[i].menu}\n별점: {self.충무아트센터_list[i].star}\n후기: {self.충무아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_충무아트센터()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.충무아트센터_list[i].name}\n위치: {self.충무아트센터_list[i].location}\n메뉴: {self.충무아트센터_list[i].menu}\n별점: {self.충무아트센터_list[i].star}\n후기: {self.충무아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_충무아트센터()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.충무아트센터_list[i].name}\n위치: {self.충무아트센터_list[i].location}\n메뉴: {self.충무아트센터_list[i].menu}\n별점: {self.충무아트센터_list[i].star}\n후기: {self.충무아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_충무아트센터()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.충무아트센터_list[i].name}\n위치: {self.충무아트센터_list[i].location}\n메뉴: {self.충무아트센터_list[i].menu}\n별점: {self.충무아트센터_list[i].star}\n후기: {self.충무아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_충무아트센터()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_충무아트센터(self):
        for i in range(18):
            print(f'{i + 1}. {self.충무아트센터_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.충무아트센터_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.충무아트센터_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.충무아트센터_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.충무아트센터_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.충무아트센터_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.충무아트센터_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.충무아트센터_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.충무아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.충무아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.충무아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.충무아트센터_list[int(restaurunt_num) - 1].star}\n후기: {self.충무아트센터_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.충무아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.충무아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.충무아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.충무아트센터_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_충무아트센터()


    def 한전아트센터(self):
        # 한식
        김치실록 = Restaurunt('김치실록 서초본점')
        김치실록.menu = {'통고기김치찌개': '9000원', '꽁치김치찌개': '7000원', '참치김치찌개': '7000원'}
        김치실록.location = '서울 서초구 강남대로37길 60 연화빌딩'
        self.한전아트센터_list.append(김치실록)

        보글이 = Restaurunt('보글이 생태탕왕코다리 서초구청점')
        보글이.menu = {'생태매운탕/맑은탕': '13000원', '해물철판': '45000원', '동태탕': '7000원'}
        보글이.location = '서울 서초구 강남대로37길 56-18 서초에메랄드빌딩 1층'
        self.한전아트센터_list.append(보글이)

        가마솥과청국장 = Restaurunt('가마솥과청국장')
        가마솥과청국장.menu = {'가마솥청국장': '8000원', '가마솥비지장': '8000원', '김치찌개': '7000원'}
        가마솥과청국장.location = '서울 서초구 강남대로37길 54 동경빌딩'
        self.한전아트센터_list.append(가마솥과청국장)

        # 중식
        연화산 = Restaurunt('연화산')
        연화산.menu = {'짜장면': '7000원', '삼선짬뽕': '9000원', '탕수육': '25000원'}
        연화산.location = '서울 서초구 효령로72길 15'
        self.한전아트센터_list.append(연화산)

        난랑 = Restaurunt('난랑')
        난랑.menu = {'생등심탕수육': '24000원', '짜장면': '7000원', '해물짬뽕': '9000원'}
        난랑.location = '서울 서초구 서운로 32 우진빌딩 1층'
        self.한전아트센터_list.append(난랑)

        도화 = Restaurunt('도화')
        도화.menu = {'중국냉면': '10000원', '짜장': '7000원', '해물짬뽕': '10000원'}
        도화.location = '서울 서초구 서운로6길 22'
        self.한전아트센터_list.append(도화)

        # 일식
        츠바키 = Restaurunt('츠바키')
        츠바키.menu = {'돈까스': '9000원', '돈까스카레': '9000원', '가츠동': '9000원'}
        츠바키.location = '서울 서초구 강남대로37길 56-6'
        self.한전아트센터_list.append(츠바키)

        우나유 = Restaurunt('우나유')
        우나유.menu = {'히츠마부시': '33000원', '우나동': '44000원', '모듬튀김': '18000원'}
        우나유.location = '서울 서초구 서운로11길 35 1층'
        self.한전아트센터_list.append(우나유)

        진스시 = Restaurunt('진스시')
        진스시.menu = {'저녁코스 A': '33000원', '저녁코스 B': '39000원', '저녁코스 C': '60000원'}
        진스시.location = '서울 서초구 강남대로43길 22-2'
        self.한전아트센터_list.append(진스시)

        # 양식
        크라이치즈버거 = Restaurunt('크라이치즈버거 양재역점')
        크라이치즈버거.menu = {'치즈버거': '3200원', '더블치즈버거': '4400원', '감자튀김': '2000원'}
        크라이치즈버거.location = '서울 서초구 강남대로41길 8 크라이치즈버거'
        self.한전아트센터_list.append(크라이치즈버거)

        이올로화덕피자 = Restaurunt('이올로화덕피자')
        이올로화덕피자.menu = {'꽈트로 포르마지': '18000원', '페스카토레': '13000원', '화덕 팬 파스타': '13000원'}
        이올로화덕피자.location = '서울 서초구 강남대로39길 5 서초동두산위브'
        self.한전아트센터_list.append(이올로화덕피자)

        바스버거 = Restaurunt('바스버거 양재점')
        바스버거.menu = {'탐욕버거': '11800원', '바스버거': '6300원', '하와이안버거': '7700원'}
        바스버거.location = '서울 서초구 서운로6길 19 1층'
        self.한전아트센터_list.append(바스버거)

        # 기타
        주박사쌀국수 = Restaurunt('주박사쌀국수')
        주박사쌀국수.menu = {'사태양지쌀국수': '8500원', '그릴불고기쌀국수': '12500원', '주박사분짜': '14000원'}
        주박사쌀국수.location = '서울 서초구 남부순환로347길 28 반도빌딩 1층'
        self.한전아트센터_list.append(주박사쌀국수)

        태국식당356 = Restaurunt('태국식당356')
        태국식당356.menu = {'똠양꿍': '14000원', '팟타이꿍': '9000원', '뿌팟봉커리': '24000원'}
        태국식당356.location = '서울 서초구 남부순환로356길 50 2층'
        self.한전아트센터_list.append(태국식당356)

        에머이 = Restaurunt('에머이 양재역점')
        에머이.menu = {'양지 쌀국수': '9800원', '분짜': '15000원', '불고기 쌀국수': '12000원'}
        에머이.location = '서울 강남구 강남대로 242 1층'
        self.한전아트센터_list.append(에머이)

        # 디저트
        데카치노 = Restaurunt('데카치노')
        데카치노.menu = {'아메리카노': '3800원', '카푸치노': '4300원', '카페 라떼': '4300원'}
        데카치노.location = '서울 서초구 서운로 26'
        self.한전아트센터_list.append(데카치노)

        파브리끄 = Restaurunt('파브리끄 양재점')
        파브리끄.menu = {'아메리카노': '3500원', '카페라떼': '4500원', '핸드드립': '5000원'}
        파브리끄.location = '서울 서초구 서운로6길 25'
        self.한전아트센터_list.append(파브리끄)

        브룸 = Restaurunt('브룸 커피')
        브룸.menu = {'에스프레소': '3500원', '아메리카노': '4000원', '바닐라라떼': '5800원'}
        브룸.location = '서울 서초구 남부순환로347길 101 1층 101호'
        self.한전아트센터_list.append(브룸)


    def str_한전아트센터(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.한전아트센터_list[i].name}\n위치: {self.한전아트센터_list[i].location}\n메뉴: {self.한전아트센터_list[i].menu}\n별점: {self.한전아트센터_list[i].star}\n후기: {self.한전아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_한전아트센터()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.한전아트센터_list[i].name}\n위치: {self.한전아트센터_list[i].location}\n메뉴: {self.한전아트센터_list[i].menu}\n별점: {self.한전아트센터_list[i].star}\n후기: {self.한전아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_한전아트센터()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.한전아트센터_list[i].name}\n위치: {self.한전아트센터_list[i].location}\n메뉴: {self.한전아트센터_list[i].menu}\n별점: {self.한전아트센터_list[i].star}\n후기: {self.한전아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_한전아트센터()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.한전아트센터_list[i].name}\n위치: {self.한전아트센터_list[i].location}\n메뉴: {self.한전아트센터_list[i].menu}\n별점: {self.한전아트센터_list[i].star}\n후기: {self.한전아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_한전아트센터()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.한전아트센터_list[i].name}\n위치: {self.한전아트센터_list[i].location}\n메뉴: {self.한전아트센터_list[i].menu}\n별점: {self.한전아트센터_list[i].star}\n후기: {self.한전아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_한전아트센터()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.한전아트센터_list[i].name}\n위치: {self.한전아트센터_list[i].location}\n메뉴: {self.한전아트센터_list[i].menu}\n별점: {self.한전아트센터_list[i].star}\n후기: {self.한전아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_한전아트센터()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_한전아트센터(self):
        for i in range(18):
            print(f'{i + 1}. {self.한전아트센터_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.한전아트센터_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.한전아트센터_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.한전아트센터_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.한전아트센터_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.한전아트센터_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.한전아트센터_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.한전아트센터_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.한전아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.한전아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.한전아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.한전아트센터_list[int(restaurunt_num) - 1].star}\n후기: {self.한전아트센터_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.한전아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.한전아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.한전아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.한전아트센터_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_한전아트센터()


    def 극장용(self):
        # 한식
        솜씨 = Restaurunt('솜씨 이촌')
        솜씨.menu = {'육전': '9000원', '매콤낚지볶음과 소면': '32000원', '생선튀김(농어)': '49000원'}
        솜씨.location = '서울 용산구 이촌로65가길 78'
        self.극장용_list.append(솜씨)

        정 = Restaurunt('정 한뿌리죽 본점')
        정.menu = {'삼계죽': '18000원', '제주식 전복죽': '21000원', '전복 미역죽': '18000원'}
        정.location = '서울 용산구 이촌로 245 로얄상가 2층 (202호)'
        self.극장용_list.append(정)

        봉피양 = Restaurunt('봉피양 용산점')
        봉피양.menu = {'벽제설렁탕': '16000원', '한우양곰탕': '18000원', '한우곰탕': '17000원'}
        봉피양.location = '서울 용산구 한강대로40길 31'
        self.극장용_list.append(봉피양)

        # 중식
        야래향 = Restaurunt('야래향')
        야래향.menu = {'삼선짜장면': '7000원', '광동식 하얀짬뽕': '9000원', '춘권': '8000원'}
        야래향.location = '서울 용산구 이촌로75길 22-5'
        self.극장용_list.append(야래향)

        일일향 = Restaurunt('일일향 신용산7호점')
        일일향.menu = {'짜장면': '7000원', '옛날짬뽕': '8000원', '육즙 돼지고기 탕수육': '28000원'}
        일일향.location = '서울 용산구 한강대로40길 26 2층'
        self.극장용_list.append(일일향)

        중화객잔 = Restaurunt('중화객잔 수')
        중화객잔.menu = {'롤멘보샤(2인용)': '25000원', '갈린빈새우': '35000원', '중화국밥': '10000원'}
        중화객잔.location = '서울 용산구 한강대로48길 17-6 1층'
        self.극장용_list.append(중화객잔)

        # 일식
        봉린 = Restaurunt('봉린')
        봉린.menu = {'치킨가라아게': '17000원', '나가사키짬뽕': '17000원', '탄탄멘': '13000원'}
        봉린.location = '서울 용산구 이촌로77길 19 이촌종합상가'
        self.극장용_list.append(봉린)

        아지겐 = Restaurunt('아지겐')
        아지겐.menu = {'게살오믈렛': '28000원', '두부튀김': '9000원', '카타야끼소바': '17000원'}
        아지겐.location = '서울 용산구 이촌로75길 22'
        self.극장용_list.append(아지겐)

        후스시 = Restaurunt('후스시')
        후스시.menu = {'초밥특선': '17000원', '모듬스시(12pcs)': '24000원', '종모듬스시(12pcs)': '24000원'}
        후스시.location = '서울 용산구 이촌로 245 로얄상가 201호'
        self.극장용_list.append(후스시)

        # 양식
        작은식당 = Restaurunt('작은식당 마당')
        작은식당.menu = {'수제 통살 치킨 버거': '9000원', '더블트러블': '12000원', '심플': '8000원'}
        작은식당.location = '서울 용산구 서빙고로 137'
        self.극장용_list.append(작은식당)

        르미야 = Restaurunt('르미야')
        르미야.menu = {'쇼가야끼카레': '10900원', '와인비프카레': '11900원', '명란크림파스타': '13900원'}
        르미야.location = '서울 용산구 이촌로77길 19 1층 르미야'
        self.극장용_list.append(르미야)

        키친아이 = Restaurunt('키친아이')
        키친아이.menu = {'지팡구샐러드': '15000원', '버섯현미리조또': '18000원', '안심스테이크 180g': '39000원'}
        키친아이.location = '서울 용산구 이촌로 248 31동 상가 204호'
        self.극장용_list.append(키친아이)

        # 기타
        쏭타이치앙마이 = Restaurunt('쏭타이치앙마이')
        쏭타이치앙마이.menu = {'팟타이꿍 Shrimp Pad Thai': '13000원', '팟카파오무쌉 Pad kapao Moo Sab': '13000원', '똠얌누들 Tom Yum with Rice Noodle': '8900원'}
        쏭타이치앙마이.location = '서울 용산구 한강대로40길 39-5 1층 쏭타이치앙마이'
        self.극장용_list.append(쏭타이치앙마이)

        바토스 = Restaurunt('바토스 이태원점')
        바토스.menu = {'허니 테킬라 윙즈': '7900원', '스윗 바비큐 윙즈': '7900원', '신선한 과카몰리와 칩스': '24000원'}
        바토스.location = '서울 용산구 이태원로15길 1 2층'
        self.극장용_list.append(바토스)

        PETRA = Restaurunt('PETRA')
        PETRA.menu = {'바바가누즈': '8000원', '라바네흐': '7000원 ~ 1100원', '미자': '11000원'}
        PETRA.location = '서울 용산구 녹사평대로40길 33 2층'
        self.극장용_list.append(PETRA)

        # 디저트
        동빙고 = Restaurunt('동빙고')
        동빙고.menu = {'단팥죽': '7000원', '팥빙수': '7000원', '딸기빙수': '7500원'}
        동빙고.location = '서울 용산구 이촌로65가길 78'
        self.극장용_list.append(동빙고)

        헤븐온탑 = Restaurunt('헤븐온탑 동부이촌동')
        헤븐온탑.menu = {'빅토리아 케이크': '33000원 ~ 55000원', '헤븐 플레이트': '12900원', '후르츠 에그헴 샌드위치': '6500원'}
        헤븐온탑.location = '서울 용산구 이촌로 264 삼익아파트 상가동 1층 102호'
        self.극장용_list.append(헤븐온탑)

        키에리 = Restaurunt('키에리')
        키에리.menu = {'아메리카노': '4900원', '콘크럼블치즈케이크': '9500원', '뽕베리레이어드치즈케이크': '9500원'}
        키에리.location = '서울 용산구 이태원로26길 16-8 1층'
        self.극장용_list.append(키에리)


    def str_극장용(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.극장용_list[i].name}\n위치: {self.극장용_list[i].location}\n메뉴: {self.극장용_list[i].menu}\n별점: {self.극장용_list[i].star}\n후기: {self.극장용_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_극장용()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.극장용_list[i].name}\n위치: {self.극장용_list[i].location}\n메뉴: {self.극장용_list[i].menu}\n별점: {self.극장용_list[i].star}\n후기: {self.극장용_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_극장용()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.극장용_list[i].name}\n위치: {self.극장용_list[i].location}\n메뉴: {self.극장용_list[i].menu}\n별점: {self.극장용_list[i].star}\n후기: {self.극장용_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_극장용()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.극장용_list[i].name}\n위치: {self.극장용_list[i].location}\n메뉴: {self.극장용_list[i].menu}\n별점: {self.극장용_list[i].star}\n후기: {self.극장용_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_극장용()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.극장용_list[i].name}\n위치: {self.극장용_list[i].location}\n메뉴: {self.극장용_list[i].menu}\n별점: {self.극장용_list[i].star}\n후기: {self.극장용_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_극장용()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.극장용_list[i].name}\n위치: {self.극장용_list[i].location}\n메뉴: {self.극장용_list[i].menu}\n별점: {self.극장용_list[i].star}\n후기: {self.극장용_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_극장용()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_극장용(self):
        for i in range(18):
            print(f'{i + 1}. {self.극장용_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.극장용_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.극장용_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.극장용_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.극장용_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.극장용_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.극장용_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.극장용_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.극장용_list[int(restaurunt_num) - 1].name}\n위치: {self.극장용_list[int(restaurunt_num) - 1].location}\n메뉴: {self.극장용_list[int(restaurunt_num) - 1].menu}\n별점: {self.극장용_list[int(restaurunt_num) - 1].star}\n후기: {self.극장용_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.극장용_list[int(restaurunt_num) - 1].name}\n위치: {self.극장용_list[int(restaurunt_num) - 1].location}\n메뉴: {self.극장용_list[int(restaurunt_num) - 1].menu}\n별점: {self.극장용_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_극장용()


    def 두산아트센터(self):
        # 한식
        박가네 = Restaurunt('박가네 육회')
        박가네.menu = {'육회김밥': '9000원', '육회탕탕이': '28000원', '육회': '15000원'}
        박가네.location = '서울 종로구 종로32길 9'
        self.두산아트센터_list.append(박가네)

        을지면옥 = Restaurunt('을지면옥')
        을지면옥.menu = {'냉면': '12000원', '비빔냉면': '12000원', '편육': '24000원'}
        을지면옥.location = '서울 중구 충무로14길 2-1'
        self.두산아트센터_list.append(을지면옥)

        순미네행복게장 = Restaurunt('순미네행복게장 동대문점')
        순미네행복게장.menu = {'간장게장 알베기': '37000원', '간장게장 숫게2마리': '27000원', '양념게장': '25000원'}
        순미네행복게장.location = '서울 중구 을지로43길 38 3층 순미네행복게장'
        self.두산아트센터_list.append(순미네행복게장)

        # 중식
        전설의짬뽕 = Restaurunt('전설의짬뽕 종로5가점')
        전설의짬뽕.menu = {'홍합해물짬뽕': '7000원', '짜장면': '5000원', '삼선짬뽕': '9000원'}
        전설의짬뽕.location = '서울 종로구 대학로 18'
        self.두산아트센터_list.append(전설의짬뽕)

        진양양꼬치 = Restaurunt('진양양꼬치')
        진양양꼬치.menu = {'특갈비': '2500원', '새우구이': '12000원', '베토구이': '12000원'}
        진양양꼬치.location = '서울 종로구 종로35길 33'
        self.두산아트센터_list.append(진양양꼬치)

        야래향 = Restaurunt('야래향')
        야래향.menu = {'쟁반짜장면': '9000원', '차돌짬뽕': '9000원', '짜장면': '5500원'}
        야래향.location = '서울 종로구 김상옥로 3'
        self.두산아트센터_list.append(야래향)

        # 일식
        나지라멘 = Restaurunt('나지라멘')
        나지라멘.menu = {'돈코츠라멘': '9000원', '쇼유라멘': '9000원', '미니차슈동': '5000원'}
        나지라멘.location = '서울 종로구 대학로1길 34 지하 1층'
        self.두산아트센터_list.append(나지라멘)

        에페 = Restaurunt('에페')
        에페.menu = {'수제안심돈까스': '10000원', '새우튀김생면우동': '8000원', '수제치즈돈까스': '9500원'}
        에페.location = '서울 종로구 종로31길 31 1층'
        self.두산아트센터_list.append(에페)

        연어가 = Restaurunt('연어가 생각날 때')
        연어가.menu = {'S스페셜연어덮밥': '13000원', '생연어덮밥': '7000원', '불연어덮밥': '7000원'}
        연어가.location = '서울 종로구 종로31가길 9'
        self.두산아트센터_list.append(연어가)

        # 양식
        바스타 = Restaurunt('바스타')
        바스타.menu = {'콩나물 바지락 모시 술국': '22000원', '스파이시 칼라마리': '16000원', '뽀모도르': '11000원'}
        바스타.location = '서울 종로구 대학로1길 34-7 1층'
        self.두산아트센터_list.append(바스타)

        지금 = Restaurunt('지금 여기가 맨 앞')
        지금.menu = {'크림 리조또 ': '9000원', '베지터블': '16000원', '북어 알리오 올리오 Non(논비건)': '12000원'}
        지금.location = '서울 중구 을지로20길 16 3층'
        self.두산아트센터_list.append(지금)

        육육간 = Restaurunt('육육간')
        육육간.menu = {'찹 스테이크': '12900원', '부채살 스테이크': '15900원', '눈꽃함박 스테이크': '10900원'}
        육육간.location = '서울 종로구 창경궁로16길 16 1층 육육간 종로점'
        self.두산아트센터_list.append(육육간)

        # 기타
        사마르칸트 = Restaurunt('사마르칸트')
        사마르칸트.menu = {'양고기 샤슬릭': '6000원', '프러프 전통 볶음밥': '10900원', '만티(5개)': '11900원'}
        사마르칸트.location = '서울 중구 마른내로 159-21'
        self.두산아트센터_list.append(사마르칸트)

        반포식스 = Restaurunt('반포식스 종로5가점')
        반포식스.menu = {'푸 팟 퐁커리': '28000원', '크림새우': '25000원', '베트남식 유린기': '20000원'}
        반포식스.location = '서울 종로구 창경궁로 120 종로 플레이스빌딩 1층'
        self.두산아트센터_list.append(반포식스)

        포베이 = Restaurunt('포베이 동대문종합시장점')
        포베이.menu = {'A1 짜조': '4500원', 'A2 썸머롤': '5000원', 'A3 짜조&웨딩쇼마이': '4500원'}
        포베이.location = '서울 종로구 종로 266 B동 6층 B6010, B6011호'
        self.두산아트센터_list.append(포베이)

        # 디저트
        모노치즈 = Restaurunt('모노치즈 종로5가점')
        모노치즈.menu = {'아메리카노': '1500원', '카페라떼': '2500원', '크림치즈베이글': '4500원'}
        모노치즈.location = '서울 종로구 종로 213-1 1층 모노치즈 종로5가점'
        self.두산아트센터_list.append(모노치즈)

        두채 = Restaurunt('두채')
        두채.menu = {'통밀호두빵': '4800원', '플레인스콘': '4000원', '카페 데 올로로소': '7000원'}
        두채.location = '서울 종로구 율곡로13가길 8 베이커리카페 두채'
        self.두산아트센터_list.append(두채)

        구움양과 = Restaurunt('구움양과')
        구움양과.menu = {'오리지날 타히티 바닐라 까눌레': '2500원', '밀크티 까눌레': '2600원', '바닐라 빈 & 고메 마들렌': '2600원'}
        구움양과.location = '서울 중구 을지로 157 대림상가 3층 라열 351호'
        self.두산아트센터_list.append(구움양과)


    def str_두산아트센터(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.두산아트센터_list[i].name}\n위치: {self.두산아트센터_list[i].location}\n메뉴: {self.두산아트센터_list[i].menu}\n별점: {self.두산아트센터_list[i].star}\n후기: {self.두산아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_두산아트센터()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.두산아트센터_list[i].name}\n위치: {self.두산아트센터_list[i].location}\n메뉴: {self.두산아트센터_list[i].menu}\n별점: {self.두산아트센터_list[i].star}\n후기: {self.두산아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_두산아트센터()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.두산아트센터_list[i].name}\n위치: {self.두산아트센터_list[i].location}\n메뉴: {self.두산아트센터_list[i].menu}\n별점: {self.두산아트센터_list[i].star}\n후기: {self.두산아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_두산아트센터()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.두산아트센터_list[i].name}\n위치: {self.두산아트센터_list[i].location}\n메뉴: {self.두산아트센터_list[i].menu}\n별점: {self.두산아트센터_list[i].star}\n후기: {self.두산아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_두산아트센터()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.두산아트센터_list[i].name}\n위치: {self.두산아트센터_list[i].location}\n메뉴: {self.두산아트센터_list[i].menu}\n별점: {self.두산아트센터_list[i].star}\n후기: {self.두산아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_두산아트센터()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.두산아트센터_list[i].name}\n위치: {self.두산아트센터_list[i].location}\n메뉴: {self.두산아트센터_list[i].menu}\n별점: {self.두산아트센터_list[i].star}\n후기: {self.두산아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_두산아트센터()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_두산아트센터(self):
        for i in range(18):
            print(f'{i + 1}. {self.두산아트센터_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.두산아트센터_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.두산아트센터_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.두산아트센터_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.두산아트센터_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.두산아트센터_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.두산아트센터_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.두산아트센터_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.두산아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.두산아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.두산아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.두산아트센터_list[int(restaurunt_num) - 1].star}\n후기: {self.두산아트센터_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.두산아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.두산아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.두산아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.두산아트센터_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_두산아트센터()


    def 명동예술극장(self):
        # 한식
        명동교자 = Restaurunt('명동교자 본점')
        명동교자.menu = {'칼국수': '9000원', '만두': '10000원', '비빔국수': '9000원'}
        명동교자.location = '서울 중구 명동10길 29'
        self.명동예술극장_list.append(명동교자)

        하동관명동본점 = Restaurunt('하동관명동본점')
        하동관명동본점.menu = {'곰탕': '13000원', '수육(중)': '30000원', '20공 곰탕': '20000원'}
        하동관명동본점.location = '서울 중구 명동9길 12'
        self.명동예술극장_list.append(하동관명동본점)

        청와옥 = Restaurunt('청와옥 을지로3가직영점')
        청와옥.menu = {'순대국밥': '8000원', '찹쌀순대': '19000원', '순대정식': '12000원'}
        청와옥.location = '서울 중구 을지로 110 1층 1호'
        self.명동예술극장_list.append(청와옥)

        # 중식
        루이키친M = Restaurunt('루이키친M')
        루이키친M.menu = {'삼선짜장면': '10000원', '삼선짬뽕': '13000원', '팔진탕면': '15000원'}
        루이키친M.location = '서울 중구 태평로1가 61-21'
        self.명동예술극장_list.append(루이키친M)

        란주라미엔 = Restaurunt('란주라미엔')
        란주라미엔.menu = {'동파육': '35000원', '와사비크림새우': '35000원', '깐풍동고': '35000원'}
        란주라미엔.location = '서울 강남구 테헤란로114길 30'
        self.명동예술극장_list.append(란주라미엔)

        유유안 = Restaurunt('포시즌스호텔서울 유유안')
        유유안.menu = {'중식 딤섬 세트': '70000원', '북경식 오리 반마리': '80000원', '석식세트A': '16000원'}
        유유안.location = '서울 종로구 새무안로 97 11층'
        self.명동예술극장_list.append(유유안)

        # 일식
        명동돈가스 = Restaurunt('명동돈가스')
        명동돈가스.menu = {'로스가스': '14000원', '히레가스': '15000원', '생선가스': '13000원'}
        명동돈가스.location = '서울 중구 명동3길 8'
        self.명동예술극장_list.append(명동돈가스)

        스시조 = Restaurunt('웨스틴조선호텔 스시조')
        스시조.menu = {'조식(Room)': '65000원 ~ 120000원', '런치(Hall)': '124000원 ~ 180000원', '디너(Hall)': '156000원 ~ 300000원'}
        스시조.location = '서울 중구 소공로 106'
        self.명동예술극장_list.append(스시조)

        동해도 = Restaurunt('동해도 광화문점')
        동해도.menu = {'회전초밥뷔페(성인)평일': '25800원', '사시미&해산물 코스요리': '65000원', '정통일식 코스요리': '52000원'}
        동해도.location = '서울 중구 무교로 28 시그너스빌딩 지하1층 동해도'
        self.명동예술극장_list.append(동해도)

        # 양식
        마르셀 = Restaurunt('마르셀 광화문점')
        마르셀.menu = {'라구 소스와 잘 구운 가지로 감싼 ‘가지라자냐’': '23000원', '트러플풍미의 버섯크림 빠르델레': '23000원', '프렌치스타일 대파풍미의 스프': '15000원'}
        마르셀.location = '서울 중구 청계천로 8 1층'
        self.명동예술극장_list.append(마르셀)

        메이드인시카고피자 = Restaurunt('메이드인시카고피자 덕수궁점')
        메이드인시카고피자.menu = {'시카고 치즈 피자': '12000원', '시카고 페퍼로니 피자': '14000원', '시카고 고구마 피자': '14000원'}
        메이드인시카고피자.location = '서울 중구 덕수궁길 5'
        self.명동예술극장_list.append(메이드인시카고피자)

        스패뉴 = Restaurunt('스패뉴')
        스패뉴.menu = {'새우크림': '17900원', '고구마 샐러드 피자': '20900원', '등심 스테이크': '30900원'}
        스패뉴.location = '서울 중구 세종대로 82 2층 스패뉴'
        self.명동예술극장_list.append(스패뉴)

        # 기타
        감성타코 = Restaurunt('감성타코 광화문점')
        감성타코.menu = {'까르니따스 치즈 타코': '9000원', '자메이카 저크 치킨 타코': '9000원', '메콩타이 스페셜세트': '14000원'}
        감성타코.location = '서울 종로구 새문안로3길 23 경희궁의 아침 4단지 지하1층'
        self.명동예술극장_list.append(감성타코)

        엘쁠라또 = Restaurunt('엘쁠라또')
        엘쁠라또.menu = {'시그니처 가지구이': '13500원', '굴튀김, 아도보 소스': '10000원', '문어 스테이크': '33000원'}
        엘쁠라또.location = '서울 중구 세종대로 136 서울파이낸스센터'
        self.명동예술극장_list.append(엘쁠라또)

        엘꾸비또 = Restaurunt('엘 꾸비또')
        엘꾸비또.menu = {'오징어 먹물 빠에야': '28000원', '이베리코 하몽': '29000원', '오징어튀김(디너)': '14000원'}
        엘꾸비또.location = '서울 종로구 새문안로 68 흥국생명빌딩 지하 1층 엘 꾸비또'
        self.명동예술극장_list.append(엘꾸비또)

        # 디저트
        언톨드 = Restaurunt('언톨드 스위츠')
        언톨드.menu = {'샤인 머스켓 밀크티': '9000원', '아메리카노': '4000원', '카페라떼': '4500원'}
        언톨드.location = '서울 중구 남대문로 68-1 1층'
        self.명동예술극장_list.append(언톨드)

        카카오그린 = Restaurunt('카카오그린')
        카카오그린.menu = {'트리플초콜렛빙수': '11800원', '블러디스트로베리빙수': '12800원', '무지방요거트': '5800원'}
        카카오그린.location = '서울 중구 명동8길 14'
        self.명동예술극장_list.append(카카오그린)

        카페마마스 = Restaurunt('카페마마스 센터원점')
        카페마마스.menu = {'리코타 샐러드': '14500원', '클럽샌드위치': '11800원', '쇠고기가지 파니니': '13500원'}
        카페마마스.location = '서울 중구 을지로5길 26 미래에셋센터원빌딩 1F'
        self.명동예술극장_list.append(카페마마스)


    def str_명동예술극장(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.명동예술극장_list[i].name}\n위치: {self.명동예술극장_list[i].location}\n메뉴: {self.명동예술극장_list[i].menu}\n별점: {self.명동예술극장_list[i].star}\n후기: {self.명동예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_명동예술극장()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.명동예술극장_list[i].name}\n위치: {self.명동예술극장_list[i].location}\n메뉴: {self.명동예술극장_list[i].menu}\n별점: {self.명동예술극장_list[i].star}\n후기: {self.명동예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_명동예술극장()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.명동예술극장_list[i].name}\n위치: {self.명동예술극장_list[i].location}\n메뉴: {self.명동예술극장_list[i].menu}\n별점: {self.명동예술극장_list[i].star}\n후기: {self.명동예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_명동예술극장()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.명동예술극장_list[i].name}\n위치: {self.명동예술극장_list[i].location}\n메뉴: {self.명동예술극장_list[i].menu}\n별점: {self.명동예술극장_list[i].star}\n후기: {self.명동예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_명동예술극장()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.명동예술극장_list[i].name}\n위치: {self.명동예술극장_list[i].location}\n메뉴: {self.명동예술극장_list[i].menu}\n별점: {self.명동예술극장_list[i].star}\n후기: {self.명동예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_명동예술극장()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.명동예술극장_list[i].name}\n위치: {self.명동예술극장_list[i].location}\n메뉴: {self.명동예술극장_list[i].menu}\n별점: {self.명동예술극장_list[i].star}\n후기: {self.명동예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_명동예술극장()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_명동예술극장(self):
        for i in range(18):
            print(f'{i + 1}. {self.명동예술극장_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.명동예술극장_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.명동예술극장_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.명동예술극장_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.명동예술극장_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.명동예술극장_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.명동예술극장_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.명동예술극장_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.명동예술극장_list[int(restaurunt_num) - 1].name}\n위치: {self.명동예술극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.명동예술극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.명동예술극장_list[int(restaurunt_num) - 1].star}\n후기: {self.명동예술극장_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.명동예술극장_list[int(restaurunt_num) - 1].name}\n위치: {self.명동예술극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.명동예술극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.명동예술극장_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_명동예술극장()


    def 홍익대아트센터(self):
        # 한식
        고궁의아침 = Restaurunt('고궁의아침')
        고궁의아침.menu = {'한우불고기': '18000원', '불낙전골': '14000원', '곱창전골': '14000원'}
        고궁의아침.location = '서울 종로구 창경궁로 158'
        self.홍익대아트센터_list.append(고궁의아침)

        모티집 = Restaurunt('모티집')
        모티집.menu = {'쟁반막국수(2인이상)': '11000원', '두루치기(소)': '25000원', '돼지수육(소)': '14000원'}
        모티집.location = '서울 종로구 이화장2길 1 모티집'
        self.홍익대아트센터_list.append(모티집)

        이화김치찌개 = Restaurunt('이화김치찌개')
        이화김치찌개.menu = {'김치찌개': '7000원', '계란말이 대': '6000원', '참치김치찌개': '7000원'}
        이화김치찌개.location = '서울 종로구 율곡로 216'
        self.홍익대아트센터_list.append(이화김치찌개)

        # 중식
        국빈 = Restaurunt('국빈')
        국빈.menu = {'볶음밥': '5000원', '짬뽕': '4500원', '자장면': '4000원'}
        국빈.location = '서울 종로구 대학로 53'
        self.홍익대아트센터_list.append(국빈)

        위례성 = Restaurunt('위례성')
        위례성.menu = {'쟁반짜장': '13000원', '볶음밥': '6000원', '해물짬뽕': '6000원'}
        위례성.location = '서울 종로구 대학로5길 10'
        self.홍익대아트센터_list.append(위례성)

        중화요리지엔 = Restaurunt('중화요리지엔')
        중화요리지엔.menu = {'해물짬뽕': '9000원', '마파가지밥': '8000원', '새우볶음밥': '9000원'}
        중화요리지엔.location = '서울 종로구 율곡로 218 중화요리지엔'
        self.홍익대아트센터_list.append(중화요리지엔)

        # 일식
        교토스시 = Restaurunt('교토스시')
        교토스시.menu = {'연어덮밥': '12000원', '알탕': '11000원', '모듬초밥(13pcs)': '16000원'}
        교토스시.location = '서울 종로구 동숭길 43'
        self.홍익대아트센터_list.append(교토스시)

        토끼정 = Restaurunt('토끼정 대학로점')
        토끼정.menu = {'토끼정 카레': '9300원', '스테이크 덮밥': '13800원', '철판 큐브 스테이크': '16300원'}
        토끼정.location = '서울 종로구 대학로8가길 133'
        self.홍익대아트센터_list.append(토끼정)

        낙원테산도 = Restaurunt('낙원테산도 혜화점')
        낙원테산도.menu = {'타마고산도': '8900원', '가츠산도': '9900원', '낙원오믈렛': '11900원'}
        낙원테산도.location = '서울 종로구 대학로11길 43 1층'
        self.홍익대아트센터_list.append(낙원테산도)

        # 양식
        핏제리아오 = Restaurunt('핏제리아오')
        핏제리아오.menu = {'마르게리따': '12000원', '오핏자': '19500원', '스텔라': '29000원'}
        핏제리아오.location = '서울 종로구 동숭길 48'
        self.홍익대아트센터_list.append(핏제리아오)

        카르페가든 = Restaurunt('메이드인시카고피자 덕수궁점')
        카르페가든.menu = {'파스타 세트': '15000원', '샌드위치': '12000원', '샐러드': '14000원'}
        카르페가든.location = '서울 종로구 이화장길 36-2'
        self.홍익대아트센터_list.append(카르페가든)

        혜화동버거 = Restaurunt('혜화동버거')
        혜화동버거.menu = {'도넛 치즈 버거': '11800원', '도넛 치킨 버거': '10800원', '혜화동 치즈 버거': '8800원'}
        혜화동버거.location = '서울 종로구 동숭3길 6-4 1층 혜화동버거'
        self.홍익대아트센터_list.append(혜화동버거)

        # 기타
        베트남노상식당 = Restaurunt('베트남노상식당 혜화점')
        베트남노상식당.menu = {'프리미엄쌀국수': '7900원', '팟타이': '8900원', '닭껍질튀김쌀국수': '8500원'}
        베트남노상식당.location = '서울 종로구 대학로5길 3'
        self.홍익대아트센터_list.append(베트남노상식당)

        이스탄불 = Restaurunt('이스탄불')
        이스탄불.menu = {'케밥샌드위치(버거)': '5800원', '피데(터키 피자)(치킨)': '13000원', '타스 케밥(더키식 덮밥)(소고기)': '8000원'}
        이스탄불.location = '서울 종로구 대학로11길 20 우리빌딩 1층'
        self.홍익대아트센터_list.append(이스탄불)

        깔리 = Restaurunt('깔리')
        깔리.menu = {'탄두리 치킨': '17000원', '양고기 반딜루': '12000원', '야채/달 타드카': '9000원'}
        깔리.location = '서울 종로구 대학로11길 43 명륜4가 171번지 2층'
        self.홍익대아트센터_list.append(깔리)

        # 디저트
        우지커피 = Restaurunt('우지커피')
        우지커피.menu = {'에스프레소': '1500원', '아메리카노': '1500원', '헤이즐넛 아메리카노': '2500원'}
        우지커피.location = '서울 종로구 대학로 85'
        self.홍익대아트센터_list.append(우지커피)

        헤이줄리 = Restaurunt('헤이줄리')
        헤이줄리.menu = {'얼그레이갸또': '5000원', '햄치즈에그샌드위치': '6800원', '아메리카노': '4000원'}
        헤이줄리.location = '서울 종로구 동순라길 108 헤이줄리'
        self.홍익대아트센터_list.append(헤이줄리)

        하이제씨 = Restaurunt('하이제씨')
        하이제씨.menu = {'버터바': '4000원', '마카롱': '2500원', '커피': '4000원'}
        하이제씨.location = '서울 종로구 동숭1길 12'
        self.홍익대아트센터_list.append(하이제씨)


    def str_홍익대아트센터(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.홍익대아트센터_list[i].name}\n위치: {self.홍익대아트센터_list[i].location}\n메뉴: {self.홍익대아트센터_list[i].menu}\n별점: {self.홍익대아트센터_list[i].star}\n후기: {self.홍익대아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_홍익대아트센터()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.홍익대아트센터_list[i].name}\n위치: {self.홍익대아트센터_list[i].location}\n메뉴: {self.홍익대아트센터_list[i].menu}\n별점: {self.홍익대아트센터_list[i].star}\n후기: {self.홍익대아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_홍익대아트센터()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.홍익대아트센터_list[i].name}\n위치: {self.홍익대아트센터_list[i].location}\n메뉴: {self.홍익대아트센터_list[i].menu}\n별점: {self.홍익대아트센터_list[i].star}\n후기: {self.홍익대아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_홍익대아트센터()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.홍익대아트센터_list[i].name}\n위치: {self.홍익대아트센터_list[i].location}\n메뉴: {self.홍익대아트센터_list[i].menu}\n별점: {self.홍익대아트센터_list[i].star}\n후기: {self.홍익대아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_홍익대아트센터()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.홍익대아트센터_list[i].name}\n위치: {self.홍익대아트센터_list[i].location}\n메뉴: {self.홍익대아트센터_list[i].menu}\n별점: {self.홍익대아트센터_list[i].star}\n후기: {self.홍익대아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_홍익대아트센터()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.홍익대아트센터_list[i].name}\n위치: {self.홍익대아트센터_list[i].location}\n메뉴: {self.홍익대아트센터_list[i].menu}\n별점: {self.홍익대아트센터_list[i].star}\n후기: {self.홍익대아트센터_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_홍익대아트센터()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_홍익대아트센터(self):
        for i in range(18):
            print(f'{i + 1}. {self.홍익대아트센터_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.홍익대아트센터_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.홍익대아트센터_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.홍익대아트센터_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.홍익대아트센터_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.홍익대아트센터_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.홍익대아트센터_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.홍익대아트센터_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.홍익대아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.홍익대아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.홍익대아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.홍익대아트센터_list[int(restaurunt_num) - 1].star}\n후기: {self.홍익대아트센터_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.홍익대아트센터_list[int(restaurunt_num) - 1].name}\n위치: {self.홍익대아트센터_list[int(restaurunt_num) - 1].location}\n메뉴: {self.홍익대아트센터_list[int(restaurunt_num) - 1].menu}\n별점: {self.홍익대아트센터_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_홍익대아트센터()


    def 백암상상마당(self):
        # 한식
        목포낙지횟집 = Restaurunt('목포낙지횟집')
        목포낙지횟집.menu = {'연포탕-대': '55000원', '갈치조림': '8000원', '활어회정식': '20000원'}
        목포낙지횟집.location = '서울 강남구 테헤란로107길 12'
        self.백암상상마당_list.append(목포낙지횟집)

        삼성골목집 = Restaurunt('삼성골목집')
        삼성골목집.menu = {'삼겹살': '13000원', '파삼겹살': '15000원', '차돌박이': '15000원'}
        삼성골목집.location = '서울 강남구 테헤란로108길 8 1층 삼성골목집'
        self.백암상상마당_list.append(삼성골목집)

        중앙해장 = Restaurunt('중앙해장')
        중앙해장.menu = {'양선지해장국': '10000원', '내장탕': '13000원', '양지곰탕': '11000원'}
        중앙해장.location = '서울 강남구 영동대로86길 17 육인빌딩'
        self.백암상상마당_list.append(중앙해장)

        # 중식
        동강 = Restaurunt('동강')
        동강.menu = {'짜장': '6500원', '짬뽕': '7500원', '쟁반짜장': '17000원'}
        동강.location = '서울 강남구 테헤란로103길 10'
        self.백암상상마당_list.append(동강)

        요리왕 = Restaurunt('요리왕')
        요리왕.menu = {'동파육': '35000원', '와사비크림새우': '35000원', '깐풍동고': '35000원'}
        요리왕.location = '서울 강남구 테헤란로114길 30'
        self.백암상상마당_list.append(요리왕)

        희래등 = Restaurunt('희래등')
        희래등.menu = {'짜장': '7000원', '짬뽕': '8000원', '간짜장': '8000원'}
        희래등.location = '서울 강남구 테헤란로108길 15'
        self.백암상상마당_list.append(희래등)

        # 일식
        김셰프의도시어부 = Restaurunt('김셰프의도시어부')
        김셰프의도시어부.menu = {'정식': '25000원', '특정식': '35000원', '생선초밥': '25000원'}
        김셰프의도시어부.location = '서울 강남구 테헤란로 614 슈페리어사옥'
        self.백암상상마당_list.append(김셰프의도시어부)

        유키즈시 = Restaurunt('유키즈시')
        유키즈시.menu = {'런치 니기리 1인': '60000원', '디너': '130000원', '키타야 토쿠베츠준마이 유메잇콘': '75000원'}
        유키즈시.location = '서울 강남구 영동대로86길 17 육인빌딩 지하 1층'
        self.백암상상마당_list.append(유키즈시)

        록스플레이트 = Restaurunt('록스플레이트')
        록스플레이트.menu = {'큐브스테이크 덮밥': '10000원', '모듬까스 덮밥': '9000원', '얼큰 탄탄멘': '8000원'}
        록스플레이트.location = '서울 강남구 영동대로86길 10 지층 록스플레이트'
        self.백암상상마당_list.append(록스플레이트)

        # 양식
        파크 = Restaurunt('파크 하얏트 서울 코너스톤')
        파크.menu = {'주말 브런치': '125000원', '런치 세트 - 2코스': '52000원', '런치 세트 - 3코스': '59000원'}
        파크.location = '서울 강남구 테헤란로 606 파크 하얏트 서울 2층'
        self.백암상상마당_list.append(파크)

        크라이치즈버거 = Restaurunt('크라이치즈버거 삼성역점')
        크라이치즈버거.menu = {'크라이 더블 치즈버거': '6400원', '크라이 치즈버거': '5200원', '더블치즈버거세트': '9200원'}
        크라이치즈버거.location = '서울 강남구 테헤란로 616 미래에셋벤처타워 B1층'
        self.백암상상마당_list.append(크라이치즈버거)

        폴리스 = Restaurunt('폴리스 파르나스몰점')
        폴리스.menu = {'갓파더': '27000원', 'Paulie\'s 클래식 스파게티 & 미트볼 파스타': '14900원', '뉴욕치즈': '19000원'}
        폴리스.location = '서울 강남구 테헤란로 521 f-13호'
        self.백암상상마당_list.append(폴리스)

        # 기타
        메콩타이 = Restaurunt('메콩타이 삼성점')
        메콩타이.menu = {'메콩세트': '12900원', '메콩타이세트': '16900원', '메콩타이 스페셜세트': '24900원'}
        메콩타이.location = '서울 강남구 테헤란로104길 9'
        self.백암상상마당_list.append(메콩타이)

        리틀사이공 = Restaurunt('리틀사이공 파르나스몰점')
        리틀사이공.menu = {'미니월남쌈': '20000원', '꼼제인틱꾸아': '14500원', '꼼징능주': '13500원'}
        리틀사이공.location = '서울 강남구 테헤란로 521 F-14리틀사이공'
        self.백암상상마당_list.append(리틀사이공)

        포포빈 = Restaurunt('포포빈')
        포포빈.menu = {'홍두께쌀국수': '10000원', '닭고기쌀국수': '9000원', '해산물쌀국수': '10500원'}
        포포빈.location = '서울 강남구 테헤란로 521 F-14리틀사이공'
        self.백암상상마당_list.append(포포빈)

        # 디저트
        비마이게스트 = Restaurunt('비마이게스트')
        비마이게스트.menu = {'빅사이즈아메리카노': '2000원', '오리엔탈치킨파스타샐러드': '7900원', '아보카도치킨파스타샐러드': '9900원'}
        비마이게스트.location = '서울 강남구 테헤란로107길 6 두양빌딩 1층 102호'
        self.백암상상마당_list.append(비마이게스트)

        웨이크업커피 = Restaurunt('웨이크업커피')
        웨이크업커피.menu = {'아메리카노': '2500원', '카페라떼': '3000원', '유자아메리카노': '4500원'}
        웨이크업커피.location = '서울 강남구 테헤란로107길 10'
        self.백암상상마당_list.append(웨이크업커피)

        커피인류 = Restaurunt('커피인류 대치삼성점')
        커피인류.menu = {'아메리카노': '3500원', '카페라떼/카푸치노': '4000원', '플랫화이트': '4000원'}
        커피인류.location = '서울 강남구 영동대로82길 29 대신빌딩 지하 1층'
        self.백암상상마당_list.append(커피인류)


    def str_백암상상마당(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.백암상상마당_list[i].name}\n위치: {self.백암상상마당_list[i].location}\n메뉴: {self.백암상상마당_list[i].menu}\n별점: {self.백암상상마당_list[i].star}\n후기: {self.백암상상마당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_백암상상마당()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.백암상상마당_list[i].name}\n위치: {self.백암상상마당_list[i].location}\n메뉴: {self.백암상상마당_list[i].menu}\n별점: {self.백암상상마당_list[i].star}\n후기: {self.백암상상마당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_백암상상마당()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.백암상상마당_list[i].name}\n위치: {self.백암상상마당_list[i].location}\n메뉴: {self.백암상상마당_list[i].menu}\n별점: {self.백암상상마당_list[i].star}\n후기: {self.백암상상마당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_백암상상마당()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.백암상상마당_list[i].name}\n위치: {self.백암상상마당_list[i].location}\n메뉴: {self.백암상상마당_list[i].menu}\n별점: {self.백암상상마당_list[i].star}\n후기: {self.백암상상마당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_백암상상마당()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.백암상상마당_list[i].name}\n위치: {self.백암상상마당_list[i].location}\n메뉴: {self.백암상상마당_list[i].menu}\n별점: {self.백암상상마당_list[i].star}\n후기: {self.백암상상마당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_백암상상마당()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.백암상상마당_list[i].name}\n위치: {self.백암상상마당_list[i].location}\n메뉴: {self.백암상상마당_list[i].menu}\n별점: {self.백암상상마당_list[i].star}\n후기: {self.백암상상마당_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_백암상상마당()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_백암상상마당(self):
        for i in range(18):
            print(f'{i + 1}. {self.백암상상마당_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.백암상상마당_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.백암상상마당_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.백암상상마당_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.백암상상마당_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.백암상상마당_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.백암상상마당_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.백암상상마당_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.백암상상마당_list[int(restaurunt_num) - 1].name}\n위치: {self.백암상상마당_list[int(restaurunt_num) - 1].location}\n메뉴: {self.백암상상마당_list[int(restaurunt_num) - 1].menu}\n별점: {self.백암상상마당_list[int(restaurunt_num) - 1].star}\n후기: {self.백암상상마당_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.백암상상마당_list[int(restaurunt_num) - 1].name}\n위치: {self.백암상상마당_list[int(restaurunt_num) - 1].location}\n메뉴: {self.백암상상마당_list[int(restaurunt_num) - 1].menu}\n별점: {self.백암상상마당_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_백암상상마당()


    def 삼일로창고극장(self):
        # 한식
        장금이전집 = Restaurunt('장금이전집')
        장금이전집.menu = {'녹두전': '20000원', '모듬전': '20000원', '김치찌개': '5000원'}
        장금이전집.location = '서울 중구 퇴계로 147-9'
        self.삼일로창고극장_list.append(장금이전집)

        충무로백암순대국 = Restaurunt('충무로백암순대국')
        충무로백암순대국.menu = {'국밥': '8000원', '순대만국밥': '8000원', '얼큰이탕': '9000원'}
        충무로백암순대국.location = '서울 중구 퇴계로 141 세룡빌딩'
        self.삼일로창고극장_list.append(충무로백암순대국)

        죽향 = Restaurunt('죽향')
        죽향.menu = {'전복죽': '15000원', '바지락 순두부죽': '8000원', '토종닭죽': '8000원'}
        죽향.location = '서울 중구 마른내로 14'
        self.삼일로창고극장_list.append(죽향)

        # 중식
        남강 = Restaurunt('남강')
        남강.menu = {'탕짜면': '8000원', '짜장면': '6000원', '짬뽕': '7000원'}
        남강.location = '서울 중구 마른내로 10'
        self.삼일로창고극장_list.append(남강)

        명동관 = Restaurunt('명동관')
        명동관.menu = {'해물짬뽕': '8000원', '탕수육+짜장면+짬뽕': '19000원', '짜장면': '5000원'}
        명동관.location = '서울 중구 명동10길 7-9 2층 명동관'
        self.삼일로창고극장_list.append(명동관)

        홍콩반점0410 = Restaurunt('홍콩반점0410 명동점')
        홍콩반점0410.menu = {'짬뽕': '6000원', '짜장면': '5000원', '짬뽕밥': '6500원'}
        홍콩반점0410.location = '서울 중구 명동10길 13'
        self.삼일로창고극장_list.append(홍콩반점0410)

        # 일식
        일식성진 = Restaurunt('일식성진')
        일식성진.menu = {'초밥': '22000원', '생태탕': '20000원', '도다리쑥국': '33000원'}
        일식성진.location = '서울 중구 수표로2길 5 1층'
        self.삼일로창고극장_list.append(일식성진)

        부자 = Restaurunt('부자')
        부자.menu = {'부자돈까스': '7000원', '생선까스': '8000원', '모듬까스': '8000원'}
        부자.location = '서울 중구 삼일대로4길 12'
        self.삼일로창고극장_list.append(부자)

        스시이소 = Restaurunt('스시이소')
        스시이소.menu = {'런치 스시': '35000원', '런치치라시스시': '35000원', '런치 카이센동': '35000원'}
        스시이소.location = '서울 중구 퇴계로 163-1'
        self.삼일로창고극장_list.append(스시이소)

        # 양식
        명동피자 = Restaurunt('명동피자 명동본점')
        명동피자.menu = {'치즈_끝판왕 피자': '17500원', '마성의 파스타': '15400원', '바다의왕자': '17500원'}
        명동피자.location = '서울 중구 명동10길 41 4층'
        self.삼일로창고극장_list.append(명동피자)

        세븐티포 = Restaurunt('세븐티포 비스트로')
        세븐티포.menu = {'예상 밖에 가지 (With 치아바타)': '14000원', '아보카도 & 닭가슴살 샐러드볼': '15000원', '라구 파스타': '18000원'}
        세븐티포.location = '서울 중구 명동길 74 파밀리아채플 1층'
        self.삼일로창고극장_list.append(세븐티포)

        보나베띠 = Restaurunt('보나베띠 명동점')
        보나베띠.menu = {'파스타': '14900원', '피자': '16900원', '스테이크': '34900원'}
        보나베띠.location = '서울 중구 명동10길 51 나인트리호텔 3층'
        self.삼일로창고극장_list.append(보나베띠)

        # 기타
        리틀하노이 = Restaurunt('리틀하노이')
        리틀하노이.menu = {'퍼보 쇠고기 쌀국수': '10000원', '퍼탑껌 해산물 쌀국수': '10000원', '껌징능주 볶음밥': '12000원'}
        리틀하노이.location = '서울 중구 명동10길 7-3'
        self.삼일로창고극장_list.append(리틀하노이)

        아그라명동점 = Restaurunt('아그라명동점')
        아그라명동점.menu = {'버터 치킨 마크니': '10000원', '치킨 띠까 마살라': '10000원', '셰프 데일리 커리': '9000원'}
        아그라명동점.location = '서울 중구 명동6길 21'
        self.삼일로창고극장_list.append(아그라명동점)

        타이가든 = Restaurunt('타이가든 명동성당점')
        타이가든.menu = {'팟타이꿍': '12000원', '똠얌꿍': '15000원', '뿌님 팟퐁가리': '29000원'}
        타이가든.location = '서울 중구 명동길 55 3층 302호'
        self.삼일로창고극장_list.append(타이가든)

        # 디저트
        에쎄레젤라또 = Restaurunt('에쎄레젤라또')
        에쎄레젤라또.menu = {'젤라또 뜨레컵': '6000원', '젤라또 우노컵': '4000원', '젤라또 두에컵': '5000원'}
        에쎄레젤라또.location = '서울 중구 명동길 74 명동성당'
        self.삼일로창고극장_list.append(에쎄레젤라또)

        루프트 = Restaurunt('루프트 커피 명동점')
        루프트.menu = {'서울 아메리카노': '4900원', '하와이 카우 아메리카노': '5900원', '루프트 아메리카노': '4900원'}
        루프트.location = '서울 중구 삼일대로 308 조양빌딩본관 1층'
        self.삼일로창고극장_list.append(루프트)

        커피광 = Restaurunt('커피광')
        커피광.menu = {'에그타르트': '2800원', '스모어쿠키': '3500원', '에스프레소': '3500원'}
        커피광.location = '서울 중구 삼일대로 330 평화빌딩 별관 1층'
        self.삼일로창고극장_list.append(커피광)


    def str_삼일로창고극장(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.삼일로창고극장_list[i].name}\n위치: {self.삼일로창고극장_list[i].location}\n메뉴: {self.삼일로창고극장_list[i].menu}\n별점: {self.삼일로창고극장_list[i].star}\n후기: {self.삼일로창고극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_삼일로창고극장()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.삼일로창고극장_list[i].name}\n위치: {self.삼일로창고극장_list[i].location}\n메뉴: {self.삼일로창고극장_list[i].menu}\n별점: {self.삼일로창고극장_list[i].star}\n후기: {self.삼일로창고극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_삼일로창고극장()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.삼일로창고극장_list[i].name}\n위치: {self.삼일로창고극장_list[i].location}\n메뉴: {self.삼일로창고극장_list[i].menu}\n별점: {self.삼일로창고극장_list[i].star}\n후기: {self.삼일로창고극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_삼일로창고극장()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.삼일로창고극장_list[i].name}\n위치: {self.삼일로창고극장_list[i].location}\n메뉴: {self.삼일로창고극장_list[i].menu}\n별점: {self.삼일로창고극장_list[i].star}\n후기: {self.삼일로창고극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_삼일로창고극장()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.삼일로창고극장_list[i].name}\n위치: {self.삼일로창고극장_list[i].location}\n메뉴: {self.삼일로창고극장_list[i].menu}\n별점: {self.삼일로창고극장_list[i].star}\n후기: {self.삼일로창고극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_삼일로창고극장()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.삼일로창고극장_list[i].name}\n위치: {self.삼일로창고극장_list[i].location}\n메뉴: {self.삼일로창고극장_list[i].menu}\n별점: {self.삼일로창고극장_list[i].star}\n후기: {self.삼일로창고극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_삼일로창고극장()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_삼일로창고극장(self):
        for i in range(18):
            print(f'{i + 1}. {self.삼일로창고극장_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.삼일로창고극장_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.삼일로창고극장_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.삼일로창고극장_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.삼일로창고극장_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.삼일로창고극장_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.삼일로창고극장_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.삼일로창고극장_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.삼일로창고극장_list[int(restaurunt_num) - 1].name}\n위치: {self.삼일로창고극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.삼일로창고극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.삼일로창고극장_list[int(restaurunt_num) - 1].star}\n후기: {self.삼일로창고극장_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.삼일로창고극장_list[int(restaurunt_num) - 1].name}\n위치: {self.삼일로창고극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.삼일로창고극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.삼일로창고극장_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_삼일로창고극장()


    def 성수아트홀(self):
        # 한식
        쵸리상경 = Restaurunt('쵸리상경')
        쵸리상경.menu = {'연어 솥밥': '15000원', '전복장 솥밥': '17000원', '스테이크 솥밥': '20000원'}
        쵸리상경.location = '서울 성동구 서울숲4길 18-8 2층 쵸리상경'
        self.성수아트홀_list.append(쵸리상경)

        성수족발 = Restaurunt('성수족발')
        성수족발.menu = {'족발(특대)': '50000원', '족발(대)': '45000원', '족발(중)': '40000원'}
        성수족발.location = '서울 성동구 아차산로7길 7 동진빌딩 1층 성수족발'
        self.성수아트홀_list.append(성수족발)

        눈꽃돼지 = Restaurunt('눈꽃돼지')
        눈꽃돼지.menu = {'한돈 눈꽃 통삼겹': '14000원', '제주 눈꽃 특목살': '15000원', '이베리코 통목살': '16000원'}
        눈꽃돼지.location = '서울 성동구 왕십리로8길 17-4'
        self.성수아트홀_list.append(눈꽃돼지)

        # 중식
        봉짬뽕 = Restaurunt('봉짬뽕')
        봉짬뽕.menu = {'짬뽕': '8000원', '짜장': '6000원', '쟁반짜장': '8000원'}
        봉짬뽕.location = '서울 성동구 성수일로11길 11'
        self.성수아트홀_list.append(봉짬뽕)

        마봉양꼬치 = Restaurunt('마봉양꼬치 성수점')
        마봉양꼬치.menu = {'오리지널양꼬치(10꼬치)': '15000원', '고급양갈비(300g)': '25000원', '송화양꼬치(10꼬치)': '13000원'}
        마봉양꼬치.location = '서울 광진구 동일로18길 70'
        self.성수아트홀_list.append(마봉양꼬치)

        반티엔야오 = Restaurunt('반티엔야오 카오위 건대점')
        반티엔야오.menu = {'마라카오위': '42000원', '치오하지아오 카오위': '38000원', '마늘향 카오위': '3800원'}
        반티엔야오.location = '서울 광진구 동일로20길 106 2층'
        self.성수아트홀_list.append(반티엔야오)

        # 일식
        소바식당 = Restaurunt('소바식당')
        소바식당.menu = {'냉소바': '9000원', '한우양지온반': '9000원', '게딱지장덮밥': '9000원'}
        소바식당.location = '서울 성동구 연무장7가길 6'
        self.성수아트홀_list.append(소바식당)

        해만식당 = Restaurunt('해만식당')
        해만식당.menu = {'아나고동': '16000원', '소유사케동': '12000원', '쇼유에비동': '10000원'}
        해만식당.location = '서울 성동구 연무장9길 10'
        self.성수아트홀_list.append(해만식당)

        오코노미야키식당하나 = Restaurunt('오코노미야키식당하나')
        오코노미야키식당하나.menu = {'돼지타마 오코노미야키': '9000원', '오징어타마 오코노미야키': '9500원', '돼지오징어타마 오코노미야키': '9500원'}
        오코노미야키식당하나.location = '서울 광진구 능동로13길 111'
        self.성수아트홀_list.append(오코노미야키식당하나)

        # 양식
        다로베 = Restaurunt('다로베')
        다로베.menu = {'다로베': '25000원', '칼존': '23000원', '마리나라': '16000원'}
        다로베.location = '서울 성동구 서울숲길 48 삼호빌딩 1층 다로베'
        self.성수아트홀_list.append(다로베)

        핑거팁스 = Restaurunt('핑거팁스')
        핑거팁스.menu = {'치즈인덱스버거 ': '7900원', '레귤러 프라이즈': '2900원', '핑키버거': '9900원'}
        핑거팁스.location = '서울 성동구 연무장7가길 5-1 1층'
        self.성수아트홀_list.append(핑거팁스)

        성수다락 = Restaurunt('성수다락')
        성수다락.menu = {'다락오므라이스': '14000원', '매콤크림파스타': '15000원', '게살매콤리조또': '15000원'}
        성수다락.location = '서울 성동구 뚝섬로9길 20 2층'
        self.성수아트홀_list.append(성수다락)

        # 기타
        꾸아 = Restaurunt('꾸아')
        꾸아.menu = {'직화쌀국수': '9500원', '왕갈비 쌀국수': '13000원', '분짜': '16000원'}
        꾸아.location = '서울 성동구 서울숲4길 26-24 B1층 꾸아'
        self.성수아트홀_list.append(꾸아)

        냐항 = Restaurunt('냐항')
        냐항.menu = {'반쎄오': '21000원', '짜죠': '6000원', '그린파파야샐러드': '14000원'}
        냐항.location = '서울 성동구 연무장길 9-6 1층 냐항'
        self.성수아트홀_list.append(냐항)

        갓잇 = Restaurunt('갓잇 성수점')
        갓잇.menu = {'갓잇 A set': '32000원', '갓잇 B set': '34000원', 'TACO set': '45000원'}
        갓잇.location = '서울 성동구 왕십리로10길 10 2층'
        self.성수아트홀_list.append(갓잇)

        # 디저트
        엔아더 = Restaurunt('엔아더')
        엔아더.menu = {'아메리카노': '5500원', '에이드': '8500원', '에스프레소': '6000원'}
        엔아더.location = '서울 성동구 서울숲2길 40-10'
        self.성수아트홀_list.append(엔아더)

        리틀포레스트 = Restaurunt('리틀포레스트')
        리틀포레스트.menu = {'페스토치킨파니니': '11000원', '부라타샐러드': '13000원', '아보카도타르틴': '11000원'}
        리틀포레스트.location = '서울 성동구 성수일로12길 23 2층'
        self.성수아트홀_list.append(리틀포레스트)

        구욱희씨 = Restaurunt('구욱희씨')
        구욱희씨.menu = {'오레오쿠키': '5300원', '카라멜로투스쿠키': '5300원', '쑥 스콘': '6000원'}
        구욱희씨.location = '서울 성동구 서울숲4길 12-22 1,2층'
        self.성수아트홀_list.append(구욱희씨)


    def str_성수아트홀(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.성수아트홀_list[i].name}\n위치: {self.성수아트홀_list[i].location}\n메뉴: {self.성수아트홀_list[i].menu}\n별점: {self.성수아트홀_list[i].star}\n후기: {self.성수아트홀_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_성수아트홀()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.성수아트홀_list[i].name}\n위치: {self.성수아트홀_list[i].location}\n메뉴: {self.성수아트홀_list[i].menu}\n별점: {self.성수아트홀_list[i].star}\n후기: {self.성수아트홀_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_성수아트홀()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.성수아트홀_list[i].name}\n위치: {self.성수아트홀_list[i].location}\n메뉴: {self.성수아트홀_list[i].menu}\n별점: {self.성수아트홀_list[i].star}\n후기: {self.성수아트홀_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_성수아트홀()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.성수아트홀_list[i].name}\n위치: {self.성수아트홀_list[i].location}\n메뉴: {self.성수아트홀_list[i].menu}\n별점: {self.성수아트홀_list[i].star}\n후기: {self.성수아트홀_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_성수아트홀()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.성수아트홀_list[i].name}\n위치: {self.성수아트홀_list[i].location}\n메뉴: {self.성수아트홀_list[i].menu}\n별점: {self.성수아트홀_list[i].star}\n후기: {self.성수아트홀_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_성수아트홀()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.성수아트홀_list[i].name}\n위치: {self.성수아트홀_list[i].location}\n메뉴: {self.성수아트홀_list[i].menu}\n별점: {self.성수아트홀_list[i].star}\n후기: {self.성수아트홀_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_성수아트홀()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_성수아트홀(self):
        for i in range(18):
            print(f'{i + 1}. {self.성수아트홀_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.성수아트홀_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.성수아트홀_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.성수아트홀_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.성수아트홀_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.성수아트홀_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.성수아트홀_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.성수아트홀_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.성수아트홀_list[int(restaurunt_num) - 1].name}\n위치: {self.성수아트홀_list[int(restaurunt_num) - 1].location}\n메뉴: {self.성수아트홀_list[int(restaurunt_num) - 1].menu}\n별점: {self.성수아트홀_list[int(restaurunt_num) - 1].star}\n후기: {self.성수아트홀_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.성수아트홀_list[int(restaurunt_num) - 1].name}\n위치: {self.성수아트홀_list[int(restaurunt_num) - 1].location}\n메뉴: {self.성수아트홀_list[int(restaurunt_num) - 1].menu}\n별점: {self.성수아트홀_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_성수아트홀()


    def 세븐파이브홀(self):
        # 한식
        두레국수 = Restaurunt('두레국수')
        두레국수.menu = {'두레국수': '9000원', '비빔국수': '9000원', '비빔밥': '9000원'}
        두레국수.location = '서울 강남구 도산대로37길 28'
        self.세븐파이브홀_list.append(두레국수)

        강남면옥 = Restaurunt('강남면옥')
        강남면옥.menu = {'갈비찜(소)': '45000원', '회냉면': '11000원', '비빔냉면': '10000원'}
        강남면옥.location = '서울 강남구 논현로152길 34'
        self.세븐파이브홀_list.append(강남면옥)

        하모 = Restaurunt('하모')
        하모.menu = {'전주비빔밥': '13000원', '헛제사밥': '11000원', '육전': '45000원'}
        하모.location = '서울 강남구 언주로 819'
        self.세븐파이브홀_list.append(하모)

        # 중식
        일일향 = Restaurunt('일일향 압구정1호점')
        일일향.menu = {'짜장면': '7000원', '황비홍깐풍기': '30000원', '유린기': '30000원'}
        일일향.location = '서울 강남구 논현로168길 30'
        self.세븐파이브홀_list.append(일일향)

        쮸즈 = Restaurunt('쮸즈')
        쮸즈.menu = {'소룡포': '3500원', '쇼마이': '4000원', '딴딴면': '7500원'}
        쮸즈.location = '서울 강남구 도산대로17길 13'
        self.세븐파이브홀_list.append(쮸즈)

        채운 = Restaurunt('채운')
        채운.menu = {'광동식 생선찜': '60000원', '다진마늘튀긴 새우': '40000원', '광동식 구운 통닭': '30000원'}
        채운.location = '서울 강남구 논현로175길 107'
        self.세븐파이브홀_list.append(채운)

        # 일식
        스시유키 = Restaurunt('스시유키')
        스시유키.menu = {'런치 카운터 오마카세': '60000원', '디너 카운터 오마카세': '150000원', '런치 룸 오마카세': '60000원'}
        스시유키.location = '서울 강남구 논현로164길 25'
        self.세븐파이브홀_list.append(스시유키)

        삿뽀로 = Restaurunt('삿뽀로 압구정점')
        삿뽀로.menu = {'사모님정식': '23000원', '런치스페셜C': '28000원', '모듬사시미 정식': '58000원'}
        삿뽀로.location = '서울 강남구 압구정로30길 51 I.S.A 빌딩'
        self.세븐파이브홀_list.append(삿뽀로)

        미미면가 = Restaurunt('미미면가')
        미미면가.menu = {'고등어구이 온소바': '18000원', '성게알 소바': '18000원', '새우튀김 소바': '11000원'}
        미미면가.location = '서울 강남구 강남대로160길 29'
        self.세븐파이브홀_list.append(미미면가)

        # 양식
        피치 = Restaurunt('피치')
        피치.menu = {'비스테카 알라 피오렌티나': '29000원', '부라따': '23000원', '라구': '32000원'}
        피치.location = '서울 강남구 도산대로37길 21 문헌빌딩 1층'
        self.세븐파이브홀_list.append(피치)

        오엔 = Restaurunt('오엔')
        오엔.menu = {'Premium Set': '109000원', 'T-bone set(2인)': '180000원', '모짜 칠리 떡볶이': '26000원'}
        오엔.location = '서울 강남구 압구정로11길 37-30'
        self.세븐파이브홀_list.append(오엔)

        메리고라운드 = Restaurunt('메리고라운드 스테이크')
        메리고라운드.menu = {'리코타 치즈샐러드': '10000원', '씨푸드 사천파스타': '10000원', '비프 크림 파스타': '9000원'}
        메리고라운드.location = '서울 강남구 논현로175길 69 원영빌딩 1층'
        self.세븐파이브홀_list.append(메리고라운드)

        # 기타
        동남아식당 = Restaurunt('동남아식당')
        동남아식당.menu = {'쌀국수': '8000원', '소고기볶음밥': '7900원', '해산물팟타이': '9500원'}
        동남아식당.location = '서울 강남구 논현로149길 51'
        self.세븐파이브홀_list.append(동남아식당)

        감성타코 = Restaurunt('감성타코 가로수길점')
        감성타코.menu = {'감성 그릴드 파히타': '38000원', '까르니따스 치즈 타고': '9000원', '파인애플 살사 베르데 타코': '9000원'}
        감성타코.location = '서울 강남구 가로수길 26 3층'
        self.세븐파이브홀_list.append(감성타코)

        수엠부 = Restaurunt('수엠부')
        수엠부.menu = {'치킨 티카': '15000원', '모듬 탄둘': '35000원', '말루 덤': '9000원'}
        수엠부.location = '서울 강남구 도산대로11길 15'
        self.세븐파이브홀_list.append(수엠부)

        # 디저트
        마당 = Restaurunt('카페 마당')
        마당.menu = {'클럽샌드위치': '25000원', '수제와규버거': '27000원', '마당 티라미수': '15500원'}
        마당.location = '서울 강남구 도산대로45길 7 에르메스도산파크'
        self.세븐파이브홀_list.append(마당)

        블루보틀 = Restaurunt('블루보틀 압구정 카페')
        블루보틀.menu = {'에스프레소': '5000원', '아메리카노': '5000원', '지브랄타': '5500원'}
        블루보틀.location = '서울 강남구 논현로 854 101호, 201호'
        self.세븐파이브홀_list.append(블루보틀)

        듀자미 = Restaurunt('듀자미')
        듀자미.menu = {'카라멜 소금케이크(조각)': '6700원', '보드라운 딸기 생크림케이크(조각)': '6700원', '카라멜 소금케이크(홀)': '52000원'}
        듀자미.location = '서울 강남구 도산대로11길 28'
        self.세븐파이브홀_list.append(듀자미)


    def str_세븐파이브홀(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.세븐파이브_list[i].name}\n위치: {self.세븐파이브_list[i].location}\n메뉴: {self.세븐파이브_list[i].menu}\n별점: {self.세븐파이브_list[i].star}\n후기: {self.세븐파이브_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세븐파이브홀()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.세븐파이브_list[i].name}\n위치: {self.세븐파이브_list[i].location}\n메뉴: {self.세븐파이브_list[i].menu}\n별점: {self.세븐파이브_list[i].star}\n후기: {self.세븐파이브_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세븐파이브홀()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.세븐파이브_list[i].name}\n위치: {self.세븐파이브_list[i].location}\n메뉴: {self.세븐파이브_list[i].menu}\n별점: {self.세븐파이브_list[i].star}\n후기: {self.세븐파이브_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세븐파이브홀()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.세븐파이브_list[i].name}\n위치: {self.세븐파이브_list[i].location}\n메뉴: {self.세븐파이브_list[i].menu}\n별점: {self.세븐파이브_list[i].star}\n후기: {self.세븐파이브_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세븐파이브홀()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.세븐파이브_list[i].name}\n위치: {self.세븐파이브_list[i].location}\n메뉴: {self.세븐파이브_list[i].menu}\n별점: {self.세븐파이브_list[i].star}\n후기: {self.세븐파이브_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세븐파이브홀()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.세븐파이브_list[i].name}\n위치: {self.세븐파이브_list[i].location}\n메뉴: {self.세븐파이브_list[i].menu}\n별점: {self.세븐파이브_list[i].star}\n후기: {self.세븐파이브_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_세븐파이브홀()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_세븐파이브홀(self):
        for i in range(18):
            print(f'{i + 1}. {self.세븐파이브홀_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.세븐파이브홀_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.세븐파이브홀_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.세븐파이브홀_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.세븐파이브홀_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.세븐파이브홀_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.세븐파이브홀_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.세븐파이브홀_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.세븐파이브홀_list[int(restaurunt_num) - 1].name}\n위치: {self.세븐파이브홀_list[int(restaurunt_num) - 1].location}\n메뉴: {self.세븐파이브홀_list[int(restaurunt_num) - 1].menu}\n별점: {self.세븐파이브홀_list[int(restaurunt_num) - 1].star}\n후기: {self.세븐파이브홀_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.세븐파이브홀_list[int(restaurunt_num) - 1].name}\n위치: {self.세븐파이브홀_list[int(restaurunt_num) - 1].location}\n메뉴: {self.세븐파이브홀_list[int(restaurunt_num) - 1].menu}\n별점: {self.세븐파이브홀_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_세븐파이브홀()


    def 신한카드판(self):
        # 한식
        옥동식 = Restaurunt('옥동식')
        옥동식.menu = {'돼지곰탕(보통)': '9000원', '육포': '9000원', '냉소면': '11000원'}
        옥동식.location = '서울 마포구 양화로7길 44-10 3차신도빌라'
        self.신한카드판_list.append(옥동식)

        우담해담 = Restaurunt('우담가&해담가')
        우담해담.menu = {'[숯불구이 코스]꽃등심코스': '69000원', '[해초바다 코스]모둠 특선': '49000원', '[해초바다 세트] 해담가 회정식': '30000원'}
        우담해담.location = '서울 마포구 양화로 45 메세나폴리스몰 1층 우담가'
        self.신한카드판_list.append(우담해담)

        한강껍데기 = Restaurunt('한강껍데기')
        한강껍데기.menu = {'껍데기': '7000원', '생목살': '13000원', '생삼겹': '13000원'}
        한강껍데기.location = '서울 마포구 망원로 48-1'
        self.신한카드판_list.append(한강껍데기)

        # 중식
        진진 = Restaurunt('진진')
        진진.menu = {'멘보샤': '17600원', '오향냉채': '17600원', '깐풍기': '18400원'}
        진진.location = '서울 마포구 잔다리로 123'
        self.신한카드판_list.append(진진)

        만두란 = Restaurunt('만두란')
        만두란.menu = {'육즙 샤우롱바오': '7000원', '생생표고마두 ': '6000원', '새우야채딤섬': '6000원'}
        만두란.location = '서울 마포구 동교로 81'
        self.신한카드판_list.append(만두란)

        연희중식 = Restaurunt('연희중식')
        연희중식.menu = {'연희탕수육': '15000원', '반반새우': '25000원', '짜장면': '6500원'}
        연희중식.location = '서울 마포구 양화로1길 32'
        self.신한카드판_list.append(연희중식)

        # 일식
        카덴 = Restaurunt('우동 카덴')
        카덴.menu = {'가케우동': '7000원', '덴뿌라우동': '9500원', '붓가케우동': '8500원'}
        카덴.location = '서울 마포구 양화로7안길 2-1'
        self.신한카드판_list.append(카덴)

        미카도스시 = Restaurunt('미카도스시 합정역점')
        미카도스시.menu = {'스페셜초밥(12P)': '19000원', '연어초밥(12P)': '14000원', '모둠초밥(12P)': '10900원'}
        미카도스시.location = '서울 마포구 월드컵로3길 14 딜라이트스퀘어2차 1층'
        self.신한카드판_list.append(미카도스시)

        마루돈까스 = Restaurunt('마루돈까스')
        마루돈까스.menu = {'마루우동': '6500원', '마루돈까스(안심)': '10000원', '치킨까스': '9500원'}
        마루돈까스.location = '서울 마포구 양화로6길 17'
        self.신한카드판_list.append(마루돈까스)

        # 양식
        팔로피자 = Restaurunt('팔로피자')
        팔로피자.menu = {'마르게리따 피자': '18700원', '버섯치즈 리조또': '18700원', '알리오 브로콜리 피자': '24800원'}
        팔로피자.location = '서울 마포구 양화로6길 9-20 카메오빌딩'
        self.신한카드판_list.append(팔로피자)

        페리도트 = Restaurunt('페리도트')
        페리도트.menu = {'로제파스타': '15000원', '감바스 알 아히오': '15000원', '부채살스테이크': '20000원'}
        페리도트.location = '서울 마포구 포은로 106-1 1층'
        self.신한카드판_list.append(페리도트)

        다이너재키 = Restaurunt('다이너재키')
        다이너재키.menu = {'구운아스파라거스(아보카도)연어샐러드': '14000원 ~ 15000원', '두부리코타치즈 따뜻한 샐러드': '13000원', '퍼플망원': '7000원'}
        다이너재키.location = '서울 마포구 포은로 82 1층'
        self.신한카드판_list.append(다이너재키)

        # 기타
        쿠차라 = Restaurunt('쿠차라 합정역점')
        쿠차라.menu = {'치킨 부리또': '6900원', '두부 부리또볼': '6900원', '스테이크 샐러드': '9900원'}
        쿠차라.location = '서울 마포구 양화로 45 메세나폴리스 지하1층'
        self.신한카드판_list.append(쿠차라)

        아그라 = Restaurunt('아그라 합정점')
        아그라.menu = {'탄두리 치킨 반마리(2pcs)': '9000원', '버터 프로운 마크니': '11700원', '커플세트': '39900원'}
        아그라.location = '서울 마포구 월드컵로3길 14 2층 210호'
        self.신한카드판_list.append(아그라)

        리틀파파포 = Restaurunt('리틀파파포 합정본점')
        리틀파파포.menu = {'양지쌀국수': '8000원', '차돌박이쌀국수': '9000원', '모듬고기쌀국수': '10000원'}
        리틀파파포.location = '서울 마포구 독막로3길 7 1~2층'
        self.신한카드판_list.append(리틀파파포)

        # 디저트
        포비 = Restaurunt('포비 베이직')
        포비.menu = {'어니언 럭스 샌드위치': '9500원', '볼케이노 샌드위치': '6800원', '플랙화이트9oz': '4500원'}
        포비.location = '서울 마포구 양화로3길 66'
        self.신한카드판_list.append(포비)

        ZTTN = Restaurunt('ZTTN')
        ZTTN.menu = {'God father': '5500원', 'Filter coffee': '5500원', 'Espresso': '4500원'}
        ZTTN.location = '서울 마포구 양화로11길 42'
        self.신한카드판_list.append(ZTTN)

        키쉬미뇽 = Restaurunt('키쉬미뇽')
        키쉬미뇽.menu = {'치즈타르트': '2800원', '갸토쇼콜라': '3500원', '새우리조토': '3800원'}
        키쉬미뇽.location = '서울 마포구 양화로6길 35'
        self.신한카드판_list.append(키쉬미뇽)


    def str_신한카드판(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.신한카드판_list[i].name}\n위치: {self.신한카드판_list[i].location}\n메뉴: {self.신한카드판_list[i].menu}\n별점: {self.신한카드판_list[i].star}\n후기: {self.신한카드판_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_신한카드판()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.신한카드판_list[i].name}\n위치: {self.신한카드판_list[i].location}\n메뉴: {self.신한카드판_list[i].menu}\n별점: {self.신한카드판_list[i].star}\n후기: {self.신한카드판_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_신한카드판()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.신한카드판_list[i].name}\n위치: {self.신한카드판_list[i].location}\n메뉴: {self.신한카드판_list[i].menu}\n별점: {self.신한카드판_list[i].star}\n후기: {self.신한카드판_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_신한카드판()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.신한카드판_list[i].name}\n위치: {self.신한카드판_list[i].location}\n메뉴: {self.신한카드판_list[i].menu}\n별점: {self.신한카드판_list[i].star}\n후기: {self.신한카드판_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_신한카드판()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.신한카드판_list[i].name}\n위치: {self.신한카드판_list[i].location}\n메뉴: {self.신한카드판_list[i].menu}\n별점: {self.신한카드판_list[i].star}\n후기: {self.신한카드판_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_신한카드판()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.신한카드판_list[i].name}\n위치: {self.신한카드판_list[i].location}\n메뉴: {self.신한카드판_list[i].menu}\n별점: {self.신한카드판_list[i].star}\n후기: {self.신한카드판_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_신한카드판()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_신한카드판(self):
        for i in range(18):
            print(f'{i + 1}. {self.신한카드판_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.신한카드판_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.신한카드판_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.신한카드판_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.신한카드판_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.신한카드판_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.신한카드판_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.신한카드판_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.신한카드판_list[int(restaurunt_num) - 1].name}\n위치: {self.신한카드판_list[int(restaurunt_num) - 1].location}\n메뉴: {self.신한카드판_list[int(restaurunt_num) - 1].menu}\n별점: {self.신한카드판_list[int(restaurunt_num) - 1].star}\n후기: {self.신한카드판_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.신한카드판_list[int(restaurunt_num) - 1].name}\n위치: {self.신한카드판_list[int(restaurunt_num) - 1].location}\n메뉴: {self.신한카드판_list[int(restaurunt_num) - 1].menu}\n별점: {self.신한카드판_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_신한카드판()


    def 연희예술극장(self):
        # 한식
        청어람 = Restaurunt('청어람 망원점')
        청어람.menu = {'막창': '20000원', '곱창': '22000원', '곱창전골(소)': '22000원'}
        청어람.location = '서울 마포구 망원로 97'
        self.연희예술극장_list.append(청어람)

        육장 = Restaurunt('육장')
        육장.menu = {'육개장': '9000원', '육갈탕': '13000원', '육라면': '9000원'}
        육장.location = '서울 마포구 월드컵로19길 74 어쩌다가게 지하 2층'
        self.연희예술극장_list.append(육장)

        밀면집 = Restaurunt('밀면집')
        밀면집.menu = {'밀면': '6000원', '삼겹한줄': '9000원', '비빔밀면': '6500원'}
        밀면집.location = '서울 마포구 포은로 90 1층 밀면집'
        self.연희예술극장_list.append(밀면집)

        # 중식
        목란 = Restaurunt('목란')
        목란.menu = {'동파육(소)': '45000원', '칠리새우': '40000원', '짜장면': '8000원'}
        목란.location = '서울 서대문구 연희로15길 21'
        self.연희예술극장_list.append(목란)

        포가 = Restaurunt('포가')
        포가.menu = {'돼지껍데기무침': '9000원', '오향장육': '19000원', '마파두부': '15000원'}
        포가.location = '서울 마포구 성미산로 190-4'
        self.연희예술극장_list.append(포가)

        중화복춘 = Restaurunt('중화복춘')
        중화복춘.menu = {'오향장육(소)': '46000원', '오색원앙 구수': '41000원', '구품복춘 양장피': '4900원'}
        중화복춘.location = '서울 마포구 동교로 220-7 101'
        self.연희예술극장_list.append(중화복춘)

        # 일식
        시오 = Restaurunt('시오')
        시오.menu = {'삼색야끼도리 런치': '1300원', '생연어덮밥': '13000원', '스끼야끼': '18000원'}
        시오.location = '서울 서대문구 연희로11가길 23 1층'
        self.연희예술극장_list.append(시오)

        저스트텐동 = Restaurunt('저스트텐동 연남점')
        저스트텐동.menu = {'저스트텐동': '9900원', '에비텐동': '118=900원', '생선텐동': '13900원'}
        저스트텐동.location = '서울 마포구 동교로46길 3'
        self.연희예술극장_list.append(저스트텐동)

        키움초밥 = Restaurunt('키움초밥')
        키움초밥.menu = {'커플세트A': '30000원', '연어초밥(10pcs)': '14000원', 'VIP초밥 15pcs': '24000원'}
        키움초밥.location = '서울 마포구 잔다리로 77 대창빌딩'
        self.연희예술극장_list.append(키움초밥)

        # 양식
        디에이프릴 = Restaurunt('디에이프릴')
        디에이프릴.menu = {'계절과일프렌치토스트': '14000원', '리코타 치즈 샐러드': '14000원', '페퍼로니라구오믈렛': '16000원'}
        디에이프릴.location = '서울 마포구 성미산로29안길 19 1층'
        self.연희예술극장_list.append(디에이프릴)

        쏘렌토 = Restaurunt('쏘렌토 연희점')
        쏘렌토.menu = {'고르곤졸라 피자': '16900원', '마르게리따 피자': '16900원', '루꼴라프리마베라 피자': '19500원'}
        쏘렌토.location = '서울 서대문구 연희로 81-26 1층 쏘렌토'
        self.연희예술극장_list.append(쏘렌토)

        센트그릴 = Restaurunt('센트그릴')
        센트그릴.menu = {'[BBQ PLATTER] 센트그릴 플래터': '36000원', '[BBQ PLATTER] 새터데이 플래터': '54000원', '[RIB PATTER] 스페어립 플래터(Half rack)': '35000원'}
        센트그릴.location = '서울 서대문구 연희로 89-3 지하 1층 센트그릴'
        self.연희예술극장_list.append(센트그릴)

        # 기타
        툭툭누들타이 = Restaurunt('툭툭누들타이')
        툭툭누들타이.menu = {'연남 갈비 국수': '13000원', '똠얌꿍': '16000원', '뿌님팟퐁커리': '27000원'}
        툭툭누들타이.location = '서울 마포구 성미산로 161-8 2층'
        self.연희예술극장_list.append(툭툭누들타이)

        하노이의아침 = Restaurunt('하노이의아침 연희점')
        하노이의아침.menu = {'볶음국수': '15900원', '쇠고기볶음밥': '17600원', '매운해물볶음밥': '16500원'}
        하노이의아침.location = '서울 서대문구 연희맛로 10'
        self.연희예술극장_list.append(하노이의아침)

        소이연남 = Restaurunt('소이연남')
        소이연남.menu = {'소고기 쌀국수(기본)': '9500원', '똠양 쌀국수(기본)': '12000원', '쏨땀': '12000원'}
        소이연남.location = '서울 마포구 동교로 267 1층'
        self.연희예술극장_list.append(소이연남)

        # 디저트
        벌스데이투미 = Restaurunt('벌스데이투미')
        벌스데이투미.menu = {'곰돌이로열밀크티': '7000원', '아메리카노': '4000원', '바닐라라떼': '5000원'}
        벌스데이투미.location = '서울 마포구 성미산로29안길 26 2F'
        self.연희예술극장_list.append(벌스데이투미)

        르솔레이 = Restaurunt('르솔레이')
        르솔레이.menu = {'연희마들렌': '3000원', '더티마틸라 마들렌': '3900원', '트러플 마들렌': '3900원'}
        르솔레이.location = '서울 서대문구 연희맛로 7-29 LE SOLEIL pâtisserie'
        self.연희예술극장_list.append(르솔레이)

        연희양과점 = Restaurunt('연희양과점')
        연희양과점.menu = {'아메리카노': '3000원', '카페라떼': '3500원', '블렌딩 티': '4000원'}
        연희양과점.location = '서울 서대문구 연희로11가길 56'
        self.연희예술극장_list.append(연희양과점)


    def str_연희예술극장(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.연희예술극장_list[i].name}\n위치: {self.연희예술극장_list[i].location}\n메뉴: {self.연희예술극장_list[i].menu}\n별점: {self.연희예술극장_list[i].star}\n후기: {self.연희예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_연희예술극장()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.연희예술극장_list[i].name}\n위치: {self.연희예술극장_list[i].location}\n메뉴: {self.연희예술극장_list[i].menu}\n별점: {self.연희예술극장_list[i].star}\n후기: {self.연희예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_연희예술극장()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.연희예술극장_list[i].name}\n위치: {self.연희예술극장_list[i].location}\n메뉴: {self.연희예술극장_list[i].menu}\n별점: {self.연희예술극장_list[i].star}\n후기: {self.연희예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_연희예술극장()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.연희예술극장_list[i].name}\n위치: {self.연희예술극장_list[i].location}\n메뉴: {self.연희예술극장_list[i].menu}\n별점: {self.연희예술극장_list[i].star}\n후기: {self.연희예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_연희예술극장()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.연희예술극장_list[i].name}\n위치: {self.연희예술극장_list[i].location}\n메뉴: {self.연희예술극장_list[i].menu}\n별점: {self.연희예술극장_list[i].star}\n후기: {self.연희예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_연희예술극장()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.연희예술극장_list[i].name}\n위치: {self.연희예술극장_list[i].location}\n메뉴: {self.연희예술극장_list[i].menu}\n별점: {self.연희예술극장_list[i].star}\n후기: {self.연희예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_연희예술극장()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_연희예술극장(self):
        for i in range(18):
            print(f'{i + 1}. {self.연희예술극장_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.연희예술극장_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.연희예술극장_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.연희예술극장_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.연희예술극장_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.연희예술극장_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.연희예술극장_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.연희예술극장_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.연희예술극장_list[int(restaurunt_num) - 1].name}\n위치: {self.연희예술극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.연희예술극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.연희예술극장_list[int(restaurunt_num) - 1].star}\n후기: {self.연희예술극장_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.연희예술극장_list[int(restaurunt_num) - 1].name}\n위치: {self.연희예술극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.연희예술극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.연희예술극장_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_연희예술극장()


    def 이해랑예술극장(self):
        # 한식
        산정 = Restaurunt('산정')
        산정.menu = {'제주 오겹살': '14000원', '사골 스지 배추탕': '8000원', '사골 갈비 배추탕': '10000원'}
        산정.location = '서울 중구 동호로 288 산정'
        self.이해랑예술극장_list.append(산정)

        느티나무집 = Restaurunt('느티나무집')
        느티나무집.menu = {'꽃등심': '40000원', '맛꽃살': '20000원', '차돌박이': '20000원'}
        느티나무집.location = '서울 중구 동호로28길 11 느티나무집'
        self.이해랑예술극장_list.append(느티나무집)

        오서방네 = Restaurunt('오서방네 푸줏간')
        오서방네.menu = {'대패삼겹살': '11000원', '항정살': '10000원', '갈매기살': '10000원'}
        오서방네.location = '서울 중구 동호로24길 27-7'
        self.이해랑예술극장_list.append(오서방네)

        # 중식
        신룽푸마라탕 = Restaurunt('신룽푸마라탕')
        신룽푸마라탕.menu = {'마라탕': '7000원', '마라샹궈': '16000원', '마라반': '12000원'}
        신룽푸마라탕.location = '서울 중구 동호로 228-1'
        self.이해랑예술극장_list.append(신룽푸마라탕)

        홍보각 = Restaurunt('홍보각')
        홍보각.menu = {'삼선짬뽕': '22000원', '고법불도장': '99000원', '군만두': '20000원'}
        홍보각.location = '서울 중구 동호로 287'
        self.이해랑예술극장_list.append(홍보각)

        서울신라호텔팔선 = Restaurunt('서울신라호텔팔선')
        서울신라호텔팔선.menu = {'삼선짜장': '23000원', '파파야전복수프': '67000원', '해산물맑은수프': '48000원'}
        서울신라호텔팔선.location = '서울 중구 동호로 249'
        self.이해랑예술극장_list.append(서울신라호텔팔선)

        # 일식
        스시도 = Restaurunt('스시도')
        스시도.menu = {'런치초밥': '8000원', '스시도초밥': '10000원', '스페셜초밥': '13000원'}
        스시도.location = '서울 중구 동호로30길 37'
        self.이해랑예술극장_list.append(스시도)

        돈돈돈까스 = Restaurunt('돈돈돈까스')
        돈돈돈까스.menu = {'등심돈까스': '9900원', '정식 안심생선': '9900원', '생선까스': '10500원'}
        돈돈돈까스.location = '서울 중구 동호로24길 19-4'
        self.이해랑예술극장_list.append(돈돈돈까스)

        스시효 = Restaurunt('스시효 앰배서더점')
        스시효.menu = {'Lunch Hyo Course': '65000원', 'Dinner Sun Course': '143000원', 'Lunch Wa Course ': '80000원'}
        스시효.location = '서울 중구 동호로 287'
        self.이해랑예술극장_list.append(스시효)

        # 양식
        도치피자 = Restaurunt('도치피자 장충점')
        도치피자.menu = {'디아볼라': '19500원', '프리마베라': '23500원', '꽈트로 포르마지': '22000원'}
        도치피자.location = '서울 중구 동호로24길 27-6'
        self.이해랑예술극장_list.append(도치피자)

        바이 = Restaurunt('레스토랑 바이 농축원')
        바이.menu = {'아보카도 샐러드 볼': '15000원', 'Caesar salad': '15000원', 'Gnocchi with onion': '22000원'}
        바이.location = '서울 중구 동호로24길 19'
        self.이해랑예술극장_list.append(바이)

        잭슨빌피자 = Restaurunt('잭슨빌피자 동국대점')
        잭슨빌피자.menu = {'입안가득 페퍼로니': '18000원', '간단하게 고르곤졸라': '15000원', '듬뿍듬뿍 치즈피자': '1400원'}
        잭슨빌피자.location = '서울 중구 서애로1길 12 3층'
        self.이해랑예술극장_list.append(잭슨빌피자)

        # 기타
        죠티인도레스토랑 = Restaurunt('죠티인도레스토랑')
        죠티인도레스토랑.menu = {'탄두리치킨': '17000원', '치킨티카케밥': '12000원', '달술바': '5000원'}
        죠티인도레스토랑.location = '서울 중구 서애로 12-4 고려빌딩51서'
        self.이해랑예술극장_list.append(죠티인도레스토랑)

        코나야 = Restaurunt('코나야 본사')
        코나야.menu = {'코나야 세트 A': '12300원', '코나야 세트 B': '12800원', '코나야 세트 C': '13300원'}
        코나야.location = '서울 중구 동호로14길 11 이베이테크빌딩 3층'
        self.이해랑예술극장_list.append(코나야)

        파파포 = Restaurunt('파파포')
        파파포.menu = {'불고기쌀국수': '7000원', '양지쌀국수': '8000원', '차돌박이쌀국수': '8500원'}
        파파포.location = '서울 중구 필동로 15-7'
        self.이해랑예술극장_list.append(파파포)

        # 디저트
        태극당 = Restaurunt('카페 마당')
        태극당.menu = {'태극당 모니카': '2500원', '버터케익': '22000원', '야채 사라다': '6000원'}
        태극당.location = '서울 중구 동호로24길 7'
        self.이해랑예술극장_list.append(태극당)

        옐로우테라스 = Restaurunt('옐로우테라스')
        옐로우테라스.menu = {'아메리카노': '4000원', '카페라떼': '4500원', '자몽에이드': '5500원'}
        옐로우테라스.location = '서울 중구 동호로 223 2층'
        self.이해랑예술극장_list.append(옐로우테라스)

        로이터 = Restaurunt('로이터 커피 셸터')
        로이터.menu = {'에스프레소': '5500원', '플렛화이트': '5500원', '라떼': '5500원'}
        로이터.location = '서울 중구 필동로 53 라비두스 별관 3층/루프탑'
        self.이해랑예술극장_list.append(로이터)


    def str_이해랑예술극장(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.이해랑예술극장_list[i].name}\n위치: {self.이해랑예술극장_list[i].location}\n메뉴: {self.이해랑예술극장_list[i].menu}\n별점: {self.이해랑예술극장_list[i].star}\n후기: {self.이해랑예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_이해랑예술극장()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.이해랑예술극장_list[i].name}\n위치: {self.이해랑예술극장_list[i].location}\n메뉴: {self.이해랑예술극장_list[i].menu}\n별점: {self.이해랑예술극장_list[i].star}\n후기: {self.이해랑예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_이해랑예술극장()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.이해랑예술극장_list[i].name}\n위치: {self.이해랑예술극장_list[i].location}\n메뉴: {self.이해랑예술극장_list[i].menu}\n별점: {self.이해랑예술극장_list[i].star}\n후기: {self.이해랑예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_이해랑예술극장()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.이해랑예술극장_list[i].name}\n위치: {self.이해랑예술극장_list[i].location}\n메뉴: {self.이해랑예술극장_list[i].menu}\n별점: {self.이해랑예술극장_list[i].star}\n후기: {self.이해랑예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_이해랑예술극장()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.이해랑예술극장_list[i].name}\n위치: {self.이해랑예술극장_list[i].location}\n메뉴: {self.이해랑예술극장_list[i].menu}\n별점: {self.이해랑예술극장_list[i].star}\n후기: {self.이해랑예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_이해랑예술극장()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.이해랑예술극장_list[i].name}\n위치: {self.이해랑예술극장_list[i].location}\n메뉴: {self.이해랑예술극장_list[i].menu}\n별점: {self.이해랑예술극장_list[i].star}\n후기: {self.이해랑예술극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_이해랑예술극장()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_이해랑예술극장(self):
        for i in range(18):
            print(f'{i + 1}. {self.이해랑예술극장_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.이해랑예술극장_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.이해랑예술극장_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.이해랑예술극장_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.이해랑예술극장_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.이해랑예술극장_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.이해랑예술극장_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.이해랑예술극장_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.이해랑예술극장_list[int(restaurunt_num) - 1].name}\n위치: {self.이해랑예술극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.이해랑예술극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.이해랑예술극장_list[int(restaurunt_num) - 1].star}\n후기: {self.이해랑예술극장_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.이해랑예술극장_list[int(restaurunt_num) - 1].name}\n위치: {self.이해랑예술극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.이해랑예술극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.이해랑예술극장_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_이해랑예술극장()


    def 정동극장(self):
        # 한식
        모모식당 = Restaurunt('모모식당')
        모모식당.menu = {'제육볶음': '9000원', '닭볶음탕백반': '9000원', '생삼겹살': '13000원'}
        모모식당.location = '서울 중구 정동길 17 이화정동빌딩'
        self.정동극장_list.append(모모식당)

        정동국시 = Restaurunt('정동국시')
        정동국시.menu = {'정동칼국수': '9000원', '정동국밥': '10000원', '만두국': '9000원'}
        정동국시.location = '서울 중구 정동길 5 정동경향갤러리'
        self.정동극장_list.append(정동국시)

        덕수정 = Restaurunt('덕수정')
        덕수정.menu = {'부대찌개': '8000원', '오징어볶음': '10000원', '삼치구이': '9000원'}
        덕수정.location = '서울 중구 정동길 41'
        self.정동극장_list.append(덕수정)

        # 중식
        서안 = Restaurunt('서안')
        서안.menu = {'짜장면': '7000원', '굴짬뽕': '10000원', '잡채밥': '9000원'}
        서안.location = '서울 중구 정동길 8 한성교회'
        self.정동극장_list.append(서안)

        백미원 = Restaurunt('백미원 시청점')
        백미원.menu = {'마라탕 1인세트': '8000원', '마라향궈(소)': '16800원', '팔보채덮밥': '12800원'}
        백미원.location = '서울 중구 서소문로11길 19 지하2층'
        self.정동극장_list.append(백미원)

        오한수 = Restaurunt('오한수 우육면가 시청점')
        오한수.menu = {'우육탕면': '8000원', '청경채 도가니 양지탕면': '10000원', '군만두(6P)': '6000원'}
        오한수.location = '서울 중구 서소문로 124'
        self.정동극장_list.append(오한수)

        # 일식
        댓짱돈까스 = Restaurunt('댓짱돈까스')
        댓짱돈까스.menu = {'장군정식': '15500원', '댓짱정식': '15000원', '로스장군정식': '14500원'}
        댓짱돈까스.location = '서울 중구 정동길 17'
        self.정동극장_list.append(댓짱돈까스)

        사누키야 = Restaurunt('사누키야')
        사누키야.menu = {'사누키우동': '5000원', '냉우동': '7000원', '자루소바': '7000원'}
        사누키야.location = '서울 중구 덕수궁길 7 오천회관빌딩'
        self.정동극장_list.append(사누키야)

        바닷가작은부엌 = Restaurunt('바닷가작은부엌 덕수궁점')
        바닷가작은부엌.menu = {'바닷가 해초 정식': '28000원', '보리굴비 정식': '29000원', '새꼬시 코스': '35000원'}
        바닷가작은부엌.location = '서울 중구 덕수궁길 7 오천회관4층'
        self.정동극장_list.append(바닷가작은부엌)

        # 양식
        정원레스토랑 = Restaurunt('정원레스토랑 어반가든')
        정원레스토랑.menu = {'평일런치20종(11:30~14:30)': '19000원 ~ 39000원', '평일디너60종(휴일종일)': '16000원 ~ 59000원', '코스6종 세트4종(평일2시반이후, 휴일종일)': '35000원 ~ 160000원)'}
        정원레스토랑.location = '서울 중구 정동길 12-15'
        self.정동극장_list.append(정원레스토랑)

        메이드인시카고피자 = Restaurunt('메이드인시카고피자 덕수궁점')
        메이드인시카고피자.menu = {'시카고 치즈 피자': '12000원', '시카고 페퍼로니 피자': '14000원', '시카고 F 세트': '20000원'}
        메이드인시카고피자.location = '서울 중구 덕수궁길 5'
        self.정동극장_list.append(메이드인시카고피자)

        몽로 = Restaurunt('광화문 몽로')
        몽로.menu = {'연어 샐러드(점심)': '16000원', '문어 샐러드(저녁)': '30000원', '감자뇨끼(저녁)': '26000원'}
        몽로.location = '서울 중구 세종대로21길 40 1층'
        self.정동극장_list.append(몽로)

        # 기타
        생어거스틴 = Restaurunt('생어거스틴 광화문파이낸스점')
        생어거스틴.menu = {'뿌 팟 봉커리': '32000원', '왕새우 팟타이': '18000원', '똠얌꿍': '21000원'}
        생어거스틴.location = '서울 중구 세종대로 136'
        self.정동극장_list.append(생어거스틴)

        호아빈 = Restaurunt('호아빈 서울시청점')
        호아빈.menu = {'양지쌀국수(M)': '9000원', '소고기샤브쌀국수 ': '12000원', '새우완탕쌀국수': '12000원'}
        호아빈.location = '서울 중구 서소문로 139'
        self.정동극장_list.append(호아빈)

        도스타코스 = Restaurunt('도스타코스 시청배달점')
        도스타코스.menu = {'소프트 타코': '10500원', '나쵸 피에스타': '9900원', '새우 치즈 께사디야': '12900원'}
        도스타코스.location = '서울 중구 서소문로 115 한산빌딩'
        self.정동극장_list.append(도스타코스)

        # 디저트
        리에제 = Restaurunt('덕수궁 리에제 와플')
        리에제.menu = {'와플플레인': '3400원', '와플메이플': '4100원', '와플크림치즈': '4700원'}
        리에제.location = '서울 중구 덕수궁길 5'
        self.정동극장_list.append(리에제)

        르풀 = Restaurunt('르풀')
        르풀.menu = {'르풀파니니(런치메뉴)': '9800원', '치킨파니니(런치메뉴)': '8900원', '햄치즈파니니(런치메뉴)': '8900원'}
        르풀.location = '서울 중구 정동길 33 신아일보'
        self.정동극장_list.append(르풀)

        라운드앤드 = Restaurunt('라운드앤드')
        라운드앤드.menu = {'더치아메리카노': '4000원', '아메리카노': '5000원', '라떼': '5500원'}
        라운드앤드.location = '서울 중구 정동길 35 두비빌딩'
        self.정동극장_list.append(라운드앤드)


    def str_정동극장(self):
        print('1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 기타\n6. 디저트')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        kind = input('❤ 음식 종류를 선택하세요 👉 ')

        if kind == '1':
            print('- 한식 -')
            for i in range(3):
                print(f'{i + 1}.')
            print(
                f'이름: {self.정동극장_list[i].name}\n위치: {self.정동극장_list[i].location}\n메뉴: {self.정동극장_list[i].menu}\n별점: {self.정동극장_list[i].star}\n후기: {self.정동극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_정동극장()
        elif kind == '2':
            print('- 중식 -')
            for i in range(3, 6):
                print(f'{i - 2}.')
            print(
                f'이름: {self.정동극장_list[i].name}\n위치: {self.정동극장_list[i].location}\n메뉴: {self.정동극장_list[i].menu}\n별점: {self.정동극장_list[i].star}\n후기: {self.정동극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_정동극장()
        elif kind == '3':
            print('- 일식 -')
            for i in range(6, 9):
                print(f'{i - 5}.')
            print(
                f'이름: {self.정동극장_list[i].name}\n위치: {self.정동극장_list[i].location}\n메뉴: {self.정동극장_list[i].menu}\n별점: {self.정동극장_list[i].star}\n후기: {self.정동극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_정동극장()
        elif kind == '4':
            print('- 양식 -')
            for i in range(9, 12):
                print(f'{i - 8}.')
            print(
                f'이름: {self.정동극장_list[i].name}\n위치: {self.정동극장_list[i].location}\n메뉴: {self.정동극장_list[i].menu}\n별점: {self.정동극장_list[i].star}\n후기: {self.정동극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_정동극장()
        elif kind == '5':
            print('- 기타 -')
            for i in range(12, 15):
                print(f'{i - 11}.')
            print(
                f'이름: {self.정동극장_list[i].name}\n위치: {self.정동극장_list[i].location}\n메뉴: {self.정동극장_list[i].menu}\n별점: {self.정동극장_list[i].star}\n후기: {self.정동극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_정동극장()
        elif kind == '6':
            print('- 디저트 -')
            for i in range(15, 18):
                print(f'{i - 14}.')
            print(
                f'이름: {self.정동극장_list[i].name}\n위치: {self.정동극장_list[i].location}\n메뉴: {self.정동극장_list[i].menu}\n별점: {self.정동극장_list[i].star}\n후기: {self.정동극장_list[i].review}')
            yesorno = input('별점을 남기시겠습니까? (y/n) 👉 ')
            if yesorno == 'y':
                self.star_정동극장()
        else:
            print('처음으로 돌아갑니다 🏃')


    def star_정동극장(self):
        for i in range(18):
            print(f'{i + 1}. {self.정동극장_list[i].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        restaurunt_num = input('❤ 별점을 남길 식당을 선택하세요 👉 ')
        print(f'선택 식당 👉 {self.정동극장_list[int(restaurunt_num) - 1].name}')
        print('다른 번호를 누르면 처음으로 돌아갑니다')
        star = input('별 개수 (1, 2, 3, 4, 5) 👉 ')
        if star == '1':
            self.정동극장_list[int(restaurunt_num) - 1].star = '★☆☆☆☆'
        elif star == '2':
            self.정동극장_list[int(restaurunt_num) - 1].star = '★★☆☆☆'
        elif star == '3':
            self.정동극장_list[int(restaurunt_num) - 1].star = '★★★☆☆'
        elif star == '4':
            self.정동극장_list[int(restaurunt_num) - 1].star = '★★★★☆'
        elif star == '5':
            self.정동극장_list[int(restaurunt_num) - 1].star = '★★★★★'
        else:
            print('처음으로 돌아갑니다 🏃')
        yesorno = input('후기를 남기시겠습니까? (y/n) 👉 ')
        if yesorno == 'y':
            self.정동극장_list[int(restaurunt_num) - 1].review = input('후기 작성(엔터키 누르면 종료) 👉 ')
            print(
                f'이름: {self.정동극장_list[int(restaurunt_num) - 1].name}\n위치: {self.정동극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.정동극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.정동극장_list[int(restaurunt_num) - 1].star}\n후기: {self.정동극장_list[int(restaurunt_num) - 1].review}')
        elif yesorno == 'n':
            print(
                f'이름: {self.정동극장_list[int(restaurunt_num) - 1].name}\n위치: {self.정동극장_list[int(restaurunt_num) - 1].location}\n메뉴: {self.정동극장_list[int(restaurunt_num) - 1].menu}\n별점: {self.정동극장_list[int(restaurunt_num) - 1].star}')
        else:
            print('처음으로 돌아갑니다 🏃')

        self.str_정동극장()