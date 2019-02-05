def count_a(s):
    '''counting the number of a in the sequence'''


    result= 0
    for b in s:
        if b == 'A':
            result += 1

    return result



'''Main program'''

s= 'AGTGCTAGCTCAGA'
count_a(s)
na= count_a(s)
print(' the number of A is: {}'.format(na))

tl= len(s)


porcentaje= round((na/len(s)) * 100, 1)

print("the total lenght", tl)
print('the porcentage', porcentaje)



