pos=-1
def search(list,n):
    l=0
    u=len(list)
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals() ['pos']=mid
            return pos
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
           
    return False                
        
list=[4,7,8,12,45,99]
n=int(input("Enter Element for search: "))
if search(list,n):
    print("Found",pos)
else:
    print("Not Found")