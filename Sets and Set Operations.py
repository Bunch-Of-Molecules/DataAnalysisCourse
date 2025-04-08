integer_set = {1, 2, 3, 4, 5}
whole_set = {0, 1, 2, 3, 4, 5, 6}

character_set = set('Indian')
state_set = {"UP", "AP", "MP"}
"""
order of elements is not defined in a set and hence we can't rely on a set to produce 
consistently the same order again and again
"""

diverse_set = {1, 34, 2.54, (3, 5, 6), "Lmao"}
#a set can contain any sort of data type as long as it's immutable

null_set = set()
#To create an empty set, use the set function and not simply x={}, as that'll just create an emtpy dict

print(character_set)
print(state_set)
#See how instantiating the sets differently gives us vastly different types of sets

unique_set = {1, 2, 3, 1, 1}
#any reoccurring values are removed and only one instance of it is kept.
#sets work by hashing the elements in a hashcode and same elements have the same hashcode, thus no repetition

unique_set.add(7)

set_union = integer_set.union(unique_set)
print(set_union)
#or
set_union = integer_set | unique_set
print(set_union)

set_intersection = integer_set.intersection(unique_set)
print(set_intersection)
#or
set_intersection = integer_set & unique_set
print(set_intersection)

set_symdiff = (integer_set | unique_set) - (integer_set & unique_set)
print(set_symdiff)
#or
set_symdiff = integer_set ^ unique_set
print(set_symdiff)

print(str(integer_set.isdisjoint(diverse_set)) + "\n")
#said to be disjoint there's nothing in common, i.e. intersection set is null

print(integer_set.issubset(whole_set))
print(whole_set.issuperset(integer_set))
print(integer_set.issuperset(whole_set))
print(whole_set.issubset(integer_set))
#or
print(integer_set <= whole_set)  #checks if integer is subset of whole
