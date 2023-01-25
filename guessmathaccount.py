print('\n\n<<<< (n1) sign (X) = (n2) >>>>\n\n')

n1 = float(input('\ntype n1:'))
n2 = float(input('\ntype n2:'))

sum = float(n2 - n1)
mult = float(n2 / n1)
sub = float(sum-(sum*2))
div = float(1/mult)

print('\n\n',f'sum: {n1} + {sum} = {n2}','\n\n',f'multiplication: {n1} . {mult} = {n2}','\n\n',f'subtraction: {n1} - {sub} = {n2}','\n\n',f'division: {n1} / {div} = {n2}','\n\n')