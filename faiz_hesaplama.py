''' Basit faiz(I)=P(ANA PARA) * İ(FAİZ ORANI YILLIK) * T(ZAMAN (YIL) 
    Bileşke faiz(Sn)= P*(1+i)^n n=dönem,i=faiz orani,p=ana para
    Paranın gelecekteki değeri= Para+Basit faiz 
'''
p=float(input("Faiz'e yatırılıcak parayı giriniz: "))
i=float(input('Faiz oranını giriniz: '))
t= int(input('Ne kadar faizde tutmayı düşünüyorsunuz, ay olarak giriniz: '))
n=t/12
basit_faiz_orani = p*(i/100)*(t/12)
bileske_faiz_orani= p*(1+(i/100))**n
paranin_son_degeri= p + basit_faiz_orani
print(basit_faiz_orani)
print('paranizin %d ay sonraki değeri= %.0f tldir.'%(t,paranin_son_degeri))