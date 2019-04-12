#讀取對話紀錄
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
#將對話紀錄轉換所想要的形式
def convert(lines, name1, name2):
	new = []
	person = None
	for line in lines:
		if line == name1:
			person = name1
			continue
		elif line == name2:
			person = name2
			continue
		if person:
			new.append(person + ':' + line)
		else:
			print('你輸入的人名未在此對話紀錄')
			return 0
			break
#寫入新的對話紀錄
def writ_file(filename, output):
	with open (filename, 'w', encoding = 'utf-8') as file:
		for p in output:
			file.write(p + '\n')
#主程式執行
def main():
	user_input = input('請輸入想讀取的對話紀錄: ')
	user_name1 = input('請輸入對話紀錄內人名1: ')
	user_name2 = input('請輸入對話紀錄內人名2: ')
	lines = read_file(user_input)
	lines = convert(lines, user_name1, user_name2)
	if lines != 0:
		writ_file('output.txt', lines)
		
main()