# program to check number is present in a range or not
def is_in_range(n, start, end):
    return start <= n <= end

print(is_in_range(int(input("Enter number : ")), int(input("Enter start : ")), int(input("Enter end : "))))
