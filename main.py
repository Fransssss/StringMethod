#string methods

print("\n--String Methods--\n")
print("1 -len(str) | Length(string)")
name = "Jacob"
print(name + ' ' + str(len(name)))
print('\n')

print("2 -len(str) | Length(string)")
animal = "Bird"
print(animal + ' ' + str(len(animal)))
print('\n')

print("3 -len(str) | Length(string)")
fruit = "An Apple"
print(fruit + ' ' + str(len(fruit)))
print('\n')

print("4 -len(str) | Length(string)")
things = "Buildings"
print(things + ' ' + str(len(things)))
print('\n')

print("5-len(str) | Length(string)")
year = "2020/21"
print(year + ' ' + str(len(year)))
print('\n\n')

print("6 - Print(str.find(toSearch)")
super = "Iron-Man"
print( 'I' + " at pos " + str(super.find('I')) + " from " + super)
print( 'n' + " at pos " + str(super.find('n')) + " from " + super)
print( 'M' + " at pos " + str(super.find('M')) + " from " + super)
print('\n')

print("7 - Print(str.find(toSearch)")
villain = "Gold-Panther"
print( 'G' + " at pos " + str(villain.find('G')) + " from " + villain)
print( 'd' + " at pos " + str(villain.find('d')) + " from " + villain)
print( 'r' + " at pos " + str(villain.find('r')) + " from " + villain)
print('\n')

print("8 - Print(str.find(toSearch)")
sport = "Running"
print( 'R' + " at pos " + str(sport.find('R')) + " from " + sport)
print( 'n' + " at pos " + str(sport.find('n')) + " from " + sport)
print( 'g' + " at pos " + str(sport.find('g')) + " from " + sport)
print('\n')

print("9 - Print(str.find(toSearch)")
noodle = "Bakmie"
print(noodle)
print('a' + " at pos " + str(noodle.find('a')) + " from " + noodle)
print('k' + " at pos " + str(noodle.find('k')) + " from " + noodle)
print('e' + " at pos " + str(noodle.find('e')) + " from " + noodle)
print('\n')

print("10 - Print(str.find(toSearch)")
out_space = "star"
print(out_space)
print('t' + " at pos " + str(out_space.find('t')) + " from " + out_space)
print('a' + " at pos " + str(out_space.find('a')) + " from " + out_space)
print('r' + " at pos " + str(out_space.find('r')) + " from " + out_space)
print('\n\n')

print("11 - string.capitalize()")
artist = "rouse"
print("bf: " + artist + "| af: " + artist.capitalize())
print('\n')

print("12 - string.capitalize()")
song = "happier"
print("bf: " + song + "| af: " + song.capitalize())
print('\n')

print("13 - string.capitalize()")
tower = "eifel"
print("bf: " + tower + "| af: " + tower.capitalize())
print('\n')

print("14 - string.capitalize()")
activity = "reading"
print("bf: " + activity + "| af: " + activity.capitalize())
print('\n')

print("15 - string.capitalize()")
place = "local market"
print("bf: " + place + "| af: " + place.capitalize())
print('\n\n')

print("16 - string.upper()")
country = "brazil"
print("bf: " + country + "| af: " + country.upper())
print('\n')

print("17 - string.upper()")
hotel = "SerayuHotel"
print("bf: " + hotel + "| af: " + hotel.upper())
print('\n')

print("18 - string.upper()")
status = "Engaged"
print("bf: " + status + "| af: " + status.upper())
print('\n')

print("19 - string.upper()")
logo = "MonoSexual"
print("bf: " + logo + "| af: " + logo.upper())
print('\n')

print("20 - string.upper()")
holiday = "4th July"
print("bf: " + holiday + "| af: " + holiday.upper())
print('\n\n')

print("21 - string.lower()")
nature = "FoResT"
print("bf: " + nature + "| af: " + nature.lower())
print('\n')

print("22 - string.lower()")
marvel = "STAR Lord"
print("bf: " + marvel + "| af: " + marvel.lower())
print('\n')

print("23 - string.lower()")
anime = "NaRUto"
print("bf: " + anime + "| af: " + anime.lower())
print('\n')

print("24 - string.lower()")
jutsu = "TaiJUTsu"
print("bf: " + jutsu + "| af: " + jutsu.lower())
print('\n')

print("25 - string.lower()")
season = "SuMMeR"
print("bf: " + season + "| af: " + season.lower())
print('\n\n')

print("26 - str.alpha()")
time = "sunset"
print("Check if all alphabetic - " + time)
print(time.isalpha())
print('\n')

print("27 - str.alpha()")
plane = "2united"
print("Check if all alphabetic - " + plane)
print(plane.isalpha())
print('\n')

print("28 - str.alpha()")
tree = "Cider 4 ever"
print("Check if all alphabetic - " + tree)
print(tree.isalpha())
print('\n')

print("29 - str.alpha()")
writing = "For life"
print("Check if all alphabetic - " + writing)
print(writing.isalpha())
print('\n')

print("30 - str.alpha()")
brand = "NikeAdidas"
print("Check if all alphabetic - " + brand)
print(brand.isalpha())
print('\n\n')


print("31 - str.count('char')")
greet = "hey there"
print("'e' in [" + greet + "] " + str(greet.count('e')))
print('\n')

print("32 - str.count('char')")
cmu = "hallo lolaYl"
print("'l' in [" + cmu + "] " + str(cmu.count('l')))
print('\n')

print("33 - str.count('char')")
veggie = "oh tomatoes"
print("'o' in [" + veggie + "] " + str(veggie.count('o')))
print('\n')

print("34 - str.count('char')")
vitamin = "Vitamin B, C, and D"


print("35 - str.count('char')")
destination = "Hii Heavenli prince"
print("'i' in [" + destination + "] " + str(destination.count('i')))
print('\n\n')


print("36 - str.replace('toreplace','replacewith')")
vehicle = "Cars and Boat"
print("Replace 'a' -> 'z' - " + vehicle + " | " + vehicle.replace('a','z'))
print('\n')

print("37 - str.replace('toreplace','replacewith')")
hour = "three am at night"
print("Replace 'e' -> 'u' - " + hour + " | " + hour.replace('e','u'))
print('\n')

print("38 - str.replace('toreplace','replacewith')")
sign = "Dont go to the pool"
print("Replace 'o' -> 'i' - " + sign + " | " + sign.replace('o','i'))
print('\n')

print("39 - str.replace('toreplace','replacewith')")
trash = "bootle and plastic"
print(trash.replace('t','r'))
print("Replace 't' -> 'r' - " + trash + " | " + trash.replace('t','r'))
print('\n')

print("40 - str.replace('toreplace','replacewith')")
suggest = "Take what you want, eat what you take"
print("Replace 'a' -> 'x' - " + suggest + " | " + suggest.replace('a','x'))
print('\n')
