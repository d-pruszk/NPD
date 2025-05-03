import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width',1000)

def create_phone_book():
  global first_names
  global last_names
  global label1
  global number1
  global label2
  global number2
  global label3
  global number3
  first_names = []
  last_names = []
  label1 = []
  number1 = []
  label2 = []
  number2 = []
  label3 = []
  number3 = []
create_phone_book()

def print_phonebook():
  d = {'First name': first_names, 'Last name': last_names, 'Label 1': label1, 'Number 1': number1, 'Label 2': label2, 'Number 2': number2, 'Label 3': label3, 'Number 3': number3}
  phonebook = pd.DataFrame(data=d)
  print(phonebook)

def add_contact(first, last, label, number):
  for i in range(len(first_names)):
    if number1[i] == number:
        print(f"Number already added for {first_names[i]} {last_names[i]}")
        return
    elif number2[i] == number:
        print(f"Number already added for {first_names[i]} {last_names[i]}")
        return
    elif number3[i] == number:
        print(f"Number already added for {first_names[i]} {last_names[i]}")
        return
    if first == first_names[i] and last == last_names[i]:
      if number2[i] != '':
        if number3[i] != '':
          print("Phone book for this person is full, number wasn't added")
          return True
        label3[i] = label
        number3[i] = number
        return True
      label2[i] = label
      number2[i] = number
      return True
  first_names.append(first)
  last_names.append(last)
  label1.append(label)
  number1.append(number)
  label2.append('')
  number2.append('')
  label3.append('')
  number3.append('')

def search_contact(first, last):
  for i in range(len(first_names)):
    if first == first_names[i] and last == last_names[i]:
      d = {'First name': first_names[i], 'Last name': last_names[i], 'Label 1': label1[i], 'Number 1': number1[i], 'Label 2': label2[i], 'Number 2': number2[i], 'Label 3': label3[i], 'Number 3': number3[i]}
      phonebook = pd.DataFrame(data=d, index=[0])
      print(phonebook)
      return
  print("No results found")
def delete_number(first,last,number):
  for i in range(len(first_names)):
    if first == first_names[i] and last == last_names[i]:
      if number1[i] == number:
        if number2[i]=='' and number2[i]=='':
          first_names.pop(i)
          last_names.pop(i)
          number1.pop(i)
          label1.pop(i)
          number2.pop(i)
          label2.pop(i)
          number3.pop(i)
          label3.pop(i)
          print("Number deleted succesfuly")
          return
        number1[i] = number2[i]
        label1[i] = label2[i]
        number2[i] = number3[i]
        label2[i] = label3[i]
        number3[i] = ''
        label3[i] = ''
        print("Number deleted succesfuly")
        return
      elif number2[i] == number:
        number2[i] = number3[i]
        label2[i] = label3[i]
        number3[i] = ''
        label3[i] = ''
        print("Number deleted succesfuly")
        return
      elif number3[i] == number:
        number3[i] = ''
        label3[i] = ''
        print("Number deleted succesfuly")
        return
  print("No results found")

print("_________________________________________ Adding contacts test: _________________________________________")
add_contact("Ala","Wesołowska", "main", "+ 048 513 056 142")
add_contact("Ala","Wesołowska", "home", "+ 048 798-123-422")
add_contact("Ala","Wesołowska", "mobile", "+ 048 222-123-422")
add_contact("John","Smith", "main", "0 800 241 6331")
add_contact("John","Smith", "work", "469 - 452 - 199")
add_contact("Janina","Brown", "work", "333 - 452 - 199")
print_phonebook()
print("_________________________________________ Search function test: _________________________________________")
search_contact("Janina","Brown")
print("_________________________________________ Delete function test: _________________________________________")
delete_number("Janina","Brown", "333 - 452 - 199")
print_phonebook()
print("______________________________ Adding the same number for two people test: ______________________________")
add_contact("Janina","Brown", "work", "+ 048 513 056 142")