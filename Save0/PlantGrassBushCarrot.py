import NewFunction
import GetPower
import PlantPumpkin

i_ws = get_world_size()

NewFunction.NewMove(0,0)


while True:
	while num_items(Items.Carrot) > 200000000:
		PlantPumpkin.PlantPumpkin()
		
	
	for i in range(get_world_size()):
		#print(i)
	
		if get_pos_x() < i_ws//2 and  get_pos_y() < i_ws//2: #左下
			if get_pos_x() == get_pos_y():
				NewFunction.NewPlant('Tree')
				move(North)
				continue
							
			if num_items(Items.Hay) < num_items(Items.Carrot):
				NewFunction.NewPlant('Grass')
				move(North)
				continue
			else:
				NewFunction.NewPlant('Carrot')
				move(North)
				continue


		if get_pos_x() < i_ws//2 and  get_pos_y() < i_ws: #左上
	
		
			if get_pos_y() - get_pos_x() == i_ws/2:
				NewFunction.NewPlant('Tree')
				move(North)
				continue
					
			if num_items(Items.Hay) < num_items(Items.Carrot):
				NewFunction.NewPlant('Grass')
				move(North)
				continue
			else:
				NewFunction.NewPlant('Carrot')
				move(North)
				continue
			

			#continue
		
		if get_pos_x() >= i_ws//2  and get_pos_y() < i_ws//2 : #右下
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				NewFunction.NewPlant('Tree')
				move(North)
				continue
									
			if num_items(Items.Hay) < num_items(Items.Carrot):
				NewFunction.NewPlant('Bush')
				move(North)
				continue
			else:
				NewFunction.NewPlant('Bush')

				move(North)
				continue
		
		if get_pos_x() >= i_ws//2  and get_pos_y() >= i_ws//2 : #右上
			if get_pos_x() == get_pos_y():
				NewFunction.NewPlant('Tree')
				move(North)
				continue
							
			if num_items(Items.Hay) < num_items(Items.Carrot):
				NewFunction.NewPlant('Grass')
				move(North)
				continue
			else:
				NewFunction.NewPlant('Carrot')
				move(North)
				continue
		
		move(North)
#		if get_pos_y() != 0:
#			harvest()
	move(East)
	

	