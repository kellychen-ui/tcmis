def Process(x):
	x = x.split(" ")
	school = x[0].replace("我是","")
	print(f"學校:{school}\n姓名:{x[2]}")

Name = "我是靜宜大學 資管二A 陳宜琳"
Process(Name)