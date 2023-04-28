arr_list=([1,1,2,2,2,3,3])

largest=arr_list[0]
for x in range(0,len(arr_list)):
    if arr_list[x]>largest:
        largest=arr_list[x]


sec_largest=-1
for y in range(0,len(arr_list)):
    if (arr_list[y]>sec_largest) and (arr_list[y] !=largest):
        sec_largest=arr_list[y]



largest=arr_list[0]
sec_largest=-1
for z in range(0,len(arr_list)):
    if (arr_list[z]>largest):
        sec_largest=largest
        largest=arr_list[z]
    elif   (arr_list[z]<largest) and (arr_list[z]>sec_largest):
        sec_largest=arr_list[z]


unique_nums = set(arr_list)
print(unique_nums)
i=0
for j in range(1,len(arr_list)):
    if (arr_list[i] != arr_list[j]):
        arr_list[i+1]=arr_list[j]
        i+=1
print(arr_list)

m=matrix()