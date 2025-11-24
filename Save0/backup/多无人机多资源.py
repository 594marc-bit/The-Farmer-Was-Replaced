import NewFunction
import GetPower
import PlantPumpkin

i_ws = get_world_size()
i_md = 2

def PlantV2():
	if get_pos_x() < i_ws//2 and  get_pos_y() < i_ws//2: 
		if get_pos_x() == get_pos_y():
				NewFunction.NewPlant('Tree')
#				move(North)
#				continue
							
		if num_items(Items.Hay) < num_items(Items.Carrot):
			NewFunction.NewPlant('Grass')
#			move(North)
#			continue
		else:
			NewFunction.NewPlant('Carrot')
#			move(North)
#			continue

	if get_pos_x() < i_ws//2 and  get_pos_y() < i_ws: #左上
	
		
		if get_pos_y() - get_pos_x() == i_ws/2:
			NewFunction.NewPlant('Tree')
#			move(North)
#			continue
				
		if num_items(Items.Hay) < num_items(Items.Carrot):
			NewFunction.NewPlant('Grass')
#			move(North)
#			continue
		else:
			NewFunction.NewPlant('Carrot')
#			move(North)
#			continue
			

			#continue
		
	if get_pos_x() >= i_ws//2  and get_pos_y() < i_ws//2 : #右下
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			NewFunction.NewPlant('Tree')
#			move(North)
		else:
			NewFunction.NewPlant('Bush')

									
#		if num_items(Items.Hay) < num_items(Items.Carrot):
#			NewFunction.NewPlant('Bush')
#			move(North)
#			continue
#		else:
#			NewFunction.NewPlant('Bush')
#			move(North)
#			continue
		
	if get_pos_x() >= i_ws//2  and get_pos_y() >= i_ws//2 : #右上
		if get_pos_x() == get_pos_y():
			NewFunction.NewPlant('Tree')
#			move(North)
#			continue
							
		if num_items(Items.Hay) < num_items(Items.Carrot):
			NewFunction.NewPlant('Grass')
#			move(North)
#			continue
		else:
			NewFunction.NewPlant('Carrot')
#			move(North)
#			continue
	



def drone_function():
	for i in range(i_ws / i_md):

		if i % 2 == 1: #偶数列，从上往下种南瓜


			for i_2 in range(i_ws / i_md):
				if i_2 +1 == i_ws / i_md :
					move(East)
					continue
				
				#NewFunction.NewPlant('Grass')
				PlantV2()	
				move(South)
				i_2 += 1
				

		if i % 2 == 0: #奇数列，从下往上检查是否死活着无南瓜，并种上

			for i_1 in range(i_ws / i_md):
				
				if i_1 + 1 ==  i_ws / i_md:

					move(East)
					continue

				#NewFunction.NewPlant('Carrot')	
				PlantV2()
				move(North)
				i_1 += 1

					#move(East)
				#print(i_3)

#NewFunction.NewMove(0,0)
#drone_function()
while True:
	for x,y in [(0,0),(0,16),(16,16),(16,0)]:
	
		NewFunction.NewMove(x,y)
		spawn_drone(drone_function)
	
	
	NewFunction.NewMove(16,0)
	drone_function()
	