import NewFunction

def PlantSunflowerGrid():
	#"""
	#在32x32网格上高效种植向日葵
	#使用蛇形模式覆盖整个网格
	#"""
	# 移动到网格起点
	NewFunction.NewMove(0, 0)
	
	for y in range(32):
		# 奇数行从左到右，偶数行从右到左（蛇形模式）
		if y % 2 == 0:
			# 从左到右
			for x in range(32):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant('Sunflower')
				use_item(Items.Water)
		else:
			# 从右到左
			for x in range(31, -1, -1):
				NewFunction.NewMove(x, y)
				NewFunction.NewPlant('Sunflower')
				use_item(Items.Water)

def PlantSunflowerSection(start_x, start_y, width, height):
	#"""
	#在指定区域种植向日葵
	#"""
	NewFunction.NewMove(start_x, start_y)
	
	for y in range(height):
		# 蛇形模式
		if y % 2 == 0:
			# 从左到右
			for x in range(width):
				NewFunction.NewMove(start_x + x, start_y + y)
				NewFunction.NewPlant('Sunflower')
				use_item(Items.Water)
		else:
			# 从右到左
			for x in range(width - 1, -1, -1):
				NewFunction.NewMove(start_x + x, start_y + y)
				NewFunction.NewPlant('Sunflower')
				use_item(Items.Water)

def CountSunflowers():
	#"""
	#统计当前向日葵数量
	#"""
	count = 0
	for y in range(32):
		for x in range(32):
			NewFunction.NewMove(x, y)
			if can_harvest() or measure() > 0:
				count += 1
	return count

def FindMaxPetalPosition():
	# 找到花瓣数量最多的向日葵位置
	# 使用优化的搜索模式
	max_petals = 0
	max_x = 0
	max_y = 0
	
	# 使用蛇形搜索模式
	for y in range(32):
		if y % 2 == 0:
			# 从左到右
			for x in range(32):
				NewFunction.NewMove(x, y)
				petals = measure()
				# 检查petals是否为None，如果是则跳过
				if petals != None and petals > max_petals:
					max_petals = petals
					max_x = x
					max_y = y
		else:
			# 从右到左
			for x in range(31, -1, -1):
				NewFunction.NewMove(x, y)
				petals = measure()
				# 检查petals是否为None，如果是则跳过
				if petals != None and petals > max_petals:
					max_petals = petals
					max_x = x
					max_y = y
	
	return max_x, max_y, max_petals

def SimpleFindMaxPetal():
	# 简化版的最大花瓣搜索，用于调试
	max_petals = 0
	max_x = 0
	max_y = 0
	
	# 只搜索部分区域进行测试
	for y in range(8):
		for x in range(8):
			NewFunction.NewMove(x, y)
			petals = measure()
			# 检查petals是否为None，如果是则跳过
			if petals != None and petals > max_petals:
				max_petals = petals
				max_x = x
				max_y = y
	
	return max_x, max_y, max_petals

def Drone1_Plant():
	# 无人机1负责左上区域 (0,0) 到 (15,15)
	PlantSunflowerSection(0, 0, 16, 16)

def Drone2_Plant():
	# 无人机2负责右上区域 (16,0) 到 (31,15)
	PlantSunflowerSection(16, 0, 16, 16)

def Drone3_Plant():
	# 无人机3负责左下区域 (0,16) 到 (15,31)
	PlantSunflowerSection(0, 16, 16, 16)

def Drone4_Plant():
	# 无人机4负责右下区域 (16,16) 到 (31,31)
	PlantSunflowerSection(16, 16, 16, 16)

def OptimizedGetPower():
	# 优化的能量收集策略
	# 使用多个无人机并行种植覆盖整个32x32网格
	spawn_drone(Drone1_Plant)
	spawn_drone(Drone2_Plant)
	spawn_drone(Drone3_Plant)
	spawn_drone(Drone4_Plant)
	
	# 等待种植完成（可以通过检查向日葵数量来判断）
	while CountSunflowers() < 900:  # 等待至少有900株向日葵（32x32=1024个位置）
		do_a_flip()  # 等待时执行空翻
	
	# 找到并收获花瓣最多的向日葵 - 使用完整版本搜索整个32x32网格
	max_x, max_y, max_petals = FindMaxPetalPosition()  # 使用完整版搜索整个网格
	if max_petals > 0:  # 如果找到有花瓣的向日葵
		# 移动到最大花瓣位置并收获
		NewFunction.NewMove(max_x, max_y)
		if can_harvest():
			harvest()
			do_a_flip()  # 庆祝
		else:
			while not can_harvest():
				do_a_flip()
			harvest()
		return max_x, max_y
	else:
		# 如果没有找到，使用原始方法
		return GetPowerOriginal()

def ContinuousEnergyCollection():
	# 持续能量收集循环
	while True:
		# 检查能量状态
		if num_items(Items.Power) > 500:
			do_a_flip()
			continue
		
		# 执行优化能量收集
		OptimizedGetPower()
		
		# 短暂休息
		for i in range(5):
			do_a_flip()

# 测试函数
def TestOptimizedSystem():
	# 测试优化系统
	# 测试单个区域种植
	PlantSunflowerSection(0, 0, 32, 32)
	
	# 测试向日葵计数
	count = CountSunflowers()
	
	# 测试最大花瓣搜索
	if count >= 10:
		max_x, max_y, max_petals = SimpleFindMaxPetal()

# 原始函数（用于备用方案）
def GetPowerOriginal():
	#"""
	#原始的能量收集函数，作为备用方案
	#"""
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
	
	NewFunction.NewMove(Xm,Ym)
	do_a_flip()
	return Xm, Ym

# 主执行函数
def Main():
	# 主执行函数 - 使用优化策略
	# 启动持续能量收集
	ContinuousEnergyCollection()

# 如果直接运行此文件，执行测试
if __name__ == "__main__":
	TestOptimizedSystem()
