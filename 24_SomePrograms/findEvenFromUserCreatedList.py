# ask user for the start and end number and create a list of that range and display all even numbers
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

List = list(range(start, end+1))
print("Generated List:", List)

evenNumbers = []
for num in List:
    if num % 2 == 0:
        evenNumbers.append(num)

print("Even Number List:", evenNumbers)