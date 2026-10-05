
# 1. Sum of Prime Numbers
# Find the sum of all prime numbers between 20 and 150.

# sum = 0
# for j in range(20,151,1):
#     n=j
#     count = 0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     if(count==2):
#         sum+=n
# print(sum)








# 2. Average of Perfect Numbers
# Find the average of all perfect numbers between 1 and 1000.

# total=0
# count = 0
# for j in range(1,1001,1):
#     n=j
#     sum=0
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum +=i
#     if(sum==n):
#         total+=n
#         count+=1
#         print(n)
# avg = total / count
# print("average : ",avg)






# 3. Leap Years in a Range(Not Nested Loop Logic)
# Print all leap years between 1900 and 2026.

# for i in range(1900, 2027,1):
#     n=i
#     if ((n%4==0 or n%400==0) and n%100!=0):
#         print(n)




# 4. Palindrome Numbers
# Print all palindrome numbers between 100 and 500

# for i in range(100,501,1):
#     n=i
#     newNum=n
#     rev=0
#     while(n!=0):
#         ld = n%10
#         rev = rev*10+ld
#         n = n//10
#     if (newNum==rev):
#         print(newNum)




# 5. Digit Sum = 10
# Print all numbers between 120 and 850 whose digit sum is exactly 10.

# for i in range(120, 851,1):
#     n=i
#     newNum = n
#     digitSum = 0
#     while (n!=0):
#         ld = n%10
#         digitSum += ld
#         n=n//10
#     # print(digitSum)
#     if(digitSum==10):
#         print(newNum)






# 6. Pairs with Target Sum
# Print all pairs (a, b) between 1 and 50 whose sum is 30. Print each pair only once.
# for j in range(1,51,1):
#     for i in range(j,51,1):
#         if(i+j==30):
#             print(j,i)







# 7. Exactly 3 Factors
# Print all numbers between 10 and 300 that have exactly 3 factors.

# for j in range(10,301,1):
#     n=j
#     count = 0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     if count==3:
#         print(n)






# 8. Prime Factors
# Print the prime factors of every number between 20 and 50.

# for j in range(20,51,1):
#     n=j
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count=0
#             for k in range(1,i+1,1):
#                 if(i%k==0):
#                     count+=1
#             if(count==2):
#                 print(i,end=" ")
#     print()




# 9. Armstrong Numbers
# Print all Armstrong numbers between 100 and 999.

# for j in range(100,1000,1):
#     n=j
#     newNum = n
#     sum=0
#     count = 0
#     while (newNum!=0):
#         count = count+ 1
#         newNum = newNum//10

#     newNum = n
#     while (newNum!=0):
#         ld=newNum%10
#         res = ld**count
#         sum+=res
#         newNum= newNum//10
#     if sum==n:
#         print(n)








# 10. Maximum Factors
# Find the number between 50 and 150 that has the maximum number of factors.

# max_Count = 0
# max_Num = 0
# for j in range(50,151,1):
#     n=j
#     count = 0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     if count>max_Count:
#         max_Count=count
#         max_Num = n
# print("Number = ", max_Num)
# print("Factors = ", max_Count)