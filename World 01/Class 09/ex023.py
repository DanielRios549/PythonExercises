'''
    Get a number from 0 to 9999 and show all the digits separately
'''
number = int(input('input a number: '))

print(f'''Unit: {number // 1 % 10}
Ten: {number // 10 % 10}
Hundred: {number // 100 % 10}
Thousand: {number // 1000 % 10}
''')
