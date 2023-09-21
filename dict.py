#1.

#vardnica1 = {}
#vardnica2 = dict()
#print(vardnica1, len(vardnica1), type(vardnica1))
#print(vardnica2, len(vardnica2), type(vardnica2))


#2.


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(thisdict["brand"], thisdict["model"], thisdict["year"])

#3.

# atslega = ['desmit', 'divdesmit', 'trīsdesmit']
# vertiba = [10, 20, 30]
# x = dict(zip(atslega, vertiba))
# print(tuple(x))

#4.

# atzimes = {
#     "fizika": 5,
#     "matematika" : 7,
#     "sports" : 10
# }
# print(min(atzimes, key=atzimes.get))

#5.


# manaVardnica = {
#     "vards": "Kitija", 
#     "vecums": 25,
#     "alga": 1500,
#     "pilseta": "Tukums", 
#}
# manaVardnica.pop("vards")
# manaVardnica.pop("alga")                 
# print(manaVardnica)\
# keys = ["vards", "alga"]
# for i in keys:
#  manaVardnica.pop(i)
# print(manaVardnica)


#6.


# darbinieki = {
#  "vards": "Ketlina",
#  "vecums": 25,
#  "telefons": "+37121212121",
#  "ciemats": "Dobele",
# }
# darbinieki.pop("ciemats")
# darbinieki.update({"pilseta": "Tukums"})
# print(darbinieki)