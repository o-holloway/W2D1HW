#Cube Number Test... Print out all cubed numbers up to the total value 1000. 
#Meaning that if the cubed number is over 1000 break the loop.

def cube_num_test():
    sum = 0
    n = 0
    while (sum < 999):
        sum = n ** 3
        print(f"{n} cubed = {sum}")
        n += 1

cube_num_test()