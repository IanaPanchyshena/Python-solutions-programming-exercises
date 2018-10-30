#hot dogs=10 in pack
#buns=8 in pack
#Enter number of people attending the cookout
#Enter number of hot dogs each person will be given

#Display:
#The minimum number of packages of hot dogs required MIN_HOTDOGS
#The minimum number of packages of hot dog buns required
#The number of hot dogs that will be left over
#The number of hot dog buns that will be left over

number_people=int(input('Enter number of people attending the cookout '))
number_hotdogs=int(input('Enter number of hot dogs each person will be given '))

total_hotdogs=number_people*number_hotdogs
number_hotdogs_left=10-total_hotdogs%10
if number_hotdogs_left==10:
    number_hotdogs_left=0
number_buns_left=8-total_hotdogs%8
if number_buns_left==8:
    number_buns_left=0

number_hotdogs_pack=total_hotdogs//10
if number_hotdogs_left>0:
    number_hotdogs_pack = number_hotdogs_pack+1

number_buns_pack=total_hotdogs//8
if number_buns_left>0:
    number_buns_pack = number_buns_pack+1


print('The minimum number of packages of hot dogs required',number_hotdogs_pack)
print('The minimum number of packages of hot dog buns required',number_buns_pack)
print('The number of hot dogs that will be left over',number_hotdogs_left)
print('The number of hot dog buns that will be left over',number_buns_left)






