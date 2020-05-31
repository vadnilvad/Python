###############################################################################################################
################################################ Sphoorthi Oum ################################################
###############################################################################################################

########Assignment_2020_05_16_001 || YYYY_MM_DD_<Assignmentnumber>
########REQUIREMENT

#	s = [1,2,3,[4,5,[6,7,8,[9,[10,[11]]]]]]
#	using above list extract, 1,3,5,7,9,11  from the above list using indexing

#Program for Assignment_2020_05_16_001

	s = [1,2,3,[4,5,[6,7,8,[9,[10,[11]]]]]]
	s[0],s[2],s[3][1],s[3][2][1],s[3][2][3][0],s[3][2][3][1][1][0]

#End of Program for Assignment_2020_05_16_001






########Assignment_2020_05_16_002 || YYYY_MM_DD_<Assignmentnumber>
########REQUIREMENT
#2 write a program that takes the year of birth as input and displays the age
#Enter your year of birth : 2019
#You are 1 years old

#Program for Assignment_2020_05_16_002
	dob= int(input("Enter your year of birth :"))
	cur_year=2020
	print ("You are",cur_year-dob,"years old")

#End of Program for Assignment_2020_05_16_002






########Assignment_2020_05_16_003 || YYYY_MM_DD_<Assignmentnumber>
########REQUIREMENT
#collect name, year of birth, education, accountNumber (any- dummy), contact number, area from the user and
#put  age, account number, contact number in a list
#put name , education, area in another list - all in upper cases
#and display both the lists

#Program for Assignment_2020_05_16_003

	name=input("Name :").upper()
	yob=int(input("year of birth :"))
	edu=input("education :").upper()
	age=2020-yob
	ac_no=input("accountNumber :")
	cont_num=int(input("Contact number :"))
	area=input("Area :").upper()

	list1=[age,ac_no,cont_num]
	list2=[name,edu,area]

	list1
	list2

#End of Program for Assignment_2020_05_16_003






########Assignment_2020_05_16_004 || YYYY_MM_DD_<Assignmentnumber>
########REQUIREMENT
#Create a variable with the text below, you can copy paste the same into idle without changing anything in the string.
	text="""Not restricting Himself to theory,
	He is making people experience the Omni concepts: Omnipresence, Omniscience and Omnipotence.
	He is The Scientific Saint,
	His Holiness Sri Sri Sri Guru ViswaSphoorthi –
	The Omnipresent, The Omniscient and The Omnipotent."""

##thats a single string. from that string, print the last 2 lines only
##the output should be

	His Holiness Sri Sri Sri Guru ViswaSphoorthi –
	The Omnipresent, The Omniscient and The Omnipotent.


#Program for Assignment_2020_05_16_004

	textlist=text.split("\n")
	print (textlist[-2]+"\n"+textlist[-1])

	print ("max\tmin\n"+listofTemp[0]["max"])
	
	##Above is WA i can figure out to cater purpose, i am not sure if print itself have some advance level of filtering that can print last two lines. If any such hoping to see it is being covered eventually in comming classes. Sphoorthi Oum.

#End of Program for Assignment_2020_05_16_004






########Assignment_2020_05_16_005 || YYYY_MM_DD_<Assignmentnumber>
########REQUIREMENT

#Program for Assignment_2020_05_16_005

#create an empty list, add 10 strings to it using .append method,
	list=[]
	list.append('1nikola tesla')
	list.append('2srinivasa ramanujam')
	list.append('3abdul kalaam')
	list.append('4sri sreedhar')
	list.append('5albert einstein')
	list.append('6nagasai')
	list.append('7charles darwin')
	list.append('8narendra modi')
	list.append('9chandra shekar')
	list.append('10subhash bose')
#print the count of it
	len(list)
#remove the first and last elements,
	list.remove(list[-1])  ##OR list.pop() ##removing Last element
	list.remove(list[1])   ##removing 1st element
#print the count of it
	len(list)
#insert 3 float values at the beginning of the list
	list.insert(0,1.1)
	list.insert(1,1.2)
	list.insert(2,1.3)
#display the count
	len(list)
#insert 2 strings at the middle of the list
	list.insert(5,'middle_nikolatesla')
	list.insert(6,'middle_subhash c bose')
	list.insert(5,'middle_X men')
#display the count
	len(list)
#add 2 duplicate values, one at the beginning and one at the end of the list
	list.insert(list[0])
	list.append(list[-1])
#remove one value using .remove method
	list.remove(list[-1])
#see which value is being removed ( first or last ?)
#above command is removing last value. apologies if I didn't understood question.

#End of Program for Assignment_2020_05_16_001
############################################################################################################################





########Assignment_2020_05_21_001 || YYYY_MM_DD_<Assignmentnumber>

	text=""" the very few seconds that you have after you wake up early in the morning.
	you're sub conscious mind has access to it and anything that you say in these few second will directly pass into the inner layers of your brain.
	these are roughly 5-7 seconds and our brain would be in alpha state.
	so, right after you wake up, see yourself and do not think about anything else .the brain has 3 layers , conscious, sub conscious, super conscious layers ."""

	text
	" the very few seconds that you have after you wake up early in the morning.\nyou're sub conscious mind has access to it and anything that you say in these few second will directly pass into the inner layers of your brain.\nthese are roughly 5-7 seconds and our brain would be in alpha state.\nso, right after you wake up, see yourself and do not think about anything else .the brain has 3 layers , conscious, sub conscious, super conscious layers ."

 #########  REQUIREMENT ##########
 # add all the 2 lettered words to a list
 # add all the 3 lettered words to a list
 # add all the 4 lettered words to a list
 # add all the words with more than 4 letters to a seperate list
 # check if you want to use , for, if-else, if-elif to identify

#Program for Assignment_2020_05_21_001

	list1=[]
	list2=[]
	for each in text.split() :
		if len(each) > 2 and len(each)<4:
			list1.append(each)
			#print ("'" +each+"'\t is added to list1 ")
		elif len(each) >4 :
			list2.append(each)
			#print ("'" +each+"'\t is added to list2 ")
		#else :
			#print ("Value :\t'"+each+ "'\tis ignored :(")

####End of Program for Assignment_2020_05_21_001


####Class work 2020_05_23_001 BEGIN

	#Collect name, age, edu, contact & area from user
	#Store them in dictionary

		name=input("Name :").upper()
		edu=input("education :").upper()
		age=input("Age :").upper()
		cont_num=int(input("Contact number :"))
		area=input("Area :").upper()

	# define dict to store all the data

		details={}

	# add all the values to dict

		details["name"]=name
		details["education"]=edu
		details["Age"]=age
		details["Contact_number"]=cont_num
		details["Area"]=area

####Class work 2020_05_23_001 END





####Class work 2020_05_23_001 BEGIN

	listofTemp=[

	{
	"day": 42.15,
	"min": 37.75,
	"max": 45.29,
	"night": 37.75,
	"eve": 44.39,
	"morn": 39.61
	},

	{
	"day": 45.72,
	"min": 33.81,
	"max": 47.01,
	"night": 37.38,
	"eve": 45.36,
	"morn": 33.81
	},

	{
	"day": 46.72,
	"min": 34.76,
	"max": 47.71,
	"night": 37.38,
	"eve": 45.98,
	"morn": 34.76
	},
	]

# extract the max temparatures from all the dictionaries in the list above
	print("\nDict#1 max Value",listofTemp[0]["max"],"\nDict#2 max Value",listofTemp[1]["max"],"\nDict#2 max Value",listofTemp[2]["max"])

# print all the min & max temparatures
	for i in listofTemp:
	print("min temperature :",i["min"],"\tmax temperature :",i["max"])

# print the third dictionary's morning temp- "morn" key
	listofTemp[2]["morn"]


####Class work 2020_05_23_001 END