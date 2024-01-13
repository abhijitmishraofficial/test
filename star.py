def starpattern():
    a=int(input());
    for i in range (1,a+1):
        for j in range (1,a+1):
            if(j<=i):
                print("*", end=' ');
            else:
                print(" ", end=' ');

        print();


    for i in range(1,a):
        for j in range (a-i):
            print("*",end=' ');
        print();
        

starpattern();
