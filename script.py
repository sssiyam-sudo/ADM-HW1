
#-------------------Introduction-----------------------#

----#Say "Hello, World!" With Python
print("Hello, World!")


#-----Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n%2!=0):
    print ("Weird")
else:
    if (n in range(2,6)):
        print ("Not Weird")
    elif n in range(6,21):
        print ("Weird")
    elif n>20:
        print ("Not Weird")
        

#----------Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a+b)
    print (a-b)
    print (a*b)


#----------Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
     
    print(a//b)
    print(a/b)

#---------Loops
if __name__ == '__main__':
    n = int(input())
    for x in range(n):
        print(x**2)
       
#-------Write a function
def is_leap(year):
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    return leap
    
#----------Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")

        
        
        
#-----------------BASICS AND DATA TYPES-----------#
        
#--------Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    zes = max(arr)
    i=0
    while(i<n):
        if zes ==max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))


#--------Nested Lists
marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] 

        for a,c in sorted(marksheet):
             if c==b:
                    print(a)

     
#----------Finding The percentage
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    zes = max(arr)
    i=0
    while(i<n):
        if zes ==max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))





#----------Mean VAr Std
import numpy as np
n,m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)
b = np.array(b)

np.set_printoptions(legacy='1.13')
print(np.mean(b, axis = 1))
print(np.var(b, axis = 0))
print(np.std(b))

        
#---------------------STRING----------------------
#-----String Split and Join
def split_and_join(line):
    a=line.split(" ")
    
    result="-".join(a)
    return result


#------Whats your name
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(a, b):
    print("Hello %s %s! You just delved into python."%(a,b))


#-------Mutation
def mutate_string(string, position, character):
    list2=list(string)
    list2[position]=character      
    return ''.join(list2)



#------Find a string
def count_substring(string, sub_string):

    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count

#-------String validators
S = raw_input()
print any([char.isalnum() for char in S])
print any([char.isalpha() for char in S])
print any([char.isdigit() for char in S])
print any([char.islower() for char in S])
print any([char.isupper() for char in S])

#--------Text alignment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#------text wrap

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result=string[i:i+max_width]
        if len(result)==max_width:
            print(result)
        else:
            return(result)



#------Designer door mat

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result=string[i:i+max_width]
        if len(result)==max_width:
            print(result)
        else:
            return(result)



#-----String formatting
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))

#-------Alphabet rangoli
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))

#-------Capitalize


# Complete the solve function below.
def solve(s):
    a= s.title()
    return a

#-------The minion game
def minion_game(string):
    # your code goes here
    
    vw = 'aeiou'.upper()
    strl = len(string)
    kevin = sum(strl-i for i in range(strl) if string[i] in vw)
    stuart = strl*(strl + 1)/2 - kevin

    if kevin == stuart:
        print ('Draw')
    elif kevin > stuart:
        print ('Kevin %d' % kevin)
    else:
        print ('Stuart %d' % stuart)



#------Merge the tools
def merge_the_tools(string, k):
    # your code goes here
    
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0
            
            
            
#---------------------------SETS-------------------

#------No Idea
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))

#------Symmetric difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    N = int(input().strip())
    stamps = set()
    
    for _ in range(N):
        stamp = input().strip()
        stamps.add(stamp)
        
    print(len(stamps))

#-------Set add
if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split())) 
    num_cmds = int(input())
    
    for _ in range(num_cmds):
        cmd = list(input().strip().split(' '))
        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
    
    print(sum(s))

#------set discard
if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split())) 
    num_cmds = int(input())
    
    for _ in range(num_cmds):
        cmd = list(input().strip().split(' '))
        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
    
    print(sum(s))

#-----set union
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
eng = set(map(int,input().split()))
b = input()
fre = set(map(int,input().split()))
print(len(eng.union(fre)))

#------set intersection
# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
eng = set(map(int,input().split()))
f = int(input())
fre = set(map(int,input().split()))
print(len(eng & fre))

#-----setdiffernce
# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng - fre))

#-----set symmetric difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng ^ fre))
#----check subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng ^ fre))

#-------check strict superset
#------
# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng ^ fre))
        
        
        
#--------------MATH-------------------#
#-----Finding angle abc
# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm
#let, 
b = mc
c = bm
a = bc
#where b=c
angel_b_radian = math.acos(a / (2*b))
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
output_str = str(angel_b_degree)
print(output_str)


#--------Triangle Quest

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
     print((10 ** i - 1) ** 2 // 81)



#--------Mod Divmod
# Enter your code here. Read input from STDIN. Print output to STDOUT
d = divmod(int(input()), int(input()))
print(*d, d, sep='\n')


#----------Pwer mod power
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, m = [int(input()) for _ in range(3)]
print(pow(a, b), pow(a, b, m), sep='\n')


#------integer comes in all size
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, c, d = [int(input()) for _ in range(4)]
print(a ** b + c ** d)


#-----Triangle quest
for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * ((pow(10, i) - 1) // 9))

        
        
        
        
        
#------------------Collections----------------------
#--------DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

D = defaultdict(list)
n, m = map(int, input().split())

for i in range(n):
    D[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(D[input()]) or -1)


#-------Collections.namedtupl
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))


#-----collectionsOrderes
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

order = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    order[item] = order.get(item, 0) + int(price)
for item, price in order.items():
    print(item, price)

#------Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

dict = OrderedDict()

for _ in range(int(input())):
    key = input()
    dict[key] = dict.get(key, 0) + 1

print(len(dict))
print(*dict.values())

#------Collection deque
#!/bin/python3

import math
import os
import random
import re
import sys
import collections

s = sorted(input().strip())
s_counter = collections.Counter(s).most_common()

s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])

#--------Company logo
# Enter your code here. Read input from STDIN. Print output to STDOUT
  
for t in range(int(input())):
    l = int(input())
    sides = list(map(int, input().split()))
    i = 0
    while i < l - 1 and sides[i] >= sides[i + 1]:
        i += 1
    while i < l - 1 and sides[i] <= sides[i + 1]:
        i += 1
    print('Yes' if i == l - 1 else 'No')

#--------Pilling up     
# Enter your code here. Read input from STDIN. Print output to STDOUT
  
for t in range(int(input())):
    l = int(input())
    sides = list(map(int, input().split()))
    i = 0
    while i < l - 1 and sides[i] >= sides[i + 1]:
        i += 1
    while i < l - 1 and sides[i] <= sides[i + 1]:
        i += 1
    print('Yes' if i == l - 1 else 'No')
   
  
  
#-----------------Calender Module-----------------#
#---Calender moduòe# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())


#----Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.

def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs((t1-t2).total_seconds())))   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

        
        
        
        
#-----------------------ERRORS AND EXCEPTION----------------------#

#---------Incorrect Rogex
#----------Exc3ption
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)

        
        
#---------------REGEX AND PARSING-------------#
#------Re.split
regex_pattern = r'[.,]+'

#-----Group, Groups, Groups dict
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(m.group(1) if m else -1)

#-----Refindal and Re Findter
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', input(), flags=re.I)
print('\n'.join(match or ['-1']))

#-----Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)

#-----Validating Roman Numerals
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)


#-----Validatin and Parsing Email address
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

#------Hex color code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')

#------HTML PArser Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        print ('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())



#-----HTML Parser Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')

        print(comment)

    def handle_data(self, data):
        if data == '\n': return
        print('>>> Data')
        print(data)


html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#------Detect html tags
# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#------validating uid
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
#------validating postal codes
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
#------Matrix script
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

