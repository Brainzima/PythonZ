zeba = {
    "fullName" : "Zeba Parween",
    "qualification" : "Gradute",
    "mobile" : 67634878433,
    "email" : "zeba@gmail.com",
    "address" : "Bindekhalpur, Sapna gali, 000000"
}
print(zeba)

#method 1
zeba["job"] = "TeleCaller"
print(zeba)

#method 2
zeba.update({"salary": 9896674000})
print(zeba)