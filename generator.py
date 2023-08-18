import random



def random_():
    list_of_alpha = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"

    star_length = 1 # integer for "for loop" , Feel free to modify it
    end_length = 5  # integer for "for loop" , Feel free to modify it

    for _ in range(star_length, end_length): # Length of pass
        with open('password.txt', 'a') as f:
            f.writelines(random.choice(list_of_alpha))
        with open('password.txt','r') as file:
            p = file.read()
    sym = "#@$&"
    
    p = p.join(sym)

    print(p)
    return p
    
    
    
    


    

    
    
    

