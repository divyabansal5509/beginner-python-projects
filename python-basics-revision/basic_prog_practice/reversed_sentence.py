def reversed_sentence(n):
    words= n.split()
    
    reversed = words[::-1]
    return " ".join(reversed)
    
n = input("Enter a string: ")
print(reversed_sentence(n))