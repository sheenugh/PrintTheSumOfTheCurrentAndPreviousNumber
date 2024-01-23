# #----- FUNCTION/S -----


#----- PSEUDO CODE -----

previous_num = 0
for i in range(10):
    sum = previous_num + i
    if previous_num == i:
        print("Current Number: ", i, "   Previous Number: ", previous_num, "   Sum: ", sum)