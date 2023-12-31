#hard 3

def Digit(n):
    count = 0
    fact = 1
    i = 1
    
    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    
    return count

# Example usage:
n = int(input("n = "))
result = Digit(n)
print(result)