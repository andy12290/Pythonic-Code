import json

movie_json = """
{
"Title":"Johnny 5",
"Year":"2001",
"Runtime":"119 min",
"Country":"USA"
}
"""

movie_data = json.loads(movie_json)
print(movie_data)

print("The title of movie is : {}".format(movie_data.get('Title')))
