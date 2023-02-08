def sumsquare(l):
    odd=0
    even=0
    for num in l:
        if num % 2==0:
            even+=num*num
        else:
            odd+=num*num
    return [odd,even]
l=list(map(int,input("Enter a list of integers separated by space: ").strip().split()))
result=sumsquare(l)
print("The sum of squares off odd numbers is:",result[0])
print("The sum of squares off even numbers is:",result[1])
