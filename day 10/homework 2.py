""""დავალება1) 0-იდან 20-ის ჩათვლით დაპრინტეთ ყველა მთელი რიცხვი"""

for x in range(0, 20 + 1):
     print(x)

"""
დავალება2) 50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით.
ეს ჯამი უნდა შეინახოს ცვლადში, ამიტომ ციკლის გარეთ შექმენით sum ცვლადი, რომელსაც ციკლში 
მიემატება საიტერაციო ცვლადის მნიშვნელობა. საბოლოოდ დაპტინტეთ sum ცვლადის მნიშვნელობა."""


for x in range(50,100 + 1):
        x = range(50, 100 + 1)
a = x
b = sum(a)
print(b)


#ricxvta jami
a = (3,4,5,6)
x = sum(a)
print(x)




"""
დავალება3) -10-იდან 10-ის ჩათვლით დაატრიალეთ for ციკლი და იტერაცია მოახდინეთ 3-ით (გაიხსენეთ step),
 დაპრინტეთ საიტერაციო ცვლადის მნიშვნელობა ყოველ ციკლის დატრიალებაზე."""


for i in range(-10, 10):
    while i <= 10:
      print(i)
      i = i + 3
     


"""დავალება4) მომხმარებელს input-ის გამოყენებით შემოატანინეთ ორი რიცხვითი მნიშვნელობა.
 შემდეგ if წინადადებით შეამოწმეთ რომელია უდიდესი და გამოიყენეთ for ციკლი: 
 უმცირესიდან უდიდესამდე მოახდინეთ იტერაცია 2-ით და დაპრინტეთ ყველა მნიშვნელობა."""

num = int(input("enter firs number: "))
num1 = int(input("enter second number: "))


num >= num1 and num >= num1
num <= num1 and num <= num1


if num > num1:
     print("The first number is more than the second")


if num < num1:
     print("The second number is more than the second")

    
"""დავალება5) მომხმარებელს input-ის გამოყენებით შემოატანინეთ ორი რიცხვითი მნიშვნელობა.
   შექმენით ჯამის ცვლადი ციკლის გარეთ რომლის საწყისი მნიშვნელობა იქნება 0. 
   ციკლში start პოზიციად მომხმარებლის შემოტანილი რიცხვებიდან უმცირესი, 
   ხოლო end პოზიციად უდიდესი აიღეთ. ციკლის მუშაობისას საიტერაციო ცვლადის მნიშვნელობა
   გადაეცით ჯამის ცვლადს, რათა გაიგოთ ყველა ამ რიცხვის ჯამი. საბოლოოდ დაპრინტეთ ჯამი"""


num = int(input("enter firs number: "))  #10
num1 = int(input("enter second number: ")) #100
sum = 10
for num in range(num1):
     while num <= num1:
      sum = sum + num
      print(num)
     break
print(sum)