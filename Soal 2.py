bio = {
    'Nama': 'Agus Kurnia Akbar',
       'Hobi1':'Ngegame', 'Hobi2':'Mendengarkan musik','Hobi3':'Memancing',
       'Sosmed1':'@aguskur_ak','Sosmed2':'@agusuka123','Sosmed3':'aguskur_ak',
       'Lagu1':'Manisnya Negeriku','Lagu2':'Nusantara','Lagu3':'Syiir Tanpo Waton',
       'Makanan1':'Mie Ayam','Makanan2':'Nasi Goreng','Makanan3':'Bakso'
       }
bio['Hobi3']= 'Jalan-Jalan'
bio['Sosmed3']='@AgusKurniaAkba1'
del bio['Makanan1']
bio.update({'Hobi4':'Nonton TV'})

print("Nama :", bio['Nama'])
print("Hobi :", bio ['Hobi1'],',',bio['Hobi2'],',',bio['Hobi3'],',',bio['Hobi4'])
print("Sosmed : ", "IG:",bio['Sosmed1'],', IG :',bio['Sosmed2'],', Twitter :', bio['Sosmed3'])
print("Lagu Favorit :", bio['Lagu1'],',', bio['Lagu2'],',',bio['Lagu3'])
print("Makanan Favorit :", bio['Makanan2'],',',bio['Makanan3'])