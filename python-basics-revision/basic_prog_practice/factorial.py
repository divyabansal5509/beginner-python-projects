#Recursive Approach:

def factorial(n):
    result = 1
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1)
        
try:
    n= int(input("Enter a number:"))
    print(factorial(n))
except ValueError:
    print("Provide a valid integer value")
    
#Iterative Approach:
# def factorial(n):
#     result = 1
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
    
#     for i in range(1,n+1):
#             result *= i

#     return result

# try:
#     n= int(input("Enter a number:"))
#     print(factorial(n))
# except ValueError:
#     print("Provide a valid integer value")
    


        
    
    