"""a""";n=input();t=input()=="Domestic";print(n[0]if len(n)==9 else n[0:2]if t else "+66"+n[1]if len(n)==10 else "",n[-8:-4],n[-4:])
