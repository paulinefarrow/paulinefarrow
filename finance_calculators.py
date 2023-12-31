import math

# display menu to allow user to choose either bond or investment calculation

user_choice = input(""" 
                Investment - to calculate the amount of interest you'll earn on your investment
                Bond - to calculate the amount you'll have to pay on a home loan
                  
                Enter either 'investment' or 'bond' from the menu above to proceed: """)

# if the user does enter 'investment' or 'bond' give an error message and repeat question

while user_choice.lower() not in ("bond", "investment" ):

    user_choice = input(""" 
                That was not a valid response, please select an option from below: 
                              
                Investment - to calculate the amount of interest you'll earn on your investment
                Bond - to calculate the amount you'll have to pay on a home loan
                  
                Enter either 'investment' or 'bond' from the menu above to proceed: """)

# if the user chooses 'investment' collect the information required to calculate interest earned    

if user_choice.lower() == "investment":
    p = float(input("Please enter the amount of money you are depositing: "))
    r = float(input("Please enter the annual interest rate (%): "))/100
    t = float(input("Please enter the number of years you intend to invest for: "))
    interest = (input("Would you like simple or compound interest (type 'simple' or 'compound'): ")).lower()
    a = 0

# if the user chooses 'simple' interest calculate total amount at end of time period for simple interest

    if interest == "simple":
        a = p *(1 + r*t)


# print out 'total interest earned' along with the values they entered        

        print(f"""
              Investment Calculation :
              Amount Deposited      = £{round(p)}
              Annual Interest Rate  = {round(r*100, 2)}%
              Number of Years       = {round(t)}
              Interest Type         = {interest.upper()}
              Total Interest Earned = £{round((a - p), 2)}""")


# otherwise if user has entered 'compound' or an invalid  response calculate total amount at end of time period for compound interest

    else:
        a = p * math.pow((1+r),t)

# print out 'total interest' earned along with the values they entered and 'Interest Type' hard coded to 'Compound'       

        print(f"""
              Investment Calculation :
              Amount Deposited      = £{round(p)}
              Annual Interest Rate  = {round(r*100, 2)}%
              Number of years       = {round(t)}
              Interest type         = COMPOUND
              Total Interest Earned = £{round((a - p), 2)}""")
    
###############################################################    
    
# if the user chooses 'bond' collect the information required to calculate the monthly repayments    
    
if user_choice.lower() == "bond":
    p = float(input("Present value of the house: "))
    i = (float(input("Please enter the annual interest rate (%): "))/100)/12
    n = float(input("Please enter the number of months you intend to take to repay the bond: "))
    repayment = 0

# calculate monthly repayments   

    repayment = (i * p)/(1 - (1 + i)**(-n))

# print out 'monthly repayment' along with the values they entered            

    print(f"""
              Bond Calculation :
              Present Value of house           = £{round(p)}
              Annual Interest Rate             = {round(i*100*12, 2)}%
              Number of months to repay        = {round(n)}
              Amount to pay on loan each month = £{round(repayment, 2)}""")  