class p():
	def __init__(self,l,m):
		self.cells = l
		self.count = m
	def known_mines(self):
		if len(self.cells) == self.count:
			return self.cells	
		return None

	def known_safes(self):
		if self.count < 1:
			return self.cells	
		return None

	
knowledge = []
q = set()
q.add((2,3))
q.add((52,3))
q.add((2,43))
q.add((12,3))

qs = set()
qs.add((2,32))
qs.add((522,3))
qs.add((22,43))
qs.add((124,3))

knowledge.append(p(q, 0))
knowledge.append(p(qs, 4))


popping = {"safe":[], "mine":[], "removing":[]}
for sentence in knowledge:
	if sentence.known_mines():
		popping["mine"].append(sentence.known_mines())
	elif sentence.known_safes():
		popping["safe"].append(sentence.known_safes())
print(popping)

def mark_safe(cell):
	for i in knowledge:
		if cell in i.cells:
			i.cells.remove(cell)

def mark_mine(cell):
	for i in knowledge:
		if cell in i.cells:
			i.cells.remove(cell)


for safe_set in popping["safe"]:
	for safe_cell in safe_set:
		mark_safe(safe_cell)
for mine_set in popping["mine"]:
	for mine_cell in mine_set:
		mark_mine(mine_cell)

print(knowledge)
