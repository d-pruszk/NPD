import random
import math

N = input("Enter the total number of iterations: ")
N = int(N)
K = input("Enter the display step: ")
K = int(K)

# N=5000000
# K=N/10

count = 0
for i in range(1,N):
    if math.sqrt(pow(random.uniform(-1, 1),2)+pow(random.uniform(-1, 1),2))<=1:
        count=count+1
    if i % K == 0:
        print(i,": ",count*4/i)
print("Final Monte Carlo Pi approximation: ",4*count/N)
print("Pi approximation using math.pi:", math.pi)

