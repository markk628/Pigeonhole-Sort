"""
    1. make a variable max equal to the maximum value in items
    2. make a variable min equal to the minimum value in items
    3. make a variable size equal to max minus min plus 1
    4. make an array holes with size amount of 0s (pigeonholes)

    5. for item in items
          add 1 to the hole at index item minus min in holes
    
    6. make a variable i equal to 0
    7. for j in range of size
          while hole at index j in holes is greater than 0
              subtract 1 from hole at index j
              set item at index 1 equal to j plus min
              add 1 to i
    8. return array
    """

def pigeonhole_sort(items):

    #1, 2, 3, 4
    biggest = max(items)
    smallest = min(items)
    size = biggest - smallest + 1
    holes = [0] * size

    #5
    for item in items:
        holes[item - smallest] += 1

    #6, 7
    i = 0
    for j in range(size):
        while holes[j] > 0:
            holes[j] -= 1
            items[i] = j + smallest
            i += 1
    
    #8
    return items

items = [8,3,2,7,4,6,8]
print(pigeonhole_sort(items))