# access individual characeters.
name = 'Neeraj'
print name[2]
#length
print len(name)
#loop through strings.
index = 0
while index < len(name):
	letter = name[index]
	print index,letter
	index += 1
#definite loops
for letter in name:
	print letter
#comparing characters
count = 0
for letter in name:
	if letter == 'e':
		count += 1
print count
#slicing
print name[0:3]
print name[:]
#concatination
sirname = 'Kumar'
print 'Full name -> ' + name + sirname
#dir will find functions are available on string or any other type parameter
print dir(name)
temp = name.replace('e', 'E')
print temp
#stripping of characters like new line characters.

#parsing text for that particular.
data = 'From stemphen.marquard@uct.ac.zasdssd Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
spacepos = data.find(' ', atpos)
host = data[atpos+1:spacepos]
print host

