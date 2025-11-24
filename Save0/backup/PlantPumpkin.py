import NewFunction


def PlantPumpkin():
	i_ws = get_world_size()
	Col_i = 0
	NewFunction.NewMove(0,0)
	
	for i in range(i_ws*2):
		#print(i)
		if i == 10000: #不执行
			NewFunction.NewMove(0,0)
			for i_1 in range(i_ws):
				NewFunction.NewMove(0,i_1)
				NewFunction.NewPlant('Pumpkin')
			move(East)
			continue
		
		if i % 2 == 1: #偶数列，从上往下种南瓜
			#print(i_1)
			for i_2 in range(i_ws,0,-1):
				#print(i2)
				NewFunction.NewPlant('Pumpkin')	
				if get_pos_y() != 0:
					move(South)
				else:
					#print('End',get_pos_y())
					move(West)

		if i % 2 == 0: #奇数列，从下往上检查是否死活着无南瓜，并种上
			#move(West)
			for i_3 in range(i_ws):
				#print(i3)
				if get_entity_type() != Entities.Pumpkin:
					NewFunction.NewPlant('Pumpkin')	
				if get_pos_y() != i_ws-1:
					move(North)
				else:
					#print('End2',get_pos_y())
					move(East)
					move(East)
				#print(i_3)

