n=int(input("n="))
counter=1
while counter<=n:
    if counter%3==0 and counter%4==0:
        print(counter,"既能被3整除又能被4整除")
    elif counter%3==0:
        print(counter,"能被3整除")
    elif counter%4==0:
        print(counter,"能被4整除")
    counter+=1
input("Press enter to end")