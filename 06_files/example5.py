with open('xxx.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')
    f.write('Line 4\n')
    f.write('The end!')

    sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
    f.write('\n'.join(sweets_list))