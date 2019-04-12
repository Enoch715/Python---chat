#讀取對話紀錄
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
#將對話紀錄轉換所想要的形式
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person ='Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ':' + line)
	return new
#寫入新的對話紀錄
def writ_file(filename, output):
	with open (filename, 'w', encoding = 'utf-8') as file:
		for p in output:
			file.write(p + '\n')
#主程式執行
def main():
	user_input = input('請輸入想讀取的對話紀錄: ')
	lines = read_file(user_input)
	lines = convert(lines)
	writ_file('output.txt', lines)


main()