#Recursive Approach

def fibonacci_series(n):
    if n <= 0:
        return 0
    elif n == 1:
         return [0]
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

#Iterative Approach
# def fibonacci_series(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     series = [0,1]
#     for i in range(2,n):
#         next_val= series[-1] + series[-2]
#         series.append(next_val)
        
#     return series


# n= int(input("Enter a number:"))
# result =fibonacci_series(n)
# print(f'Fibonacci series of {n} terms are: {result}')
