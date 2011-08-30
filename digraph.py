#!/usr/bin/env python

import networkx as nx
import random

def connect_digraph(D):
	""" Take a DiGraph with weakly connected components, and coalesce into one component."""

	s = nx.weakly_connected_component_subgraphs(D)
	#s is sorted by the size of the subgraph

	if len(s) > 1:
		largest = s[0]
		remaining = s[1:]

		largest_edges = largest.edges()

		#Let's filter out the one degree edges (otherwise we'll disconnect 
		#the graph when we swap edges around).
		candidates = []
		for u,v in largest_edges:
			if D.degree(u) > 1 and D.degree(v) > 1:
				candidates.append((u,v))

		if len(candidates) < len(remaining):
			raise Exception("There are not enough candidates for swapping.")

		#Connect the largest subgraph to the remaining.
		for G in remaining:
			u,v = random.choice(candidates)
			x,y = random.choice(G.edges())

			D.remove_edge(u, v)
			D.remove_edge(x, y)
			D.add_edge(u, y)
			D.add_edge(x, v)

			largest_edges.remove((u,v))
