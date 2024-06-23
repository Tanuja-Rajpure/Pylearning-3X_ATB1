hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Women", "Diane Prince")
new_tuple = (hero1, hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[0][0])
print(new_tuple[0][1])
print(new_tuple[1][0])
print(new_tuple[1][1])

# Unpacking of tuple
q, w, e = (45, 56, 78)
print(q)
print(w)
print(e)

#Search in tuple
cities = ("Paris", "London", "Los Angeles", "Tokyo")
print("Paris" in cities)  # in used for finding / searching item in tuple
print("New Delhi" in cities)

# When to use tuple
# API Autoationd passing urls

ENV_API_URLS = tuple(["www.abc.com/get","www.xyz.com/post", "www.internet.com"])
print("Use of Tuple ", ENV_API_URLS)