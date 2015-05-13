from p6_game import Simulator
from heapq import heappush, heappop

ANALYSIS = {}

def analyze(design):
	sim = Simulator(design)
	init = sim.get_initial_state()

	#BFS
	ANALYSIS = {init: None}

	q = [init]

	while q:
		node = q.pop()

		#no goal state required as we're doing an exhaustive search

		moves = sim.get_moves()
		#see all possible states for each move
		states = []
		for move in moves:
			#NONETYPE not iterable error
			if sim.get_next_state(node, move) != None:
				pos, abil = sim.get_next_state(node, move)
				newState = (pos, abil)
						
				states.append(newState)

		#Use ANALYSIS like a prev dict, only each key now has states so the solution will be unique for each set of abilities
		for state in states:
			if state not in ANALYSIS:
				ANALYSIS[state] = node
				q.append(state)

	# TODO: fill in this function, populating the ANALYSIS dict
	#raise NotImplementedError

def inspect((i,j), draw_line):
	#search the dict for every solution that starts with that pos, the build paths from each soltion back to the start
	#Error: ANALYSIS is empty when called here despite analyze being called previously
	print ANALYSIS
	# TODO: use ANALYSIS and (i,j) draw some lines

	#raise NotImplementedError
