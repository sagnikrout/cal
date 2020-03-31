print("|+| |-| |*| |/| |off|\n")
a=int(input(""))
o="m"
while(o!="off"):
	o=input(str(a)+" ")
	if o =="+":
		a=a+int(input(str(a)+" "+o+" "))
		print(" = "+str(a)+"\n--------------------")
	if o =="-":
		a=a-int(input(str(a)+" "+o+" "))
		print(" = "+str(a)+"\n--------------------")
	if o =="*":
		a=a*int(input(str(a)+" "+o+" "))
		print(" = "+str(a)+"\n--------------------")
	if o =="/":
		a=a/int(input(str(a)+" "+o+" "))
		print(" = "+str(a)+"\n--------------------")
