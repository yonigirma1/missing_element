#Four ways to find the missing element given two arrays.
#The second array is created by shuffling the first array and
#taking out a random number


#First way of doing it
def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


#Second way of doing it
import colletions

def finder2(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

#Third way of doing it
def finder3(arr1, arr2):
    sum1 = 0
    sum2 = 0

    for num in arr1:
        sum1 = sum1 + num

    for num in arr2:
        sum2 = sum2 + num

    return sum1 - sum2


#Fourth way of doing it
def finder4(arr1, arr2):
    result = 0

    for num in arr1 + arr2:
        result ^= num

    return result
                    
