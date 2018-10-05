
list1 = []
count = 0
sum = 0
try:
    while True:
        n = input("enter a valid number")
        n = int(n)
        list1.append(n)
        if n == 'done':
            print('done')
            for i in list1:
                count = count +1
                sum = sum + i
                Average = sum/count
            print('sum is {}' .format(sum))
            print('count is {}' .format(count))
            print('Average is {}' .format(Average))
            break
except:
    print('invalid input')
    for i in list1:
        count = count + 1
        sum = sum + i
        Average = sum / count
    print('sum is {}'.format(sum))
    print('count is {}'.format(count))
    print('Average is {}'.format(Average))



