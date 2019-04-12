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
	name1_word_count = 0
	name1_picture_count = 0
	name1_strike_count = 0
	name2_word_count = 0
	name2_strike_count = 0
	name2_picture_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == name1:
			if s[2] == '貼圖':
				name1_strike_count += 1
			elif s[2] == '圖片':
				name1_picture_count += 1
			else:
				for msg in s[2:]:
					name1_word_count += len(msg)
		elif name == name2:
			if s[2] == '貼圖':
					name2_strike_count += 1
			elif s[2] == '圖片':
					name2_picture_count += 1
			else:
					for msg in s[2:]:
						name2_word_count += len(msg)
		else:
			print('此對話紀錄未含有此人名')
			return 0
			break
	print(f'{name1}說了 {name1_word_count} 個字')
	print(f'{name1}傳了 {name1_strike_count} 張貼圖') 
	print(f'{name1}傳了 {name1_picture_count} 張圖片')
	print(' ')
	print(f'{name2}說了 {name2_word_count} 個字') 
	print(f'{name2}傳了 {name2_strike_count} 張貼圖')
	print(f'{name2}傳了 {name2_picture_count} 張圖片')
#寫入新的對話紀錄
def writ_file(filename, output):
	with open (filename, 'w', encoding = 'utf-8') as file:
		for p in output:
			file.write(p + '\n')

#主程式執行
def main():
	user_input = input('請輸入要讀取的LINE對話紀錄: ')
	user_name1 = input('請輸入對話紀錄內人名1: ')
	user_name2 = input('請輸入對話紀錄內人名2: ')
	lines = read_file(user_input)
	lines = convert(lines, user_name1, user_name2)

main()
