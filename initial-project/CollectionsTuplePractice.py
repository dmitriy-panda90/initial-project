# Create tuple - practice

# 1 - Create a tuple of tech terms
tehnological_terms = ('python','pycharm','tuple','collections','string')
print('(1) - This is the tuple collections : ' +str(tehnological_terms))

# 2 - Print a sentence using cell exctraction : Regular & negative
print('(2) - we are ninja developers. We write ' + tehnological_terms[0] + ' code in ' + tehnological_terms[-4] + ' , and now practicing ' + tehnological_terms[2])

# 3 - Insert 'float' and 'list'  variables into the tuple
tehnological_terms_list = list(tehnological_terms)

tehnological_terms_list.append('float')
tehnological_terms_list.append('list')

tehnological_terms = tuple(tehnological_terms_list)

print('(3) - This is our new tuple with the added cells : ' + str(tehnological_terms))

# 4 - Create a single cell tuple
single_cell_tuple = (1,)
print('(4) - Print the single cell tuple : ' +str(single_cell_tuple))
print(type(single_cell_tuple))