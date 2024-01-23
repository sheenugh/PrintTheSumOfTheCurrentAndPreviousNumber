
#----- PSEUDO CODE -----
# - Getting the Loop of prev, current, and sum number
previous_num = 0
for i in range(10):
    sum = previous_num + i
    print("Current Number ", i,  "Previous Number: ", previous_num,  "Sum: ", sum) 
    previous_num = i
    
