import sys
# Default value "World"
# Author: Eric Meltzer (etmeltzer@gmail.com)
names = sys.argv[1:] if len(sys.argv)>1 else ["World"]

for i in range(len(names)):
 print("Hello, "+str(names[i]))
