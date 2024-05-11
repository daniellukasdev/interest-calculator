# Need to accept input from user
# total, interest, term (in months)
# lump-sum payment and interest

def interest_calc():
    total = get_total()
    print(total)
    int_rate = get_rate()
    print(int_rate)

def get_total():
    return input('Please enter the total loan amount:')

def get_rate():
    return input('Please enter the interest rate including the decimal:')

if __name__ == '__main__':
    interest_calc()