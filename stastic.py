def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def stastic(lines):
	new = []
	Allen_count = 0
	Allen_sticker_count = 0
	Viki_count = 0
	Viki_sticker_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				Allen_sticker_count += 1
			else:
				for msg in s[2:]:
					Allen_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1
			else:
				for msg in s[2:]:
					Viki_count += len(msg) 
	print('Allen說了',Allen_count, '個字' )
	print('Viki說了',Viki_count, '個字' )
	print('Allen用了', Allen_sticker_count,'個貼圖')
	print('Viki用了', Viki_sticker_count,'個貼圖')
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line+'\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = stastic(lines)
	#write_file('output,txt', lines)

main()