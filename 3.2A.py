bottles = 99 
while bottles > 0: 

    if bottles > 1: 
        bottle_word = "bottles" 

    else: 
        bottle_word = "bottle" 

    print(f"{bottles} {bottle_word} of beer on the wall") 

    print(f"{bottles} {bottle_word} of beer") 

    print("Take one down, pass it around") 

    bottles -= 1 

    if bottles > 1: 
        next_bottle_word = "bottles" 

    elif bottles == 1: 
        next_bottle_word = "bottle" 
    else: 
        next_bottle_word = "no bottles" 

    if bottles >= 0: 
        print(f"{bottles} {next_bottle_word} of beer on the wall!\n") 
    else: 
        print("No bottles of beer on the wall!\n")