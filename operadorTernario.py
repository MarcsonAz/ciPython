# video de material de python: https://www.youtube.com/watch?v=sjRrpEPY-SA
# dario radecic
# IF-ELIF-ELSE IN ONE LINE OF CODE

import sys
import timeit

def main():
# normal statement
    age = 18
    if age < 16:
        print('Go home!')
    elif 16 <= age < 18:
        print('Not sure...')
    else:
        print('Welcome!')

    print('-------with 1 option----------')
# 1
    if age < 18: print('Go home!')
 
    print('---------with a function-------------')
# 1.1
    def ps():
        print('Go home.')

    if age < 18: ps()

    print('-------with 2 options----------')
# 2
    outcome = 'Go home!' if age < 18 else 'Welcome!'
    print(outcome)

    print('------with the 3 options---------')
# 3
    outcome = 'Go home!' if age < 16 else 'Not sure...' if 16 <= age < 18 else 'Welcome!'
    print(outcome)

    print('--------inside a list!---------')
# 4
    li = ['+' if i > 4 else '-' for i in range(10)]
    print(li)

    print('--------list comprehension & dicts---------')
# 4
    students = [
    {'name': 'Mama', 'score': 71},
    {'name': 'Manu', 'score': 65},
    {'name': 'Marcson', 'score': 99},
    {'name': 'Marcos', 'score': 55}]

    def passed(name):
        return(f"{name} passed the exam!")

    def failed(name):
        return(f"{name} failed the exam!")    

    outcomes = [passed(st['name']) if st['score'] > 70 else failed(st['name']) for st in students]

    print(outcomes)

if __name__ == '__main__':
    main()