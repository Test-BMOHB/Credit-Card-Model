#Developer    : Ivana Donevska
#Date         : 2016-01-12
#Program Name : Credit Card Transactions Generator
#Version#     : 1
#Description  : Logic for credit card transactions, and use cases based on the Wolfsberg principles
#-----------------------------------------------------------------------------
# History  | ddmmyyyy  |  User     |                Changes
#          | 01202016  | Ivana D.  | Transactions Model, code, Use cases implementation and gen_tran function
#		   | 01222016  | Jeff  K.  | File parsing logic, credit card business logic validation, ref lists
#          | 02022016  | Ivana D.  | Code review and comments
#-----------------------------------------------------------------------------*/
#Reference data for python_account_ID, python_merchant_cat, python_CC is located on the test-bmohb console gs://newccdatav3
from random import randrange, random, shuffle
from faker import Faker
from barnum import gen_data
from datetime import date, timedelta, datetime
from collections import defaultdict
from multiprocessing import Pool
from functools import partial
import csv, re, random, python_merchant_cat, Airlines, Country, Hotels, Merchant_Category, Transaction_DistLoc, Transaction_Type, multiprocessing, multiprocessing.pool

fake = Faker()
#Distinct List of Payments, Credits and Debits
Account_Holder_Type_Red = ['2222'] * 5 + ['1111'] * 5
Account_Holder_Type_Yellow = ['2222'] * 3 + ['1111'] * 5
Account_Holder_Type_Green = ['2222'] + ['1111'] * 6
Payment_DistLoc_Red = ['BH', 'BB', 'BW', 'BG', 'CM', 'CG', 'HR', 'CW', 'CZ', 'TL', 'TP', 'SV', 'ET', 'GE', 'IN', 'IL', 'JM', 'KI', 'XK', 'LS', 'MK', 'MT', 'FM', 'ME', 'NA', 'NR', 'NZ', 'NU', 'PS', 'PL', 'QA', 'RW', 'RS', 'SG', 'SK', 'ZA', 'ES', 'TW', 'TC', 'AE', 'AG', 'AM', 'AU', 'AT', 'BT', 'BQ', 'CA', 'CV', 'CL', 'CX', 'CC', 'DK', 'DJ', 'EE', 'FO', 'FJ', 'DE', 'GL', 'VA', 'HK', 'IS', 'IT', 'LV', 'MU', 'NL', 'NF', 'OM', 'PR', 'AX', 'AS', 'BE', 'FK', 'FI', 'FR', 'GF', 'PF', 'GP', 'GU', 'HU', 'IE', 'LT', 'MQ', 'YT', 'NC', 'MP', 'NO', 'PN', 'PT', 'RE', 'BL', 'SH', 'MF', 'PM', 'SM', 'SI', 'SJ', 'SE', 'CH', 'TV', 'GB', 'VI', 'WF'] + ['US'] * 98
Payment_DistLoc_Yellow = ['BH', 'BB', 'BW', 'BG', 'CM', 'CG', 'HR', 'CW', 'CZ', 'TL', 'TP', 'SV', 'ET', 'GE', 'IN', 'IL', 'JM', 'KI', 'XK', 'LS', 'MK', 'MT', 'FM', 'ME', 'NA', 'NR', 'NZ', 'NU', 'PS', 'PL', 'QA', 'RW', 'RS', 'SG', 'SK', 'ZA', 'ES', 'TW', 'TC', 'AE', 'AG', 'AM', 'AU', 'AT', 'BT', 'BQ', 'CA', 'CV', 'CL', 'CX', 'CC', 'DK', 'DJ', 'EE', 'FO', 'FJ', 'DE', 'GL', 'VA', 'HK', 'IS', 'IT', 'LV', 'MU', 'NL', 'NF', 'OM', 'PR', 'AX', 'AS', 'BE', 'FK', 'FI', 'FR', 'GF', 'PF', 'GP', 'GU', 'HU', 'IE', 'LT', 'MQ', 'YT', 'NC', 'MP', 'NO', 'PN', 'PT', 'RE', 'BL', 'SH', 'MF', 'PM', 'SM', 'SI', 'SJ', 'SE', 'CH', 'TV', 'GB', 'VI', 'WF'] + ['US'] * 119
Payment_DistLoc_Green = ['CA', 'CV', 'CL', 'CX', 'CC', 'DK', 'DJ', 'EE', 'FO', 'FJ', 'DE', 'GL', 'VA', 'HK', 'IS', 'IT', 'LV', 'MU', 'NL', 'NF', 'OM', 'PR', 'AX', 'AS', 'BE', 'FK', 'FI', 'FR', 'GF', 'PF', 'GP', 'GU', 'HU', 'IE', 'LT', 'MQ', 'YT', 'NC', 'MP', 'NO', 'PN', 'PT', 'RE', 'BL', 'SH', 'MF', 'PM', 'SM', 'SI', 'SJ', 'SE', 'CH', 'TV', 'GB', 'VI', 'WF'] + ['US'] * 183
High_Risk_Countries_Green = ['AF', 'AO', 'AZ', 'BD', 'BY', 'BZ', 'BO', 'MM', 'KH', 'KM', 'CD', 'CI', 'CU', 'GN', 'GW', 'GY', 'HT', 'ID', 'IR', 'IQ', 'KZ', 'KE', 'KP', 'LA', 'LB', 'LR', 'LY', 'NG', 'PK', 'PG', 'PY', 'SL', 'SX', 'SO', 'SD', 'SY', 'TH', 'TR', 'VE', 'VN', 'YE', 'ZW', 'AL', 'DZ', 'AD', 'AI', 'AR', 'AW', 'BS', 'BJ', 'BM', 'BA', 'BR', 'VG', 'BN', 'BF', 'BI', 'KY', 'CF', 'TD', 'CN', 'CO', 'CK', 'CR', 'CY', 'DM', 'DO', 'EC', 'EG', 'GQ', 'ER', 'GA', 'GM', 'GH', 'GI', 'GR', 'GD', 'GT', 'GG', 'HN', 'IM', 'JP', 'JE', 'JO', 'KR', 'KW', 'KG', 'LI', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MH', 'MR', 'MX', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'NP', 'NI', 'NE', 'PW', 'PA', 'PE', 'PH', 'RO', 'RU', 'KN', 'LC', 'VC', 'WS', 'ST', 'SA', 'SN', 'SC', 'SB', 'SS', 'LK', 'SR', 'SZ', 'TJ', 'TZ', 'TG', 'TO', 'TT', 'TN', 'TM', 'UG', 'UA', 'UY', 'UZ', 'VU', 'EH', 'ZM'] + ['BH','BB','BW','BG','CM','CG','HR','CW','CZ','TL','TP','SV','ET','GE','IN','IL','JM','KI','XK','LS','MK','MT','FM','ME','NA','NR','NZ','NU','PS','PL','QA','RW','RS','SG','SK','ZA','ES','TW','TC','AE','AG','AM','AU','AT','BT','BQ','CA','CV','CL','CX','CC','DK','DJ','EE','FO','FJ','DE','GL','VA','HK','IS','IT','LV','MU','NL','NF','OM','PR','AX','AS','BE','FK','FI','FR','GF','PF','GP','GU','HU','IE','LT','MQ','YT','NC','MP','NO','PN','PT','RE','BL','SH','MF','PM','SM','SI','SJ','SE','CH','TV','GB', 'VI','WF'] * 4 + ['US'] * 295
High_Risk_Countries_Yellow = ['AF', 'AO', 'AZ', 'BD', 'BY', 'BZ', 'BO', 'MM', 'KH', 'KM', 'CD', 'CI', 'CU', 'GN', 'GW', 'GY', 'HT', 'ID', 'IR', 'IQ', 'KZ', 'KE', 'KP', 'LA', 'LB', 'LR', 'LY', 'NG', 'PK', 'PG', 'PY', 'SL', 'SX', 'SO', 'SD', 'SY', 'TH', 'TR', 'VE', 'VN', 'YE', 'ZW', 'AL', 'DZ', 'AD', 'AI', 'AR', 'AW', 'BS', 'BJ', 'BM', 'BA', 'BR', 'VG', 'BN', 'BF', 'BI', 'KY', 'CF', 'TD', 'CN', 'CO', 'CK', 'CR', 'CY', 'DM', 'DO', 'EC', 'EG', 'GQ', 'ER', 'GA', 'GM', 'GH', 'GI', 'GR', 'GD', 'GT', 'GG', 'HN', 'IM', 'JP', 'JE', 'JO', 'KR', 'KW', 'KG', 'LI', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MH', 'MR', 'MX', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'NP', 'NI', 'NE', 'PW', 'PA', 'PE', 'PH', 'RO', 'RU', 'KN', 'LC', 'VC', 'WS', 'ST', 'SA', 'SN', 'SC', 'SB', 'SS', 'LK', 'SR', 'SZ', 'TJ', 'TZ', 'TG', 'TO', 'TT', 'TN', 'TM', 'UG', 'UA', 'UY', 'UZ', 'VU', 'EH', 'ZM'] + ['BH','BB','BW','BG','CM','CG','HR','CW','CZ','TL','TP','SV','ET','GE','IN','IL','JM','KI','XK','LS','MK','MT','FM','ME','NA','NR','NZ','NU','PS','PL','QA','RW','RS','SG','SK','ZA','ES','TW','TC','AE','AG','AM','AU','AT','BT','BQ','CA','CV','CL','CX','CC','DK','DJ','EE','FO','FJ','DE','GL','VA','HK','IS','IT','LV','MU','NL','NF','OM','PR','AX','AS','BE','FK','FI','FR','GF','PF','GP','GU','HU','IE','LT','MQ','YT','NC','MP','NO','PN','PT','RE','BL','SH','MF','PM','SM','SI','SJ','SE','CH','TV','GB','VI','WF'] * 2 + ['US'] * 99
High_Risk_Countries_Red = ['AF', 'AO', 'AZ', 'BD', 'BY', 'BZ', 'BO', 'MM', 'KH', 'KM', 'CD', 'CI', 'CU', 'GN', 'GW', 'GY', 'HT', 'ID', 'IR', 'IQ', 'KZ', 'KE', 'KP', 'LA', 'LB', 'LR', 'LY', 'NG', 'PK', 'PG', 'PY', 'SL', 'SX', 'SO', 'SD', 'SY', 'TH', 'TR', 'VE', 'VN', 'YE', 'ZW', 'AL', 'DZ', 'AD', 'AI', 'AR', 'AW', 'BS', 'BJ', 'BM', 'BA', 'BR', 'VG', 'BN', 'BF', 'BI', 'KY', 'CF', 'TD', 'CN', 'CO', 'CK', 'CR', 'CY', 'DM', 'DO', 'EC', 'EG', 'GQ', 'ER', 'GA', 'GM', 'GH', 'GI', 'GR', 'GD', 'GT', 'GG', 'HN', 'IM', 'JP', 'JE', 'JO', 'KR', 'KW', 'KG', 'LI', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MH', 'MR', 'MX', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'NP', 'NI', 'NE', 'PW', 'PA', 'PE', 'PH', 'RO', 'RU', 'KN', 'LC', 'VC', 'WS', 'ST', 'SA', 'SN', 'SC', 'SB', 'SS', 'LK', 'SR', 'SZ', 'TJ', 'TZ', 'TG', 'TO', 'TT', 'TN', 'TM', 'UG', 'UA', 'UY', 'UZ', 'VU', 'EH', 'ZM', 'BH', 'BB', 'BW', 'BG', 'CM', 'CG', 'HR', 'CW', 'CZ', 'TL', 'TP', 'SV', 'ET', 'GE', 'IN', 'IL', 'JM', 'KI', 'XK', 'LS', 'MK', 'MT', 'FM', 'ME', 'NA', 'NR', 'NZ', 'NU', 'PS', 'PL', 'QA', 'RW', 'RS', 'SG', 'SK', 'ZA', 'ES', 'TW', 'TC', 'AE', 'AG', 'AM', 'AU', 'AT', 'BT', 'BQ', 'CA', 'CV', 'CL', 'CX', 'CC', 'DK', 'DJ', 'EE', 'FO', 'FJ', 'DE', 'GL', 'VA', 'HK', 'IS', 'IT', 'LV', 'MU', 'NL', 'NF', 'OM', 'PR', 'AX', 'AS', 'BE', 'FK', 'FI', 'FR', 'GF', 'PF', 'GP', 'GU', 'HU', 'IE', 'LT', 'MQ', 'YT', 'NC', 'MP', 'NO', 'PN', 'PT', 'RE', 'BL', 'SH', 'MF', 'PM', 'SM', 'SI', 'SJ', 'SE', 'CH', 'TV', 'GB', 'US', 'VI', 'WF']
Airport_Code =['0AK', '16A', '1G4', '2A3', '2A9', '3A5', '3T7', '3W2', '6R7', '74S', 'A61', 'A85', 'ABE', 'ABI', 'ABQ', 'ABR', 'ABY', 'ACB', 'ACK', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 'AFM', 'AGC', 'AGN', 'AGS', 'AHN', 'AIA', 'AID', 'AIY', 'AIZ', 'AKN', 'AKP', 'AKW', 'ALB', 'ALM', 'ALN', 'ALO', 'ALS', 'ALW', 'AMA', 'ANB', 'ANC', 'AND', 'ANI', 'AOO', 'APF', 'APN', 'AQH', 'AQT', 'ART', 'ASE', 'ASN', 'AST', 'ATK', 'ATL', 'ATW', 'ATY', 'AUG', 'AUK', 'AUS', 'AVL', 'AVP', 'AWI', 'AXN', 'AZO', 'BAF', 'BAK', 'BCE', 'BDE', 'BDL', 'BDR', 'BED', 'BEH', 'BET', 'BFD', 'BFF', 'BFI', 'BFL', 'BGM', 'BGR', 'BHB', 'BHM', 'BID', 'BIG', 'BIL', 'BIS', 'BJI', 'BKL', 'BKW', 'BKX', 'BLI', 'BLM', 'BLV', 'BMG', 'BMI', 'BNA', 'BOI', 'BOS', 'BPK', 'BPT', 'BQK', 'BQN', 'BRD', 'BRL', 'BRO', 'BRW', 'BTI', 'BTL', 'BTM', 'BTR', 'BTV', 'BUF', 'BUR', 'BVK', 'BWG', 'BWI', 'BZN', 'CAE', 'CAK', 'CCR', 'CDB', 'CDC', 'CDV', 'CDW', 'CEC', 'CEF', 'CEZ', 'CFK', 'CGA', 'CGF', 'CGI', 'CGX', 'CHA', 'CHO', 'CHS', 'CIC', 'CID', 'CIU', 'CKB', 'CLE', 'CLL', 'CLM', 'CLT', 'CMH', 'CMI', 'CMX', 'CNM', 'CNY', 'COD', 'COE', 'COS', 'COU', 'CPR', 'CPX', 'CRP', 'CRQ', 'CRW', 'CSG', 'CVG', 'CVO', 'CVX', 'CWA', 'CWI', 'CYS', 'D76', 'DAB', 'DAL', 'DAN', 'DAY', 'DBQ', 'DCA', 'DDC', 'DDH', 'DEC', 'DEN', 'DET', 'DFW', 'DHN', 'DIK', 'DLG', 'DLH', 'DNV', 'DRO', 'DRT', 'DSM', 'DTW', 'DUJ', 'DUT', 'DUY', 'DVL', 'DVT', 'DXR', 'EAR', 'EAT', 'EAU', 'EEK', 'EEN', 'EFD', 'EFK', 'EGE', 'EKM', 'EKO', 'ELI', 'ELM', 'ELO', 'ELP', 'ELY', 'ENA', 'ENM', 'ENW', 'ERI', 'ESC', 'ESF', 'EUG', 'EVV', 'EWB', 'EWN', 'EWR', 'EWU', 'EYW', 'FAI', 'FAQ', 'FAR', 'FAT', 'FAY', 'FHR', 'FHU', 'FKL', 'FLG', 'FLL', 'FLO', 'FMN', 'FNL', 'FNT', 'FOD', 'FOE', 'FRG', 'FRM', 'FSD', 'FSM', 'FTW', 'FWA', 'FYU', 'FYV', 'GAL', 'GAM', 'GBD', 'GBH', 'GCC', 'GCK', 'GCN', 'GED', 'GEG', 'GFK', 'GFL', 'GGG', 'GGV', 'GGW', 'GJT', 'GKN', 'GLD', 'GLH', 'GLR', 'GLS', 'GNV', 'GON', 'GPI', 'GPT', 'GPZ', 'GRB', 'GRI', 'GRK', 'GRO', 'GRR', 'GSN', 'GSO', 'GSP', 'GST', 'GTF', 'GTR', 'GUC', 'GUM', 'GUP', 'GYH', 'GYR', 'GYY', 'HDN', 'HFD', 'HGR', 'HIB', 'HII', 'HKS', 'HKY', 'HLA', 'HLN', 'HND', 'HNH', 'HNL', 'HNM', 'HNS', 'HOB', 'HOM', 'HON', 'HOT', 'HOU', 'HPB', 'HPN', 'HRL', 'HRO', 'HSL', 'HSV', 'HTS', 'HUF', 'HUT', 'HVN', 'HXD', 'HYA', 'HYL', 'HYS', 'IAD', 'IAH', 'IAN', 'ICT', 'IDA', 'IFP', 'IGM', 'IIK', 'ILE', 'ILG', 'ILI', 'ILL', 'ILM', 'IMT', 'IND', 'INL', 'INT', 'IPL', 'IPT', 'IRK', 'ISN', 'ISO', 'ISP', 'ITH', 'ITO', 'IWA', 'IWD', 'IXD', 'IYK', 'JAC', 'JAN', 'JAX', 'JBR', 'JEF', 'JFK', 'JHW', 'JLN', 'JMS', 'JNU', 'JRB', 'JST', 'JVL', 'JXN', 'KAE', 'KAL', 'KDK', 'KEB', 'KKA', 'KLG', 'KOA', 'KSM', 'KTB', 'KTN', 'KVC', 'KVL', 'KWT', 'LAA', 'LAF', 'LAL', 'LAN', 'LAR', 'LAS', 'LAW', 'LAX', 'LBB', 'LBE', 'LBF', 'LBL', 'LBX', 'LCH', 'LCK', 'LEB', 'LEX', 'LFT', 'LGA', 'LGB', 'LHD', 'LIH', 'LIT', 'LMT', 'LNK', 'LNS', 'LNY', 'LPR', 'LRD', 'LRU', 'LSE', 'LUK', 'LWB', 'LWS', 'LYH', 'MAF', 'MAZ', 'MBA', 'MBL', 'MBS', 'MCC', 'MCE', 'MCG', 'MCI', 'MCK', 'MCN', 'MCO', 'MCW', 'MDH', 'MDM', 'MDT', 'MDW', 'MDY', 'MEI', 'MEM', 'MFD', 'MFE', 'MFR', 'MGM', 'MGW', 'MHE', 'MHK', 'MHT', 'MIA', 'MIE', 'MIV', 'MJX', 'MKC', 'MKE', 'MKG', 'MKK', 'MKL', 'MKT', 'MLB', 'MLI', 'MLL', 'MLU', 'MMH', 'MMU', 'MMV', 'MNM', 'MOB', 'MOD', 'MOT', 'MOU', 'MPV', 'MQI', 'MQJ', 'MQY', 'MRI', 'MRY', 'MSL', 'MSN', 'MSO', 'MSP', 'MSS', 'MSV', 'MSY', 'MTH', 'MTJ', 'MTM', 'MTO', 'MUE', 'MVL', 'MVN', 'MVY', 'MWA', 'MWH', 'MYR', 'MZJ', 'N93', 'NEW', 'NQA', 'NUL', 'OAJ', 'OAK', 'OCF', 'OFK', 'OGD', 'OGG', 'OGS', 'OKC', 'OLM', 'OMA', 'OME', 'ONP', 'ONT', 'OOK', 'OQU', 'ORD', 'ORF', 'ORH', 'ORI', 'ORS', 'ORV', 'OSH', 'OSU', 'OTG', 'OTH', 'OTM', 'OTZ', 'OWB', 'OXC', 'OXR', 'PAE', 'PAH', 'PBI', 'PCW', 'PDT', 'PDX', 'PFN', 'PGA', 'PGD', 'PGM', 'PGV', 'PHF', 'PHL', 'PHO', 'PHX', 'PIA', 'PIB', 'PIE', 'PIH', 'PIR', 'PIT', 'PKB', 'PLB', 'PLK', 'PLN', 'PMD', 'PNC', 'PNS', 'POU', 'PPC', 'PPG', 'PQI', 'PQL', 'PRB', 'PRC', 'PSC', 'PSE', 'PSG', 'PSM', 'PSP', 'PTH', 'PTK', 'PUB', 'PUW', 'PVC', 'PVD', 'PVU', 'PWM', 'PWT', 'RAP', 'RDD', 'RDG', 'RDM', 'RDU', 'RFD', 'RHI', 'RIC', 'RIW', 'RKD', 'RKS', 'RME', 'RMG', 'RNO', 'ROA', 'ROC', 'ROW', 'RSH', 'RST', 'RSW', 'RUT', 'RWI', 'SAF', 'SAN', 'SAT', 'SAV', 'SAW', 'SBA', 'SBD', 'SBN', 'SBP', 'SBY', 'SCC', 'SCK', 'SCM', 'SDF', 'SDP', 'SDY', 'SEA', 'SFB', 'SFO', 'SFZ', 'SGF', 'SGH', 'SGJ', 'SGU', 'SGY', 'SHD', 'SHG', 'SHH', 'SHR', 'SHV', 'SIG', 'SIT', 'SJC', 'SJT', 'SJU', 'SKX', 'SLC', 'SLE', 'SLK', 'SLN', 'SMF', 'SMX', 'SNA', 'SNP', 'SOP', 'SOV', 'SOW', 'SPI', 'SPS', 'SQI', 'SRQ', 'SRR', 'STC', 'STJ', 'STL', 'STP', 'STS', 'STT', 'STX', 'SUN', 'SUS', 'SUX', 'SVA', 'SVC', 'SWF', 'SWO', 'SYR', 'T44', 'TAL', 'TBN', 'TCL', 'TEB', 'TEX', 'TIX', 'TLH', 'TLT', 'TNI', 'TOG', 'TOL', 'TPA', 'TPL', 'TRI', 'TTN', 'TUL', 'TUP', 'TUS', 'TVC', 'TVF', 'TVL', 'TVR', 'TWF', 'TXK', 'TYR', 'TYS', 'UCA', 'UIN', 'UNK', 'UNV', 'UOX', 'UUU', 'VAK', 'VCT', 'VCV', 'VDZ', 'VGT', 'VIS', 'VLD', 'VPS', 'VPZ', 'VQQ', 'VQS', 'VRB', 'WBB', 'WDG', 'WLK', 'WNA', 'WRG', 'WRL', 'WST', 'WTK', 'WWD', 'WYS', 'X44', 'X95', 'XNA', 'YAK', 'YKM', 'YKN', 'YNG', 'YUM', 'Z08', 'Z09']

#Lists for Cust details
CCs=[]
ACCTs=[]
CCTypes=[]
Holders=[]
Users1=[]
Users2=[]
Users3=[]
CCsCount=[]
Cities=[]
States=[]
ZIPs=[]
Countries=[]
UseCase=[]
ClsdFlags=[]
count=0
columns = defaultdict(list) # each value in each column is appended to a list
with open('uber_cust_101.csv') as f:
    reader = csv.DictReader(f,delimiter='|') # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

CCs=columns['CREDITCARDNUMBER']
ACCTs=columns['ACCOUNTID']
CCTypes=columns['CREDITCARDTYPE']
Holders=columns['NAME']
CCsCount=columns['NUM_CCS']
Cities=columns['CITY']
States=columns['STATE']
ZIPs=columns['ZIP']
Countries=columns['COUNTRY']
UseCase=columns['USE_CASE_SCENARIO']
ClsdFlags=columns['CLOSEDACCOUNT']

def gen_tran(MCC_credits,MCC_debits,Tran_Country_Credits,Tran_Country_Debits,Tran_Type_C,Tran_Type_D,Upper_Limit,Delta,count,j,usecase):
    liTrans = []
    #Initiate start date for transactions 
    startDate=date(2015,01,01)
	#Pick out account based on counter
    acct=ACCTs[j]
    #Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
    limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
    #local Amt variable to calculate customer total usage
    usedAmt = 0
    tmpAmt = 0
    Balance = limit
    maxDate= startDate
	#Random number generator for transactions per customer
    NoTrans = randrange(100,150,1)
    desc=''
    flag=0
    maxCheckin=''
    maxBook=''
    #loop to generate NoTrans transactions per customer
    for k in range(NoTrans):
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cr_dbt='D'
        tranType = ''
        country=[]
        cat_desc=''
        flag=0
        #If Balance is within the credit limit, generate credits/debits 
        if(Balance>0 and Balance<=limit*1.2):
			#Probability of credits (tmpAmt>0) and debits (tmpAmt==0) is driven by parameters Upper_Limit and Delta
            tmpAmt = max((randrange(1,Upper_Limit,1)+Delta),0)*randrange(1,Balance+1,1)
            flag=1
		#Define time delta for next transaction
        tdelta = timedelta(days=randrange(1,4,1))
        row = [str(count)+'_'+dt] + [acct]
        #If we have credit or debit within balance
        if tmpAmt == 0 and flag==1:
            #print '1'
            tmpAmt=random.randrange(1,Balance+1,1)
            tranType = random.choice(Tran_Type_D)
            cat = random.choice(MCC_debits)
            cat_desc=python_merchant_cat.All_Merchant_Cat[cat]
            Balance = Balance - tmpAmt
            merch=gen_data.create_company_name()
            row.append(merch)
            row.append(cat)
            row.append(cat_desc)
            country=random.choice(Tran_Country_Debits)
        else:
            if tmpAmt > 0 and flag==1:
                #print '2'
                cr_dbt='C'
                tranType=random.choice(Tran_Type_C)
                Balance = Balance + tmpAmt
				merch=''
                cat = random.choice(MCC_credits)
				cat_desc=python_merchant_cat.All_Merchant_Cat[cat]
                if(tranType=='Merchant Credit'):
                        cat=random.choice(Merchant_Category.Green)
						cat_desc=python_merchant_cat.All_Merchant_Cat[cat]
				if(tranType=='Refund'):
                        cat='0000'
						cat_desc=python_merchant_cat.All_Merchant_Cat[cat]
                row.append(merch)
                row.append(cat)
                row.append(cat_desc)
                country=random.choice(Tran_Country_Credits)
		#If we need to make a payment or get credit then assign codes
        if Balance > limit and flag==0:
            #print '3'
            tmpAmt=random.randrange(1,Balance-limit+1,1)
            tranType = random.choice(Tran_Type_D)
            cat = random.choice(MCC_debits)
            cat_desc=python_merchant_cat.All_Merchant_Cat[cat]
            Balance = Balance - tmpAmt
            merch=gen_data.create_company_name()
            row.append(merch)
            row.append(cat)
            row.append(cat_desc)
            country=random.choice(Tran_Country_Debits)
        else:
            if ((Balance < 0 or Balance==0)and flag==0):
                #print '4'
                cr_dbt='C'
                tranType='Payment'
                tmpAmt = random.randrange(1,limit/2,1)
                Balance = Balance + tmpAmt
                merch = ''
				cat = '1111'
                cat_desc=python_merchant_cat.All_Merchant_Cat[cat]
                row.append(merch)
                row.append(cat)
                row.append(cat_desc)
                country=random.choice(Tran_Country_Credits)

        #date posted
        date1 = maxDate+tdelta
        maxDate = date1
        #date of transaction a day later
        date2 = date1-timedelta(days=1)
        row.extend([country,date1,date2,tranType,cr_dbt,limit,tmpAmt,Balance,CCs[j],
        CCTypes[j],usecase,Holders[j],CCsCount[j],Cities[j],States[j],ZIPs[j],Countries[j]])
        count = count + 1
        checkin=''
        checkout=''
        transDetail=''
		#Add details or Hotel Transactions 
        if((cat_desc=='Hotels/Motels/Inns/Resorts' or cat_desc=='Hotels, Motels, and Resorts') and (UseCase[j]=='28' or UseCase[j]=='29')):
            if (maxCheckin == ''):
                checkin=maxDate+timedelta(days=randrange(365,389,1))
                checkout=checkin+timedelta(days=randrange(4,11,1))
                maxCheckin=checkin
                tmp2=gen_data.create_name()
                addr=gen_data.create_city_state_zip()
                hotel=tmp2[1]+' Hotels; '+'; Address: '+addr[1]+' '+addr[2]+', '+addr[0]
                transDetail='Checkin: '+str(checkin)+'; Checkout: '+str(checkout)+'; Hotel: '+hotel
            else:
                checkin=maxCheckin + timedelta(days=randrange(2,5,1))
                checkout=checkin+timedelta(days=randrange(4,11,1))
                maxCheckin=checkin
                tmp2=gen_data.create_name()
                addr=gen_data.create_city_state_zip()
                hotel=tmp2[1]+' Hotels; '+'; Address: '+addr[1]+' '+addr[2]+', '+addr[0]
                transDetail='Checkin: '+str(checkin)+'; Checkout: '+str(checkout)+'; Hotel: '+hotel
        if((cat_desc=='Hotels/Motels/Inns/Resorts' or cat_desc=='Hotels, Motels, and Resorts') and UseCase[j]=='30'):
            checkin=maxDate+timedelta(days=randrange(30,200,1))
            checkout=checkin+timedelta(days=randrange(4,11,1))
            tmp2=gen_data.create_name()
            addr=gen_data.create_city_state_zip()
            hotel=tmp2[1]+' Hotels; '+'; Address: '+addr[1]+' '+addr[2]+', '+addr[0]
            transDetail='Checkin: '+str(checkin)+'; Checkout: '+str(checkout)+'; Hotel: '+hotel
		#Add details or Airline Transactions 
        if(cat_desc=='Airlines' and (UseCase[j]=='31' or UseCase[j]=='32')):
            if (maxBook == ''):
                booking=maxDate+timedelta(days=randrange(1,15,1))
                maxBook=booking
                tmp2=gen_data.create_name()
                addr=gen_data.create_city_state_zip()
                transDetail='Date Booked: '+str(booking)+'; Name Booked: '+tmp2[0]+tmp2[1]+'; Address: '+addr[1]+' '+addr[2]+', '+addr[0]+'; Source :'+random.choice(Airport_Code)+'; Destination:'+random.choice(Airport_Code)
            else:
                booking=maxBook + timedelta(days=randrange(1,15,1))
                maxBook=booking
                tmp2=gen_data.create_name()
                addr=gen_data.create_city_state_zip()
                transDetail='Date Booked: '+str(booking)+'; Name Booked: '+ tmp2[0] + tmp2[1] + '; Address: '+ addr[1] + ' ' + addr[2]+', '+addr[0]+'; Source :'+random.choice(Airport_Code)+'; Destination:'+random.choice(Airport_Code)
        if(cat_desc=='Airlines' and UseCase[j]=='33'):
            booking=maxDate + timedelta(days=randrange(1,15,1))
            tmp2=gen_data.create_name()
            addr=gen_data.create_city_state_zip()
            transDetail='Date Booked: '+str(booking)+'; Name Booked: '+ tmp2[0] + tmp2[1] + '; Address: '+addr[1]+' '+addr[2]+', '+addr[0]+'; Source :'+random.choice(Airport_Code)+'; Destination:'+random.choice(Airport_Code)
        row.append(transDetail)
        liTrans.append(row)
    #post generating all transactions, check account balance - if overpaid - refund $ and add a refund transaction
    if Balance > limit:
        row = [str(count)+'_'+dt]+ [acct]+['Uber Bank']+['0000']+['Refund to Customer from Bank']+[random.choice(Tran_Country_Debits)]
        date1=maxDate+timedelta(days=90)
        date2=date1-timedelta(days=1)
        row.extend([date1, date2, 'Credit Balance Refund','D',limit,Balance-limit,limit,CCs[j],CCTypes[j],
        usecase,Holders[j],CCsCount[j],Cities[j],States[j],ZIPs[j],Countries[j],''])
        count = count + 1
        usedAmt = 0
        maxDate= datetime(0001,01,01)
    else:
        date1 = maxDate+tdelta
        maxDate = date1
        #date of transaction a day later
        date2 = date1-timedelta(days=1)
        row = [str(count)+'_'+dt]+[acct]+['Customer Payment']+['1111']+['Customer Payment']+[random.choice(Tran_Country_Credits)]
        row.extend([date1, date2, 'Payment','C',limit,limit-Balance,limit,CCs[j],CCTypes[j],usecase,
        Holders[j],CCsCount[j],Cities[j],States[j],ZIPs[j],Countries[j],''])
        count = count + 1
        usedAmt = 0
    liTrans.append(row)
    return liTrans

def createCSV(ccount, remainder, lenI, iterator):
#5)Open CSV file for writing
    liTrans = []
    if iterator == 0:
        x = xrange(ccount)
    else:
        if iterator < (lenI-1):
            x = xrange(iterator * ccount, (iterator+1) * ccount)
        else:
            x = xrange(iterator * ccount, ((iterator * ccount) + (ccount+remainder))) 
    for i in x:
        if(ClsdFlags[i]=='No'):
            #Use Case 1.0: Threshold for overpayments
            #Red Risk
            if(UseCase[i]=='1'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Ovpmt_Refund,Transaction_Type.Debit_Ovpmt_Red,3,-1,count,i,'Use Case 1.0 - Red'))
            #Yellow Risk
            if(UseCase[i]=='2'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Ovpmt_Refund,Transaction_Type.Debit_Ovpmt_Yellow,4,-2,count,i,'Use Case 1.0 - Yellow'))
            #Green Risk
            if(UseCase[i]=='3'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Ovpmt_Refund,Transaction_Type.Debit_Ovpmt_Green,5,-3,count,i,'Use Case 1.0 - Green'))
            #Use Case 1.1: Threshold for refunds
            #Red Risk
            if(UseCase[i]=='4'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Refund_Red,Transaction_Type.Debit_Refund_Red,3,-1,count,i,'Use Case 1.1 - Red'))
            #Yellow Risk
            if(UseCase[i]=='5'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Refund_Yellow,Transaction_Type.Debit_Refund_Yellow,3,-1,count,i,'Use Case 1.1 - Yellow'))
            #Green Risk
            if(UseCase[i]=='6'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Refund_Green,Transaction_Type.Debit_Refund_Green,3,-1,count,i,'Use Case 1.1 - Green'))
            #Use Case 2: Method of payment to card balances
            #Red Risk
            if(UseCase[i]=='7'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Payments_Red,Transaction_Type.Debit_Payments_Red,3,-1,count,i,'Use Case 2 - Red'))
            #Yellow Risk
            if(UseCase[i]=='8'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Payments_Yellow,Transaction_Type.Debit_Payments_Yellow,3,-1,count,i,'Use Case 2 - Yellow'))
            #Green Risk
            if(UseCase[i]=='9'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Payments_Green,Transaction_Type.Debit_Payments_Green,3,-1,count,i,'Use Case 2 - Green'))
            #Use Case 3: Payment source is owned by non-account holder
            #Red Risk
            if(UseCase[i]=='10'):
                liTrans.extend(gen_tran(Account_Holder_Type_Red,Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_10_41No19_21No25_27,Transaction_Type.Debit_10_41No19_21No25_27,4,-2,count,i,'Use Case 3 - Red'))
            #Yellow Risk
            if(UseCase[i]=='11'):
                liTrans.extend(gen_tran(Account_Holder_Type_Yellow,Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_10_41No19_21No25_27,Transaction_Type.Debit_10_41No19_21No25_27,4,-2,count,i,'Use Case 3 - Yellow'))
            #Green Risk
            if(UseCase[i]=='12'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_10_41No19_21No25_27,Transaction_Type.Debit_10_41No19_21No25_27,3,-1,count,i,'Use Case 3 - Green'))
            #Use Case 4: Payment is frequently made at a location that is materially distant from the account address
            #Red Risk
            if(UseCase[i]=='13'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,Payment_DistLoc_Red,['US'],Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 4 - Red'))
            #Yellow Risk
            if(UseCase[i]=='14'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,Payment_DistLoc_Yellow,['US'],Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 4 - Yellow'))
            #Green Risk
            if(UseCase[i]=='15'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,Payment_DistLoc_Green,['US'],Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 4 - Green'))
            #Use Case 5: Frequent or large transactions at high-risk countries
            #Red Risk
            if(UseCase[i]=='16'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],High_Risk_Countries_Red,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 5 - Red'))
            #Yellow Risk
            if(UseCase[i]=='17'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],High_Risk_Countries_Yellow,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 5 - Yellow'))
            #Green Risk
            if(UseCase[i]=='18'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],High_Risk_Countries_Green,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 5 - Green'))
            #Use Case 6: Usual ATM withdrawals for cash advance
            #Red Risk
            if(UseCase[i]=='19'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_ATM,Transaction_Type.Debit_ATM_Red,3,-1,count,i,'Use Case 6 - Red'))
            #Yellow Risk
            if(UseCase[i]=='20'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_ATM,Transaction_Type.Debit_ATM_Yellow,3,-1,count,i,'Use Case 6 - Yellow'))
            #Green Risk
            if(UseCase[i]=='21'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_ATM,Transaction_Type.Debit_ATM_Green,3,-1,count,i,'Use Case 6 - Green'))
            #Use Case 7: Frequent Credit Card transactions at locations "materially distant" from the account address
            #Red Risk
            if(UseCase[i]=='22'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.Red,Transaction_DistLoc.Red,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 7 - Red'))
            #Yellow Risk
            if(UseCase[i]=='23'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.Yellow,Transaction_DistLoc.Yellow,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 7 - Yellow'))
            #Green Risk
            if(UseCase[i]=='24'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.Green,Transaction_DistLoc.Green,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case 7 - Green'))
            #Use Case 8: Merchant credits without offseting merchant transactions
            #Red Risk
            if(UseCase[i]=='25'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,['US'],['US'],Transaction_Type.Merchant_Credits_Red,Transaction_Type.Merchant_Debit,3,-1,count,i,'Use Case 8 - Red'))
            #Yellow Risk
            if(UseCase[i]=='26'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,['US'],['US'],Transaction_Type.Merchant_Credits_Yellow,Transaction_Type.Merchant_Debit,3,-1,count,i,'Use Case 8 - Yellow'))
            #Green Risk
            if(UseCase[i]=='27'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,['US'],['US'],Transaction_Type.Merchant_Credits_Green,Transaction_Type.Merchant_Debit,3,-1,count,i,'Use Case 8 - Green'))
            #Use Case 9: Hotel room rentals at different hotels over the same time period
            #Red Risk
            if(UseCase[i]=='28'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Hotels.Red,['US'],['US'],Transaction_Type.Payments,Transaction_Type.Debit,4,-2,count,i,'Use Case 9 - Red'))
            #Yellow Risk
            if(UseCase[i]=='29'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Hotels.Yellow,['US'],['US'],Transaction_Type.Payments,Transaction_Type.Debit,4,-2,count,i,'Use Case 9 - Yellow'))
            #Green Risk
            if(UseCase[i]=='30'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Hotels.Green,['US'],['US'],Transaction_Type.Payments,Transaction_Type.Debit,4,-2,count,i,'Use Case 9 - Green'))
            #Use Case 10: Multiple airline tickets for non-account holders
            #Red Risk
            if(UseCase[i]=='31'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Airlines.Red,['US'],['US'],Transaction_Type.Payments,Transaction_Type.Debit,4,-2,count,i,'Use Case 10 - Red'))
            #Yellow Risk
            if(UseCase[i]=='32'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Airlines.Yellow,['US'],['US'],Transaction_Type.Payments,Transaction_Type.Debit,4,-2,count,i,'Use Case 10 - Yellow'))
            #Green Risk
            if(UseCase[i]=='33'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Airlines.Green,['US'],['US'],Transaction_Type.Payments,Transaction_Type.Debit,4,-2,count,i,'Use Case 10 - Green'))
            #Use Case 11: Unusually large payments for accumulated balances
            #Red Risk
            if(UseCase[i]=='34'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Ovpmt_Refund,Transaction_Type.Debit_Ovpmt_Red,6,-4,count,i,'Use Case 11 - Red'))
            #Yellow Risk
            if(UseCase[i]=='35'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Ovpmt_Refund,Transaction_Type.Debit_Ovpmt_Yellow,5,-3,count,i,'Use Case 11 - Yellow'))
            #Green Risk
            if(UseCase[i]=='36'):
                liTrans.extend(gen_tran(['1111'],Merchant_Category.Green,['US'],['US'],Transaction_Type.Credits_Ovpmt_Refund,Transaction_Type.Debit_Ovpmt_Green,4,-2,count,i,'Use Case 11 - Green'))
            #Use Case 12: Custom out of country scenario
            if(UseCase[i]=='37'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.OutofCountry_100,Transaction_DistLoc.OutofCountry_100,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case Out of Country - US'))
            if(UseCase[i]=='38'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.OutofCountry_95,Transaction_DistLoc.OutofCountry_95,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case Out of Country - 95'))
            if(UseCase[i]=='39'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.OutofCountry_50,Transaction_DistLoc.OutofCountry_50,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case Out of Country - 50'))
            if(UseCase[i]=='40'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.OutofCountry_40,Transaction_DistLoc.OutofCountry_40,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case Out of Country - 40'))
            if(UseCase[i]=='41'):
                liTrans.extend(gen_tran(Account_Holder_Type_Green,Merchant_Category.Green,Transaction_DistLoc.OutofCountry_10,Transaction_DistLoc.OutofCountry_10,Transaction_Type.Payments,Transaction_Type.Debit,3,-1,count,i,'Use Case Out of Country - 10'))
    return liTrans

with open('uber_trans_multithreading_101.csv','w') as f1:
    writer=csv.writer(f1, delimiter='|',lineterminator='\n',)
	#File header
    writer.writerow(['ROWNUM']+['ACCOUNTID']+['MERCHANT_NAME']+['MERCHANT_CATEGORY_CODE']+['MERCHANT_CATEGORY_DESC']+['MERCHANT_COUNTRY']+\
            ['POST_DATE'] +	['TRANSACTION_DATE'] + ['TRANSACTION_TYPE']+['CREDIT_DEBIT']+['CREDIT_LIMIT']+['AMOUNT']+['BALANCE']+\
            ['CREDITCARDNUMBER']+['CC_TYPE']+['USE_CASE']+['CUST_NAME']+['NUM_CCS']+['CUST_CITY']+['CUST_STATE']+['CUST_ZIP']+['CUST_COUNTRY']+['TRANS_DETAIL'])
    Cust_Count=len(CCs)
	#Define number of processes then multithread
    proc = 16
    iterator = xrange(proc)
    remainder = Cust_Count % proc
    ccount = Cust_Count/proc
    lenI = len(iterator)
    func = partial(createCSV, ccount, remainder, lenI)
    pool = Pool(processes=proc)
    results = pool.map(func, iterator)
    liMaster = results[0] + results[1] + results[2] + results[3] + results[4] + results[5] + results[6] + results[7] + results[8] + results[9] + results[10] + results[11] + results[12] + results[13] + results[14] + results[15]
    for row in liMaster:
        writer.writerow(row)
