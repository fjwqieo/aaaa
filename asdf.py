def hw1():
    with open ('test.txt', 'w') as f:
        f.write("Buddy, you're a boy, make a big nose\nPlaying in the street, gonna be a big man someday\nYou got mud on your face, you big disgrace\nKicking your can all over the place, singin'\nWe will, we will rock you\nWe will, we will rock you")
    my_file=open('test.txt', 'r')
    print(my_file.readline().rstrip())
    print(my_file.readline().rstrip())
    print(my_file.readline().rstrip())
    print(my_file.readline().rstrip())
    print(my_file.readline().rstrip())
    print(my_file.readline().rstrip())
    my_file.close()
    my_file=open('test.txt', 'r')
    lst=my_file.readlines()
    print(lst)
    my_file.close()
    with open('test.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
def hw2():
    usr=input('입력할 파일의 이름 : ')
    with open(f'{usr}', 'r') as f:
        print(f.readline().rstrip().upper())
        print(f.readline().rstrip().upper())
        print(f.readline().rstrip().upper())
        print(f.readline().rstrip().upper())
        print(f.readline().rstrip().upper())
        print(f.readline().rstrip().upper())
def hw3():
    sum1=0
    cnt=0
    with open('sales.txt', 'w') as f:
        print('1000000', file=f)
        print('1000000', file=f)
        print('1000000', file=f)
        print('500000', file=f)
        print('1500000', file=f)
    with open('sales.txt', 'r') as my_file:
        for line in my_file:
            sales=int(line)
            sum1+=sales
            cnt+=1
    print(f'총매출 = {sum1}')
    print(f'평균 일매출 = {sum1/cnt}')
def hw4():
    import string
    freq_list=[0]*26
    with open ('alpha_tst.txt', 'w') as f:
        print('aaaaaaaaaa', file=f)
        print('bbb', file=f)
        print('cccc', file=f)
        print('defg', file=f)
        print('c', file=f)
        print('python', file=f)
        print('java', file=f)
        print('programming', file=f)
        print('zoo', file=f)
        print('test', file=f)
    with open('alpha_tst.txt', 'r') as f:
        for line in f:
            line=line.lower()
            for char in line:
                if char in string.ascii_lowercase:
                    freq_list[ord(char)-ord('a')]+=1
    print(freq_list)
'''def hw5():
    import os
    usr=input('alpha_tst.py: ')
    for i in os.listdir():
        if os.path.isfile(i):
            with open(i, 'r') as f2:
                for line in f2:
                    if f'{usr}' in line:
                        print(line)
                        파일안에 한국어가 없어야 실행 됨'''
def hw6():
    while True:
        try:
            usr=input('파일명: ')
            with open (f'{usr}', 'r') as f:
                for line in f:
                    print(line)
                    line=f.readline()
                    while line:
                        print(line)
                        line=f.readline()
        except FileNotFoundError:
            print(f'{usr} 파일을 찾을 수 없습니다. 파일 이름을 확인해주세요.')
        else: break
'''def hw7():
    cnt=10
    rsltlst=[]
    usrlst=[]
    import random as rd
    with open('words.txt', 'r') as f:
        lst=f.readlines()
        rsltword=lst[rd.randint(0,len(lst))]
        rslt=list(rsltword)
        rslt.pop()
        for i in range(len(rslt)):
            rsltlst.append('_')
        bar=''.join(rsltlst)
        print(bar)
        print(''.join(rslt))
        while True:
            
            usr=input('알파벳: ')
            if usr==rslt[i]:
                print(i)
            else:
                cnt-=1
                print(f'오답입니다.{cnt}번의 기회가 남았습니다.')
            
              '''  
hw7()