
kelasA = ['Adrian','Attar','Bagus','Ervizal','Athan','Afiq','Safri','Elisa','Fahruddin','Amar']
print("KelasA[4,6,7]:", kelasA[4],',', kelasA[6],',', kelasA[7])
kelasA[3]='Zaki'
kelasA[5]='Dendy'
kelasA[9]='Danendra'
kelasA.append('Dhea')
kelasA.append('Gea')

for x in kelasA*2 : print (x)

print("Jumlah data pada variabel kelasA :", len(kelasA))







