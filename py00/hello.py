ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# list
try:
  ft_list[-1] = "Word!"
except indexError:
  print("IndexError: list assignment index out of range")

# tuple
try:
  new_tuple = list(ft_tuple)
  new_tuple.remove("toto!")
  new_tuple.append("Morocco!")
  ft_tuple = tuple(new_tuple)
except ValueError:
  print("ValueError: tuple assignment index out of range")

# set
try:
  ft_set.remove("tutu!")
  ft_set.add("Benguerir!")
except Exception as e:
  print("Error with set {e}")

# dictionary
try:

  ft_dict["Hello"] = "1337!"
except Exception as e:
  print("Error with dictionary {e}")

#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)