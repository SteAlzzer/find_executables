# -*- coding: windows-1251 -*-
__author__ = 'm.kruglov'
__version__ = 1.0
import os
import sys


#### Usage ####
# Первый аргумент - путь до папки с бинарями.
# Второй - путь до файла с отчетом.
# Если не указать второй аргумент, будет подставлен по умолчанию (./binaries.tre)
# Если не указать первый аргумент, будет работать по текущему каталогу.

def main():
	if len(sys.argv) >= 2:
		dir_to_analyse = sys.argv[1]

		if len(sys.argv) == 3:
			output_file = sys.argv[2]
		else:
			output_file = './binaries.tre'
	else:
		dir_to_analyse = os.getcwd().replace('\\', '/') + '/'
		output_file = './binaries.tre'

	dir_to_analyse = os.path.abspath(dir_to_analyse)
	counter = binaries(dir_to_analyse, output_file)
	print('Found:', counter)
	print('Saved to', output_file)




dir = 'c:/Balabit/bin_compare/pairs/LAB/'
output = 'c:/Balabit/bin_compare/pairs/lab_balabit.txt'

def binaries(dirs, output):
	counter = 0
	with open(output, 'w') as tre:
		for root, dirs, files in os.walk(dirs):
			for name in files:
				curname = os.path.join(root, name)
				with open(curname, 'rb') as curfile:
					start = curfile.read(4)
					if b'MZ' in start[:2] or b'ELF' in start[1:]:
						counter += 1
						tre.write(curname.replace('\\', '/') + '\n')
	return counter

if __name__ == "__main__":
    main()