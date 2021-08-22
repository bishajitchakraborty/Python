#xargs
def add(*a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)

add(10,20)
add(4,6,10)