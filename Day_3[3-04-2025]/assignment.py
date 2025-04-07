

# print(arr[0]) # 2
# print(arr[3]) # 1
# print(arr[5]) # 8
# print(len(arr)-1) # 6
# print(arr.__len__()) # 6


# arr=[2,3,4,1,6,8]
# max=arr[0]
# i=0
# while(i<len(arr)):
#     if(arr[i]>max):
#         max=arr[i]
#     i+=1

# arr=[2,3,8,4,1,6]
# print(max)
#  i => 0 , 1 , 2, 3, 4,5 , 6 i<len(arr)
# i=0 (0<6)
    # max => 2 
    # 3>2 => max=>3 arr[i]=3
    # i=1
# i=1 (1<6)
    # max => 3 
    # 3 >3 
    # i=2
#  i=2
    # max => 3 arr[i]=4
    # 4>3
    # max =>4
    #i=3
# i=3
    # max => 4
    # 1>4 max => 4
    # i=4
#i=4
    # max=> 4
    # 6>4 max => 6
    # i=5
# i=5
    # max =6
    # 8>6 max=> 8
    # i=6
#i=6 (6<6)


# factorial 
#  5 ! => 5* 4 *3*2*1
i=5
res=1
while(i>=1):
    res*=i  #=> res=res*i
    i-=1
print(res)

# i = 5 => 5>=1 => res =>1*5 i =>4
# i = 4 => 4>=1 => res =>5*4 i=> 3
# i = 3 => 3>=1 => res =>5*4*3 i=> 2
# i = 2 => 2>=1 => res =>5*4*3*2 i=> 1
# i = 1 => 1>=1 => res =>5*4*3*2*1 i=> 0
# i = 0 => 0>=1 => False
# 5*4*3*2*1 => 120

# print(range(3,8))
# print(range(3,8,2))
# print(range(5,2,-1))

# print(range(8))
# range => start , end , steps

for i in range(5):
    print(i)

