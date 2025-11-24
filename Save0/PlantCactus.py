import NewFunction


def PlantCactus():
	i_ws = get_world_size()*2
	NewFunction.NewMove(0,0)
	
	for c1 in range(i_ws/2):
		
		for r1 in range(i_ws/2):
			#print('r1',r1)
			NewFunction.NewPlant('Cactus')
			move(North)
			if r1+1 ==  i_ws/2 :
				NewFunction.NewMove(c1+1,0)
	
	#NewFunction.NewMove(0,0)	
#每一列排序		
	for c2 in range(i_ws/2):
		
		NewFunction.NewMove(c2,0)
		
		while True:
			
			m = 0 #移动仙人掌的次数
			
			if measure(North) == None: #如果到了边界顶端直接退出循环
				break

			while measure() <= measure(North): #当前小于上方
				move(North)                    #上移一格
				m += 1
				if get_pos_y() == i_ws/2-1:
					break 
			
			if m == i_ws/2-1: #如果都小于上方，表示此列排序完成
				break		  #退出循环，进入下一列排序
			#NewFunction.NewMove(c2,0)
			
			while measure() > measure(North): #如果大于上方
				swap(North)                   #上移一格
				m += 1
				move(North)
				if get_pos_y() == i_ws/2-1:  #上移一格后到顶端后退出循环避免出错
					break
			if m == 0: #如果以上情况均未触发，说明已经完成排序
				break	
			#print(measure(),measure(North))
			NewFunction.NewMove(c2,0)

#每一行排序		
	for r2 in range(i_ws/2):
		
		NewFunction.NewMove(0,r2)
		
		while True:
			
			m = 0 #移动仙人掌的次数
			
			if measure(East) == None: #如果到了边界顶端直接退出循环
				break

			while measure() <= measure(East): #当前小于上方
				move(East)                    #上移一格
				m += 1
				if get_pos_x() == i_ws/2-1:
					break 
			
			if m == i_ws/2-1: #如果都小于上方，表示此列排序完成
				break		  #退出循环，进入下一列排序
			#NewFunction.NewMove(c2,0)
			
			while measure() > measure(East): #如果大于上方
				swap(East)                   #上移一格
				m += 1
				move(East)
				if get_pos_x() == i_ws/2-1:  #上移一格后到顶端后退出循环避免出错
					break
			if m == 0: #如果以上情况均未触发，说明已经完成排序
				break	
			#print(measure(),measure(North))
			NewFunction.NewMove(0,r2)


while 1:
	set_world_size(12)
	PlantCactus()
	