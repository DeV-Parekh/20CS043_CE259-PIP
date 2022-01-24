# Taking length input
n = int(input())

# Taking numbers input in a list
numbers = list(map(int, input().split()))

# To check whether input length is equal to n
if len(numbers) == n:
    # Reversing sorting set of the numbers list
    sorted_set = sorted(set(numbers), reverse=True)
    # printing the 2nd element
    print(sorted_set[1])
