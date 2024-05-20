list_number = [10,20,30,40,50]

try:
    number_input = int(input("정수입력 > "))

    # 리스트의 요소 출력
    print(f'{number_input}번째 요소 : {list_number[number_input]}')

except Exception as ex:
    print("type(ex) :",type(ex))
    print("ex:", ex)
