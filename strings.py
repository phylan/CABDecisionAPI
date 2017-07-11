def findAll(inString, searchString):
	
	start = 0
	while True:
		start = inString.find(searchString, start)
		if start == -1:
			return
		yield start
		start += len(searchString)
		
def getExcerpts(inString, searchString):
	
	indices = [(a-180, a+180) for a in list(findAll(inString, searchString))]
	
	rawExcerpts = [inString[a[0]:a[1]] for a in indices]
	finalExcerpts = []
	
	for excerpt in rawExcerpts:
		try:
			finalExcerpts.append(excerpt[excerpt.index(" ")+1:excerpt.rindex(" ")])
		except ValueError:
			finalExcerpts.append(excerpt)
			
	return finalExcerpts