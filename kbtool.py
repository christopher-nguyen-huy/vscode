#! /usr/bin/env python3
import sys
import json

class Command(object):
	def __init__(self, input_d):
		self.parse(input_d)

	def parse(self, input_d):
		cmd = input_d['command']
		remove = False
		if cmd.startswith('-'):
			cmd = cmd[1:]
			remove = True
		self.keys = input_d['key']
		self.remove = remove
		self.command = cmd
		self.context = input_d.get('when')

	def render(self):
		d = dict(
			key = self.keys,
			command = f'{"-" if self.remove else ""}{self.command}'
		)
		if self.context:
			d['when'] = self.context
		return d

def loadfile(filename):
	with open(filename, 'r', encoding='utf-8') as inf:
		return json.loads(inf.read())

def output(data):
	print(json.dumps(data, indent='\t'))

def print_help():
	output = '''
./kbtool command options filename
help	print this helpfile
sort	sort a file
'''
	print(output)

def sort_keys(filename):
	data = loadfile(filename)
	data = [Command(cmd) for cmd in data]
	data.sort(key=lambda x: (x.remove, x.command))
	data = [cmd.render() for cmd in data]
	output(data)

def main(args):
	commands = {
		'help': print_help,
		'sort': sort_keys
	}
	if not args:
		print_help()
		return
	command = args[0]
	options = args[1:]
	if command not in commands:
		print_help()
		return
	commands[command](*options)

if __name__ == "__main__":
	main(sys.argv[1:])