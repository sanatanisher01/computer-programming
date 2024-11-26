# program to check if number is exist in list
def is_exist(lst, n):
    return n in lst

print(is_exist(list(map(int, input().split())), int(input())))
