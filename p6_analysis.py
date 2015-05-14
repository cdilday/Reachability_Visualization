from p6_game import Simulator
from heapq import heappush, heappop

import p6_tool

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
				
	return ANALYSIS
	# TODO: fill in this function, populating the ANALYSIS dict
	#raise NotImplementedError

def inspect(report, (i,j), draw_line):
	#search the dict for every solution that starts with that pos, the build paths from each soltion back to the start
	paths = []
	for node in report:
		if node[0] == (i, j):
			currNode = node
			offset = p6_tool.make_offset()
			color = p6_tool.make_color()
			while report[currNode] != None:
				draw_line(currNode[0], report[currNode][0], offset, color)
				currNode = report[currNode]
			
	# TODO: use ANALYSIS and (i,j) draw some lines

	#raise NotImplementedError
