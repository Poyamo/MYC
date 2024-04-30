#MYC PROGRMMING LANGUGE
#MAIN BUILD FILE PYTHON
#VERSION ONE POINT ZERO 1.0
#c_to_bash
from errors_build import *
from activity import *
c_t_b1 = open("/storage/emulated/0/MYC/_connected_fmyc.od","r")
c_t_b = c_t_b1.read()
if ".myc" in c_t_b:
  print("")
  mkmk = c_t_b.replace("\n","")
  file = open("/storage/emulated/0/MYC/"+mkmk ,"r")
  files = file.read()
  finall = files.replace(' "','("')
  finall2 = finall.replace(";",")")
  finall3 = finall2.replace('>',"(")
  global finall4
  finall4 = finall3.replace("<",")")
  try:
    if "activity" in finall4:
    		hj = finall4.replace(" {",":")
    		qulases = hj.replace("activity","def", 1)
    		exec(qulases)
    else:
    	exec(finall4)
  except Exception as error:
    ers = str(error)
    if "'(' was never closed" in ers:
      from errors_build import *
      syntex_error()
    else:
      unknown_error()
      print(ers)
