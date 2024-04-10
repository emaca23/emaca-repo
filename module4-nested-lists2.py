cells = [['A1', 'B1', 'C1'], ['A2','B2','C2']]
for x in cells:
    print('Element', x)
    
cells = [['A1', 'B1', 'C1'], ['A2','B2','C2']]
for x in cells:
    for y in x:
        print('Element', y)

table = [['A1', 'B1', 'C1'], ['A2','B2','C2']]
for row in table:
    for cell in row:
        print(cell, '', end='')