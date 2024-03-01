# NOT competition style input
# read using f.read
# this is so we can 'run' as usual

from gear_class import Gear







options = '''
\nHere are your options:
(show) to show all items
(count) to count food items
(fuel) to total fuel
(heavy) to show id of any food > 10000
(tech) to create sublist of Mechanical and Fuel
(q) to quit
'''

choice = 'jjj'
while choice[0] != 'q':
    print(options)
    choice = input().lower()
    if choice == 'show':
        pass
    elif choice == 'count':
        pass
    elif choice == 'fuel':
        pass
    elif choice == 'heavy':
        pass
    elif choice == 'tech':
        pass



