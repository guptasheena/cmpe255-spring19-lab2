def mean_num_friends(x):
    sum = 0
    for num in x:
        sum += num
    print("mean=" + str(sum/len(x)))


def median_num_friends(x):
    x.sort()
    length = len(x)

    if (length < 0):
        print("median= NA")
    elif (length % 2 == 0):
        print("median=" + str((x[length//2] + x[length // 2 - 1]) / 2))
    else:
        print("median=" + str(x[length//2]))


num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
mean_num_friends(num_friends)
median_num_friends(num_friends)
