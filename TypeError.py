def divide_numbers(x, y):
    try:
        result = x / y
        print("Result of division:", result)
    except TypeError:
        print("Error: Division operation cannot be performed on the given types.")

x = 10
y = '2'  
divide_numbers(x, y)

