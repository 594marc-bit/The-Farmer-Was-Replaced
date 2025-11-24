#t=
#0 Grass
#1 plant(Entities.Bush)
#2 plant(Entities.Carrot)
#3 plant(Entities.Pumpkin)
#4 plant(Entities.Tree)
#5 plant(Entities.Sunflower)

def NewPlant(t):
	if t == 'Grass':
		harvest()
		if get_ground_type() == Grounds.Soil:
			till()
	
	if t == 'Bush':
		harvest()
		plant(Entities.Bush)
	
	if t == 'Carrot':
		if can_harvest():
				harvest()

		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Carrot)
		else:
			plant(Entities.Carrot)		

	if t == 'Pumpkin':
		if can_harvest():
			harvest()

		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Pumpkin)
		else:
			plant(Entities.Pumpkin)		
			
	if t == 'Tree':
		if can_harvest():
			harvest()
		else:
			till()
		plant(Entities.Tree)
		
	if t == 'Cactus':
		if can_harvest():
			harvest()

		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Cactus)
		else:
			plant(Entities.Cactus)			

	
	if t == 'Sunflower':
		if can_harvest():
				harvest()

		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Sunflower)
#			while measure() <  11:
#				if can_harvest():
#					harvest()
#					plant(Entities.Sunflower)
				
		else:
			plant(Entities.Sunflower)	
#			while measure() <  11:
#				if can_harvest():
#					harvest()
#					plant(Entities.Sunflower)
#-----------------------------------------------
#移动到指定坐标
#			
def NewMove(X,Y):
	CX = get_pos_x()
	CY = get_pos_y()
	
	if CX > X:
		for a in range(CX - X):
			move(West)
	else:
		for a in range(X - CX):
			move(East)
	
	if CY > Y:
		for b in range(CY - Y):
			move(South)
	else:
		for b in range(Y - CY):
			move(North)	

			
		
			
			
			