from random import choice

def available (row, collums):
    available = []
    for a1 in range(1,collums+1):
        
        for a2 in range(1,row+1):
            position_xy = [a2, a1]
            available.append(position_xy)
    return available

def generate_boats(boat_parameters, available, row, collums):
    
    boats=[]
        
    for i in range(boat_parameters["quantity"]):    
        error = True
        position = choice(available)
        t = available.index(position)
        available.pop(t)
        
        directions = ['up', 'down', 'right', 'left']
        
        if position[0] - boat_parameters["lenght"] < 1:
            directions.pop(3)
        if position[0] + boat_parameters["lenght"] > collums :
            directions.pop(2)
        if position[1] - boat_parameters["lenght"] < 1 :
            directions.pop(0)
        if position[1] + boat_parameters["lenght"] > row :
            directions.pop(1)
        
        position_saved = position
            
        while error == True :
            boat=[position_saved]
            if directions == [] :
                available.append(position_saved)
                position = choice(available)
                directions = ['up', 'down', 'right', 'left']
                if position[0] - boat_parameters["lenght"] < 1:
                    directions.pop(3)
                if position[0] + boat_parameters["lenght"] > collums :
                    directions.pop(2)
                if position[1] - boat_parameters["lenght"] < 1 :
                    directions.pop(0)
                if position[1] + boat_parameters["lenght"] > row :
                    directions.pop(1)
                print("restart")
            where = choice(directions)
            position = position_saved
            print(position)
            print(where)
            for n in range(boat_parameters["lenght"]-1):
                            
                if where == 'right':
                   position = [position[0]+1,position[1] ] 
                if where == 'left':
                    position = [position[0]-1,position[1] ]
                if where == 'up':
                    position = [position[0],position[1]-1 ]
                if where == 'down':
                    position = [position[0],position[1]+1 ]
                    
                if position in available :
                    
                    t = available.index(position)
                    available.pop(t)
                    boat.append(position)
                    error = False
                    boats.append(boat)
                
                elif (position in available) == False :
                    print(position)
                    print('-----already used-----')
                    print(" ")
                    error = True
                    directions.pop(directions.index(where))
                    break
        
        #print("bateau = ")
        print (boat)
        print(" ")
    return boats
    
boat_lenght = 3

row = 10
collums = 10
boat_parameters_1 = {
    "lenght" : 4,
    "quantity" :  2}

boat_parameters_2 = {
    "lenght" : 5,
    "quantity" :  2}

available = available(row, collums)
boats = generate_boats(boat_parameters_1, available, row, collums)

boats = generate_boats(boat_parameters_2, available, row, collums)
#ne pas sortir du cadre du plateau 
