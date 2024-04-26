#mutable- can change values- lists

#list_1 = ['history', 'math', 'physics', 'science']
#list_2 = list_1

#list_1[0] = 'Art'

#print(list_1)
#print(list_2)

#Immuntable- cannot change values- tuples, loop and access

#tuple_1 = ('history', 'math', 'physics', 'art')
#tuple_2 = tuple_1

#tuple_1[0] = 'english'

#print(tuple_1)
#print(tuple_2)

#cs_courses = {'history', 'math', 'physics', 'science', 'math'} # duplicates are removed from the output # this is a set

#art_courses = {'history', 'math', 'art', 'design'}

#print(cs_courses)

#print('math' in cs_courses)

#print(cs_courses.intersection(art_courses)) # shows courses that are in both sets

#print(cs_courses.difference(art_courses)) # shows the difference between the cs_courses and art_courses

#print(cs_courses.union(art_courses))

#Empty lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {} #this sin't right, this creates a dictionary
empty_set = set()