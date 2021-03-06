# Import DFA from Eppstein
from lib.Automata import *
from pprint import pprint


states = {}

x = int(input("Enter k: "))
# this is for a test
for i in range(0, x):
	print "========================= state: ", i, "===================================="
	states[i] = {}
	for j in range(0,10):
		states[i][j] = set(str(int(str(i)+str(j)) % x));
		print "Input:", j, "--->", int(str(i)+str(j)) % x
		print
delta = {'A' : { '0' : set(['B']), '1': set(['B','C'])}, 
	'B': {'0': set(['C']), '1':set(['D'])}, 
	'C': {'0':set(['A', 'B']), '1': set(['D'])}, 
	'D': {'0': set(['D']), '1': set(['D'])}
 } 
alphabet = set(['0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9']);
nfa = LookupNFA(alphabet, 'A', states, 'D')
pprint(delta)



#this prints stuff. idk if it works or not or what.
# alphabet = set([0, 1, 2, 3, 4, 5, 6, 7, 8,9]);
# delta = { 'A' : { '0' : set(['B']), '1': set(['B','C'])}, 
#  'B': {'0': set(['C']), '1':set(['D'])}, 
#  'C': {'0':set(['A', 'B']), '1': set(['D'])}, 
#  'D': {'0': set(['D']), '1': set(['D'])}} 
# N = LookupNFA("ABCD", delta, 'A',['C'])
# pprint(delta)