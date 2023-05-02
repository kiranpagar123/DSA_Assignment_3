def insert_sort(my_list):
    for index in range(1,len(my_list)):
        currunt_element=my_list[index]
        pos=index
        
        while currunt_element<my_list[pos-1] and pos>0:
            my_list[pos]=my_list[pos-1]
            pos=pos-1
        my_list[pos]=currunt_element


list=[2,4,3,5,1]
insert_sort(list)
print(list)
