

def getFirstDigit(s):
	for c in s:
		if c.isdigit():
			return c

def getLastDigit(s):
	for c in s:
		if c.isdigit():
			return c

def par1():
	arr=[]
	with open('advent-of-code-1.txt', "r") as f:
		for line in f:
			x=''
			x+=getFirstDigit(line)
			x+=getLastDigit(line[::-1])
			#print(str(x))
			arr.append(int(x))

	print(sum(arr))
#-------------------------------------------------------------------------------
def parseFirstDigit(line):
	if len(line) == 1:
		if line.isdigit(): return line
		else: raise Exception('Linea lunga 1 ma non è un digit')
	elif len(line) == 2:
		if line[0].isdigit(): return line[0]
		else: return parseFirstDigit(line[1])
	elif len(line) == 3:
		if line[0].isdigit(): return line[0]
		elif line == 'one': return 1
		elif line =='two': return 2
		elif line == 'six': return 6
		else: return parseFirstDigit(line[1:])
	elif len(line) == 4:
		if line[0].isdigit(): return line[0]
		elif line == 'four': return 4
		elif line =='five': return 5
		elif line == 'nine': return 9
		elif line.startswith('one'): return 1
		elif line.startswith('two'): return 2
		elif line.startswith('six'): return 6
		else: return parseFirstDigit(line[1:])
	elif len(line) >= 5:
		if line[0].isdigit(): return line[0]
		elif line.startswith('one'): return 1
		elif line.startswith('two'): return 2
		elif line.startswith('three'): return 3
		elif line.startswith('four'): return 4
		elif line.startswith('five'): return 5
		elif line.startswith('six'): return 6
		elif line.startswith('seven'): return 7
		elif line.startswith('eight'): return 8
		elif line.startswith('nine'): return 9
		else: return parseFirstDigit(line[1:])



def parseLastDigit(line):
	if len(line) == 1:
		if line.isdigit(): return line
		else: raise Exception('Linea lunga 1 ma non è un digit')
	elif len(line) == 2:
		if line[0].isdigit(): return line[0]
		else: return parseLastDigit(line[1])
	elif len(line) == 3:
		if line[0].isdigit(): return line[0]
		elif line == 'eno': return 1
		elif line =='owt': return 2
		elif line == 'xis': return 6
		else: return parseLastDigit(line[1:])
	elif len(line) == 4:
		if line[0].isdigit(): return line[0]
		elif line == 'ruof': return 4
		elif line =='evif': return 5
		elif line == 'enin': return 9
		elif line.startswith('eno'): return 1
		elif line.startswith('owt'): return 2
		elif line.startswith('xis'): return 6
		else: return parseLastDigit(line[1:])
	elif len(line) >= 5:
		if line[0].isdigit(): return line[0]
		elif line.startswith('eno'): return 1
		elif line.startswith('owt'): return 2
		elif line.startswith('eerht'): return 3
		elif line.startswith('ruof'): return 4
		elif line.startswith('evif'): return 5
		elif line.startswith('xis'): return 6
		elif line.startswith('neves'): return 7
		elif line.startswith('thgie'): return 8
		elif line.startswith('enin'): return 9
		else: return parseLastDigit(line[1:])

def part2():
	arr=[]
	with open('advent-of-code-1.txt', "r") as f:
		for line in f:
			x=''
			x+=str(parseFirstDigit(line))
			x+=str(parseLastDigit(line[::-1]))
			print(str(x))
			arr.append(int(x))

	print("Sum: " + str(sum(arr)))



part2()