import time

# example functions
def concatenate1(strings):
    result = ""
    for s in strings:
        result += s
    return result

def concatenate2(strings):
    return "".join(strings)

# run examples
chars = [str(char) for char in range(5000000)] 

print('Try first function')
start = time.time()
concatenate1(chars)
end = time.time()
print(end - start) # 92 seconds
print('Try second function')
start = time.time()
concatenate2(chars)
end = time.time()
print(end - start) # less than 0.1 seconds