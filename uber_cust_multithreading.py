#Developer	: Ivana Donevska
#Date	 : 2016-01-28
#Program Name : Customer DataGenerator
#Version#	 : 6
#Description  : Sample customer data for credit card account holders and users. 
#-----------------------------------------------------------------------------
# History | ddmmyyyy  |  User	 |		Changes
#	  | 01192016  | Ivana D.  | Credit Card customer model,code, ref lists, etc...
#	  | 01202016  | Ivana D.  | Use Case Model and control flag design 
#	  | 01202016  | Ivana D.  | SAR, PEP and HR Probabilities 
#	  | 01202016  | Jeff K.   | Credit Card customer business rules, comments, ref lists, etc...
#	  | 01212016  | Jeff K.   | Customer testing
#	  | 01272016  | Justin S. | Update SSN2, SSN3 and SSN4 logic with unique values
#	  | 01282016  | Justin S. | multi-threading, creating functions
#	  | 01282016  | Jeff K.   | multi-threading bug fixes
#	  | 01292016  | Ivana D.  | multi-threading odd number bug identification
#	  | 02012016  | Ivana D.  | Code review for multithreading and comment updates 
#-----------------------------------------------------------------------------*/
#Reference data is located on the test-bmohb console gs://newccdatav3

from random import randrange, random, shuffle
from datetime import datetime
from faker import Faker
from barnum import gen_data
from multiprocessing import Pool
import csv, NAICS, random, geo_data, zips, re, time
liSSNMaster = []

def createCusts(N):
	#List for client whose net worth is over $500K
	HighNetWorth = ['Yes'] + ['No'] * 30
	#List for type of account
	Related_Type = ['Primary','Secondary','Joint']
	#List for how the account was opened
	Party_Type = ['Person','Non-Person']
	#List for a BMO customer
	Party_Relation = ['Customer','Non-Customer']
	#List for random Yes/No Flag
	Yes_No = ['Yes'] + ['No'] * 12
	#List for random Yes/No Consent
	Yes_No_Consent = ['Yes'] + ['No'] * 4
	#List for equal Yes/No Flag
	Yes_No_50 = ['Yes','No']
	#List for official language
	Official_Lang = ['English'] * 3 + ['French']
	#List for method of communication
	Preffered_Channel = ['Direct Mail','Telemarketing','Email','SMS']
	#List for status of customer
	#Customer_Status = ['Prospect','Inactive Customer','Past Customer'] + ['Active Customer'] * 56
	#List for LOB Segment Type
	Seg_Model_Type = ['LOB Specific','Profitability','Geographical','Behavioral','Risk Tolerance']
	#List for Model ID
	Model_ID = ['01','02','03','04','05']
	#List for Model Name
	Seg_Model_Name = ['IRRI', 'CRS Risk Score','Geo Risk','Financial Behavior Risk','CM Risk']
	#List for Model Score
	Seg_Model_Score = ['200','300','400','100','500']
	#List for Model Group
	Seg_Model_Group = ['Group 1'] * 2 + ['Group 2','Group 3','Group 4']
	#List for Model Description
	Seg_Model_Description = ['High Risk Tier','Mid Risk Tier','Low Risk Tier','Vertical Risk','Geographical Risk']
	#List for random Arms Dealer flag
	Arms_Manufacturer=['Yes'] + ['No'] * 2 + [''] * 392
	#List for random auction flag
	Auction=['Yes'] + ['No'] * 2 + [''] * 392
	#List for random Cash Intensive flag
	CashIntensive_Business=['Yes'] + ['No'] * 2 + [''] * 392
	#List for random Casino?Gaming flag
	Casino_Gambling=['Yes'] + ['No'] * 2 + [''] * 392
	#List for random Client Onboarding flag
	Channel_Onboarding=['E-mail','In Person','In person - In Branch/Bank Office','In person - Offsite/Client Location','Mail','Online','Phone','Request for Proposal (RFP)'] + ['Not Applicable'] * 10
	#List for random Transaction flag
	Channel_Ongoing_Transactions=['ATM','E-mail','Fax','Mail','Not Applicable','OTC Communication System','Phone'] + ['Online'] * 4 + ['In Person'] * 31
	#List for random HI_Vehicle flag
	Complex_HI_Vehicle=['Yes'] + ['No'] * 2 + [''] * 392
	#List for random Metals flag
	Dealer_Precious_Metal=['Yes'] + ['No'] * 2 + [''] * 392
	#List for random Arms Dealer flag
	Digital_PM_Operator=['Yes'] + ['No'] * 2 + [''] * 392
	#List for random Embassy flag
	Embassy_Consulate=['Yes'] + ['No'] * 2 + [''] * 392
	#Sets variable to Embassy flag
	Exchange_Currency=Embassy_Consulate
	#Sets variable to Embassy flag
	Foreign_Financial_Institution=Embassy_Consulate
	#Sets variable to Embassy flag
	Foreign_Government=Embassy_Consulate
	#Sets variable to Embassy flag
	Foreign_NonBank_Financial_Institution=Embassy_Consulate
	#Sets variable to Embassy flag
	Internet_Gambling=Embassy_Consulate
	#Sets variable to Embassy flag
	Medical_Marijuana_Dispensary=Embassy_Consulate
	#Sets variable to Embassy flag
	Money_Service_Business=Embassy_Consulate
	#Sets variable to Embassy flag
	NonRegulated_Financial_Institution=Embassy_Consulate
	#Sets variable to Embassy flag
	Not_Profit=Embassy_Consulate
	#List for random occupation
	Occupation=['11-1011 Chief Executives',\
	'11-3011 Administrative Services Managers',\
	'11-3031 Financial Managers',\
	'11-3061 Purchasing Managers',\
	'13-1011 Agents and Business Managers of Artists Performers and Athletes',\
	'13-1031 Claims Adjusters Examiners, and Investigators',\
	'13-1199 Business Operations Specialists, All Other',\
	'13-2099 Financial Specialists All Other',\
	'17-1011 Architects Except Landscape and Naval',\
	'23-1011 Lawyers',\
	'23-1023 Judges, Magistrate Judges and Magistrates',\
	'25-2012 Kindergarten Teachers Except Special Education',\
	'25-2021 Elementary School Teachers Except Special Education',\
	'29-1041 Optometrists',\
	'29-2054 Respiratory Therapy Technicians',\
	'33-2011 Firefighters',\
	'37-1012 First-Line Supervisors of Landscaping Lawn Service and Groundskeeping Workers',\
	'39-1011 Gaming Supervisors',\
	'39-2011 Animal Trainers',\
	'41-1011 First-Line Supervisors of Retail Sales Workers',\
	'41-1012 First-Line Supervisors of Non-Retail Sales Workers',\
	'41-2011 Cashiers',\
	'41-2031 Retail Salespersons',\
	'43-3021 Billing and Posting Clerks',\
	'45-1011 First-Line Supervisors of Farming, Fishing, and Forestry Workers',\
	'49-2011 Computer Automated Teller and Office Machine Repairers',\
	'53-3021 Bus Drivers Transit and Intercity',\
	'53-4031 Railroad Conductors and Yardmasters',\
	'55-1011 Air Crew Officers',\
	'55-1012 Aircraft Launch and Recovery Officers',\
	'55-1013 Armored Assault Vehicle Officers',\
	]
	#Sets variable to Embassy flag
	Privately_ATM_Operator=Embassy_Consulate
	#List for random products
	Products=['Certificate of Deposit',\
	'Checking Account',\
	'Credit Card',\
	'Custodial and Investment Agency - Institutional',\
	'Custodial and Investment Agency - Personal',\
	'Custodial/Trust Outsourcing Services (BTOS)',\
	'Custody Accounts (PTIM)',\
	'Custody Accounts (RSTC)',\
	'DTF (BHFA)',\
	'Investment Agency - Personal',\
	'Investment Management Account (PTIM)',\
	'Lease',\
	'Loan / Letter of Credit',\
	'Money Market',\
	'Mortgage / Bond / Debentures',\
	'None',\
	'Savings Account',\
	'Trust Administration - Irrevocable and Revocable (PTIM)',\
	'Trust Administration - Irrevocable and Revocable Trusts (BDTC)',\
	] + ['Nondeposit Investment Products'] * 14 + ['Investment Agency - Institutional'] * 5
	#Sets variable to Embassy flag
	Sales_Used_Vehicles=Embassy_Consulate
	#Dictionary for random Services
	Services=['Benefit Payment Services',\
	'Domestic Wires and Direct Deposit / ACH',\
	'Family Office Services (FOS)',\
	'Fiduciary Services',\
	'International Wires and IAT',\
	'Investment Advisory Services (IAS)',\
	'Investment Services',\
	'None',\
	'Online / Mobile Banking',\
	'Payroll',\
	'Short Term Cash Management',\
	'Trust Services',\
	'Trustee Services',\
	'Vault Cash Services',\
	] + ['Financial Planning'] * 6 + ['Retirement Plans'] * 19
	#Dictionary for random SIC_Code
	SIC_Code=['6021 National Commercial Banks',\
	'6211 Security Brokers Dealers and Flotation Companies',\
	'6282 Investment Advice',\
	'6311 Life Insurance',\
	'6733 Trusts Except Educational Religious and Charitable',\
	'8999 Services NEC',\
	] + ['6722 Management Investment Offices Open-End'] * 12
	#Dictionary for random Market Listing
	Stock_Market_Listing=['Australian Stock Exchange',\
	'Brussels Stock Exchange',\
	'Montreal Stock Exchange',\
	'Tiers 1 and 2 of the TSX Venture Exchange (also known as Tiers 1 and 2 of the Canadian Venture Exchange)',\
	'Toronto Stock Exchange',\
	] + ['Not Found'] * 30
	#Sets variable to Embassy flag
	Third_Party_Payment_Processor=Embassy_Consulate
	#Sets variable to Embassy flag
	Transacting_Provider=Embassy_Consulate
	#Dictionary for random Low Net Worth
	LowNet=[1,2] + [0] * 5
	#Dictionary for Consumer vs Business
	Acct_Type = ['B'] + ['C'] * 5
	#Dictionary for random number of credits cards per account
	Number_CC = [1] * 7 + [2] * 11 + [3] * 3 + [4]
	#Dictionary for Account list set to blank
	acct_list=[]
	#Dictionary for CreditCard list set to blank
	CC_list = []
	
	#Dictionary for random Wolfsberg scenario
	Use_Case = [1,4,7,10,13,16,19,22,25,28,31,34,39] * 4 + [2,5,8,11,14,17,20,23,26,29,32,35,38] * 7 + [3,6,9,12,15,18,21,24,27,30,33,36] * 65 + [37] * 73 + [40,41] * 2
	refrating = ['1','1','1','2','3','4','2','4','5','5','5','5','5','5','5','5','5','5','5','5']
	fake = Faker()
	global liSSNMaster
	start=10786147
	acct_list=[]
	liCSV = []
	for i in xrange(N):
		#Initiate High Risk Flags
		#Politically Exposed Person
		PEP='No'
		#Customer with a Suspicous Activity Report
		SAR='No'
		#Customer with a closed account
		Clsd='No'
		#High risk customer flag
		high_risk='No'
		#High Risk Rating
		hr_rating=''
		#Customer that was demarketed by the bank
		demarket='No'
		dem_date=''
		#generate closed acct flag
		if (max((randrange(0,98,1)-96),0)==1):
			Clsd='Yes'
		#Random choice for number of credit card users per account number
		No_CCs = random.choice(Number_CC)
		#Generate account number
		acct=start+1+randrange(1,10,1)
		start=acct
		#Randomly generate customer name + middle name in tmp
		name = fake.name()
		tmp=gen_data.create_name()
		#Adds account number to account dictionary
		acct_list.extend([acct])
		#Creates a new row and adds data elements
		row = [i]+[acct]+[random.choice(Acct_Type)]+[No_CCs]+[name]+[tmp[0]]+[liSSNMaster[i]]
		#Dictionary for names list set to blank
		names=[]
		#Dictionary for Social Security Number list set to blank
		ssn=[]
		#Middle Name to reduce name dups
		mdl=[]
		
		for j in range(No_CCs-1):
			names.insert(j,fake.name())
			tmp2=gen_data.create_name()
			mdl.insert(j,tmp2[0])
		##Pull from SSN Master list
			randInt = randrange(1,len(liSSNMaster),1)
			if randInt != i:
				ssn.insert(j,liSSNMaster[randInt])
			else:
				ssn.insert(j,liSSNMaster[randInt - 1])
			
		#Name and SSN is set to blank if less than 4 customers on an account
		for k in range(4-No_CCs):
			names.insert(No_CCs+k,'')
			ssn.insert(No_CCs+k,'')
			mdl.insert(No_CCs,'')
			
		#Sets CC_NO to a random credit card number
		CC_NO=gen_data.cc_number()
		#Extract CC_Number from the tuple returned by CC_Number then scramble to ensure uniqueness...Tuple contains CC Number and Type
		CC_TRANS=CC_NO[1][0]
		dt = str(datetime.now())
		clean=re.sub('\W','',dt)
		printCC=str(CC_TRANS[-4:])+str(clean[-12:-3])+str(randrange(1111,9999,randrange(1,10,1)))
		
		#Add data elements to current csv row
		row.extend([names[0],mdl[0],ssn[0],names[1],mdl[1],ssn[1],names[2],mdl[2],ssn[2],printCC,CC_NO[0],gen_data.create_company_name()+' '+tmp[1],\
		gen_data.create_email(),gen_data.create_job_title()])
		#Create Current Address
		zip=random.choice(zips.zip)
		addr=geo_data.create_city_state_zip[zip]
		#Create Previous address
		zip2=random.choice(zips.zip)
		addr2=geo_data.create_city_state_zip[zip2]
		#Add additional data elements to current csv row
		lrg_cash_ex=random.choice(Yes_No)
		#Condition for SARs and Demarketed Clients
		if(Clsd=='Yes'):
			#1% of closed accounts are demarketed but never had a SAR filed
			if (max((randrange(0,101,1)-99),0)==1 and SAR=='No'):
				demarket='Yes'
				dem_date=gen_data.create_date(past=True)
			if (max((randrange(0,11,1)-9),0)==1 and demarket=='No'):
				#10% of closed accounts have SARs
				SAR='Yes'
				#90% of closed accounts with SARs are demarketed
				if(max((randrange(0,11,1)-9),0)==0):
					demarket='Yes'
					dem_date=gen_data.create_date(past=True)
				
		if (max((randrange(0,101,1)-99),0)==1):
			PEP='Yes'
		row.extend([addr[0],addr[1],zip,'US',addr2[0],addr2[1],zip2,'US',gen_data.create_birthday(min_age=2, max_age=85),PEP,SAR,Clsd])
		
		#Start Generating related accounts from account list once 10,000 accounts are generated - to avoid duplicating accounts in the beginning
		if i > 10000:
			rel = int(random.choice(acct_list))*max((randrange(0,10001,1)-9999),0)
			if rel <> 0:
				row.append(rel)
				row.append(random.choice(Related_Type))
			else:
				row.append('')
				row.append('')
		else:
			row.append('')
			row.append('')
		
		#Randomly generates account start date
		party_start=gen_data.create_date(past=True)
		#Randomly selects consent option for sharing info
		Consent_Share = random.choice(Yes_No_Consent)
		#Add additional data elements to current csv row
		row.extend([random.choice(Party_Type),random.choice(Party_Relation),party_start,gen_data.create_date(past=True),\
		lrg_cash_ex,demarket,dem_date,randrange(0,100,1),random.choice(Official_Lang)])
		#Add data element preferred methond of contact for yes to share info...if not then blank to current row
		
		if Consent_Share == 'Yes':
			row.extend(['Yes',random.choice(Preffered_Channel)])
		else:
			row.extend(['No',''])
		
		row.extend([zip,randrange(0,5,1)])
		#Generate Segment ID then add additional Segment data based on the selection to the current csv row
		Segment_ID = randrange(0,5,1)%5
		if Segment_ID == 0:
			row.extend([Model_ID[0],Seg_Model_Type[0],Seg_Model_Name[0],Seg_Model_Group[0],Seg_Model_Description[0],Seg_Model_Score[0]])
		if Segment_ID == 1:
			row.extend([Model_ID[1],Seg_Model_Type[1],Seg_Model_Name[1],Seg_Model_Group[1],Seg_Model_Description[1],Seg_Model_Score[1]])
		if Segment_ID == 2:
			row.extend([Model_ID[2],Seg_Model_Type[2],Seg_Model_Name[2],Seg_Model_Group[2],Seg_Model_Description[2],Seg_Model_Score[2]])
		if Segment_ID == 3:
			row.extend([Model_ID[3],Seg_Model_Type[3],Seg_Model_Name[3],Seg_Model_Group[3],Seg_Model_Description[3],Seg_Model_Score[3]])
		if Segment_ID == 4:
			row.extend([Model_ID[4],Seg_Model_Type[4],Seg_Model_Name[4],Seg_Model_Group[4],Seg_Model_Description[4],Seg_Model_Score[4]])
		
		#Add additional data elements to current csv row
		hr0=random.choice(Arms_Manufacturer)
		hr01=random.choice(Auction)
		hr02=random.choice(CashIntensive_Business)
		hr03=random.choice(Casino_Gambling)
		hr04=random.choice(Channel_Onboarding)
		hr05=random.choice(Channel_Ongoing_Transactions)
		row.extend([hr0,hr01,hr02,hr03,hr04,hr05])
		#Randomly select whether customer has a High Net Worth
		HighNetWorthFlag = random.choice(HighNetWorth)
		#Randomly Generate customer net worth based on the above flag
		if HighNetWorthFlag == 'Yes':
			row.append(max(max((randrange(0,101,1)-99),0)*randrange(1000000,25000000,1),randrange(1000000,5000000,1)))
		else:
			flag=random.choice(LowNet)
			if flag==0:
				row.append(randrange(-250000,600000,1))
			else:
				if flag==1:
					row.append(randrange(149000,151000,1))
				else:
					row.append(randrange(40000,50000,1))
		#Add data elements to current csv row
		hr1=random.choice(Complex_HI_Vehicle)
		hr2=random.choice(Dealer_Precious_Metal)
		hr3=random.choice(Digital_PM_Operator)
		hr4=random.choice(Embassy_Consulate)
		hr5=random.choice(Exchange_Currency)
		hr6=random.choice(Foreign_Financial_Institution)
		hr7=random.choice(Foreign_Government)
		hr8=random.choice(Foreign_NonBank_Financial_Institution)
		hr9=random.choice(Internet_Gambling)
		hr10=random.choice(Medical_Marijuana_Dispensary)
		hr11=random.choice(Money_Service_Business)
		hr12=random.choice(NAICS.NAICS_Code)
		hr13=random.choice(NonRegulated_Financial_Institution)
		hr14=random.choice(Not_Profit)
		#hr15=random.choice(Occupation) - added before through gen_data
		hr16=random.choice(Privately_ATM_Operator)
		hr17=random.choice(Products)
		hr18=random.choice(Sales_Used_Vehicles)
		hr19=random.choice(Services)
		hr20=random.choice(SIC_Code)
		hr21=random.choice(Stock_Market_Listing)
		hr22=random.choice(Third_Party_Payment_Processor)
		hr23=random.choice(Transacting_Provider)
		
		if(PEP=='Yes' or SAR=='Yes' or lrg_cash_ex=='Yes' or demarket=='Yes' or hr0=='Yes'
		or hr01=='Yes' or hr02=='Yes' or hr03=='Yes' or hr1=='Yes' or hr2=='Yes' or hr3=='Yes' or hr4=='Yes' or
		hr5=='Yes' or hr6=='Yes' or hr7=='Yes' or hr8=='Yes' or hr9=='Yes' or hr10=='Yes' or hr11=='Yes' or hr13=='Yes' or hr14=='Yes' or
		hr16=='Yes' or hr17=='Yes' or hr18=='Yes' or hr22=='Yes' or hr23=='Yes' or HighNetWorthFlag=='Yes'):
			high_risk='Yes'
			hr_rating=random.choice(refrating)
		if(SAR=='No' and high_risk=='No'):
			if(max((randrange(0,101,1)-99),0)==1):
				high_risk='Yes'
				hr_rating=random.choice(refrating)
		if(PEP=='No' and high_risk=='No'):
			if(max((randrange(0,101,1)-99),0)==1):
				high_risk='Yes'
				hr_rating=random.choice(refrating)
		if(high_risk=='No'):
			if(max((randrange(0,101,1)-99),0)==1):
				high_risk='Yes'
				hr_rating=random.choice(refrating)
		row.extend([hr1,hr2,hr3,hr4,hr5,hr6,hr7,hr8,hr9,hr10,hr11,hr12,hr13,hr14,hr16,hr17,hr18,hr19,hr20,hr21,hr22,hr23,
		HighNetWorthFlag,high_risk,hr_rating,random.choice(Use_Case)])
		liCSV.append(row)
	return liCSV

def createSSNs(N):
	liSSN=[]
	for i in xrange(N):
		liSSN.append(''.join(str(random.randint(0,9)) for _ in xrange(9)))
	return liSSN

def createFile(liCust):
	#Creates CSV
	with open('uber_cust.csv','w') as f1:
		#Writer for CSV...Pipe delimited...Return for a new line
		writer=csv.writer(f1, delimiter='|',lineterminator='\n',)
		#Header Row
		writer.writerow(['ROWNUM']+['ACCOUNTID']+['ACCT_TYPE']+['NUM_CCS']+['NAME']+['M_NAME']+['SSN']+['AUTHORIZED_NAME2']+['M_NAME2']+['SSN2']+\
		['AUTHORIZED_NAME3']+['M_NAME3']+['SSN3']+['AUTHORIZED_NAME4']+['M_NAME4']+['SSN4']+['CREDITCARDNUMBER']+['CREDITCARDTYPE']+['EMPLOYER']+['CUSTEMAIL']+\
		['OCCUPATION']+['CITY']+['STATE']+['ZIP']+['COUNTRY']+['PREVIOUS_CITY']+['PREVIOUS_STATE']+\
		['PREVIOUS_ZIP']+['PREVIOUS_COUNTRY']+['DOB']+['PEP']+['SAR']+['CLOSEDACCOUNT']+['RELATED_ACCT']+['RELATED_TYPE']+['PARTY_TYPE']+['PARTY_RELATION']+['PARTY_STARTDATE']+['PARTY_ENDDATE']+\
		['LARGE_CASH_EXEMPT']+['DEMARKET_FLAG']+['DEMARKET_DATE']+['PROB_DEFAULT_RISKR']+['OFFICIAL_LANG_PREF']+['CONSENT_SHARING']+\
		['PREFERRED_CHANNEL']+['PRIMARY_BRANCH_NO']+['DEPENDANTS_COUNT']+['SEG_MODEL_ID']+['SEG_MODEL_TYPE']+\
		['SEG_MODEL_NAME']+['SEG_MODEL_GROUP']+['SEG_M_GRP_DESC']+['SEG_MODEL_SCORE']+['ARMS_MANUFACTURER']+['AUCTION']+\
		['CASHINTENSIVE_BUSINESS']+['CASINO_GAMBLING']+['CHANNEL_ONBOARDING']+['CHANNEL_ONGOING_TRANSACTIONS']+['CLIENT_NET_WORTH']+\
		['COMPLEX_HI_VEHICLE']+['DEALER_PRECIOUS_METAL']+['DIGITAL_PM_OPERATOR']+['EMBASSY_CONSULATE']+['EXCHANGE_CURRENCY']+\
		['FOREIGN_FINANCIAL_INSTITUTION']+['FOREIGN_GOVERNMENT']+['FOREIGN_NONBANK_FINANCIAL_INSTITUTION']+['INTERNET_GAMBLING']+\
		['MEDICAL_MARIJUANA_DISPENSARY']+['MONEY_SERVICE_BUSINESS']+['NAICS_CODE']+['NONREGULATED_FINANCIAL_INSTITUTION']+\
		['NOT_PROFIT']+['PRIVATELY_ATM_OPERATOR']+['PRODUCTS']+['SALES_USED_VEHICLES']+['SERVICES']+\
		['SIC_CODE']+['STOCK_MARKET_LISTING']+['THIRD_PARTY_PAYMENT_PROCESSOR']+['TRANSACTING_PROVIDER']+['HIGH_NET_WORTH']+['HIGH_RISK']+['RISK_RATING']+['USE_CASE_SCENARIO'])
		for i in liCust:
			writer.writerow(i)


#Create list of SSNs up to numUniSSNs and use that as a source for SSN numbers
#Multi-Thread SSN creation
startT = time.time()
numUniSSNs = 300
#set number of processes 
proc = 10
remainder = numUniSSNs % proc
pool = Pool(processes=proc)
results = pool.map(createSSNs, (numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,((numUniSSNs/10) + remainder)))
liSSNMaster = results[0] + results[1] + results[2] + results[3] + results[4] + results[5] + results[6] + results[7] + results[8] + results[9]
liSSNMaster = list(set(liSSNMaster))
endT = time.time()
totT = endT - startT
totT = ("{0:.1f}".format(round(totT,2)))
print "It took " + str(totT) + " seconds to create " + str(len(liSSNMaster)) + " SSNs"

#Only create as many records as unique SSNs in liSSNMaster
startT = time.time()
#Use xrange instead of range to minimize memory allocation
numCusts = 101
#if the list of unique SSNs is lesser than the cust count to be created, regenerate an increased list
if len(liSSNMaster) < numCusts:
	liSSNMaster=[]
	numUniSSNs = numUniSSNs + numCusts
	remainder = numUniSSNs % proc
	results = pool.map(createSSNs, (numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,numUniSSNs/10,((numUniSSNs/10) + remainder)))
	liSSNMaster = results[0] + results[1] + results[2] + results[3] + results[4] + results[5] + results[6] + results[7] + results[8] + results[9]
	liSSNMaster = list(set(liSSNMaster))

#Multi-thread the customer list generation 
pool2 = Pool(processes=proc)
remainder = numCusts % proc
custResults = pool2.map(createCusts, (numCusts/10,numCusts/10,numCusts/10,numCusts/10,numCusts/10,numCusts/10,numCusts/10,numCusts/10,numCusts/10,((numCusts/10) + remainder)))
liCust = custResults[0] + custResults[1] + custResults[2] + custResults[3] + custResults[4] + custResults[5] + custResults[6] + custResults[7] + custResults[8] + custResults[9]
for index,cust in enumerate(liCust):
	cust[0] = index
endT = time.time()
totT = endT - startT
totT = ("{0:.1f}".format(round(totT,2)))
print "It took " + str(totT) + " seconds to create " + str(len(liCust)) + " customer records"
createFile(liCust)
print "File created"
