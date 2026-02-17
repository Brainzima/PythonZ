intro = "hi guys, Rahman this side from Brainzima Innovation Institute."
print(intro)

print(intro.find("Brainzima"))

print(intro[31])

# let's assume that i want to extract the institute name from the intro
startT = intro.find("Brainzima")
print(startT)
print(intro[startT:])