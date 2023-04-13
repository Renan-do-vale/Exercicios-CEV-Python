from Pacotes.modulos import leiafloat


def calculoTinta(l , a):
    area = l * a
    totlata = area/2
    print(f'the wall has an area of {area:.1f}m²') 
    print(f'to paint the wall you need {totlata:.1f}l of paint')  

    
LarguraP = leiafloat('Wall width: ')
AlturaP = leiafloat('Wall height: ')
calculoTinta(LarguraP, AlturaP)