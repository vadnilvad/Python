###############################################################################################################
################################################ Sphoorthi Oum ################################################
###############################################################################################################

########Assignment_2020_05_16_001 || YYYY_MM_DD_<Assignmentnumber>
########REQUIREMENT

#	s = [1,2,3,[4,5,[6,7,8,[9,[10,[11]]]]]]
#	using above list extract, 1,3,5,7,9,11  from the above list using indexing

#Program for Assignment_2020_05_16_001

	##Awaiting topic to be covered in class. value fetch from nexted list/collection is pending Learning.

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

