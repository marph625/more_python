def solution(number):
    empty_list = []
    if number < 0:
        print(0)
    else:
        for x in range(number - 1):
            x += 1
            if x % 3 == 0 or x % 5 == 0:
                empty_list.append(x)
    print(empty_list)
    sum_of_elements = sum(empty_list)
    print(sum_of_elements)


solution(16)
