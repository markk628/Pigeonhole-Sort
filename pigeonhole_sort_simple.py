"""
    1. make a variable max equal to the maximum value in items
    2. make a variable min equal to the minimum value in items
    3. make a variable size equal to max minus min plus 1
    4. make an empty array holes
    5. make an an empty array sorted

    6. for i in range of size
          append an empty array (pigeonhole)

    7. for item in items
          append item to hole at the index of item minus smallest
    
    8. for i in range of size
          add hole at index i of holes to sorted
    9. return sorted
    """

def pigeonhole_sort(items):
    
    #1, 2, 3, 4, 5
    biggest = max(items)
    smallest = min(items)
    size = biggest - smallest + 1
    holes = []
    sorted = []

    #6
    for i in range(size):
        holes.append([])

    #7
    for item in items:
        holes[item - smallest].append(item)

    #8
    for i in range(size):
        sorted += holes[i]
    
    #9
    return sorted

items = [8,3,2,7,4,6,8]
print(pigeonhole_sort(items))