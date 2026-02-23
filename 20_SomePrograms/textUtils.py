"""
Write a program as below:
Output:
    Enter the content:
    Want do you want? (upper, lower, capitalize) :
"""
print("----------------------------------------------------------------------------")
content = input("Enter the content: ")
ask = input("Want do you want? (upper, lower, capitalize): ")
print("----------------------------------------------------------------------------")
if ask == "upper":
    print(content.upper())
elif ask == "lower":
    print(content.lower())
elif ask == "capitalize":
    print(content.capitalize())
else:
    print("Please choose valid ask.")
print("----------------------------------------------------------------------------")
