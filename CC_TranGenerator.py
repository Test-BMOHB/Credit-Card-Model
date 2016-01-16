#Developer    : Ivana Donevska
#Date         : 2015-12-10
#Program Name : Credit Card Transactions Generator
#Version#     : 5
#Description  : Code that generates debit and credit transactions with refunds
#-----------------------------------------------------------------------------
# History  | ddmmyyyy  |  User     |                Changes       
#          | 11122015  | Ivana D.  | Intial Coding Steps 
#          | 12232015  | Ivana D.  | Added date for refund to be +90 days of      
#          | 01032015  | Ivana D.  | Added balances  
#-----------------------------------------------------------------------------*/
#Reference data for python_account_ID, python_merchant_cat, python_CC is located on the test-bmohb console gs://credit_card_transactions
import python_account_ID
import python_merchant_cat
import python_CC
from random import randrange
from random import random
import random
from datetime import datetime
from random import shuffle
from faker import Faker
from barnum import gen_data
import csv
from datetime import date, timedelta
fake = Faker()

#Steps 1-4
#1)Define list with Merchant Category Codes
#2)Define list with Transaction Types based on how often a transaction should appear
#3)Define Country_Green Codes list
#4)Define a dictionary with all merchants

#Transactions' Risk is defined by Merchant Category, Transaction Types and Country_Red.
#Merchant Category is divided into three risk categories per senor Kamin's best judgement. - % to be updated
#As a reference is used MCC (Merchant Category Codes)
#Transaction Types were divided by risk and their frequencies were distributed accordingly. 
#Tran Type Percentage Distribution Table:
#Transaction Type	Green	Yellow	Red
#Cash Advance	        5	15      20
#Cash Payment			5	10	    20
#Purchase				55	37	    20
#Payment				20	10	    5
#Payment Reversal		1	5	    0
#Wire Transfer			3	0	    10
#Void					3	10	    0
#Refund					3	10	    15
#ACH 					5	3	    10
#						100	100	    100

Transaction_Type_Credits = ['Cash Payment','Payment','Payment Reversal','Wire Transfer']
Transaction_Type_Debits = ['Cash Advance','Purchase']

Country_Yellow = ['BH', 'BB', 'BW', 'BG', 'CM', 'CG', 'HR', 'CW', 'CZ', 'TL', 'TP', 'SV', 'ET', 'GE', 'IN', 'IL', 'JM', 'KI', 'XK', 'LS', 'MK', 'MT', 'FM', 'ME', 'NA', 'NR', 'NZ', 'NU', 'PS', 'PL', 'QA', 'RW', 'RS', 'SG', 'SK', 'ZA', 'ES', 'TW', 'TC', 'AE']
Merchant_Category_Yellow = ['4215', '4722', '5099', '5122', '5131', '5541', '5542', '5921', '5932', '6011', '6012', '6051', '6211', '7210', '7216', '7531', '7535', '7538', '7542', '7631', '8398']
Transaction_Type_Yellow = ['ACH', 'ACH', 'ACH', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Payment Reversal', 'Payment Reversal', 'Payment Reversal', 'Payment Reversal', 'Payment Reversal', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund']

Merchant_Category_Green = ['742', '763', '780', '1520', '1711', '1731', '1740', '1750', '1761', '1771', '1799', '2741', '2791', '2842', '3000', '3001', '3002', '3003', '3004', '3005', '3006', '3007', '3008', '3009', '3010', '3011', '3012', '3013', '3014', '3015', '3016', '3017', '3018', '3019', '3020', '3021', '3022', '3023', '3024', '3025', '3026', '3027', '3028', '3029', '3030', '3031', '3032', '3033', '3034', '3035', '3036', '3037', '3038', '3039', '3040', '3041', '3042', '3043', '3044', '3045', '3046', '3047', '3048', '3049', '3050', '3051', '3052', '3053', '3054', '3055', '3056', '3057', '3058', '3059', '3060', '3061', '3062', '3063', '3064', '3065', '3066', '3067', '3068', '3069', '3070', '3071', '3072', '3073', '3074', '3075', '3076', '3077', '3078', '3079', '3080', '3081', '3082', '3083', '3084', '3085', '3086', '3087', '3088', '3089', '3090', '3091', '3092', '3093', '3094', '3095', '3096', '3097', '3098', '3099', '3100', '3101', '3102', '3103', '3104', '3105', '3106', '3107', '3108', '3109', '3110', '3111', '3112', '3113', '3114', '3115', '3116', '3117', '3118', '3119', '3120', '3121', '3122', '3123', '3124', '3125', '3126', '3127', '3128', '3129', '3130', '3131', '3132', '3133', '3134', '3135', '3136', '3137', '3138', '3139', '3140', '3141', '3142', '3143', '3144', '3145', '3146', '3147', '3148', '3149', '3150', '3151', '3152', '3153', '3154', '3155', '3156', '3157', '3158', '3159', '3160', '3161', '3162', '3163', '3164', '3165', '3166', '3167', '3168', '3169', '3170', '3171', '3172', '3173', '3174', '3175', '3176', '3177', '3178', '3179', '3180', '3181', '3182', '3183', '3184', '3185', '3186', '3187', '3188', '3189', '3190', '3191', '3192', '3193', '3194', '3195', '3196', '3197', '3198', '3199', '3200', '3201', '3202', '3203', '3204', '3205', '3206', '3207', '3208', '3209', '3210', '3211', '3212', '3213', '3214', '3215', '3216', '3217', '3218', '3219', '3220', '3221', '3222', '3223', '3224', '3225', '3226', '3227', '3228', '3229', '3230', '3231', '3232', '3233', '3234', '3235', '3236', '3237', '3238', '3239', '3240', '3241', '3242', '3243', '3244', '3245', '3246', '3247', '3248', '3249', '3250', '3251', '3252', '3253', '3254', '3255', '3256', '3257', '3258', '3259', '3260', '3261', '3262', '3263', '3264', '3265', '3266', '3267', '3268', '3269', '3270', '3271', '3272', '3273', '3274', '3275', '3276', '3277', '3278', '3279', '3280', '3281', '3282', '3283', '3284', '3285', '3286', '3287', '3288', '3289', '3290', '3291', '3292', '3293', '3294', '3295', '3296', '3297', '3298', '3299', '3351', '3352', '3353', '3354', '3355', '3356', '3357', '3358', '3359', '3360', '3361', '3362', '3363', '3364', '3365', '3366', '3367', '3368', '3369', '3370', '3371', '3372', '3373', '3374', '3375', '3376', '3377', '3378', '3379', '3380', '3381', '3382', '3383', '3384', '3385', '3386', '3387', '3388', '3389', '3390', '3391', '3392', '3393', '3394', '3395', '3396', '3397', '3398', '3399', '3400', '3401', '3402', '3403', '3404', '3405', '3406', '3407', '3408', '3409', '3410', '3411', '3412', '3413', '3414', '3415', '3416', '3417', '3418', '3419', '3420', '3421', '3422', '3423', '3424', '3425', '3426', '3427', '3428', '3429', '3430', '3431', '3432', '3433', '3434', '3435', '3436', '3437', '3438', '3439', '3440', '3441', '3501', '3502', '3503', '3504', '3505', '3506', '3507', '3508', '3509', '3510', '3511', '3512', '3513', '3514', '3515', '3516', '3517', '3518', '3519', '3520', '3521', '3522', '3523', '3524', '3525', '3526', '3527', '3528', '3529', '3530', '3531', '3532', '3533', '3534', '3535', '3536', '3537', '3538', '3539', '3540', '3541', '3542', '3543', '3544', '3545', '3546', '3547', '3548', '3549', '3550', '3551', '3552', '3553', '3554', '3555', '3556', '3557', '3558', '3559', '3560', '3561', '3562', '3563', '3564', '3565', '3566', '3567', '3568', '3569', '3570', '3571', '3572', '3573', '3574', '3575', '3576', '3577', '3578', '3579', '3580', '3581', '3582', '3583', '3584', '3585', '3586', '3587', '3588', '3589', '3590', '3591', '3592', '3593', '3594', '3595', '3596', '3597', '3598', '3599', '3600', '3601', '3602', '3603', '3604', '3605', '3606', '3607', '3608', '3609', '3610', '3611', '3612', '3613', '3614', '3615', '3616', '3617', '3618', '3619', '3620', '3621', '3622', '3623', '3624', '3625', '3626', '3627', '3628', '3629', '3630', '3631', '3632', '3633', '3634', '3635', '3636', '3637', '3638', '3639', '3640', '3641', '3642', '3643', '3644', '3645', '3646', '3647', '3648', '3649', '3650', '3651', '3652', '3653', '3654', '3655', '3656', '3657', '3658', '3659', '3660', '3661', '3662', '3663', '3664', '3665', '3666', '3667', '3668', '3669', '3670', '3671', '3672', '3673', '3674', '3675', '3676', '3677', '3678', '3679', '3680', '3681', '3682', '3683', '3684', '3685', '3686', '3687', '3688', '3689', '3690', '3691', '3692', '3693', '3694', '3695', '3696', '3697', '3698', '3699', '3700', '3701', '3702', '3703', '3704', '3705', '3706', '3707', '3708', '3709', '3710', '3711', '3712', '3713', '3714', '3715', '3716', '3717', '3718', '3719', '3720', '3721', '3722', '3723', '3724', '3725', '3726', '3727', '3728', '3729', '3730', '3731', '3732', '3733', '3734', '3735', '3736', '3737', '3738', '3739', '3740', '3741', '3742', '3743', '3744', '3745', '3746', '3747', '3748', '3749', '3750', '3751', '3752', '3753', '3754', '3755', '3756', '3757', '3758', '3759', '3760', '3761', '3762', '3763', '3764', '3765', '3766', '3767', '3768', '3769', '3770', '3771', '3772', '3773', '3774', '3775', '3776', '3777', '3778', '3779', '3780', '3781', '3782', '3783', '3784', '3785', '3786', '3787', '3788', '3789', '3790', '4011', '4111', '4112', '4119', '4121', '4131', '4214', '4225', '4411', '4457', '4468', '4511', '4582', '4723', '4784', '4812', '4814', '4816', '4899', '4900', '5013', '5021', '5039', '5044', '5045', '5046', '5047', '5051', '5065', '5072', '5074', '5085', '5111', '5137', '5139', '5169', '5172', '5192', '5193', '5198', '5199', '5200', '5211', '5231', '5251', '5261', '5271', '5300', '5309', '5310', '5311', '5331', '5399', '5411', '5422', '5441', '5451', '5462', '5499', '5511', '5521', '5531', '5532', '5533', '5551', '5561', '5571', '5592', '5598', '5599', '5611', '5621', '5631', '5641', '5651', '5655', '5661', '5681', '5691', '5697', '5698', '5699', '5712', '5713', '5714', '5718', '5719', '5722', '5732', '5733', '5734', '5735', '5811', '5812', '5813', '5814', '5912', '5931', '5935', '5937', '5940', '5941', '5942', '5943', '5945', '5946', '5947', '5948', '5949', '5950', '5960', '5962', '5963', '5964', '5965', '5966', '5967', '5968', '5969', '5970', '5971', '5972', '5973', '5975', '5976', '5977', '5978', '5983', '5992', '5993', '5994', '5995', '5996', '5997', '5998', '5999', '6300', '6399', '6513', '7011', '7012', '7032', '7033', '7211', '7217', '7221', '7230', '7251', '7261', '7273', '7276', '7277', '7278', '7296', '7297', '7298', '7299', '7311', '7321', '7333', '7338', '7339', '7342', '7349', '7361', '7372', '7375', '7379', '7392', '7393', '7394', '7395', '7399', '7511', '7512', '7513', '7519', '7523', '7534', '7549', '7622', '7623', '7629', '7641', '7692', '7829', '7832', '7841', '7911', '7922', '7929', '7932', '7933', '7941', '7991', '7992', '7993', '7996', '7997', '7998', '7999', '8011', '8021', '8031', '8041', '8042', '8043', '8049', '8050', '8062', '8071', '8099', '8111', '8211', '8220', '8241', '8244', '8249', '8299', '8351', '8641', '8651', '8675', '8699', '8734', '8911', '8931', '8999', '9211', '9222', '9223', '9311', '9399', '9402', '9405']
Transaction_Type_Green = ['ACH', 'ACH', 'ACH', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Wire Transfer', 'Void', 'Refund', 'Wire Transfer', 'Void', 'Refund', 'Wire Transfer', 'Void', 'Refund', 'Payment Reversal']
Country_Green = ['AG', 'AM', 'AU', 'AT', 'BT', 'BQ', 'CA', 'CV', 'CL', 'CX', 'CC', 'DK', 'DJ', 'EE', 'FO', 'FJ', 'DE', 'GL', 'VA', 'HK', 'IS', 'IT', 'LV', 'MU', 'NL', 'NF', 'OM', 'PR', 'AX', 'AS', 'BE', 'FK', 'FI', 'FR', 'GF', 'PF', 'GP', 'GU', 'HU', 'IE', 'LT', 'MQ', 'YT', 'NC', 'MP', 'NO', 'PN', 'PT', 'RE', 'BL', 'SH', 'MF', 'PM', 'SM', 'SI', 'SJ', 'SE', 'CH', 'TV', 'GB', 'US', 'VI', 'WF']

Country_Red = ['AF', 'AO', 'AZ', 'BD', 'BY', 'BZ', 'BO', 'MM', 'KH', 'KM', 'CD', 'CI', 'CU', 'GN', 'GW', 'GY', 'HT', 'ID', 'IR', 'IQ', 'KZ', 'KE', 'KP', 'LA', 'LB', 'LR', 'LY', 'NG', 'PK', 'PG', 'PY', 'SL', 'SX', 'SO', 'SD', 'SY', 'TH', 'TR', 'VE', 'VN', 'YE', 'ZW', 'AL', 'DZ', 'AD', 'AI', 'AR', 'AW', 'BS', 'BJ', 'BM', 'BA', 'BR', 'VG', 'BN', 'BF', 'BI', 'KY', 'CF', 'TD', 'CN', 'CO', 'CK', 'CR', 'CY', 'DM', 'DO', 'EC', 'EG', 'GQ', 'ER', 'GA', 'GM', 'GH', 'GI', 'GR', 'GD', 'GT', 'GG', 'HN', 'IM', 'JP', 'JE', 'JO', 'KR', 'KW', 'KG', 'LI', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MH', 'MR', 'MX', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'NP', 'NI', 'NE', 'PW', 'PA', 'PE', 'PH', 'RO', 'RU', 'KN', 'LC', 'VC', 'WS', 'ST', 'SA', 'SN', 'SC', 'SB', 'SS', 'LK', 'SR', 'SZ', 'TJ', 'TZ', 'TG', 'TO', 'TT', 'TN', 'TM', 'UG', 'UA', 'UY', 'UZ', 'VU', 'EH', 'ZM']
Merchant_Category_Red = ['4789', '4821', '4829', '5094', '5933', '5944', '6010', '7699', '7994', '7995', '9950']
Transaction_Type_Red = ['Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance',\
'Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance',\
'Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance',\
'Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment',\
'Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment',\
'Cash Payment','Cash Payment','Cash Payment','Cash Payment',\
 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', \
'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', \
 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Wire Transfer', 'Wire Transfer','Wire Transfer','Wire Transfer',\
 'Wire Transfer','Wire Transfer','Wire Transfer','Wire Transfer','Wire Transfer','Wire Transfer','Refund','Refund','Refund',\
 'Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','ACH','ACH','ACH',\
 'ACH','ACH','ACH','ACH','ACH','ACH','ACH']
count=0

def generate_cc_data(merchant,country,upper,delta,no_trans,count):
	#6)Create a loop for each account and generate account from the customer account_id file 
	for i in range(no_trans):
		acct=random.choice(python_account_ID.accountid)
		cc_list=python_CC.CC_Dict[acct]
		#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
		limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
		#local Amt variable to calculate customer total usage
		usedAmt = 0
		tmpAmt = 0
		maxDate= datetime(0001,01,01) 
		NoTrans = randrange(100,150,1)
		#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
		for j in range(NoTrans):
			dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			tmpAmt = max((randrange(1,upper,1)+delta),0)* randrange(1,limit,100)*(-1)
			#if not credit then generate debit
			if tmpAmt == 0:
				tmpAmt = randrange(1,limit,100)
			#add current amount to client total account usage
			tmp = usedAmt + tmpAmt
			usedAmt = tmp
			#pull value from dictionary for randomly selected merchant category 
			cat = random.choice(merchant)
			tranType = ''
			#set transaction type based on amount
			if tmpAmt < 0:
				tranType = random.choice(Transaction_Type_Credits)
			else: 
				tranType = random.choice(Transaction_Type_Debits)
			#tranType random.choice(Transaction_Type)
			#append values to row list 
			row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
			row.append(cat)
			row.append(python_merchant_cat.All_Merchant_Cat[cat])
			#date posted
			date1 = gen_data.create_date(past=True)
			if date1 > maxDate:
				maxDate = date1
			#date of transaction a day later
			date2 = date1-timedelta(days=1)
			row.extend([date1, date2, tranType,random.choice(country),limit,tmpAmt,usedAmt,cc_list[0],cc_list[1]])
			count = count + 1
			writer.writerow(row)
		#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
		if usedAmt < limit * (-1):
			row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
			date1temp=maxDate+timedelta(days=90)
			date2=date1temp-timedelta(days=1)
			row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0,cc_list[0],cc_list[1]])
			count = count + 1
			usedAmt = 0
			maxDate= datetime(0001,01,01)
			writer.writerow(row)
			
#Green Transactions with Merchant Credits - but no corresponding debits		
def generate_cc_credits(merchant,no_trans,count):
	for i in range(no_trans):
		acct=random.choice(python_account_ID.accountid)
		cc_list=python_CC.CC_Dict[acct]
		#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
		limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
		#local Amt variable to calculate customer total usage
		usedAmt = 0
		maxDate= datetime(0001,01,01) 
		NoTrans = randrange(100,150,1)
		#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
		for j in range(NoTrans):
			dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			#generate amount for current transaction with 50%-50% distribution on credits and debits
			tmpAmt = randrange(1,limit,100)
			#if not credit then generate debit
			#if tmpAmt == 0:
			#tmpAmt = randrange(1,limit,100)
			#add current amount to client total account usage
			usedAmt = usedAmt + tmpAmt
			#pull value from dictionary for randomly selected merchant category 
			cat = random.choice(merchant)
			tranType = ''
			#set transaction type based on amount		
			tranType = random.choice(Transaction_Type_Credits)
			#tranType random.choice(Transaction_Type)
			#append values to row list 
			row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
			row.append(cat)
			row.append(python_merchant_cat.All_Merchant_Cat[cat])
			#date posted
			date1 = gen_data.create_date(past=True)
			if date1 > maxDate:
				maxDate = date1
			#date of transaction a day later
			date2 = date1-timedelta(days=1)
			row.extend([date1, date2, tranType,'US',limit,tmpAmt,usedAmt,cc_list[0],cc_list[1]])
			count = count + 1
			writer.writerow(row)
		#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
		if usedAmt < limit * (-1):
			row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
			date1temp=maxDate+timedelta(days=90)
			date2=date1temp-timedelta(days=1)
			row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0,cc_list[0],cc_list[1]])
			count = count + 1
			usedAmt = 0
			maxDate= datetime(0001,01,01)
			writer.writerow(row)
			
def gen_cc_external(merchant,no_trans,count):
	for i in range(no_trans):
		acct=random.choice(python_account_ID.accountid)
		cc_list=python_CC.CC_Dict[acct]
		#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
		limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
		#local Amt variable to calculate customer total usage
		usedAmt = 0
		maxDate= datetime(0001,01,01) 
		NoTrans = randrange(100,150,1)
		#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
		for j in range(NoTrans):
			dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			#generate amount for current transaction with 50%-50% distribution on credits and debits
			tmpAmt = max((randrange(1,3,1)-1),0)* randrange(1,limit,100)*(-1)
			#if not credit then generate debit
			if tmpAmt == 0:
				tmpAmt = randrange(1,limit,100)
			#add current amount to client total account usage
			usedAmt = usedAmt + tmpAmt
			#pull value from dictionary for randomly selected merchant category 
			cat = ''
			tranType = ''
			row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
			#set transaction type based on amount
			if tmpAmt < 0:
				tranType = random.choice(Transaction_Type_Credits)
				row.append('Non-BMO Acct')
				row.append('')
			else: 
				tranType = random.choice(Transaction_Type_Debits)
				cat = random.choice(merchant)
				row.append(cat)
				row.append(python_merchant_cat.All_Merchant_Cat[cat])
			#tranType random.choice(Transaction_Type)
			
			#date posted
			date1 = gen_data.create_date(past=True)
			if date1 > maxDate:
				maxDate = date1
			#date of transaction a day later
			date2 = date1-timedelta(days=1)
			row.extend([date1, date2, tranType,random.choice(Country_Red),limit,tmpAmt,usedAmt,cc_list[0],cc_list[1]])
			count = count + 1
			writer.writerow(row)
		#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
		if usedAmt < limit * (-1):
			row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
			date1temp=maxDate+timedelta(days=90)
			date2=date1temp-timedelta(days=1)
			row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0,cc_list[0],cc_list[1]])
			count = count + 1
			usedAmt = 0
			maxDate= datetime(0001,01,01)
			writer.writerow(row)
			
#5)Open CSV file for writing
with open('CC.Transactions_1B.csv','w') as f1:
	writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
	writer.writerow(['rownum']+['Account_Number']+['Merchant_Name']+['Merchant_Category_Code']+['Merchant_Category_Desc']+\
	['Post_Date'] +	['Transaction_Date'] + ['Transaction_Type'] +['Merchant_Country']+['Credit_Limit']+['Amount']+['Balance']+\
	['CC_NO']+['CC_TYPE'])
	# Overpayments with green transactions - green activity that doesn't trigger red flags
	#generate amount for current transaction with 33%-66% distribution on credits and debits
	generate_cc_data(Merchant_Category_Green,Country_Green,4,-2,160000,count)

	#Yellow Transactions are defined by Merchant Category, Transaction Types and Country_Yellow.
	#generate amount for current transaction with 50%-50% distribution on credits and debits
	generate_cc_data(Merchant_Category_Yellow,Country_Yellow,3,-1,800000,count)
	
	#Green Transactions are defined by Merchant Category, Transaction Types and Country_Green.
	#generate amount for current transaction with 50%-50% distribution on credits and debits
	generate_cc_data(Merchant_Category_Green,Country_Green,3,-1,6800000,count)
	
	#Country_Red Risk is distrubuted in three categories from the US AML Risk Guide Table 
	#generate amount for current transaction with 50%-50% distribution on credits and debits
	generate_cc_data(Merchant_Category_Red,Country_Red,3,-1,80000,count)
	
	#generate ML activity that consists of merchant credits without matching payments
	generate_cc_credits(Merchant_Category_Green,80000,count)
	
	#Red Transactions with payments from non BMO entities 
	gen_cc_external(Merchant_Category_Red,80000,count)
