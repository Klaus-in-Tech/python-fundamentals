def name_printer(name,n,i):
    if i>n:
        return 0
    print(name)
    i+=1
    name_printer(name,n,i)

def asc_numbers(n_times,counter):
    if counter>n_times:
        return
    print(counter,end=' ')
    counter+=1
    asc_numbers(n,counter)

def reverse_numbers(z_times):
    if z_times<1:
        return
    z_times-=1
    reverse_numbers(z_times)
    print(z_times,end=' ')

def sum(n,i):
    sum=0
    if n<i:
        return
    sum=sum+n
    n-=1
    sum(n,i)
    print(sum)
    
def palindrome_checker(index,my_string):
    if (index>=len(my_string)/2):
        return True
    if (my_string[index] != my_string[len(my_string)-index-1]):
        return False
    return palindrome_checker(index+1,my_string)

def util(m,n): return 1 if m == 0 or n == 0 else util(m-1,n) + util(m,n-1)


def util2(m,n):
    if m==1 or n==1: 
        return 1
    prev = [1]*n 
    for i in range(1,m):
        curr=[0]*n
        curr[0]=1
        for j in range(1,n) :  
            curr[j] = prev[j]+curr[j-1]
        prev=curr
    print(curr)
    return curr[n-1]

def traverse_rec(i,j,dp):
    dp[i][j] = -1
    if (i==0) and (j==0):
        return 1
    if (i<0) or (j<0):
        return 0
    if (dp[i][j] != -1):
        return dp[i][j]
    
    dp[i][j] = traverse_rec(i-1,j,dp) + traverse_rec(i,j-1,dp)
    return dp[i][j]
# dp = [[None for j in range(4)] for i in range(4)]
# print(traverse_box(3,3,dp))

def traverse_tab(i,j,dp):
    dp[i][j]
    for x in range(0,i):
        for y in range(0,j):
            if(i==0) and (j==0): 
                dp[i][j]=1
            else:
                up=0
                left=0
                if (i>0):
                    up = dp[i-1][j]
                if (j>0):
                    left = dp[i][j-1]
                dp[i][j] = up + left
    return dp[i-1][j-1]

dp = [[None for j in range(4)]for i in range(4)]
traverse_tab(2,2,dp)