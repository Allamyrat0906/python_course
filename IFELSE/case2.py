mark={
    1:"bad",
    2:"unsatisfactory",
    3:"mediocre",
    4:"good",
    5:"excelent"
}

k=int(input("Enter: "))
if k>0 and k<6:
    print(mark[k])
else:
    print("error")




