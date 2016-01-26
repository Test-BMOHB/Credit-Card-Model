#Developer    : Ivana Donevska/Jeff Kamin
#Date         : 2016-01-20
#Program Name : Customer DataGenerator
#Version#     : 5
#Description  : Code that generates customer data
#-----------------------------------------------------------------------------
# History  | ddmmyyyy  |  User     |                Changes
#          | 01192016  | Ivana D.  | Credit Card model,code, ref lists, etc...
#			 01202016  | Jeff K.   | Comments, ref lists, etc...
#-----------------------------------------------------------------------------*/
#Reference data is located on the test-bmohb console gs://newccdatav3

from random import randrange, random, shuffle
from datetime import datetime
from faker import Faker
from barnum import gen_data
import csv, NAICS, random, geo_data, zips, re

#Dictionary for client whose net worth is over $500K
HighNetWorth = ['Yes','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No']
#Dictionary for type of account
Related_Type = ['Primary','Secondary','Joint']
#Dictionary for how the account was opened
Party_Type = ['Person','Non-Person']
#Dictionary for a BMO customer
Party_Relation = ['Customer','Non-Customer']
#Dictionary for random Yes/No Flag
Yes_No = ['Yes','No','No','No','No','No','No','No','No','No','No','No','No']
#Dictionary for random Yes/No Consent
Yes_No_Consent = ['Yes','No','No','No','No']
#Dictionary for equal Yes/No Flag
Yes_No_50 = ['Yes','No']
#Dictionary for official language
Official_Lang = ['English','English','English','French']
#Dictionary for method of communication
Preffered_Channel = ['Direct Mail','Telemarketing','Email','SMS']
#Dictionary for status of customer
#Customer_Status = ['Prospect','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Inactive Customer','Past Customer']
#Dictionary for LOB Segment Type
Seg_Model_Type = ['LOB Specific','Profitability','Geographical','Behavioral','Risk Tolerance']
#Dictionary for Model ID
Model_ID = ['01','02','03','04','05']
#Dictionary for Model Name
Seg_Model_Name = ['IRRI', 'CRS Risk Score','Geo Risk','Financial Behavior Risk','CM Risk']
#Dictionary for Model Score
Seg_Model_Score = ['200','300','400','100','500']
#Dictionary for Model Group
Seg_Model_Group = ['Group 1','Group 1','Group 2','Group 3','Group 4']
#Dictionary for Model Description
Seg_Model_Description = ['High Risk Tier','Mid Risk Tier','Low Risk Tier','Vertical Risk','Geographical Risk']
#Dictionary for random Arms Dealer flag
Arms_Manufacturer=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
#Dictionary for random auction flag
Auction=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
#Dictionary for random Cash Intensive flag
CashIntensive_Business=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
#Dictionary for random Casino?Gaming flag
Casino_Gambling=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
#Dictionary for random Client Onboarding flag
Channel_Onboarding=['E-mail','In Person','In person - In Branch/Bank Office','In person - Offsite/Client Location','Mail', \
                                                                                'Not Applicable','Not Applicable','Not Applicable','Not Applicable','Not Applicable','Not Applicable','Not Applicable',\
                                                                                'Not Applicable','Not Applicable','Not Applicable','Online','Phone',\
                                                                                'Request for Proposal (RFP)']
#Dictionary for random Transaction flag
Channel_Ongoing_Transactions=['ATM','E-mail','Fax','In Person','In Person','In Person','In Person',\
                                                                                                                'In Person','In Person','In Person','In Person','In Person','In Person','In Person',\
                                                                                                                'In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person',\
                                                                                                                'In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person',\
                                                                                                                'In Person','In Person','Mail','Not Applicable','Online','Online','Online','Online','OTC Communication System','Phone',]

#Dictionary for random HI_Vehicle flag
Complex_HI_Vehicle=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
#Dictionary for random Metals flag
Dealer_Precious_Metal=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
#Dictionary for random Arms Dealer flag
Digital_PM_Operator=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
#Dictionary for random Embassy flag
Embassy_Consulate=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
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
#Dictionary for random occupation
Occupation=['11-1011 Chief Executives',\
'11-3011 Administrative Services Managers',\
'11-3031 Financial Managers',\
'11-3061 Purchasing Managers',\
'13-1011 Agents and Business Managers of Artists, Performers, and Athletes',\
'13-1031 Claims Adjusters, Examiners, and Investigators',\
'13-1199 Business Operations Specialists, All Other',\
'13-2099 Financial Specialists, All Other',\
'17-1011 Architects, Except Landscape and Naval',\
'23-1011 Lawyers',\
'23-1023 Judges, Magistrate Judges, and Magistrates',\
'25-2012 Kindergarten Teachers, Except Special Education',\
'25-2021 Elementary School Teachers, Except Special Education',\
'29-1041 Optometrists',\
'29-2054 Respiratory Therapy Technicians',\
'33-2011 Firefighters',\
'37-1012 First-Line Supervisors of Landscaping, Lawn Service, and Groundskeeping Workers',\
'39-1011 Gaming Supervisors',\
'39-2011 Animal Trainers',\
'41-1011 First-Line Supervisors of Retail Sales Workers',\
'41-1012 First-Line Supervisors of Non-Retail Sales Workers',\
'41-2011 Cashiers',\
'41-2031 Retail Salespersons',\
'43-3021 Billing and Posting Clerks',\
'45-1011 First-Line Supervisors of Farming, Fishing, and Forestry Workers',\
'49-2011 Computer, Automated Teller, and Office Machine Repairers',\
'53-3021 Bus Drivers, Transit and Intercity',\
'53-4031 Railroad Conductors and Yardmasters',\
'55-1011 Air Crew Officers',\
'55-1012 Aircraft Launch and Recovery Officers',\
'55-1013 Armored Assault Vehicle Officers',\
]
#Sets variable to Embassy flag
Privately_ATM_Operator=Embassy_Consulate
#Dictionary for random products
Products=['Certificate of Deposit',\
'Checking Account',\
'Credit Card',\
'Custodial and Investment Agency - Institutional',\
'Custodial and Investment Agency - Personal',\
'Custodial/Trust Outsourcing Services (BTOS)',\
'Custody Accounts (PTIM)',\
'Custody Accounts (RSTC)',\
'DTF (BHFA)',\
'Investment Agency - Institutional','Investment Agency - Institutional','Investment Agency - Institutional','Investment Agency - Institutional','Investment Agency - Institutional',\
'Investment Agency - Personal',\
'Investment Management Account (PTIM)',\
'Lease',\
'Loan / Letter of Credit',\
'Money Market',\
'Mortgage / Bond / Debentures',\
'Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products',\
'None',\
'Savings Account',\
'Trust Administration - Irrevocable and Revocable (PTIM)',\
'Trust Administration - Irrevocable and Revocable Trusts (BDTC)',\
]
#Sets variable to Embassy flag
Sales_Used_Vehicles=Embassy_Consulate
#Dictionary for random Services
Services=['Benefit Payment Services',\
'Domestic Wires and Direct Deposit / ACH',\
'Family Office Services (FOS)',\
'Fiduciary Services',\
'Financial Planning','Financial Planning','Financial Planning','Financial Planning','Financial Planning','Financial Planning',\
'International Wires and IAT',\
'Investment Advisory Services (IAS)',\
'Investment Services',\
'None',\
'Online / Mobile Banking',\
'Payroll',\
'Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans',\
'Short Term Cash Management',\
'Trust Services',\
'Trustee Services',\
'Vault Cash Services',\
]
#Dictionary for random SIC_Code
SIC_Code=['6021 National Commercial Banks',\
'6211 Security Brokers Dealers and Flotation Companies',\
'6282 Investment Advice',\
'6311 Life Insurance',\
'6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End','6722 Management Investment Offices Open-End',\
'6733 Trusts Except Educational Religious and Charitable',\
'8999 Services NEC',\
]
#Dictionary for random Market Listing
Stock_Market_Listing=['Australian Stock Exchange',\
'Brussels Stock Exchange',\
'Montreal Stock Exchange',\
'Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found',\
'Tiers 1 and 2 of the TSX Venture Exchange (also known as Tiers 1 and 2 of the Canadian Venture Exchange)',\
'Toronto Stock Exchange',\
]
#Sets variable to Embassy flag
Third_Party_Payment_Processor=Embassy_Consulate
#Sets variable to Embassy flag
Transacting_Provider=Embassy_Consulate
#Dictionary for random Low Net Worth
LowNet=[0,0,0,0,0,1,2]
#Dictionary for Consumer vs Business
Acct_Type = ['C','C','C','C','C','B']
#Dictionary for random number of credits cards per account
Number_CC = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,4]
#Dictionary for Account list set to blank
acct_list=[]
#Dictionary for CreditCard list set to blank
CC_list = []
#Dictionary for random Wolfsberg scenario
Use_Case = [1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,13,13,13,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,20,20,20,20,20,20,20,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,22,22,22,22,23,23,23,23,23,23,23,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,25,25,25,25,26,26,26,26,26,26,26,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,28,28,28,28,29,29,29,29,29,29,29,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,31,31,31,31,32,32,32,32,32,32,32,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,34,34,34,34,35,35,35,35,35,35,35,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,38,38,38,38,38,38,38,39,39,39,39,40,40,41,41]
fake = Faker()

#Creates CSV
with open('uber_cust_185M.csv','w') as f1:
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
	#Loop for number of accounts to generate
	start=10786147
	acct_list=[]
	#JS - Update code 1/26/2016
 	#JS - Create list of SSNs up to 20M and use that to pull from
        liSSNMaster=[]
        for i in xrange(30000000):
                liSSNMaster.append(''.join(str(random.randint(0,9)) for _ in xrange(9)))
        #JS - Only create as many records as the SSN list has available
 	#JS - Use xrange instead of range to minimize memory allocation
 	liSSNMaster = list(set(liSSNMaster))
 	if len(liSSNMaster) < 18500000:
                liSSNMaster=[]
                for i in xrange(50000000):
                        liSSNMaster.append(''.join(str(random.randint(0,9)) for _ in xrange(9)))
                liSSNMaster = list(set(liSSNMaster))
 	for i in xrange(18500000):
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

		#Random number generator for account number
		#acct = randrange(100000,100000000,1)
		#Random choice for number of credit cards per account number
		No_CCs = random.choice(Number_CC)
		#while acct_list.count(acct) > 0:
		#	acct = randrange(100000,100000000,1)
		#dt = str(datetime.now())
		#acct=str(i)++re.sub('\W','',dt)
		acct=start+1+randrange(1,10,1)
		start=acct
		#Randomly generates customer name
		name = fake.name()
		tmp=gen_data.create_name()
		#Adds account number to account dictionary
		acct_list.extend([acct])
		#Creates a new row and adds data elements
##      JS - Main Account Holder SSN as current index in master SSN list	
##		row = [i]+[acct]+[random.choice(Acct_Type)]+[No_CCs]+[name]+[tmp[0]]+[(str(randrange(101,1000,1))+str(randrange(10,100,1))+str(randrange(1000,10000,1)))]
		row = [i]+[acct]+[random.choice(Acct_Type)]+[No_CCs]+[name]+[tmp[0]]+[liSSNMaster[i]]
		#Dictionary for names list set to blank
		names=[]
		#Dictionary for Social Security Number list set to blank
		ssn=[]
		#Generates Name and SSN for Credit Users
        #Middle Name to reduce name dups
		mdl=[]
		for j in range(No_CCs-1):
			names.insert(j,fake.name())
			tmp2=gen_data.create_name()
			mdl.insert(j,tmp2[0])
##      JS - Pull from SSN Master list
 			#ssn.insert(j,(str(randrange(101,1000,1))+str(randrange(10,100,1))+str(randrange(1000,10000,1))))
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

		#Extract CC_Number from the tuple returned by CC_Number...Tuple contains CC Number and Type
		#while CC_list.count(CC_NO[1][0]) > 0:
		CC_TRANS=CC_NO[1][0]

		dt = str(datetime.now())
		clean=re.sub('\W','',dt)
		printCC=str(CC_TRANS[-4:])+str(clean[-12:-3])+str(randrange(1111,9999,randrange(1,10,1)))
		#str(CC_TRANS[-4:])+str(clean[-12:-2])+str(randrange(1111,9999,randrange(1,10,1)))
		#Add CC_Number to control list to prevent duplicates
		#Add data elements to current csv row
		row.extend([names[0],mdl[0],ssn[0],names[1],mdl[1],ssn[1],names[2],mdl[2],ssn[2],printCC,CC_NO[0],gen_data.create_company_name()+' '+tmp[1],\
		gen_data.create_email(),gen_data.create_job_title()])

		#Creates Current Address
		zip=random.choice(zips.zip)
		addr=geo_data.create_city_state_zip[zip]
		#Creates Previous address
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
		#Start Generating related accounts from account list once 10,000 accounts are generated
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
		#DO NOT USE CUST STATUS BELOW - NOT INTEGRATED WITH CLOSED STATUS! Add additional data elements to current csv row
		row.extend([zip,randrange(0,5,1)])

		#Generates Segment ID then adds additional Segment data based on the selection to the current csv row
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

		#Randomly select whther customer has a High Net Worth
		HighNetWorthFlag = random.choice(HighNetWorth)

		#Randomly Generates customer net worth based on the above flag
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
		#hr15=random.choice(Occupation)
		hr16=random.choice(Privately_ATM_Operator)
		hr17=random.choice(Products)
		hr18=random.choice(Sales_Used_Vehicles)
		hr19=random.choice(Services)
		hr20=random.choice(SIC_Code)
		hr21=random.choice(Stock_Market_Listing)
		hr22=random.choice(Third_Party_Payment_Processor)
		hr23=random.choice(Transacting_Provider)


		refrating=['1','1','1','2','3','4','2','4','5','5','5','5','5','5','5','5','5','5','5','5']
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
		#End the current row
		writer.writerow(row)
