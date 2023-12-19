ism=input("Ismingizni kiriting: ")
n=ism.lower()
q="❄️"
u=q*3
p="  "
for i in n:
	if i=="q":
		print(f"{u}\n{q+p+q}\n{q+p+q}\n{u}\n{p*2} {q}\n")
	elif i=="w":
		print(f"{q}      {q}\n {q} {q} {q}\n  {u}\n   {q*2}\n")
	elif i=="e":
		print(f"{u}\n{q}\n{u}\n{q}\n{u}\n")
	elif i=="r":
		print(f"{u}\n{q+p+q}\n{u}\n{q+p} {q}\n")
	elif i=="t":
		print(f"{u}\n{p+q}\n{p+q}\n{p+q}\n")
	elif i=="y":
		print(f"{q+p+q}\n {q*2}\n  {q}\n  {q}\n")
	elif i=="u":
		print((q+p+q+"\n")*3+u+"\n")
	elif i=="i":
		print((p+q+"\n")*4+"\n")
	elif i=="o":
		print(u+"\n"+(q+p+q+"\n")*2+u+"\n")
	elif i=="p":
		print(f"{u}\n{q+p+q}\n{u}\n{q}\n{q}\n")
	elif i=="a":
		print(f"    {q}\n   {q*2}\n  {q+p+q}\n {q*4}\n{q+p*3+q}\n")
	elif i=="s":
		print(f"{u}\n{q}\n{u}\n    {q}\n{u}\n")
	elif i=="d":
		print(f"{q*2}\n{q+p+q}\n{q+p+q}\n{q*2}\n")
	elif i=="f":
		print(f"{u}\n{q}\n{u}\n{q}\n{q}\n")
	elif i=="g":
		print(f"{u}\n{q}\n{q+p+q}\n{u}\n")
	elif i=="h":
		print(f"{q+p+q}\n{u}\n{q+p+q}\n")
	elif i=="j":
		print((p*2+q+"\n")*2+q+p+q+"\n"+u+"\n")
	elif i=="k":
		print(f"{q}  {q}\n{q}{q}\n{q}{q}\n{q}  {q}\n")
	elif i=="l":
		print((q+"\n")*3+u+"\n")
	elif i=="z":
		print(f"{u}\n   {q}\n{p+q}\n {q}\n{u}\n")
	elif i=="x":
		print(f"{q+p+q}\n {q}{q}\n {q*2}\n{q+p+q}\n")
	elif i=="c":
		print(u+"\n"+(q+"\n")*2+u+"\n")
	elif i=="v":
		print(f"{q+p+q}\n {q}{q}\n  {q}\n")
	elif i=="b":
		print(f"{q*2}\n{q+p+q}\n{q*2}\n{q+p+q}\n{q*2}\n")
	elif i=="n":
		print(f"{q*2+p+q}\n{q} {q} {q}\n{q}  {q}{q}\n")
	elif i=="m":
		print(f"{q*2+p*2+q*2}\n{q} {q+p+q} {q}\n{q}  {q*2}  {q}\n")