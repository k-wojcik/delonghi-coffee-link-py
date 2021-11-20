#!/usr/bin/env python3
import sys, argparse, json
from protocol import *
import commands

#bd_addr = "00:a0:50:c8:6a:a0" # insert your Bluetooth Address

def send_command_to_device(addr, command_arr):
	adapter = None
	try:
		(adapter, device) = connect(addr)
		send(device, command_arr)
	finally:
		if adapter:
			adapter.stop()

def make_command(args, command):
	print('Make command to')
	print(args.addr)
	
	print('Command:')
	if args.stop:
		if 'stop' not in command:
			raise RuntimeError("Stop is not supported for this command")
		
		print(command['stop'])
		print(bytearray.fromhex(command['stop']))
		#send_command_to_device(addr, bytearray.fromhex(command['stop']))
	else:
		print(command['start'])
		print(bytearray.fromhex(command['start']))
		#send_command_to_device(addr, bytearray.fromhex(command['start']))
		
	return command
	
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', '--addr')
	parser.add_argument('-c', '--command')
	parser.add_argument('-s', '--stop', dest='stop', action='store_true')
	parser.add_argument('--amount')
	parser.add_argument('--hotness')
	parser.add_argument('--aroma')
	args = parser.parse_args()

	command = commands.get_command(args.command)

	result = make_command(args, command)
	sys.stdout.write(json.dumps(result))
	return 0

if __name__ == '__main__':
	exit(main())