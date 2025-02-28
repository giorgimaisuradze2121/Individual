# ჩამოწერე  თითოეული collection type-ის თვისებები რაც დღეს ვისწავლეთ ( list, tuple , set )

# list - mutable - ცვალებადი , შეიძლება შეიცავდეს დუპლიკატ ელემენტებს, ინახავს ნებისმიერ მონაცემთა ტიპს, აღინიშნება []
# tuple - immutable - არაცვალებადი , ელემენტების რიგი არის შენარჩუნებული, შეიძლება შეიცავდეს დუპლიკატ ელემენტებს, ინახავს სხვადასხვა ტიპის მონაცემებს,ელემენტზე წვდომა შესაძლებელია ინდექსის გამოყენებით,აღინიშნება ()
# set - mutable - შიგნით რაცაა ელემეტები უცვლელია, მაგრამ ელემენტები უნდა იყოს immutable - უცვლელი,არარის შენახული ელემენტების რიგი unordered , არ შეიცავს დუპლიკატ ელემენტებს,ინახავს  სხვადასხვა ტიპის მონაცემებს immutable ელემენტებს,აღინიშნება {}


# list - ordered, დუპლიკატი,ცვლილება 
# tuple - ordered, დუპლიკატი , არააცვლილება
# set - ordered, დუპლიკატი, ცვლილება



# 2) შექმენი რამონიდემე list, tuple და set. შექმნილ collection type-ებზე გამოიყენე ნასწავლი მეთოდები:

# .append()

# .add()

# .remove()

# .clear()

# .union()

# .difference() 


# list=[1,2,3]

# list.append(4)
# print(list)



# list1=[1,2,3,4]

# list1.remove(4)
# print(list1)


# list2=[1,2,3,4]

# list2.clear()
# print(list2)






# set={1,2,3}
# set.add(4)
# print(set)




# set={1,2,3,4,5}
# set.remove(4)
# print(set)




# set={1,2,3,4,5,6,7,8,9,10}
# set.clear()
# print(set)



# set_1={1,2,3}
# set_2={3,4,5}

# union=set_1.union(set_2)

# print(union)


# set_1={1,2,3,4,5}
# set_2={4,5,6,7}


# dif=set_1.difference(set_2)

# print(dif)







# 3) points = (124, 84, 19, 100, 99)
# tuple-დან for loop-ის დახმარებით გამოიტანე მხოლოდ 100-ზე მეტი ციფრები


# points = (124, 84, 19, 100, 99)
# for point in points:
#     if point > 100:
#         print(point)



# შენი სიტყვებით ახსენი რა არის Tuple unpacking და მოიყვანე მაგალითი



# x=(10,20,30)
# y, z, o = x


# print(y)
# print(z)
# print(o)



# tuple=(1,2,3,4,5,6,7,8,9,10)
# first, second, third,*Four = tuple 

# print(first)
# print(second)
# print(third)
# print(Four)





