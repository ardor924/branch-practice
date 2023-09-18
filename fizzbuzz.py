def fizz(num:int) :
    for i in range(1,num) :
        if i % 3 == 0 :
            print('fizz')
        else :
            print(i)

if __name__ == '__main__' :
    fizz(15+1)
