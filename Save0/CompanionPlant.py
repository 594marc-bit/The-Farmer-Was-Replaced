# Companion Planting Script for 5x Harvest
# This script plants carrots in a snake pattern and then plants companion plants
# at the coordinates specified by each carrot's companion preference.
import NewFunction

def plant_carrots_snake_pattern():
	#"""Plant carrots in a snake pattern across the farm and plant companion plants when reaching their positions"""
	size = get_world_size()
	companions_to_plant = []
	
	# Single pass: plant carrots, collect companion info, and plant companions when reaching their positions
	for y in range(size):
		if y % 2 == 0:  # Even rows: left to right
			for x in range(size):
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
				
				# Plant carrot if ground is suitable
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
			for x in range(size-1, -1, -1):
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
				
				# Plant carrot if ground is suitable
				#NewFunction.NewPlant('Carrot')
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
	#"""Main function to execute companion planting strategy"""
	# First, plant carrots in snake pattern
	plant_carrots_snake_pattern()

# Run the main function
if __name__ == "__main__":
	set_world_size(12)
	while True:
		main()
		