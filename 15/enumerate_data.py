names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
   """Outputs:
      1. Julian     Australia
      2. Bob        Spain
      3. PyBites    Global
      4. Dante      Argentina
      5. Martin     USA
      6. Rodolfo    Mexico"""
   names_countries = {}
   for x in range(len(names)):
      names_countries[names[x]] = countries[x]
   x = 1
   for n, c in names_countries.items():
      print(str(x) + ". {:<11}".format(n) + c)
      x += 1