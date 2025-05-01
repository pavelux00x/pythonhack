import subprocess
import optparse
import re 

if __name__ == "__main__":
	parser = optparse.OptionParser()
	parser.add_option('-o','--output',help="Test",dest="output")
	options,args = parser.parse_args()

	def check_start():
		if options.output != None:
			print(options.output)
			print(args)
		else:
			a=input("wanna change your mac? y/n")
			if a=="y":
				command = "ifconfig eth0 | grep ether | awk -F ' ' '{print $2}'"
				r=subprocess.run(command,shell=True,capture_output=True,encoding="utf-8")
				print("X : ",r.stdout)
				b=input("ok?")
				split=(b.split(';'))
				c=subprocess.run(split,shell=True)
				print(c.stdout)
			elif a=="s":
				command="ifconfig eth0"
				r=subprocess.run(command,shell=True,capture_output=True,encoding="utf-8")
				print(r.stdout)
				result=re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',r.stdout)
				if "00" in result.group():
					print("x")

check_start()
