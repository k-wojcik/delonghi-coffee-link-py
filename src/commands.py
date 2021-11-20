#!/usr/bin/env python3
import json

def get_command(command):
	f = open('protocol/coffee-link-commands.json',)
	data = json.load(f)
	f.close()
	
	default_definition = next(filter(lambda x: x['models'] == None, data['definitions']))	
	return default_definition['commands'][command]
	
	