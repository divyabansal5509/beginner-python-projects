def is_palindrome(n):
    
    if n < 0:
        return False
    
    reversed_num = 0
    original = n
    
    while n > 0 :
            rem = n % 10
            reversed_num =reversed_num*10 + rem
            n = n//10
    
    return reversed_num == original
try:
    n = int(input("Enter a number to check palindrome: "))
    print(is_palindrome(n)) 
except ValueError:
    print("Invalid type value ,Please input an integer value")
    
    
# def is_palindrome(num):

#     if num < 0:
#         return False
    
#     s = str(num)
    
#     Reverse the string using slicing [::-1]
#     reversed_s = s[::-1]

#     return s == reversed_s


# print(is_palindrome(121))    # True
# print(is_palindrome(-121))   # False