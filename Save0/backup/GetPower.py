import NewFunction

def PlantSunflower():
	
	for i in range(get_pos_x()):
		move(West)
	for i in range(get_world_size()-get_pos_y()-1):
		move(North)
	
	
	
	for x in range(1):
		NewFunction.NewPlant('Sunflower')
		use_item(Items.Water) 
		for i in range(4):
			move(East)
			NewFunction.NewPlant('Sunflower')
			use_item(Items.Water) 
		move(South)
		NewFunction.NewPlant('Sunflower')
		use_item(Items.Water) 
		for i in range(4):
			move(West)
			NewFunction.NewPlant('Sunflower')
			use_item(Items.Water) 
		
		#print(x)
		#if x != 1: #最后一次循环时不往下移动和种植
		#	move(South)
		#	NewFunction.NewPlant('Carrot')
		#	use_item(Items.Water) 


def GetPower():
	#global Xm
	#global Ym
	Xm = 0	
	Ym = 0
	Pm = 0
	
	NewFunction.NewMove(0,15)
	
	measure()
	
	for x in range(1):
		if measure() > Pm:
			Pm = measure()
			Xm = get_pos_x()
			Ym = get_pos_y() 
		#NewFunction.NewPlant('Sunflower')
		for i in range(4):
			move(East)
			if measure() > Pm:
				Pm = measure()
				Xm = get_pos_x()
				Ym = get_pos_y() 
		move(South)
		if measure() > Pm:
			Pm = measure()
			Xm = get_pos_x()
			Ym = get_pos_y() 
			
		for i in range(4):
			move(West)
			if measure() > Pm:
				Pm = measure()
				Xm = get_pos_x()
				Ym = get_pos_y()
		#print(x)
		#if x != 1: #最后一次循环时不往下移动和种植
		#	move(South)
		#	if measure() > Pm:
		#		Pm = measure()
		#		Xm = get_pos_x()
		#		Ym = get_pos_y()
	
	NewFunction.NewMove(Xm,Ym)
	do_a_flip()
	#do_a_flip()
	#print(Xm,Ym)
	return Xm,Ym

#GetPower()

#PlantSunflower()

#NewFunction.NewMove(x)
#PlantSunflower()