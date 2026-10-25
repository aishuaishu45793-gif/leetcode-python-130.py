numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to remove: "))

result = [number for number in numbers if number != target]

print("Updated list:", result)