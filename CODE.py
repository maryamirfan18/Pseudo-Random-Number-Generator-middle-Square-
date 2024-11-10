seed = int(input("Enter a six digit number: ")) 
def random(): 
    global seed 
    s = str(seed ** 2) 
    while len(s) != 12: 
        s = "0" + s 
    seed = int(s[3:9]) 
    return seed 
for i in range(0,5): 
    print(random())