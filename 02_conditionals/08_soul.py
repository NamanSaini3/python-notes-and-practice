password = "sec7655848"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "medium"
else:
    strength = "storong"

print("password strength is ", strength)   

