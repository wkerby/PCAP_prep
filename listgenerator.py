indexnumber = list(range(1,163))
size = ['large','medium','small']
urgency = ['high','medium','low']
priority = urgency
pmo_involvement = ['PMO Project Manager','PMO Representative','Business Analyst']
consultants = ['Yes','No']
dtype = ['Software/Hardware Implementation']
totaldecisionlist = []
for i in size:
	for j in urgency:
		for k in priority:
			for l in pmo_involvement:
				for m in consultants:
					for o in dtype:
						totaldecisionlist.append([i,j,k,l,m,o])
print(list(enumerate(totaldecisionlist)))



