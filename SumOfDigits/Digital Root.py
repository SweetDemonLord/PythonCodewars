def digital_root(n):
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

#def digital_root(n):
    #if n < 10:
        #return n
   # return digital_root(sum(int(d) for d in str(n)))

#def digital_root(n):
    #while n >= 10:
       # n = sum(int(d) for d in str(n))
    #return n

print(digital_root(16))      # Output: 7
print(digital_root(942))     # Output: 6
print(digital_root(132189))  # Output: 6
print(digital_root(493193))  # Output: 2