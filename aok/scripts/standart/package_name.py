#-*- coding:utf-8 -*-


def to_packagename(instr):
	instr = instr.lower()
	instr = instr.replace(' ','')
	instr = instr.replace('-','')

	return instr

def generate_package_name(templatePackageName, themeTitle):
	outPackageName = ""
	parts = templatePackageName.split('.')
	s = len(parts)
	for i in range(s):
		if i < s-1:
			outPackageName += parts[i] + '.'
		else:
			outPackageName += to_packagename(themeTitle)

	return outPackageName