import csv
filename = "/home/paindr/PycharmProjects/pythonProject1/database.csv"
champ =[]
database=[]
num_rows=[]
num_cols = []

with open(filename,'r')as csvfile:
    csvreader = csv.reader(csvfile)
    champ = next(csvreader)
    for row in csvreader:
        database.append(row)

print(champ[1:-1])


print(database[1:16])

num_rows = [int(j[3]) for j in database ]
num_cols = [int(j[2]) for j in database ]

'''Data stored  on the heap'''
fixed_data_size =[300]*len(num_rows)
Num_variable_cols = [0]*len(num_rows)
Max_var_size = [0]*len(num_rows)
Null_Bitmap =  [int(2+((j+7)/8)) for j in num_cols]

variable_data_size = [2+j*2+0  for j in Num_variable_cols  ]

#row size
k=0
Row_size =[]
while k<len(num_rows):
 Row_size .append( fixed_data_size[k]+variable_data_size[k]+Null_Bitmap[k]+4)
 k+=1
print(Row_size)

Rows_per_page=[]

k=0
while k<len(num_rows):
    Rows_per_page.append(8096/(Row_size[k]+2))
    k+=1

k=0

num_pages=[]
while k<len(num_rows):
 num_pages.append(num_rows[k]/Rows_per_page[k])
 k+=1

Heap_size = sum([j*8192  for j in num_pages])
print(f"la taille utilisée par la BD dans la Heap  est {Heap_size} octets")

'''Taille utilisée par la BD dans la  Leaf'''

Free_rows_per_page = []
k=0
Fill_factor=99
while k<len(num_rows):
    Free_rows_per_page.append(8096*((100-Fill_factor)/100)/(Row_size[k]+2))
    k+=1

NNum_Leaf_Pages = []
k=0
while k<len(num_rows):
    NNum_Leaf_Pages.append(num_rows[k]/(Rows_per_page[k]-Free_rows_per_page[k]))
    k+=1
Leaf_space_used=sum([8192*j for j in NNum_Leaf_Pages])

print(f"The space used by the database on the leaf level is {Leaf_space_used} bytes")

database_size = Leaf_space_used+Heap_size

print(f"The size of the database is {database_size*9.31*10**(-10)} Gb")