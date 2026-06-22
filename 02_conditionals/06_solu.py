distance  = 14

if distance < 3:
    trasportation = "walk"
elif distance < 15:
    trasportation = "bike"
else:
    trasportation = "car"

print("AI Recommendation for you the transportation of:", trasportation)