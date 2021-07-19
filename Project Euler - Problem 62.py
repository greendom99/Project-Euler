list_of_cubes = []
for n in range(1, 1000000):
    list_of_cubes.append(n ** 3)


def search():
    for length in range(1, 15):
        sample_cubes = []
        for cube in list_of_cubes:
            if len(str(cube)) == length:
                sample_cubes.append(cube)

        digits_dict = {}
        for cube in sample_cubes:
            digits_list = []
            for digit in str(cube):
                digits_list.append(int(digit))
            digits_list.sort()

            if tuple(digits_list) in digits_dict:
                digits_dict[tuple(digits_list)] += 1
            else:
                digits_dict[tuple(digits_list)] = 1

        if 5 in digits_dict.values():
            my_list = [k for k, count in digits_dict.items() if count == 5]
            answer = 100000000000000
            for entry in my_list:
                check_list = []
                for digit in entry:
                    check_list.append(digit)

                for cube in sample_cubes:
                    temp_list = []
                    for digit in str(cube):
                        temp_list.append(int(digit))
                    temp_list.sort()
                    if temp_list == check_list:
                        if cube < answer:
                            answer = cube
            return answer
        else:
            continue


print(search())
