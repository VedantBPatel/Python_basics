#Jump Statements
"""
Loop control statements are the statements that change execution from its normal sequence.
It consists total of 3 statements:
1.Break: Brings the control out of the loop when some external condition is triggered.
2.Continue:It forces to execute next iteration of the loop skippping the current one.
3.Pass:Used to write empty loops and also for empty control statement, functoin and classes.
"""


#Combined Example:
s="Parul University"
for letter in s:
    if letter =='e' or letter == 's':
        break
    print(letter,end = " ")#end is used to replace default newline '\n' with some space or any character to keep it in same line.
print()#just to add some verticle spacing.. 

for letter in s:
    if letter == 'e' or letter == 's':
        continue
    print(letter, end=" ")
print()

for letter in s:
    if letter == 'e' or letter == 's':
        pass
    print(letter,end=" ")
print()
