age = 13
if age < 18:
    print("you be a child")


num = 0
    
while num <= 20:
    print(num)
    num = num + 1
print("DONE")


#target = 38
#guess = None

#while guess != target:
    #guess = input('Guess')
    #guess = int(guess)

#print('You got it')


#for snack in ['peanut', 'candy', 'apple']:
 #   print('I ate a', snack)

#colors = ['red','green','purple']
#for color in colors:
 #   print(color)

#for num in range(8):
 #   print(num)

#def add_numbers(a,b):
 #   sum = a + b
  #  print('do math')
   # return sum

def greet(person):
    return f"Hi there, {person}"

def divide(a,b):
    if type(a) is int and type(b) is int:
        return a/b
    return 'a and b must be integers'


def send_email(to_email, from_email, subject, body):
    email = f"""
        to: {to_email}
        from: {from_email}
        subject: {subject}
        ------------------
        body: {body}
    """
    print(email)

send_email(subject='Hi', from_email='bob@bob.com', to_email='tom@tom.com', body='Hey')


good_food = ['eggs', 'meat', 'milk']
meatloaf = ['meat', 'eggs', 'onion']

for food in meatloaf:
    if food in good_food:
        print('MEATLOAF')
    else:
        print(f'No {food}')


#Iterating over Dictionaries
dog = {'name': 'Sadie',
       'breed': 'mix',
       'age': 10,
       'leg_chart': {'front_left': 1,
       'front_right': 1,
       'back_legs': 2
    },
    'other_dogs': ['Abby', 'Amy']   
       }

for key in dog.keys():
    print(key)

for value in dog.values():
    print(value)

for pair in dog.items():
    print(pair)
    
    #(k)is for key and (v) is for value
for (k, v) in dog.items():
    print(k, '--->', v)

#Sets
languages = {'Javascript', 'Python', 'Java'}