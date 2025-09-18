print("""***********(*******************
Harf Notunuzu Hesaplayalım
""")
vize1=float(input("1.Vize notunuzu buraya girin: "))
if(vize1>100 or vize1<0 ):
    print("Sınav notlarınız 100 üzerinden hesaplanır .Hatalı değer girdiniz doğru sonuç için düzeltin lütfen.")
vize2=float(input("2.Vize notunuzu buraya girin:"))
if (vize2>100 or vize2<0):
    print("Sınav notlarınız 100 üzerinden hesaplanır .Hatalı değer girdiniz doğru sonuç için düzeltin lütfen.")
final=float(input("Final notunuzu buraya girin:"))
if(final>100 or final<0):
    print("Sınav notlarınız 100 üzerinden hesaplanır .Hatalı değer girdiniz doğru sonuç için düzeltin lütfen.")


toplam_not=(vize1*30/100)+(vize2*30/100)+(final*40/100)
if (toplam_not>=90):
    print("Notunuz {} yani AA".format(toplam_not))
elif(toplam_not>=85):
    print("Notunuz {} yani AB :))))".format(toplam_not))
elif(toplam_not>=80):
    print("Notunuz {} yani BB <3 <3 <3".format(toplam_not))
elif(toplam_not>=75):
    print("Notunuz {} yani BC :D".format(toplam_not))
elif(toplam_not>=70):
    print("Notunuz {} yani CC ".format(toplam_not))
elif(toplam_not>=65):
    print("Notunuz {} yani CD :d".format(toplam_not))
elif(toplam_not>=60):
    print("Notunuz {} yani DD".format(toplam_not))
elif(toplam_not>=55):
    print("Notunuz {} yani DF".format(toplam_not))
else:
    print("Notunuz {} yani FF".format(toplam_not))
print("Başarılarrrr :)")
