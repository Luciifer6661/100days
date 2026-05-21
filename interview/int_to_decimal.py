import decimal

def int_to_decimal(input1, precision=2):
    print(type(input1))
    dec=decimal.Decimal(input1)
    return dec
    
print(type(int_to_decimal(100)))
    