def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	for line in lines:
		if line == 'Allen':
			person ='Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		new.append(person + ':' + line)
	return new
def writ_file(filename, output):
	with open (filename, 'w', encoding = 'utf-8') as file:
		for p in output:
			file.write(p + '\n')
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	writ_file('output.txt', lines)


main()