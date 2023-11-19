from decimal import Decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return decimal_to_binary(decimal // 2) + str(decimal % 2)

test=int(input())
while test>0:
    decimal_number = Decimal(input())
    binary_number = decimal_to_binary(decimal_number)
    print( binary_number)
    test-=1
