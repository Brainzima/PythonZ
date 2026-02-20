zeba = {
    "fullName" : "Zeba Parween",
    "qualification" : "Gradute",
    "mobile" : 67634878433,
    "email" : "zeba@gmail.com",
    "address" : "Bindekhalpur, Sapna gali, 000000"
}
print(zeba)

 # method 1
zeba["mobile"]=46565674454
print(zeba)

#method 2
zeba.update({"qualification":"Post Graduate"})
print(zeba)