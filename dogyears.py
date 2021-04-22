'''
File: dogyears.py
'''

DOG_YEARS = 7

def main():
  human_age = int(input('Enter human age: '))
  dog_age = convert_to_dog(human_age)
  print('Dog age is: ' + str(dog_age))

def convert_to_dog(human_age):
  return human_age * DOG_YEARS

if __name__ == '__main__':
  main()
