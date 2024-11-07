total_price = int(0)
print("Rollercoaster Ticket")
height=float(input('Please enter your height: '))
if height>=1.2:
    print("You have the permitted height,\nYou can now buy a ticket.")
    age=int(input('Please enter your age: '))
    if age >= 18:
        print("The ticket price is $12 .")
        total_price = 12
    elif age<=12:
        print('The ticket price is $5 .')
        total_price = 5
    else:
        print('The ticket price is $7 .')
        total_price = 7
    q_photo=input('Do you want to take a photo?')
    if q_photo == 'y' or q_photo == 'Y' or q_photo == 'yes' or q_photo == 'Yes':
       total_price += 3
       print(f'The price to be paid is ${total_price} .')

else:
    print('You are shorter then the permitted')
'''

print('Even or Odd Calculator')
number=int(input('Write a number to check: '))
calc=number%2
if calc==0:
    print("That's an even number")
else:
    print("That's a odd number")
'''