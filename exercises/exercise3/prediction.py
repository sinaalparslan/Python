import random


number = random.randint(1,100)
wLife=int(input('how many life do you want:'))
nLife = wLife
counter=0

while nLife > 0:

    nLife -= 1
    counter +=1
    prediction=int(input('Prediction:'))
    if number==prediction:
        print(F'Congratulations.Total point:{100-((100/wLife)*(counter-1))}')
        print(F'You got it on the { counter}. try' )
    elif number< prediction:
        print(F'You counldnt find it on the { counter}. try')
        print('You have to estimate a smaller number')

    else:
        print(F'You counldnt find it on the { counter}. try')
        print('You have to estimate a bigger number ')

    if nLife==0:
        print('Unfortunately you couldnt find the correct result')









