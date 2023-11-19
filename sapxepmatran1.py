n,m,k=map(int,input().split())
matrix_input=input()
elements=matrix_input.split()
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
       element= int(elements[i*m+j])
       row.append(element)
    matrix.append(row)
matrix[k-1].sort()
string_matrix=" "
for row in matrix:
    string_row=' '.join(str(elements) for elements in row)
    string_matrix+= string_row+'\n'
print(string_matrix)
