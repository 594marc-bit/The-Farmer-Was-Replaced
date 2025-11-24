def step(previousdir,tree,knot):

	#initialize

	dir2num = {North:0,East:1,South:2,West:3}

	num2dir = {0:North,1:East,2:South,3:West}

	dir = []

	avaliabledir = []

	

	#acquire direction

	dir.append(can_move(North))

	dir.append(can_move(East))

	dir.append(can_move(South))

	dir.append(can_move(West))

	for idx in range(4):

		if dir[idx] and previousdir != idx:

			avaliabledir.append(idx)

	

	#move

	if len(avaliabledir) == 0:

		return 0, None, tree, knot

	elif len(avaliabledir) == 1:

		move(num2dir[avaliabledir[0]])

		if avaliabledir[0] == 0:

			p = 2

		elif avaliabledir[0] == 2:

			p = 0

		elif avaliabledir[0] == 1:

			p = 3

		else:

			p = 1

		return 1, p, tree, knot 

	elif len(avaliabledir) == 2:

		for i in tree:

			#if back from a dead end

			if tree[i][1] == [get_pos_x(),get_pos_y()]:

				if tree[i][3] == 0:

					for j in avaliabledir:

						if j != previousdir and j != tree[i][2]:

							tree[i][3] = 1

							for k in tree[i][0]:

								if k != knot:

									currentknot = k

							move(num2dir[j])

							if j == 0:

								p = 2

							elif j == 2:

								p = 0

							elif j == 1:

								p = 3

							else:

								p = 1

							return 2, p, tree, currentknot

				#if "i" knot has been finished, goto senior knot

				if tree[i][3] == 1:

					tree[i][3] = 2

					currentknot = i

					move(num2dir[tree[i][2]])

					if tree[i][2] == 0:

						p = 2

					elif tree[i][2] == 2:

						p = 0

					elif tree[i][2] == 1:

						p = 3

					else:

						p = 1

					return 2, p, tree, currentknot

		treelength=0

		for i in tree:

			treelength = treelength + len(tree[i][0])

		currentknot = treelength+1

		tree[knot] = [[treelength+1,treelength+2],[get_pos_x(),get_pos_y()],[],0]

		move(num2dir[avaliabledir[0]])

		if avaliabledir[0] == 0:

			p = 2

		elif avaliabledir[0] == 2:

			p = 0

		elif avaliabledir[0] == 1:

			p = 3

		else:

			p = 1

		tree[knot][2] = previousdir 

		return 2, p, tree, currentknot 

	else:

		for i in tree:

			#if back from a dead end

			if tree[i][1] == [get_pos_x(),get_pos_y()]:

				if tree[i][3] == 0:

					for j in avaliabledir:

						if j != previousdir and j != tree[i][2]:

							tree[i][3] = 1

							tree[i][4] = previousdir

							for k in tree[i][0]:

								if k != knot:

									currentknot = k

							move(num2dir[j])

							if j == 0:

								p = 2

							elif j == 2:

								p = 0

							elif j == 1:

								p = 3

							else:

								p = 1

							return 3, p, tree, currentknot

			#if back from a dead end

			if tree[i][1] == [get_pos_x(),get_pos_y()]:

				if tree[i][3] == 1:

					for j in avaliabledir:

						if j != previousdir and j != tree[i][2] and j != tree[i][4]:

							tree[i][3] = 2

							for k in tree[i][0]:

								if k != knot:

									currentknot = k

							move(num2dir[j])

							if j == 0:

								p = 2

							elif j == 2:

								p = 0

							elif j == 1:

								p = 3

							else:

								p = 1

							return 3, p, tree, currentknot

				#if "i" knot has been finished, goto senior knot

				if tree[i][3] == 2:

					tree[i][3] = 3

					currentknot = i

					move(num2dir[tree[i][2]])

					if tree[i][2] == 0:

						p = 2

					elif tree[i][2] == 2:

						p = 0

					elif tree[i][2] == 1:

						p = 3

					else:

						p = 1

					return 3, p, tree, currentknot

		treelength=0

		for i in tree:

			treelength = treelength + len(tree[i][0])

		currentknot = treelength+1

		#the last element is recording the dir that finished

		tree[knot] = [[treelength+1,treelength+2,treelength+3],[get_pos_x(),get_pos_y()],[],0,0]

		move(num2dir[avaliabledir[0]])

		if avaliabledir[0] == 0:

			p = 2

		elif avaliabledir[0] == 2:

			p = 0

		elif avaliabledir[0] == 1:

			p = 3

		else:

			p = 1

		tree[knot][2] = previousdir 

		return 3, p, tree, currentknot



 

 

def mainprogram(size):		

	#initialize

	clear()

	plant(Entities.Bush)

	use_item(Items.Weird_Substance, size * 2**(num_unlocked(Unlocks.Mazes) - 1))

	#tree = {idx: [[subknot1,subknot2],[x,y],return direction,if arrived]}

	tree = {0:[[1],[-1,-1],[None],[0]]}

	previousdir = "Start"

	knot = 1

	

	if get_entity_type() == Entities.Treasure:

		harvest()

	

	while 1:

		stage,previousdir,tree,knot = step(previousdir,tree,knot)

		if stage == 0:

			if get_entity_type() == Entities.Treasure:

				harvest()

				break



while 1:

	mainprogram(16)

	