
import random

datafile = open('C:\\bigData\\CodeSamplesEtc\\FRTB\\demo\\generatedData_x.csv', 'w')

print("BDATE,DEAL_ID,PROD_ID,PORTFOLIO,PNLS")

num_of_records = 1000
num_of_pnls = 100

bdate="20170228"
product_ids = ["PROD_001", "PROD_002", "PROD_003","PROD_004","PROD_005","PROD_006","PROD_007","PROD_008","PROD_009","PROD_010","PROD_011","PROD_012","PROD_013","PROD_014","PROD_015",]
portfolios = ["PORTF_001", "PORTF_002", "PORTF_003","PORTF_004","PORTF_005","PORTF_006","PORTF_007","PORTF_008","PORTF_009","PORTF_010"]

random.seed(200)

for line_num in range(1,num_of_records):
    deal_id = "DEAL_" + str(line_num).rjust(8,'0')

    prod_index = random.randrange(0,15,1)
    product_id = product_ids[prod_index]

    portfolio_index = random.randrange(0,10,1)
    portfolio_id = portfolios[portfolio_index]

    pnl_str = ""
    sss = 0  ## This variable is to select a negative or a positive number at random.

    # dealMu and dealSigma are meant to be distribution parameters for a deal.
    dealMu = random.uniform(-2,15)
    dealSigma = random.uniform(2,6)
    for xx in range(1,num_of_pnls):
        if random.uniform(0,2) < 1:
            sss = -1
        else:
            sss = 1

        pnl = format(random.normalvariate(dealMu, dealSigma) * 50 * sss, '.2f')
        pnl_str = pnl_str + str(pnl) + "|"

    pnl_str = pnl_str[:-1]
    dataline = bdate + "," + deal_id + "," + product_id + "," + portfolio_id + "," + pnl_str + "\n"
    #print(dataline)
    datafile.write(dataline)
