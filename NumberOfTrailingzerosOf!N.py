def zeros(n):
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    return count

print(zeros(0), "Testing with n = 0")                     #0
print(zeros(6), "Testing with n = 6")                     #1
print(zeros(30), "Testing with n = 30")                   #7
print(zeros(100), "Testing with n = 100")                 #24
print(zeros(1000), "Testing with n = 1000")               #249
print(zeros(100000), "Testing with n = 100000")           #24999
print(zeros(1000000000), "Testing with n = 1000000000")   #249999998