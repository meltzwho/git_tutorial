import sys
# Default value "World"
name = sys.argv[1] if len(sys.argv)>1 else "World"

print("Hello, "+name)
