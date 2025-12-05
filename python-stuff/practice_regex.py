import re

pattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
obj = pattern.search('My number is 415-555-4242.')
thing =  obj.group()
matches = obj.groups()
test = 'hello', 'nice'
first, sec = test
print(first)
print(sec)
