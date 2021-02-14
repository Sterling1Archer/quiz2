import math
a=0
b=0
c=0
x=0

def captureinputs():
    global a,b,c
    a = input("Enter the value for a: ")
    b = input("Enter the value for b: ")
    c = input("Enter the value for c: ")
    
    return


if __name__ == '__main__':
    captureinputs()
    #Calculate what's inside the square root
    b_pow_2 = math.pow(int(b),2)
    a_ac = 4*int(c)
    sqrt_temp = b_pow_2 - a_ac
    square_root = math.sqrt(sqrt_temp)
    
    b_prod = -1*int(b)
    numerator_positive = b_prod + square_root
    numerator_negative = b_prod - square_root
    denominator = 2*int(a)
    
    #Result for positive
    x_positive = numerator_positive / denominator
    print("x = ", x_positive)
    #Result for negative
    x_negative = numerator_negative / denominator
    print("x = ", x_negative)
