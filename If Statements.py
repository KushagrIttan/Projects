
is_male = False
is_tall = False

if is_male and is_tall:
   print("You are a male and tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and (is_tall):
    print("You are a tall male")
else:
    print("You are ether not male and not tall")