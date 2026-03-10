# ask user for the start and end number and create a list of that range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

List = list(range(start, end+1))
print(List)