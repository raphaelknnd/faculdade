aux = 0
res = input("Telefonou para a vítma?")
res = res.lower()

if res == "s":
  aux += 1

res = input("Esteve no local do crime?")
res = res.lower()

if res == "s":
  aux += 1

res = input("Mora perto da vítima?")
res = res.lower()

if res == "s":
  aux += 1

res = input("Devia para a vítima?")
res = res.lower()

if res == "s":
  aux += 1

res = input("Já trabalhou com a vítima?")
res = res.lower()

if res == "s":
  aux += 1

if aux == 2:
  print("Suspeita")
elif aux == 3 or aux == 4:
  print("Cúmplice")
elif aux == 5:
  print("Assassino")
else:
  print("Inoscente")