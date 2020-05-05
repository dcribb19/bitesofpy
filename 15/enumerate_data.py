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
   """
   ALTERNATE SOLUTION WITH ENUMERATE
   for i, name in enumerate(names, start=1):
      print(str(i) + ". {:<11}".format(name) + countries[i-1])
   enumerate(iterable, start=0) can take 2 args, so we can use 2 args in for loop to produce what we need using only 1 loop
   
   ADDITIONAL NOTES
   Could have also used zip() to combine names and countries into an iterator of tuples instead of using dictionary

   eg. zip_names_countries = zip(names, countries)
   """