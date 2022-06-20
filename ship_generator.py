from random import choice
class boat :
    def __init__ (self, row, collums, boat_parameters, available) :
       self.row = row
       self.collums = collums
       boat_parameters = []
       available = []
    
    def generate(boat_parameters, available, row, collums):
        
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
                    #print("restart")
                where = choice(directions)
                position = position_saved
                #print(position)
                #print(where)
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
                    
                    elif (position in available) == False :
                        #print(position)
                        #print('-----already used-----')
                        #print(" ")
                        error = True
                        boat = []
                        directions.pop(directions.index(where))
                        break
                    
                if boat != []:
                    boats.append(boat)
            #print("bateau = ")
            #print (boat)
            #print(" ")
        return boats

    
    
    #ne pas sortir du cadre du plateau 
