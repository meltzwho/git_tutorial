import sys
# Default value "World"
# Author: Eric Meltzer (etmeltzer@gmail.com)
name = sys.argv[1] if len(sys.argv)>1 else "World"

for i in range(len(sys.argv)):
 print("Hello, "+name)
