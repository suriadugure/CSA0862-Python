def countVowelStrings(n):
    return sum(range(1,n+1))

n = int(input("Enter the length of the strings: "))
result = countVowelStrings(n)
print("The number of lexicographically sorted strings of length",n,"consisting only of vowels is:",result)