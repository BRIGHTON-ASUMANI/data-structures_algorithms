def fizzBuzz(n):
    # Write your code here
    a="Fizz"
    b="Buzz"
    for x in range(1,n+1):
        print(a+b if x%15==0 else a if x%3==0 else b if x%5==0 else x)
