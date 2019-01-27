import time

class MainLoop():
	def __init__(self):
		init()
		run()

def init():
	print("Init")

def run():
	print("Run")
	while True:
		try:
			print("Running")
			time.sleep(5)
		except:
			print("Error")
			break

	print("Stop")