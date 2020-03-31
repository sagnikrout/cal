a=int(input(">"))
o="m"
while(o!="off"):
	o=input("|+| |-| |*| |/| |off|\n")
	if o =="+":
		print("\n\n "+str(a)+"\n+")
		a=a+int(input())
		print("----------\n"+str(a))
	if o =="-":
		print("\n\n "+str(a)+"\n-")
		a=a-int(input())
		print("----------\n="+str(a))
	if o =="*":
		print("\n\n "+str(a)+"\n*")
		a=a*int(input())
		print("----------\n="+str(a))
	if o =="/":
		print("\n\n "+str(a)+"\n/")
		a=a/int(input())
		print("----------\n="+str(a))


