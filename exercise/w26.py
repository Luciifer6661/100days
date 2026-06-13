'''dictionary'''

def printDict():
    # d = dict()
    dic = {}
    dic[1]=1
    dic[2]=2**2
    dic[3]=3**2
    print(type(dic))

# printDict()


def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print (d)
		

# printDict2()


def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.values():	
		print (k)
		

printDict()
