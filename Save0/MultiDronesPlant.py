import NewFunction

def plant_section_0():
	ws = get_world_size()
	i = 0
	j = 0
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Grass'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_1():
	ws = get_world_size()
	i = 0
	j = 1
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Bush'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_2():
	ws = get_world_size()
	i = 0
	j = 2
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Bush'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_3():
	ws = get_world_size()
	i = 0
	j = 3
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Pumpkin'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_4():
	ws = get_world_size()
	i = 1
	j = 0
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Carrot'#tree
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_5():
	ws = get_world_size()
	i = 1
	j = 1
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Cactus'
	
	while True:
		# 先种植仙人掌
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)
		
		# 纵向排序（按列）
		for col in range(start_x, end_x + 1):
			NewFunction.NewMove(col, start_y)
			while True:
				m = 0  # 移动仙人掌的次数
				if measure(North) == None:  # 如果到了边界顶端直接退出循环
					break
				while measure() <= measure(North):  # 当前小于上方
					move(North)
					m += 1
					if get_pos_y() == end_y:
						break
				if m == section_height - 1:  # 如果都小于上方，表示此列排序完成
					break
				while measure() > measure(North):  # 如果大于上方
					swap(North)
					m += 1
					move(North)
					if get_pos_y() == end_y:
						break
				if m == 0:  # 如果以上情况均未触发，说明已经完成排序
					break
				NewFunction.NewMove(col, start_y)
		
		# 横向排序（按行）
		for row in range(start_y, end_y + 1):
			NewFunction.NewMove(start_x, row)
			while True:
				m = 0  # 移动仙人掌的次数
				if measure(East) == None:  # 如果到了边界右端直接退出循环
					break
				while measure() <= measure(East):  # 当前小于右方
					move(East)
					m += 1
					if get_pos_x() == end_x:
						break
				if m == section_width - 1:  # 如果都小于右方，表示此行排序完成
					break
				while measure() > measure(East):  # 如果大于右方
					swap(East)
					m += 1
					move(East)
					if get_pos_x() == end_x:
						break
				if m == 0:  # 如果以上情况均未触发，说明已经完成排序
					break
				NewFunction.NewMove(start_x, row)

def plant_section_6():
	ws = get_world_size()
	i = 1
	j = 2
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Sunflower'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_7():
	ws = get_world_size()
	i = 1
	j = 3
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Grass'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_8():
	ws = get_world_size()
	i = 2
	j = 0
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Bush'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_9():
	ws = get_world_size()
	i = 2
	j = 1
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Carrot'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_10():
	ws = get_world_size()
	i = 2
	j = 2
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Pumpkin'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_11():
	ws = get_world_size()
	i = 2
	j = 3
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Carrot' #tree
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_12():
	ws = get_world_size()
	i = 3
	j = 0
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Cactus'
	
	while True:
		# 先种植仙人掌
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)
		
		# 纵向排序（按列）
		for col in range(start_x, end_x + 1):
			NewFunction.NewMove(col, start_y)
			while True:
				m = 0  # 移动仙人掌的次数
				if measure(North) == None:  # 如果到了边界顶端直接退出循环
					break
				while measure() <= measure(North):  # 当前小于上方
					move(North)
					m += 1
					if get_pos_y() == end_y:
						break
				if m == section_height - 1:  # 如果都小于上方，表示此列排序完成
					break
				while measure() > measure(North):  # 如果大于上方
					swap(North)
					m += 1
					move(North)
					if get_pos_y() == end_y:
						break
				if m == 0:  # 如果以上情况均未触发，说明已经完成排序
					break
				NewFunction.NewMove(col, start_y)
		
		# 横向排序（按行）
		for row in range(start_y, end_y + 1):
			NewFunction.NewMove(start_x, row)
			while True:
				m = 0  # 移动仙人掌的次数
				if measure(East) == None:  # 如果到了边界右端直接退出循环
					break
				while measure() <= measure(East):  # 当前小于右方
					move(East)
					m += 1
					if get_pos_x() == end_x:
						break
				if m == section_width - 1:  # 如果都小于右方，表示此行排序完成
					break
				while measure() > measure(East):  # 如果大于右方
					swap(East)
					m += 1
					move(East)
					if get_pos_x() == end_x:
						break
				if m == 0:  # 如果以上情况均未触发，说明已经完成排序
					break
				NewFunction.NewMove(start_x, row)

def plant_section_13():
	ws = get_world_size()
	i = 3
	j = 1
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Sunflower'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_14():
	ws = get_world_size()
	i = 3
	j = 2
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Grass'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

def plant_section_15():
	ws = get_world_size()
	i = 3
	j = 3
	section_width = ws // 4
	section_height = ws // 4
	start_x = j * section_width
	if j < 3:
		end_x = (j + 1) * section_width - 1
	else:
		end_x = ws - 1
	start_y = i * section_height
	if i < 3:
		end_y = (i + 1) * section_height - 1
	else:
		end_y = ws - 1
	plant_type = 'Bush'
	
	while True:
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant(plant_type)

if num_drones() < max_drones():
	spawn_drone(plant_section_1)
if num_drones() < max_drones():
	spawn_drone(plant_section_2)
if num_drones() < max_drones():
	spawn_drone(plant_section_3)
if num_drones() < max_drones():
	spawn_drone(plant_section_4)
if num_drones() < max_drones():
	spawn_drone(plant_section_5)
if num_drones() < max_drones():
	spawn_drone(plant_section_6)
if num_drones() < max_drones():
	spawn_drone(plant_section_7)
if num_drones() < max_drones():
	spawn_drone(plant_section_8)
if num_drones() < max_drones():
	spawn_drone(plant_section_9)
if num_drones() < max_drones():
	spawn_drone(plant_section_10)
if num_drones() < max_drones():
	spawn_drone(plant_section_11)
if num_drones() < max_drones():
	spawn_drone(plant_section_12)
if num_drones() < max_drones():
	spawn_drone(plant_section_13)
if num_drones() < max_drones():
	spawn_drone(plant_section_14)
if num_drones() < max_drones():
	spawn_drone(plant_section_15)
#  主线程执行第0部分的种植任务12
plant_section_0()
