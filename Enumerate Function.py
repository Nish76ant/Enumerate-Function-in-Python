#Enumerate Function

# l1 = ['Bhindi','Aloo','Chopstics','Chowmein']
# i = 1
# for item in l1:
#     if i%2 != 0:
#         print(f'Jarvis Please buy item {item} ')
#     i = i+1    

l1 = ['Bhindi','Aloo','Chopstics','Chowmein']

for index,item in enumerate(l1):
    if index%2 == 0:
        print(f'Jarvis Please buy {item}')
