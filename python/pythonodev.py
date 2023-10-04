###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8


y = 3.2


z = 8j + 18


a = "Hello World"


b = True


c = 23 < 22



l = [1, 2, 3, 4,"String",3.2, False]



d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}


t = ("Machine Learning", "Data Science")



s = {"Python", "Machine Learning", "Data Science","Python"}


x = 8


y = 3.2


z = 8j + 18


a = "Hello World"


b = True


c = 23 < 22



l = [1, 2, 3, 4,"String",3.2, False]



d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}


t = ("Machine Learning", "Data Science")

#############################################################################################################################################

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

type(s)
text = "The goal is to turn data into information, and information into insight."

text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")

words = text.split()

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

len(lst)

ilk_eleman = lst[0]
onuncu_eleman = lst[10]

print("sıfırıncı eleman", ilk_eleman, "onuncueleman", onuncu_eleman)

data = lst[0: 4]

del lst[8]

lst.append(1)

print(lst)

lst[8] = "N"
###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.


# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.


# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.


# Adım 4: Sekizinci index'teki elemanı silin.


# Adım 5: Yeni bir eleman ekleyin.



# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
##############################################################################################
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

keys = dict.keys()
value = dict.values()

dict["Daisy"][1] = 13

dict["ahmet"] = ["turkey, 24"]

del dict["Antonio"]
###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]
###############################################
l = [2,13,18,93,22]
k = []
m = []

for i in l:
    if i % 2 == 0:
        k.append(i)
    else:
        m.append(i)
return k m

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

A = []
B = []
for index, ogrenci in enumerate(ogrenciler):
    if index <= 2:
        A.append(ogrenci)
    else:
        B.append(ogrenci)
print(A, B)

#mulakat sorusu
############################################################
ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

grup = [[], []]

def divide_students(ogrenciler):
    for index, ogrenci in enumerate(ogrenciler):
        if index % 2 == 0:
            grup[0].append(ogrenci)
        else:
            grup[1].append(ogrenci)
    print(grup)
    return grup

st = divide_students(ogrenciler)

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu, kredi, kontenjan))



###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kümes(kume1, kume2):
    if kume1.issuperset(kume2):
        ortak_elemanlar = kume1.intersection(kume2)
        return ortak_elemanlar
    else:
        fark = kume2 - kume1
        return fark

sonuc = kümes(kume1, kume2)
########
def kume_kontrol(kume1, kume2):
    if kume1.issuperset(kume2):
        ortak_elemanlar = kume1.intersection(kume2)
        return ortak_elemanlar
    else:
        fark = kume2 - kume1
        return fark

# Verilen kümeler
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

# Fonksiyonu çağırarak sonuçları alın
sonuc = kume_kontrol(kume1, kume2)

print("Sonuç:", sonuc)
Bu düzeltilmiş kod, parantezleri doğru bir şekilde kullanarak çalışacaktır. issuperset() ve intersection() yöntemleri ile kümeler arasındaki ilişkiyi kontrol edecek ve sonuca göre işlem yapacaktır.


##########################################################################################################

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def tek_cift(l):
    c = []
    t = []

    for i in l:
        if i % 2 == 0:
            c.append(i)
        else:
            t.append(i)
    return c, t

tek_cift(l)


###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

muhendislik = []
tıp = []

for index, oogrenci in enumerate(ogrenciler):
    if index <= 2:
        muhendislik.append(oogrenci)
    else:
        tıp.append(oogrenci)
print(muhendislik, tıp)


# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#df.columns = ["_NUM" + col.upper() for col in df.columns if not col.isnumeric()]
#df.columns
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

#result = ["NUM_" + var.upper() for var in df.columns if not var.isnumeric()]

#print(result)


# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
result = [col.upper() + "_FLAG" if "NO" not in col else col.upper for col in df.columns]
result
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']

## result = [flag.upper() + "FLAG" if "no" not in flag else flag.upper() for flag in df.columns]
## print(result)

# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
new_col = [col for col in df.columns if col not in og_list]
og_list = ["abbrev", "no_previous"]
new_df = df[new_col]
new_df
# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630

## new_cols = [col for col in df.columns if col not in og_list]

### new_df = df[new_cols]



##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################
df = sns.load_dataset("titanic")
df.head(10)
#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################
kadın_sayısı = df[df["sex"] == "female"]["sex"].count()
kadın_sayısı
erkek_sayısı = df[df["sex"] == "male"]["sex"].count()
erkek_sayısı

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################
unique_degerler = df.nunique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################
pclass_benzersiz = df["pclass"].unique()
pclass_benzersiz


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

pclass_unique = df["pclass"].nunique()
parch_unique = df["parch"].nunique()

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################
type(df["embarked"])
df.head(10)
df["embarked"] == df["embarked"].astype("category")
type(df["embarked"])
#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

embarked_c = df[df["embarked"] == "C"]
embarked_c


#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################
embarked_s = df[df["embarked"] != "S"]
embarked_s

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################
df[(df["age"] < 30) & (df["sex"] == "female")].head()


#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################
df[(df["fare"] > 500) | (df["age"] > 70)].head(10)


#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################
bos_deger_toplamı = df.isnull().sum()


#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df.drop(columns= "who")

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################
deck_mod = df["deck"].mode()[0]
df["deck"].fillna(deck_mod, inplace=True)
df.head(20)

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################
age_medyan = df["age"].median()

df["age"].fillna(age_medyan, inplace=True)
df.head(6)
#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################
survival_stat = df.groupby(["pclass", "sex"])["survived"].agg(["sum", "count", "mean"])
print(survival_stat)
#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)
df.head(10)
#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

tips = sns.load_dataset("tips")



#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

tips.groupby("time")["total_bill"].agg(["sum", "min", "max", "mean"])

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

tips.groupby(["day", "time"])["total_bill"].agg(["sum", "min", "max", "mean"])

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################
lunch_female_data = tips[(tips["time"] == "Lunch") & (tips["sex"] == "Female")]

tips.groupby("day")[["total_bill", "tip"]].agg(["sum", "min", "max", "mean"])


#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################
filtered_orders = tips[(tips["size"] < 3) & (tips["total_bill"] > 10)]

filtered_orders = tips[(tips["size"] < 3) & (tips["total_bill"] > 10)]
mean_total_bill = filtered_orders["total_bill"].mean()
mean_total_bill

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

tips["total_bill_sum"] = tips["total_bill"] + tips["tip"]
tips.head(10)


#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

sorted_df = tips.sort_values(by="total_bill_sum", ascending=False)
ilk_30_kisi = sorted_df.head(30)
ilk_30_kisi