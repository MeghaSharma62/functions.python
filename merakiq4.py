# def sort1():
#         unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
#         a=unorder_list.sort()
#         print(unorder_list)
# sort1()

# By using reverse function print the reverse order of the list.

# def reve():
#         reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
#         i=1
#         b=[]
#         while i<=len(reverse_list):
#                 a=reverse_list[-i]
#                 b.append(a)
#                 i+=1
#         print(b)
# reve()


# print(minimum number)
def min1():
        list = [8, 6, 4, 8, 4, 50, 2, 7,1]
        i=0
        min=list[0]
        while i<len(list):
                if list[i]<min:
                        min=list[i]
                i+=1
        print(min)
min1()