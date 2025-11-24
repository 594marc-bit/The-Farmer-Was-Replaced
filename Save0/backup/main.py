import NewFunction
import GetPower

NewFunction.NewMove(0,0)

while True:

	for i in range(get_world_size()):
		#print(i)
	
		if num_items(Items.Power) > 300:
			pass 
		else:
		
			while num_items(Items.Power) < 600:
				GetPower.GetPower()
				if can_harvest():
					harvest()
					plant(Entities.Sunflower)
					use_item(Items.Water) 
					use_item(Items.Fertilizer) 
					use_item(Items.Water) 
		
	
		if get_pos_x() < 6 and  get_pos_y() < 6: #左下
			NewFunction.NewPlant('Pumpkin')
			use_item(Items.Water)
			while not can_harvest():
				do_a_flip()
				plant(Entities.Pumpkin)
				#use_item(Items.Water)
			move(North)
			continue

		if get_pos_x() < 6 and get_pos_y() < 12: #左上
			NewFunction.NewPlant('Pumpkin')
			use_item(Items.Water)
			while not can_harvest():
				do_a_flip()
				plant(Entities.Pumpkin)
				#use_item(Items.Water)
			move(North)
			continue			
		
#			if get_pos_y() - get_pos_x() == 6:
#				NewFunction.NewPlant('Tree')
#				move(North)
#				continue
#					
#			if num_items(Items.Hay) < num_items(Items.Carrot):
#				NewFunction.NewPlant('Grass')
#				move(North)
#				continue
#			else:
#				NewFunction.NewPlant('Carrot')
#				move(North)
#				continue
			

			#continue
		
		if get_pos_x() > 5 and get_pos_y() < 6: #右下
			if get_pos_x() - get_pos_y() == 6:
				NewFunction.NewPlant('Tree')
				move(North)
				continue
									
			if num_items(Items.Hay) < num_items(Items.Carrot):
				NewFunction.NewPlant('Bush')
#				substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
#				use_item(Items.Weird_Substance, substance)
				move(North)
				continue
			else:
				NewFunction.NewPlant('Bush')
#				substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
#				use_item(Items.Weird_Substance, substance)
				move(North)
				continue
		
		if get_pos_x() > 5 and get_pos_y() > 5: #右上
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
	

	