'''
    Show a countdown to the fireworks, from 10 to 0 with a break of 1 second between them
'''
from time import sleep
from emoji import emojize

for count in range(10, 0, -1):
    print(count)
    sleep(1)

print('{0} \33[32mHAPPY NEW YEAR!\33[m {0}'.format(emojize(":fireworks:", use_aliases=True)))
