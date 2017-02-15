nj = 299
zf = 23
cl = 44
zs = 10
qe = 26
d8 = "9pMaVs5DxiOPGe8JETXYmg3lbudro6Qk1WLKwyhfnS4Iv0ABtjUCc7RZz2NFHqKfeROdEILJs5W6D1m4XFtH7YbwgrUConPuqQBcSxT092zljv8yMAGhpZN3akVi"
chick = "210 209 22 126 188 29 212 101 24 125 145 -22 180 134 -30 162 107 18 142 210 8 185 95 -23 221 123 54 183 180 39 103 145 57 141 181 56 141 138 -25 124 133"
#chick = "144 207 93 170 111 25 130 144 21 152 172 -3 113 164 -24 94 117 -25 173 106 77 169 119 15 135 127 9 111 123 -12 109 218 61 155 98 50 199 131 -2 168 205 75 169 164 24 139 116 95 127 113 71 102 141 -18 152 153 28 111 131 74 207 201 -21 174 155 74 138 164 -7 179 215 94 187 142 55 147 99 64 176 117 25 193 177 47 135 111 -5 108 137 -8 132 120"
def decr(num, num2):
	if (num2 == 0):	
		num -= qe * 2 + cl * 2 - zf * 2;
	elif (num2 == 1):
		num -= zs * 3 + cl * 2 - zf * 1;
	elif (num2 == 2):
		num -= nj - zs * (num2*5) - cl * 2 - zf * 6 - 2 * 2
	if (num<0):
		num = not num #* -1
	return num

def rev_xor(a,i):
	return ord(d8[i+zs])^a

def decription():
	i=0
	str = ""
	for c in chick.split(" "):
		get = (rev_xor(decr(int(c),i%3),i))
		str += chr(get)
		i+=1
	for i in range(len(str)):
		print str[len(str)-1-i]

decription()

