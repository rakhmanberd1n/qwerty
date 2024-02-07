def spy_game(nums, n):
    for i in range(0,n):
        if nums[i]==0:
            i+=1
            for j in range(i, n):
                if nums[j]==0:
                    j+=1
                    for l in range(j,n):
                        if nums[l]==7:
                            return True
    return False

nums = []

n=int(input("Give me the size of list: "))
print("Write down elements of the list: ")
for i in range(0, n):
    inp = int(input())
    nums.append(inp)

if spy_game(nums, n):
    print("True, list contains 007 in order")
else:
    print("False, list do not contain 007 in order")