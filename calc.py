'''
With this code we will be testing unitests for some easy functions
'''

def multiply(a, b):
    '''This function takes two numbers and multiplies them'''
    return a * b

def add(a, b):
    '''This function takes two numbers and adds them'''
    return a + b

def divide(a, b):
    '''This function takes two numbers and divides them'''
    if b == 0:
        raise ValueError('division by zero is not allowed!!!')
    return a / b


#print(multiply(1,2))
#print(divide(1, 0))