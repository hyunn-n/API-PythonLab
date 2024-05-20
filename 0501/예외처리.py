while True:
    user_input = input("정수 입력 : > ")
    # 문자열.isdigit() 메서드를 사용하면
    # 문자열이 숫자로만 구성되어 있는지 여부를 판별해 준다


    if user_input.isdigit():
        number_input = int(user_input)
        print("원의 둘레 :", 2 * 3.14 * number_input)
        break


    else:
        print("(오류발생)정수로만 입력해 주세요")