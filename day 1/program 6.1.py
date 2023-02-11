def countvowelStrings(n):
    return sum(range(1, n + 1))

n = int(input("Enter the lenght of the strings:"))
result = countvowelStrings(n)
print("the number of lexicographically sorted strings of length",n,"consisting only vowels is:",result)
