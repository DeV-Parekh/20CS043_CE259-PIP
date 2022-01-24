n = int(input())

# converting input to list
room = list(map(int, input().split()))
# creating empty list
room_no_repeat = []

# creating list of non repeated elements
for i in room:
    if i not in room_no_repeat:
        room_no_repeat.append(i)

print(room_no_repeat)
# printing element of which count is not equal to n
for i in room_no_repeat:
    if room.count(i) != n:
        print(i)
