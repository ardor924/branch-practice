def buzz(num:int) :
    for i in range(1,num+1) :
        if i % 5 == 0 :
            print('buzz')
        else :
            print(i)

if __name__ == '__main__' :
    buzz(15)
