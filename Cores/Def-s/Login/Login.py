from affirm import *
import shutil
import os
from errors_build import *
if (os.path.exists("/storage/emulated/0/MYC/order.py")):
	from order import *

def login(fname):
	if (fname == "affirm"):
		print("")
	if (fname == "order"):
		k = open('/storage/emulated/0/MYC/order.myc','r')
		ko = k.read()
		jkj = ko.replace(">","(")
		kar = jkj.replace("<",")")
		yeah = kar.replace(";",")")
		spa = yeah.replace(' "','("')
		bleed = spa.replace(" {",":")
		if "activity" in spa:
			lookatme = bleed.replace("activity","def")
			dic = lookatme.replace(" {",":")
			open("/storage/emulated/0/MYC/order.py","w").close()
			f = open("/storage/emulated/0/MYC/order.py","a")
			fcow = f.write(dic)

login("order")
order.log(0)
