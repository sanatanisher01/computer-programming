# program to create a dictionary with keys and values and print the keys in ascending order 
n = int(input())
d = {input(): input() for _ in range(n)}
print(*sorted(d.keys()), sep='\n')