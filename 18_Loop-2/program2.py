students= ["Zeba","Afiya","Neha","Shalini","Jitesh","Mitesh","Kumesh"]
# print(students)
#
# for name in students:
#     print(name)

txt = "Hi {}, Hope you are doing well. You are invited for the Iftaar Party!"
# print(txt)
# print(txt.format(students[0]))
# print(txt.format(students[1]))
# print(txt.format(students[2]))

for student in students:
    print(txt.format(student))