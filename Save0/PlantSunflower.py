import NewFunction

def count_sunflowers():
	#"""Count total sunflowers on the entire farm"""
	count = 0
	ws = get_world_size()
	original_x, original_y = get_pos_x(), get_pos_y()
	
	for x in range(ws):
		for y in range(ws):
			NewFunction.NewMove(x, y)
			if get_entity_type() == Entities.Sunflower:
				count += 1
	
	NewFunction.NewMove(original_x, original_y)
	return count

def find_max_petal_sunflower():
	#"""Find and harvest all sunflowers with maximum petals for 5x bonus"""
	ws = get_world_size()
	max_petals = 0
	max_sunflowers = []  # List of (x,y) coordinates for sunflowers with max petals
	original_x, original_y = get_pos_x(), get_pos_y()
	
	# First, check if there are at least 10 sunflowers on the farm
	if count_sunflowers() < 10:
		return  # Not enough sunflowers for bonus
	
	# Scan entire farm to find all sunflowers with maximum petals
	for x in range(ws):
		for y in range(ws):
			NewFunction.NewMove(x, y)
			if get_entity_type() == Entities.Sunflower and can_harvest():
				petal_count = measure()
				if petal_count > max_petals:
					max_petals = petal_count
					max_sunflowers = [(x, y)]  # Reset list with new max
				elif petal_count == max_petals:
					max_sunflowers.append((x, y))
	
	# Harvest all max petal sunflowers
	for x, y in max_sunflowers:
		NewFunction.NewMove(x, y)
		harvest()
		# After harvesting, immediately plant a new sunflower to maintain count
		if get_entity_type() == None:
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Sunflower)
	
	NewFunction.NewMove(original_x, original_y)

def optimized_sunflower_section(start_x, end_x, start_y, end_y):
	#"""Optimized sunflower planting for a section with efficient harvesting"""
	while True:
		# Normal planting and harvesting in assigned section
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				NewFunction.NewMove(x, y)
				entity_type = get_entity_type()
				
				# Harvest if ready (normal harvesting)
				if entity_type == Entities.Sunflower and can_harvest():
					harvest()
				
				# Plant new sunflower if tile is empty
				if get_entity_type() == None:
					if get_ground_type() == Grounds.Grassland:
						till()
					plant(Entities.Sunflower)

def specialized_scanner():
	#"""Dedicated scanner drone that continuously finds and harvests max petal sunflowers"""
	while True:
		find_max_petal_sunflower()

def plant_section_0():
	#"""Plant and harvest sunflowers in section 0 (top-left quadrant)"""
	ws = get_world_size()
	half = ws / 2
	start_x = 0
	end_x = half - 1
	start_y = 0
	end_y = half - 1
	optimized_sunflower_section(start_x, end_x, start_y, end_y)

def plant_section_1():
	#"""Plant and harvest sunflowers in section 1 (top-right quadrant)"""
	ws = get_world_size()
	half = ws / 2
	start_x = half
	end_x = ws - 1
	start_y = 0
	end_y = half - 1
	optimized_sunflower_section(start_x, end_x, start_y, end_y)

def plant_section_2():
	#"""Plant and harvest sunflowers in section 2 (bottom-left quadrant)"""
	ws = get_world_size()
	half = ws / 2
	start_x = 0
	end_x = half - 1
	start_y = half
	end_y = ws - 1
	optimized_sunflower_section(start_x, end_x, start_y, end_y)

# Main program
# Spawn drones: 3 for planting sections, 1 dedicated scanner
if num_drones() < max_drones():
	spawn_drone(plant_section_1)
if num_drones() < max_drones():
	spawn_drone(plant_section_2)
if num_drones() < max_drones():
	spawn_drone(specialized_scanner)

# Main drone plants in section 0
plant_section_0()
