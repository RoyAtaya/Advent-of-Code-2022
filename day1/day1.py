data = open("day1/d1input.txt", "r")

curr_sum = 0
arr = []
for idx, item in enumerate(data):
    if item == "\n":
        arr.append(curr_sum)
        curr_sum = 0
        continue
    curr_sum += int(item)
else:
    arr.append(curr_sum)

arr = sorted(arr,reverse=True)
print("task 1: ", arr[0])

print("task 2: ",arr[0], "+", arr[1], "+", arr[2],"=", sum(arr[0:3]))
data.close()