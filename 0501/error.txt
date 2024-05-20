while True:
    try:
        # 사용자로 부터 입력을 받는다.
        number_input = int(input("정수입력 > "))


        # 출력
        print("원의둘레 : ", 2 * 3.14 * number_input)
        break


    except:
        print("(오류)잘못된 값을 입력했습니다")