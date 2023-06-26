start = 1
end = 100
list_primes = []
list_multiple = []
for i in range(1, end + 1):
    if i > 1:
        for j in range(2, i + 1):
            if i % j == 0:
                list_multiple.append(j)
        if len(list_multiple) < 2:
            list_primes.append(i)
        list_multiple.clear()
print(f'List of prime numbers of 1 to 100: {list_primes}')

