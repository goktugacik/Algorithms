#https://www.codechef.com/problems/MINEAT

the_string = input()
N, H = the_string.split()
N= int(N)
H = int(H)

list = list(map(int,input().split()))


for i in range(1, max(list)+1):
    counter=0
    for a in list:

        if a<=i:
            counter += 1
        elif a%i==0:
            counter += int(a/i)
        else:
            counter += int (a/i)+1
        #print(counter)

    if(counter<=H):
        break
        
print(i)