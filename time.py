import datetime


d = datetime.datetime.now()

print(type(d))    # >>> objet datetime.datetime

print(d) # >>>2020-12-27 19:35:51.013790

print(datetime.datetime.strftime(d,"%Y-%m-%d")) # >>>2020-12-27  (argument2 est le format)


print(datetime.datetime.strftime(d + datetime.timedelta(days=1), "%Y-%m-%d")) # timedelta ajoute un intervalle de temps



# https://docs.python.org/fr/3/library/datetime.html#strftime-strptime-behavior


x = datetime.datetime(d.year, d.month, d.day)-datetime.timedelta(days=1)  # jour précédent à 0h
print(x, d)