#!/usr/bin/env python
import sys
import re
key = "UNKNOWN"
for line in sys.stdin:
	#bad = re.findall("[\\x80-\\xFF]",line)
	#if (bad):
	#	continue
		

	title = re.search(r"<title>(.*)</title>",line)
	
	if (title):
		key = str(title.group(1)).lower()

	# Need to check: did I exclude any characters?
	values = re.findall("\[\[([a-zA-Z0-9|_ ;,-]+)\]\]",line)

	if values != None:	
		for value in values:

			separator = re.search(r"\|", value)
		
			# If there is a piped link, take the actual link	
			if separator != None:
				first = re.split(r"\|",value)
				value = first[0]

			if len(value) > 0:
				#if key == None:
				#	key = "Unknown"
				if (key):
					print (value.lower() + "\t1" )
