# Companion Planting Script for 5x Harvest with 4 Drones
# This script divides the farm into 4 sections and uses 4 drones to plant Bushs
# and companion plants independently in each section.
import NewFunction

def plant_section_1():
	#"""Plant in top-left section"""
	size = get_world_size()
	half_size = size // 2
	companions_to_plant = []
	
	# Plant in snake pattern within top-left section (0,0 to half_size,half_size)
	for y in range(0, half_size):
		if y % 2 == 0:  # Even rows: left to right
			for x in range(0, half_size):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break
						
		
		else:  # Odd rows: right to left
			for x in range(half_size-1, -1, -1):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break

def plant_section_2():
	#"""Plant in top-right section"""
	size = get_world_size()
	half_size = size // 2
	companions_to_plant = []
	
	# Plant in snake pattern within top-right section (half_size,0 to size,half_size)
	for y in range(0, half_size):
		if y % 2 == 0:  # Even rows: left to right
			for x in range(half_size, size):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break
		
		else:  # Odd rows: right to left
			for x in range(size-1, half_size-1, -1):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break

def plant_section_3():
	#"""Plant in bottom-left section"""
	size = get_world_size()
	half_size = size // 2
	companions_to_plant = []
	
	# Plant in snake pattern within bottom-left section (0,half_size to half_size,size)
	for y in range(half_size, size):
		if y % 2 == 0:  # Even rows: left to right
			for x in range(0, half_size):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break
		
		else:  # Odd rows: right to left
			for x in range(half_size-1, -1, -1):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break

def plant_section_4():
	#"""Plant in bottom-right section"""
	size = get_world_size()
	half_size = size // 2
	companions_to_plant = []
	
	# Plant in snake pattern within bottom-right section (half_size,half_size to size,size)
	for y in range(half_size, size):
		if y % 2 == 0:  # Even rows: left to right
			for x in range(half_size, size):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break
		
		else:  # Odd rows: right to left
			for x in range(size-1, half_size-1, -1):
				# Move to position (x, y)
				while get_pos_x() != x:
					if get_pos_x() < x:
						move(East)
					else:
						move(West)
				while get_pos_y() != y:
					if get_pos_y() < y:
						move(North)
					else:
						move(South)
				
				# Plant Bush
				cur_x = get_pos_x()
				cur_y = get_pos_y()
				i_x = 0
				i_y = 0
				if_p = 0
				
				for plant_type_pref,target_x, target_y in companions_to_plant:
					if cur_x == target_x and cur_y == target_y:
						# Plant the companion plant if position is empty
						#if get_entity_type() == None:
						#print(companions_to_plant)
						NewFunction.NewPlant(plant_type_pref)
						companions_to_plant.remove((plant_type_pref,target_x, target_y))
						if_p = 1
						break
				if if_p ==0:
					#print(companions_to_plant)
					NewFunction.NewPlant('Bush')
	
				# Get companion preference and add to array
					companion = get_companion()
					if companion != None:
						plant_type_pref, (target_x, target_y) = companion
						if companions_to_plant == []: 
							companions_to_plant.append((plant_type_pref,target_x, target_y))
						else:
							for plant_type_pref, i_x,i_y in companions_to_plant:
								if target_x == i_x and target_y == i_y:
									break
								else:
									companions_to_plant.append((plant_type_pref,target_x, target_y))
									break

def main():
	#"""Main function to execute multi-drone companion planting strategy"""
	# Spawn 3 additional drones to work on different sections
	spawn_drone(plant_section_2)  # Drone 1: Top-right section
	spawn_drone(plant_section_3)  # Drone 2: Bottom-left section
	spawn_drone(plant_section_4)  # Drone 3: Bottom-right section
	
	# Main drone (drone 0) works on top-left section
	plant_section_1()

# Run the main function
if __name__ == "__main__":
	while True:
		main()
