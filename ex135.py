def prime_calc(limit):
    nums = list(range(limit + 1))
    nums[0] = 0
    nums[1] = 0
    
    p = 2
    
    while p * p <= limit:
        if nums[p] != 0:
            for multiple in range(p * 2, limit + 1, p):
                nums[multiple] = 0
        p += 1
    primes = [num for num in nums if num != 0] 
    return primes

limit = int(input('Please type in your max number for me to calculate all the prime numbers in between: '))
print(prime_calc(limit))
