import csv
import time

global total
total = 0

def promising(i, keep):
    k =0
    flag = 1
    while(k < i and flag):
        if ( (keep[i][0] == keep[k][0]  and keep[i][1] == keep[k][1]) or (abs(keep[i][0] - keep[k][0]) == i-k and abs(keep[i][1] - keep[k][1]) == i - k) or (keep[i][0] == keep[k][0] and abs(keep[i][1] - keep[k][1]) == i-k)  or (keep[i][1] == keep[k][1] and abs(keep[i][0] - keep[k][0]) == i-k)):
            flag = 0
        k +=1
    return flag



def queen(i, N, keep):
    global total
    if(promising (i, keep)):
        if(i == N-1):
            #print(keep)
            total += 1
        else:
            for j in range(0,N):
                for l in range(0,N):
                    keep[i+1][0] = j
                    keep[i+1][1] = l
                    queen(i+1, N, keep)

def main():
    N = 2
    keep = [[0 for i in range(2)] for j in range(N)]
    global total
    total = 0
    queen(-1, N, keep)
    print("Total number of solutions for N=2 is " + str(total))

    N = 3
    keep = [[0 for i in range(2)] for j in range(N)]
    total = 0
    queen(-1, N, keep)
    print("Total number of solutions for N=3 is " + str(total))

    N = 4
    keep = [[0 for i in range(2)] for j in range(N)]
    total = 0
    queen(-1, N, keep)
    print("Total number of solutions for N=4 is " + str(total))


    N = 5
    keep = [[0 for i in range(2)] for j in range(N)]
    queen(-1, N, keep)
    total = 0
    queen(-1, N, keep)
    print("Total number of solutions for N=5 is " + str(total))


if __name__ == "__main__" :
    start = time.time()
    main()
    end = time.time()
    print("\n\nRuntime of the program is " + str(end - start) + "s.")