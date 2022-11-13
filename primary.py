import datetime
import time
import random
from miller_rabin import miller_rabin

def makeArrayFromNumber(number):
    return [int(x) for x in str(number)]

def divideByTwo(array):
    endings = [0, 2, 4, 6, 8]
    last = array[len(array)-1]
    if (last in endings):
        return True
    else:
        return False

def divideByFive(array):
    endings = [0, 5]
    last = array[len(array)-1]
    if (last in endings):
        return True
    else:
        return False

def divideByThree(array):
    sum = 0
    for i in range(0, len(array)):
        sum = sum + array[i]
    if(sum % 3 == 0):
        return True
    else:
        return False

def divideByEleven(number):
    if(number % 11 == 0):
        return True
    else:
        return False

def firstCheck(number):
    if number == 2 or number == 3:
        return True

    array = makeArrayFromNumber(number)
    if(number < 9223372036854775807):
        if(divideByTwo(array) or divideByFive(array) or divideByThree(array) or divideByEleven(number)):
            return False
        else:
            return True
    else:
        return 'out of range'

def secondCheck(number):
    x = miller_rabin(number, 10)
    return x
    # 9223372036854775807

# Press the green button in the gutter to run the script.
def if_prime(number):
    isPrime = False
    isSusspectedPrime = firstCheck(number)

    if (isSusspectedPrime):
        isPrime = secondCheck(number)

    return isPrime

# for i in range(1, 1000):
#     isPrime = False
#     start_time = time.process_time()
#     number = random.randint(2, 9223372036854775807)
#     isSusspectedPrime = firstCheck(number)
#
#     if(isSusspectedPrime):
#         isPrime = secondCheck(number)
#     end_time = time.process_time()
#     time_diff = end_time - start_time
#     print(time_diff)
#     print(number)
#     print(isPrime)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
