# We will see about the merging files.

route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}

# we have different three dict we would like to merge

# Classic pythonic way
m4 = { k:v for d in [route, query, post] for k,v in d.items()}
print(m4)

# more pythonic way

m5 = (**route, **query, **post)
print(m5)
