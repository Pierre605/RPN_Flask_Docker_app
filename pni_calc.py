import itertools


def pni_calculator(query: str):
	pni_split = query.split(" ")
	pni = []

	for c in pni_split:
		try:
			c = float(c)
			pni.append(c)
		except Exception:
			if c:
				pni.append(c)

	groups = []

	for key, group in itertools.groupby(pni, lambda x: type(x)):
		groups.append(list(group))

	pni = groups
	res = 0
	invalid_operator = None

	
	for x in range(0, len(pni), 2):
		if x == 0:
			if (len(pni[x]) >= 2) and (len(pni[x+1]) == len(pni[x])-1) and (len(pni) > 1):
				sub = 0
				for y in range(len(pni[x])-1):
					if y == 0:
						if pni[x+1][y] == '+':
							ope = pni[x][len(pni[x]) - y-2] + pni[x][len(pni[x]) - y - 1]
							sub += ope

						elif pni[x+1][y] == '-':
							ope = pni[x][len(pni[x]) - y-2] - pni[x][len(pni[x]) - y - 1]
							sub += ope

						elif pni[x+1][y] == 'x':
							ope = pni[x][len(pni[x]) - y-2] * pni[x][len(pni[x]) - y - 1]
							sub += ope

						elif pni[x+1][y] == '/':
							ope = pni[x][len(pni[x]) - y-2] / pni[x][len(pni[x]) - y - 1]
							sub += ope

						else:
							invalid_operator = pni[x+1][y]

						if invalid_operator:
							return "<b>ERROR</b></br>" + f'''Operator <b>' {invalid_operator} '</b> not vaild.</br>''' + "Valid operators are: <b>+ - x /</b>"

					else:
						if pni[x+1][y] == '+':
							sub = pni[x][len(pni[x]) - y-2] + sub
			
						elif pni[x+1][y] == '-':
							sub = pni[x][len(pni[x]) - y-2] - sub

						elif pni[x+1][y] == 'x':
							sub = pni[x][len(pni[x]) - y-2] * sub

						elif pni[x+1][y] == '/':
							sub = pni[x][len(pni[x]) - y-2] / sub

						else:
							invalid_operator = pni[x+1][y]

						if invalid_operator:
							return "<b>ERROR</b></br>" + f'''Operator <b>' {invalid_operator} '</b> not vaild.</br>''' + "Valid operators are: <b>+ - x /</b>"

				res += sub

			else:
				return '''<b>ERROR</b></br>Wrong PNI query syntax</br><i>Query example: 1 2 + 4 7 x + 2 -</i>'''

		else:
			sub = 0
			if len(pni[x+1]) == len(pni[x]) and (len(pni[x]) > 1):
				for y in range(len(pni[x])):
					if y == 0:
						if pni[x+1][y] == '+':
							ope = pni[x][len(pni[x]) - y-2] + pni[x][len(pni[x]) - y - 1]
							sub += ope

						elif pni[x+1][y] == '-':
							ope = pni[x][len(pni[x]) - y-2] - pni[x][len(pni[x]) - y - 1]
							sub += ope

						elif pni[x+1][y] == 'x':
							ope = pni[x][len(pni[x]) - y-2] * pni[x][len(pni[x]) - y - 1]
							sub += ope

						elif pni[x+1][y] == '/':
							ope = pni[x][len(pni[x]) - y-2] / pni[x][len(pni[x]) - y - 1]
							sub += ope

						else:
							invalid_operator = pni[x+1][y]

						if invalid_operator:
							return "<b>ERROR</b></br>" + f'''Operator <b>' {invalid_operator} '</b> not vaild.</br>''' + "Valid operators are: <b>+ - x /</b>"


					elif y == len(pni[x]) - 1:
						if pni[x+1][y] == '+':
							ope = res + sub
							res = ope

						elif pni[x+1][y] == '-':
							ope = res - sub
							res = ope

						elif pni[x+1][y] == 'x':
							ope = res * sub
							res = ope

						elif pni[x+1][y] == '/':
							ope = res / sub
							res = ope

						else:
							invalid_operator = pni[x+1][y]


					else:
						if pni[x+1][y] == '+':
							sub = pni[x][len(pni[x]) - y-2] + sub
			
						elif pni[x+1][y] == '-':
							sub = pni[x][len(pni[x]) - y-2] - sub

						elif pni[x+1][y] == 'x':
							sub = pni[x][len(pni[x]) - y-2] * sub

						elif pni[x+1][y] == '/':
							sub = pni[x][len(pni[x]) - y-2] / sub

						else:
							invalid_operator = pni[x+1][y]

						if invalid_operator:
							return "<b>ERROR</b></br>" + f'''Operator <b>' {invalid_operator} '</b> not vaild.</br>''' + "Valid operators are: <b>+ - x /</b>"
						

			elif len(pni[x+1]) == len(pni[x]) and (len(pni[x]) == 1):
				for y in range(len(pni[x])):
					if pni[x+1][y] == '+':
						res += pni[x][len(pni[x]) - y - 1]

					elif pni[x+1][y] == '-':
						res -= pni[x][len(pni[x]) - y - 1]

					elif pni[x+1][y] == 'x':
						res = res * pni[x][len(pni[x]) - y - 1]

					elif pni[x+1][y] == '/':
						res = res / pni[x][len(pni[x]) - y - 1]

					else:
						invalid_operator = pni[x+1][y]

					if invalid_operator:
						return "<b>ERROR</b></br>" + f'''Operator <b>' {invalid_operator} '</b> not vaild.</br>''' + "Valid operators are: <b>+ - x /</b>"

			else:
				return '''<b>ERROR</b></br>Wrong PNI query syntax</br><i>Query example: 1 2 + 4 7 x + 2 -</i>'''

	if res == 0:
		res = 'null'
		return res
	else:
		return str(round(res, 2))
