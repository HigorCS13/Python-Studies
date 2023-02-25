
def fork():

	# draw the first tine
	print("|", end="")
	for i in range(2):
		print(" ", end="")
	print("|", end="")
	for i in range(2):
		print(" ", end="")
	print("|")


	# draw the second tine
	print("|", end="")
	for i in range(2):
		print(" ", end="")
	print("|", end="")
	for i in range(2):
		print(" ", end="")
	print("|")

	# draw the handle
	print("\\", end="")
	for i in range(5):
		print("-", end="")
	print("/")
	for i in range(5):
		for i in range(2):
			print(" ", end="")
		print('| |')


print(fork())


print("  ______")
print(" |    _\\")
print(" |   _ \\")
print(" |  |_|_\\")
print(" |_______\\")
print("  \\     /")
print("   \\___/")