def count_vowels(Sample):
    string_count = len(Sample)
    count=0
    for word in Sample:
        for char in word:
            if char in "aeiouAEIOU":
                count +=1
    return count
                
                
Sample = input('Enter a string: ')
print(count_vowels(Sample))
