def has_33(nums, n):
    for i in range(1,n):
        if nums[i]==3 and 3==(nums[i-1]):
            return True
    return False

nums = []

n=int(input("Give me the size of list: "))
print("Write down elements of the list: ")
for i in range(0, n):
    inp = int(input())
    nums.append(inp)

if has_33(nums, n):
    print("True, list contains 3 next to 3 somewhere")
else:
    print("False, list do not contain 3 next to 3 somewhere")