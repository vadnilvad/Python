import win32com
from win32com.client import Dispatch
import codecs
import re
import json

# Login Credentials
qcServer = "https://qc.a1.bg/qcbin"
qcUser = "vadnal_n"
qcPassword = "Nileshv@1"
qcDomain = "IT_MDA_10"
testList = []

testdict = {}
project = "Billing_CRM_Group"
  # Do the actual login
td = win32com.client.Dispatch("TDApiOle80.TDConnection.1")
td.InitConnectionEx(qcServer)
td.Login(qcUser,qcPassword)
td.Connect(qcDomain,project)
if td.Connected == True:
    print ("System: Logged in to " +project)
else:
    print ("Connect failed to " +project)

mg = td.TreeManager  # Tree manager
name = ['TC001','TC002','TC003','TC003','TC004','TC005','TC006','TC007','TC008','TC009','TC010','TC011','TC012','TC013','TC014']
folder = mg.NodeByPath('Subject\\Test Factory\\MPG\\MPG Regression Test_Yearly Request\\GUI')
for x in name:
    testList = folder.FindTests(x)
    #print(type(testList))
    print(testList[0].Name)
    print(testList[0].DesStepsNum)

td.Disconnect()
td.Logout()
