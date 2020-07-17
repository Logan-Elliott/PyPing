#!/usr/bin/python3
# Sweeps /24 CIDR subnet
import subprocess

print("PyPing: Simple /24 CIDR Subnet Ping Sweeper")
print("Beginning ping sweep...")
for ping in range(1,255):
	address = "10.x.x." + str(ping) # Modify address to reflect target subnet, example: address = "192.168.1."
	res = subprocess.call(['ping','-c','1',address])
if res == 0:
	print("ping to", address, "OK")
elif res == 1:
	print("no response from", address)
else:
	print("ping to", address, "failed!")
