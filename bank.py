sina={
    'acaunt_Name' : 'Sina Alparslan',
    'acaunt_Number' : '123456',
    'password':'4736',
    'remaining_Balance':5000,
    'additional_Balance':3000

}
alp = {
    'acaunt_Name': 'alp alp',
    'acaunt_Number': '123457',
    'password': '3540',
    'remaining_Balance': 3000,
    'additional_Balance': 1000

}
def withrawMoney(acaunt,amount):
    print(f"Hello, {acaunt['acaunt_Name']}")

    if (acaunt['remaining_Balance']>=amount ):
        acaunt['remaining_Balance']-=amount
        print('you can withdraw money')
    else:
        total=acaunt['remaining_Balance']+acaunt['additional_Balance']
        if total >= amount :
            use_addBalance=input('do you allow withdraw from additional account y/n :')
            if (use_addBalance=='Y' or use_addBalance=='y'):
                residual_Value=amount-acaunt['remaining_Balance']
                acaunt['remaining_Balance']=0
                acaunt['additional_Balance']-=residual_Value

                print(' you can take money')
            else:
                print(f"there is a balance of {acaunt['remaining_Balance']} in your acount number {acaunt['acaunt_Number'] }")
        else:
            print('you don have enough money')

withrawMoney(sina,6000)
