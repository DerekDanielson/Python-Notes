#Lists***********
vegan_no_nos = ['eggs', 'meat', 'milk', 'figs']

pie_ingredients = ['flour', 'apples', 'sugar', 'eggs', 'salt']

for food in pie_ingredients:
    if food in vegan_no_nos:
        print(f"Oh no, I cannot eat {food}!")
    else:
        print(f"Yum, I love {food}!")

#Yum, I love flour!
#Yum, I love apples!
#Yum, I love sugar!
#Oh no, I cannot eat eggs!
#Yum, I love salt!



special_chars = "$%#&@"

"#" in special_chars
#True

"!" in special_chars
#False



#RETRIEVING BY INDEX**********
vegan_no_nos[0]
#'eggs'

vegan_no_nos[2]
#'milk'

#COUNT BACKWARDS
vegan_no_nos[-3]
#'meat'


#CHANGE INDEX*******************
vegan_no_nos[2] = 'dairy'

vegan_no_nos 
#['eggs', 'meat', 'dairy', 'figs']


vegan_no_nos[4] = 'butter'
#IndexError: list assignment index out of range


#LIST SLICING***********
vegan_no_nos[0:4:2]
#['eggs', 'milk']


nums = list(range(0,100,1))
nums #[1, 2, 3, 4, 5, 6, etc to 99]

nums[90:]
#[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

nums[90::2]
#[90, 92, 94, 96, 98]

nums[:10]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[:10:5]
#[0, 5]

nums[::10]
#[10, 20, 30, 40, 50, 60, 70, 80, 90]

nums[::-10]
#[99, 89, 79, 69, 59, 49, 39, 29, 19, 9]

#**nums will still stay the same (1-99).  
#Have to variable
#Ex. 
reversed_nums = nums[::-10]
reversed_nums 
#[99, 89, 79, 69, 59, 49, 39, 29, 19, 9]

nums[20:10:-1]
#[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]



#LIST SPLICING***************
#Can assign a list to a splice:
alpha = ['a', 'b', 'c', 'd', 'e']
#['a', 'b', 'c', 'd', 'e']

alpha[2:] = ['y', 'z']
print(alpha)
#['a', 'b', 'y', 'z']

alpha[1:3] = []
print(alpha)
#['a', 'z']


colors = ['red', 'orange', 'yellow']

colors[0:1] = ['dark red', 'pink']

colors
#['dark red', 'pink', 'orange', 'yellow']

colors[3:] = ['dark yellow', 'green', 'blue', 'purple']

colors
#['dark red', 'pink', 'orange', 'dark yellow', 'green', 'blue', 'purple']

colors[5:] = []

colors
#['dark red', 'pink', 'orange', 'dark yellow', 'green']



#LIST METHODS**********
#dir(list) - For list of methods
#CORE API

# l.append(x) - Add X to end of list
# l.copy() - Return shall copy of list l
# l.count(x) - Return # times X appears in l
# l.extend(l2) - Add items of l2 to l
# l.index(x) - Return (0-based) index of X in l
# l.insert(i, x) - Insert X at position l
# l.pop(i) - Remove & return item at l(default last)
# l.reverse() - Reverse list (change in place)
# l.sort() - Sort list in place

chickens = ['butters', 'lady gray', 'stevie chicks']
chickens
#['butters', 'lady gray', 'stevie chicks']
len(chickens)
#3

#APPEND
chickens.append('henry')
chickens
#['butters', 'lady gray', 'stevie chicks', 'henry']

#COPY
copy_chickens = chickens.copy()
#Makes copy of chickens

#COUNT
#How many times a certain element appears in list
chickens.count('butters')
#1

binary = [1, 0, 1, 0, 0, 1, 1, 0]
binary.count(0)
#4

#EXTEND
#Adds items of one list to another
chicks = ['herbert', 'annabelle']

chickens.extend(chicks)
chickens
#['butters', 'lady gray', 'stevie chicks', 'henry', 'herbert', 'annabelle']

#INDEX
#Tells you index of element
'henry' in chickens
#True     --Does not show index

chickens.index('henry')
#3

#INSERT
#Adds element at specified index
chickens.insert(0, 'tina')
chickens
#['tina', 'butters', 'lady gray', 'stevie chicks', 'henry', 'herbert', 'annabelle']

#POP
#Remove & return item at i - default is last element
chickens.pop()
#'annabelle'

chickens.pop(0)
#['butters', 'lady gray', 'stevie chicks', 'henry', 'herbert', 'annabelle']
#tina has been removed

#REVERSE
#Reverse list (change in place)
chickens.reverse()
chickens
#['annabelle', 'herbert', 'henry', 'stevie chicks', 'lady gray', 'butters']

#SORT
#Sorts list in place
chickens.sort()
#will sort chickens alphabetically
num = [1, 3, 5, 2, 4]
num.sort()
#[1, 2, 3, 4, 5]

#help(list.sort)

num.sort(reverse=True)
num
#[5, 4, 3, 2, 1]


#STRINGS CONTINUED**********
#Immutable sequence of characters (like JS)
#Can use '', " ", or """ """
#""" """ is used in 2 scenerios:
# 1. When you want a multiple line string,
#    and type it exactly as it should look

# 2. Create doc strings for functions or   #    classes
# 
# f strings are formatted strings
# Like JS string template literals
price = 3.50
qty = 7
print(f"Your total is {price * qty}") 
#Your total is 24.5

str(5.6)
# '5.6'  - Can turn numbers into strings

nums = [3,4,5]
str(nums)
# '[3, 4, 5]'

#Membership/ Substrings
#Can use *in* for membership:
'3' in nums
#True

'8' in nums
#False

#Can slice to retrieve substring 
# ("apple"[1:3] == "pp")
#   Cannot splice; strings are immutable!

#Multiply string
'^' * 10
# '^^^^^^^^^^'

msg = 'hellohihey'
msg
# 'hellohihey'

len(msg)
# 10

#SPLICING
msg[5:]
# 'hihey'

msg[0:5]
# 'hello'

msg[::2]
# 'hloie'


for char in msg:
    print(char)
# h
# e
# l
# l
# o
# h
# i
# h
# e
# y


#STRING METHODS*********

dir(str)

#    CORE API
#
# s.count(t) - Returns # of times t occurs in s
# s.endswith(st) - Does s end with string t?
# s.find(t) - Index of first occurence of t in s (-1 for failure)
# s.isdigit() - Is s entirely made up of digits?
# s.join(seq) - Make new string of seq joined by s ("|".join(nums))
# s.lower() - Return lowercased copy of s
# s.replace(t, count) - Replace count (default: all) occurrences of t in s
# s.split(sep) - Return list of items made from splitting s on sep
# s.splitlines() - Split s at newlines
# s.startswith(t) - Does s start with t?
# s.strip() - Remove whitespace at start/end of s


#COUNT
msg
# hellohihey
msg.count('h')
# 3
msg.count('H')
# 0


#ENDSWITH
msg.endswith('y')
# True
msg.endswith('!')
# False
msg.endswith('ey')
# True


#STARTSWITH
person = "Mr. Jones"
person.startswith('Mr.')
# True
person.startswith('M')
# True


#FIND
#Finds the first occurrence of some string
person.find('J')
# 4


#ISDIGIT
'hello4'.isdigit()
# False
'456'.isdigit()
# True


#JOIN
"|".join(chickens)
# 'annabelle|herbert|henry|stevie chicks|lady gray|butters'
"@".join('LOL')
# 'L@O@L'


#LOWER
"LOL".lower()
# 'lol'

#UPPER
"bikes".upper()
# 'BIKES'

'ms kitty'.capitalize()
# 'Ms kitty'

'LOL'.isupper()
# True

'LOl'.isupper()
# False

'lol'.islower()
# True

'loL'.islower()
# False


#REPLACE
things = 'apples-tomatoes-pickles'
things.replace('-', '&')
'apples&tomatoes&pickles'

things.replace('-', '&', 1)
# 'apples&tomatoes-pickles'

text = 'I hate you so much'
text.replace('-', '...')
# 'I...hate...you...so...much'

text.replace('hate', '')
# 'I......you...so...much'


#SPLIT
animals = 'goats,chickens,ducks,pigs,alpacas'
animals.split(',')
# ['goats', 'chickens', 'ducks', 'pigs', 'alpacas']

text.split('...')
# ['I', 'hate', 'you', 'so', 'much']

list('YOLO')
# ['Y', 'O', 'L', 'O']

"""
Hello
I
Love
You
""".splitlines()
# ['', 'Hello', 'I', 'Love', 'You']

#STRIP
user_input = '     catlady    '
user_input.strip()
# 'catlady'



#DICTIONARIES********
# Python dictionaries are data structures
# that store data as 'an unordered  
# collective
# of key:value pairs'

# Key-value pair data structures
# Mutable, ordered mapping of keys -> values
# O(1) runtime for adding, retrieving, 
# deleting items (like JS object or Map)

person = {'first':'henry'}

#Making Dictionaries
fruit_colors = {
    'apple':'red',
    'berry':'blue',
    'cherry':'red',
}

# Values can be any type
# Keys can be any 'immutable type'
chicken = {'name': 'butters', 'age': '6 months', 'breed': 'silkie'}

stuff = {True: 34, 100: 'AWESOME'}

#MEMBERSHIP & RETRIEVAL
# in Checks for membership of key 
# ('apple' in fruit_colors)

'breed' in chicken
# True
'butters' in chicken
# False    ---ONLY LOOKS FOR KEYS
'name' in chicken
# True

# [] Retrieves item by key 
# (fruit_colors['apple])
#    Cannot use dot notation
#    (no  fruit_colors.apple)

chicken['breed']
# 'silkie'
chicken['age']
# '6 months'

chicken['age'] = 12
# age is updated to 12

chicken.get('weight', '2 lbs')
# '2 lbs'
# 'weight' isnt in dictionary, so we can 
# add a default value ('2 lbs')


dict()
# {}  - Creates new empty dictionary
# You can just type {} as well
dict([[True, 0], [False, 1]])
# {True: 0, False: 1}


#ITERATING(Looping over)DICTIONARIES******
chicken = {'name': 'Lady Gray',
    'breed': 'Silkie', 
    'total_egg_count': 12,
    'egg_chart': {
        'M': True,
        'T': True,
        'W': True,
        'TH': True,
        'F': True,
        'S': False,
        'SU': True
    },
    'coop_mates': ['Butters', 'Stevie', 'Henry']
}
# ^^^^^^^Chicken is a dictionary, 
# 'Egg_chart' is a dictionary as a value, 
# 'coop_mates' is a list in dictionary

# Iterate over the Keys:
chicken.keys()
# dict_keys(['name', 'breed', 'total_egg_count', 'egg_chart', 'coop_mates'])

# For loop iterating over keys
for key in chicken.keys():
    print(key)
# name
# breed
# total_egg_count
# egg_chart
# coop_mates

# Iterate over values:
chicken.values()
# dict_values(['Lady Gray', 'Silkie', 12, {'M': True, 'T':True, 'W':True, 'Th': True, 'F': True, 'S':False, 'SU': True}, ['Butters', 'Stevie', 'Henry']])

for value in chicken.values():
    print(value)
# Lady Gray
# Silkie
# 12
# {'M': True, 'T':True, 'W':True, 'Th': True, 'F': True, 'S':False, 'SU': True} ['Butters', 'Stevie', 'Henry']

# Items method
chicken.items()
# dict_items([('name', 'Lady Gray'),    
# ('breed', 'Silkie'), ('total_egg_count', # '12'), ('egg_chart', {'M': True, 'T': 
# True, 'W': True, 'TH': True, 'F': True, 
# 'S': False, 'SU': True}), ('coop-mates',  # ['Butters', 'Stevie', 'Henry'])])
#^^^^^^^Gives us a dict items() collection, 
#which consists of pairs(called the tuple)

for pair in chicken.items():
    print(pair)
# "Key" and "Value" are printed:
# ('name', 'Lady Gray')
# ('breed', 'silkie')
# ('total_egg_count', 12)
# ('egg_chart', {'M': True, 'T': True, 'W': # True, 'TH': True, 'F': True, 'S': False, # 'SU': True})
# ('coop_mates', ['Butters', 'Stevie', 
# 'Henry'])

# UNPACK VALUES
#  "Key", "Value" - Can be anyname
for (k, v) in chicken.items():
    print(k, '--->', v)
# name ---> Lady Gray
# breed ---> Silkie
# total_egg_count ---> {'M': True, 'T': 
# True, 'W': True, 'TH': True, 'F': True, 
# 'S': False, 'SU': True}
# coop_mate ---> ['Butters', 'Stevie', 'Henry']


# Dictionaries are ordered by insertion 
# order (Order stays the same)



# DICTIONARY METHODS *************







# Set() *************************
# Use {}, but with only keys, not key: value
#Sets do not have duplicate elements
#Do not accept immutables
#Sets are iterable
#Faster runtime than Lists
languages = {'ruby', 'python', 'javascript'}
#{'ruby', 'python', 'javascript'} - creates set of elements

# Can use constructor function to make set from iterable:
voted_languages = ['ruby', 'python', 'javascript', 'scala', 'ruby', 'python', 'python', 'scala']

set(voted_languages)
#{'javascript', 'python', 'ruby', 'scala'}

# Turn string into set
set('#$%^#$')
#{'#', '$', '%', '&'}

things = {3, 'snake', 'mario', True, [1,2,3]}
#Error - Unhasable type: 'list'
things = {3, 'snake', 'mario', True}
#{3, True, 'mario', 'snake'}

# Sets_Methods
# Use 'in' for membership check:
'scala' in languages
#False

'ruby' in languages
#True

# Core API
# s.add(x)    - Add item x to s
# s.copy()    - Make new copy of s
# s.pop()     - Remove & return arbitrary item from s
# s.remove(x) - Remove x from s

# Add
languages.add('scala')
languages
#{'javascript', 'python', 'ruby', 'scala'}


# Pop
languages.pop()
#'scala'

languages
#{'javascript', 'python', 'ruby'}


# Remove
languages.remove('javascript')
languages
#{'python', 'ruby'}


# Copy
copy = languages.copy()
copy
#{'python', 'ruby'}


# Set Operations

moods = {'happy', 'sad', 'grumpy'}
dwarfs = {'happy', 'grumpy', 'doc'}

moods | dwarfs   #union: {'happy', 'sad', 'grumpy', 'doc'}
moods & dwarfs   #intersection: {'happy', 'grumpy'}
moods - dwarfs   #difference: {'sad'}
dwarfs - moods   #difference: {'doc'}
moods ^ dwarfs   #symmetric difference: {'sad', 'doc'}


# Tuples
# An immutable data structure, used a lot.
# Ordered sequence (like a list, but immutable)

#Making Tuples
t1 = (1, 2, 3)
t2 = ()    # empty tuple
t3 = (1,)  # one-item tuple: Note trailing comma

colors = ('red', 'yellow', 'green')

type(colors)
#tuple

len(colors)
#3

(1, True, (1,2), [])
#(1, True, (1, 2), [])
# Can't change or remove or add any values to this tuple

#Can make an empty tuple, just with empty parentheses
()
#()

# To create a one item tuple, need to add comma after item
tup = (3,)
#(3)

# Can use constructor function to make tuple from iterable:
ids = [1, 12, 44]
t_of_ids = tuple(ids)

#list to tuple
tuple([1,2,3,4])
#(1,2,3,4)

# TIC-TAC-TOE
board = {
    (0,0): 'X',
    (0,1): None,
    (0,2): 'O',
    (1,0): 'X',
    (1,1): 'O'
}

board
#{(0,0): 'X', (0,1): None, (0,2): 'O', (1,0): 'X', (1,1): 'O'}

board[(1,0)]
#'O'

board[(0,0)]
#'X'

(1,2,3,1,2,1).count(1)
#3

(1,2,3,1,2,1).index(3)
#2  - first index of 3

(1,2,3,1,2,1).index(1)
#0


# LIST COMPREHENSIONS ************
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#Make a new list of even numbers without Comprehensions
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)
#[2, 4, 6, 8, 10, 12]

#Make a new list with Comprehensions
#Filtering into list
evens = [num for num in nums if num % 2 == 0]

evens
#[2, 4, 6, 8, 10, 12]

odds = [num for num in nums if num % 2 == 1]

odds
#[1, 3, 5, 7, 9, 11, 13]


[num * 2 for num in nums]
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]


['HIIII' for num in nums]
#['HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII',
# 'HIIII', 
# 'HIIII',
# 'HIIII']

# ******* [what_to_append for thing in list]

#Square
[n * n for n in [2,4,6,8]]
#[4,16,36,64]

[char for char in 'lmfao']
#['l', 'm', 'f', 'a', 'o']

[char.upper() for char in 'lmfao']
#['L', 'M', 'F', 'A', 'O']

[char.upper() + '.' for char in 'lmfao']
#['L.', 'M.', 'F.', 'A.', 'O.']

[num for num in range(10,20)]
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# MORE COMPREHENSIONS *************
# Mapping Into List
doubled = []

for num in nums:
    doubled.append(num + 2)

# You can say instead:
doubled = [num * 2 for num in nums]

#Nesting
[x for x in range(3)]
#[0, 1, 2]

[[] for x in range(3)]
#[[], [], []]

[[0 for y in range(3)] for x in range(3)]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

[[None for y in range(3)] for x in range(3)]
#[[None, None, None], [None, None, None], [None, None, None]]


def gen_board(size, initial_val=None):
    return[[initial_val for x in range(size)] for y in range(size)]

gen_board(3)
#[[None, None, None], [None, None, None], [None, None, None]]

gen_board(5)
#[[None, None, None, None, None], 
# [None, None, None, None, None], 
# [None, None, None, None, None],
# [None, None, None, None, None],
# [None, None, None, None, None]]

gen_board(5, 0)
#[[0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]]


#Can combine this mapping and filtering:
doubled_evens = [n * 2 for n in nums if n % 2 == 0]


[x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[x for x in range(10) if x % 2== 0]
#[0, 2, 4, 6, 8]

[x * 2 for x in range(10) if x % 2 == 0]
#[0, 4, 8, 12, 16]

chickens = [
    {'name': 'Henry', 'sex': 'Rooster'},
    {'name': 'Lady Gray', 'sex': 'Hen'},
    {'name': 'Junior', 'sex': 'Rooster'},
    {'name': 'Stevie Chicks', 'sex': 'Hen'},
    {'name': 'Rocket', 'sex': 'Hen'},
    {'name': 'Butters', 'sex': 'Rooster'}
]
#List of just hens:
hens = [bird['name'] for bird in chickens if bird['sex'] == 'Hens']
hens
#['Lady Gray', 'Stevie Chicks', 'Rocket']

scores = [55, 89, 99, 87, 60, 70, 74, 76, 90, 50, 82]
grades = ['PASS' for score in scores if score >= 70]
#['PASS', 'PASS', 'PASS', 'PASS', 'PASS', 'PASS', 'PASS', 'PASS']


#IF AND ELSE
grades = ['PASS' if score >= 70 else 'FAIL' for score in scores]
#['FAIL',
# 'PASS',
# 'PASS',
# 'PASS',
# 'FAIL',
# 'PASS',
# 'PASS',
# 'PASS',
# 'PASS',
# 'FAIL',
# 'PASS']



# DICTIONARY AND SET COMPREHENSIONS
#Can make lists via comprehensions from any kind of iterable:

#Dictionary Comprehension:
{day:0 for day in 'MTWRFSU'}
#{'M': 0, 'T': 0, 'W': 0, 'R': 0, 'F': 0, 'S': 0, 'U': 0}


{num: num * num for num in range(1,10)}
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

{num: num * num for num in range(1,10) if num % 2 == 0}
#{2: 4, 4: 16, 6: 36, 8: 64}

# SET COMPREHENSION
{day for day in 'MTWRFSU'}
#{'F', 'M', 'R', 'S', 'T', 'U', 'W'}

{char for char in 'abracadabra'}
#{'a', 'b', 'c', 'd', 'r'}


{char for char in 'hello darkness my old friend'}
#{' '. 'a', 'd', 'e', 'f', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'r', 's', 'y'}

{char for char in 'hello darkness my old friend' if char in 'aeiou'}
#{'a', 'e', 'i', 'o'}

{char for char in 'hello darkness my old friend' if char not in 'aeiou'}
#{' ', 'd', 'f', 'h', 'k', 'l', 'm', 'n', 'r', 's', 'y'}


# PYTHON TOOLS & TECHNIQUES ***********

# UNPACKING - Can "unpack" iterables ********
names = ['charlie', 'lucy']
name1, name2 = names

name1
#'charlie'
name2
#'lucy'

point = (100, 58)
x,y = point

x
# 100
y
# 58


# Can gather the rest using * before variable:
sorted_scores = [2400, 2350, 2100, 1960]
top_score, *scores = sorted_scores

top_score
# 2400
scores
# [2350, 2100, 1960]
sorted_scores
# [2400, 2350, 2100, 1960]  -  Stays the same

first_name = 'Xander'
initial, *rest = first_name

initial
# 'X'
rest
# ['a', 'n', 'd', 'e', 'r']

point = (40,50,20)
x,y,z = point

x
# 40
y
# 50
z
# 20

(x,y,z) = (40,50,20)


color_pairs = [['red', 'green'], ['purple', 'orange']]
pair1, pair2 = color_pairs

pair1
# ['red', 'green']
pair2
# ['purple', 'orange']

((primary1, secondary1), (primary2, secondary2)) = color_pairs
primary1
#'red'
secondary1
#'green'
primary2
#'purple'
secondary2
#'orange'

grades = {
    'A': 12,
    'B': 19,
    'C': 30
}

for pair in grades.items():
    print(pair)
#('A', 12)
#('B', 19)
#('C', 30)

for (k,v) in grades.items():
    print(k,v)
#A 12
#B 19
#C 30


# SPREADING(packing) *******
# Can "spread" iterables
nums = [2,4,6,8]
[*nums]
#[2,4,6,8]

[-2,0,*nums]
#[-2, 0, 2, 4, 6, 8]

odds = [1,3,5,7,9]  

[*odds, *nums]
#[1, 3, 5, 7, 9, 2, 4, 6, 8]

['hello']
#['hello']
[*'hello']
#['h', 'e', 'l', 'l', 'o']

{*'hello'}
#{'e', 'h', 'l', 'o'}
{*'hello', 45}
#{45, 'e', 'h', 'l', 'o'}

rainfall = {'Jan': 2.5, 'Feb': 4.9}

{*rainfall}
{'Feb', 'Jan'}

# Have to use ** to spread a dictionary
{'Dec': 0.5, **rainfall}
#{'Dec': 0.5, 'Jan': 2.5, 'Feb': 4.9}

print(2,3,4,5,6)
#2 3 4 5 6
nums = [1,2,3,4,5,6,7,8,9]
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*nums)
#1 2 3 4 5 6 7 8 9

print(*'hello')
#h e l l o


# ERROR HANDLING ************
# Catching Errors
def get_days_alive(person):
    days = person['age'] * 365
    print(f'You have been alive for {days} days')

get_days_alive({'age': 50})
#You have been alive for 18250 days

# TRY & EXCEPT
def get_days_alive(person):
    try:
        days = person['age'] * 365
        print(f'You have been alive for {days} days')
    except:
        print('ERROR')

get_days_alive({}) # <---No age entered
#'ERROR'

# COMMON EXCEPTION TYPES ***********

# AttributeError - Couldn't find attr: o.missing
# KeyError       - Couldn't find key: d['missing']
# IndexError     - Couldn't find index: lst[99]
# NameError      - Couldn't find variable: not_spelled_right
# OSError        - Operating system error: can't read/write file, etc
# ValueError     - Incorrect value (tried to convert "hello" to int, etc)

def get_days_alive(person):
    try:
        days = person['age'] * 365
        print(f'You have been alive for {days} days')
    except KeyError:
        print('Missing key: age')
    except:
        print('SOMETHING ELSE WENT WRONG')

get_days_alive({})
#Missing key: age
get_days_alive(1)
#SOMETHING ELSE WENT WRONG


def get_days_alive(person):
    try:
        days = person['age'] * 365
        print(f'You have been alive for {days} days')
    except KeyError as exc:
        print('EXC =>', exc)
        print('Missing key: age')
    except:
        print('SOMETHING ELSE WENT WRONG')

get_days_alive({'age': 19})
#EXC => 'name'
#Missing key: age


# RAISING EXCEPTIONS ************
#Common to raise exceptions when the code is running and then examine why #its not working by looking at the exception

# COMMON EXCEPTION TYPES

# AttributeError - Couldn't find attr: o.missing
# KeyError       - Couldn't find key: d["missing"]
# IndexError     - Couldn't find index: lst[99]
# NameError      - Couldn't find variable: not_spelled_right
# OSError        - Operating system error: can't read/write file, etc
# ValueError     - Incorrect value (tried to convert "hello" to int, etc)

# use "raise" keyword then some exception like listed above
raise ValueError('I dont like that value')
# ValueError: I dont like that value

# Raise exception when you know it shoulde be an error
def bounded_avg(nums):
    "Return avg of nums (makes sure nums are 1-100)"

    for n in nums:
        if n < 1 or n > 100:
            raise ValueError("Outside bounds of 1-100")

    return sum(nums) / len(nums)

bounded_avg([1,2,3,3,88,99]) 
# 32.6666666666664
bounded_avg([3,8,69,72,103])
# ValueError: Outside bounds of 1-100


def handle_data():
    #"Process data from database"

    ages = [10,40,50,99,103,2,0]
    
    try: 
        avg = bounded_avg(ages)
        print("Average was", avg)

    except ValueError as exc:
        # exc is exception object -- you can examine it!
        print("Invalid age in list of ages")



# DOCTESTS ***************
# ************* TEST YOUR CODE REGULARLY!!!!!!!!!!! *************
# doctests, built-in testing function

def bounded_avg(nums):       
    """returns average of list of nums (nums must be between 1-100)""" #docstring
    for n in nums:                     
        if n < 1 or n > 100:
            raise ValueError("Outside bounds of 1-100")  

    return sum(nums) / len(nums)
# Can do "help(bound_avg)" in python and itll show the docstring

# Doctests are snippets of interactive demonstration in a docstring:

def bounded_avg(nums):
    """Return avg of nums (makes sure nums are 1-100}
        
        >>> bounded_avg([2, 4, 6])  ###### <== Function call and some input
        4.0                         ###### <== Expected return value

        >>> bounded_avg([1, 2, 101])
        Traceback (most recent call last):
            ...
        ValueError: Outside bounds of 1-100
    """

    for n in nums:
        if n < 1 or n > 100:
            raise ValueError("Outside bounds of 1-100")
    
    return sum(nums) / len(nums)

# RUN TEST IN PYTHON ****************
# $ python3 -m doctest -v your-file.py
# doctest is a module (-m) and verbose((-v)gives more info about the test)

# OUTPUT FROM RUNNING TEST FILE:
# Trying:
#   bounded_avg([2,4,6])
# Expecting:
#   4.0
# ok



# PYTHON STANDARD LIBRARY AND IMPORTING **********
# standard library of Python (std lib) - native library
# NEED TO IMPORT TO USE!!!!
import math
import random

# Can rename when importing using "as"
from random import choice as pick_one, randint

pick_one('asdgqwet')
#'d'


# SHARING CODE BETWEEN FILES **********************
# Use the "import" keyward all the time when you want to utilize code that # is in a file outside of the file you are currently using.  

# 1st file:
# score.py
def get_high_score():
    ...
def save_high_score():
    ...

# 2nd file:
# game.py
from score import get_high_score

high = get_high_score()

# Example 2:
# 1st file
# helpers.py:
from random import randint, choice

def get_rand_year():
    return randint(1900, 2020)

def get_rand_month():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',  
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return choice(months)

get_rand_month()
# 'Sep'
get_rand_month()
# '1942'

# 2nd file
# people.py:
import helpers   #Or from helpers import get_rand_year, get_rand_month

def make_person(name, favColor):
    return {
        'name': name,
        'favColor': favColor,
        'birth_year': helpers.get_rand_year(),
        'birth_month': helpers.get_rand_month()
    }

make_person('Tom', 'purple')
# {'name': 'Tom',
#  'favColor': 'purple',
#  'birth_year': 1965,
#  'birth_month': 'Jun'}



# INSTALLING 3RD PARTY LIBRARIES *************
# USE "Pip" to install a new package
pypi.org  #The python package index *******************

pip3 install forex-python

pip3 list  #Will show different libraries that have been installed

from forex_python.converter import convert

convert("USD", "GBP", 10)
#7.6543


# INTRO TO VIRTUAL ENVIRONMENTS **************
cd my-project-directory
python3 -m venv venv
#using 'venv'(virtual environment) module, make a folder, venv, with all #the needed stuff
# This makes a virtual environment folder

source venv/bin/activate
# Start virtual environment

#INSTALL LIBRARY IN VIRTUAL ENVIRONMENT
pip install Faker

# LEAVE VIRTUAL ENVIRONMENT
# Use "deactivate"




# OBJECT ORIENTED PROGRAMMING ***********
# class:
#   -blueprint for new objects, define attributes & methods

# method:
#   -function defined on class, can see/change attributes on instance

# class method:
#   -function defined on class, called on class, not individual instance





































































































































































































































































































































































































































































































































































































