import time

print('This program will calculate the sum for 1 to the number you input.')

number = int(input('Please input a positive integer: '))

start = time.time()

#print(start)

sum1_1000=0

for i in range(1,number+1):
    sum1_1000 = sum1_1000 + i

end = time.time()

print('The sum of 1 to %s is: %s' % (number,sum1_1000))

print('Total time is: ' + str(end-start))
