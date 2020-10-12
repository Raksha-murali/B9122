## This is my solution to question 1

# We want the function to take the following inputs
# float rate (interest rate), int N (number of payments),
# int FV (future value), int PV (present value)

#I have set default values for rate and N, but this can just be
# changed by calling the function differently as seen in the
# two examples below. I have imposed type values on the inputs
# just for good measure

PV = int(input("Enter the present value:"))
FV= int(input("Enter the future value:"))

def compute_emi(PV:int,FV:int,rate = 0.04,N = 20,):
    emi = (PV+(FV/(1+(rate))**N))*(rate*(1+rate)**N/((1+rate)**N-1))
    print("The required EMI value is", emi)
    return emi

compute_emi(PV,FV)


