loan_size = int(input('how large is the loan? (1/10) '))
Credit = int(input('Rate you credit history: (1/10) '))
Income = int(input('Rate you current income: (1/10) '))
Payment = int(input('how large is your down payment? (1/10) '))

if loan_size >= 5:
    if Credit >= 7 and Income >= 7:
        Decision = 'Approved'
    elif Credit >= 7 or Income >=7:
        if Payment  >=5:
            Decision = 'Approved'
        else:
            Decision = 'Denied'
    else:
        Decision = 'Denied'
else :
    if Credit < 4 :
        Decision = 'Denied'
    elif Income >= 7 or Payment >= 7:
        Decision = 'Approved'
    elif Income >= 4 and Payment >= 4:
        Decision = 'Approved'
    else : 
        Decision = 'Denied'
print (f'Your loan Request has been {Decision}')
