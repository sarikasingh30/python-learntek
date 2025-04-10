# Sum of factorials
# 4
# 4! 3! 2! 1!

# 2 loops => nested => 2 => 1 factorial 2 Adding Up
# num*num + number

# 4*3*2*1
num = 3
# fact = 1
# while num >= 1:
#     fact = fact * num
#     num -= 1
# print(fact)


# 1+2+3+4
sum = 0
for i in range(1, num + 1):
    fact = 1
    j = i
    while j >= 1:
        fact = fact * j
        j -= 1
    # print(fact)
    sum += fact

print(sum)

# sum=0
# i=1 => fact=1 j=1 (1,1) => 1=>1 fact =>1*1=1 j=>0 sum=1
# i=2 => fact=1 j=2 (2,2) => 2=>1  j=2 fact =>1*2 =2 j=>1 fact=2*1=2 j=>0 sum=1+2 =>3
# i=3 => fact=1 j=3 (3,3) => 3=>1  j=3 fact =>1*3 =3 j=>2 fact=3*2=6 j=>1 fact=6*1=6 j=>0 sum=3+6 =>9
