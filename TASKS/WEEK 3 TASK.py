
print("Enter you Name:")
name = input()
print("Enter you Surname:")
surname = input()



def greet(name, surmname):
    if(surname == ""):
        print("Hello " + name + ".")
    else:
        print("Hello there, " + name + " of " + surmname + "!")

greet(name,surname)

print("Enter a word in english:")
word = input()

vowel1 = "a";
vowel2 = "e";
vowel3 = "i";
vowel4 = "o";
vowel5 = "u";
vowel6 = "A";
vowel7 = "E";
vowel8 = "I";
vowel9 = "O";
vowel10 = "U";

consonant1 = "b";
consonant2 = "c";
consonant3 = "d";
consonant4 = "f";
consonant5 = "g";
consonant6 = "h";
consonant7 = "j";
consonant8 = "k";
consonant9 = "l";
consonant10 = "m";
consonant12 = "n";
consonant13 = "p";
consonant14 = "q";
consonant15 = "r";
consonant16 = "s";
consonant17 = "t";
consonant18 = "v";
consonant19 = "w";
consonant20 = "x";
consonant21 = "y";
consonant22 = "z";
consonant23 = "B";
consonant24 = "C";
consonant25 = "D";
consonant26 = "F";
consonant27 = "G";
consonant28 = "H";
consonant29 = "J";
consonant30 = "K";
consonant31 = "L";
consonant32 = "M";
consonant33 = "N";
consonant34 = "P";
consonant35 = "Q";
consonant36 = "R";
consonant37 = "S";
consonant38 = "T";
consonant39 = "V";
consonant40 = "W";
consonant41 = "X";
consonant42 = "Y";
consonant43 = "Z";



x = 0

def EngToPL(word):
    global x 
    wordToLetters = list(word)
    #print(wordToLetters[0])
  

    if ((wordToLetters[0] == vowel1)or(wordToLetters[0] == vowel2)or(wordToLetters[0] == vowel3)or(wordToLetters[0] == vowel4)or(wordToLetters[0] == vowel5)or(wordToLetters[0] == vowel6)or(wordToLetters[0] == vowel7)or(wordToLetters[0] == vowel8)or(wordToLetters[0] == vowel9)or(wordToLetters[0] == vowel10)):
        if (x == 0):
            print(word + "yay")
        else:
            print(word + "ay")

    else:
        wordToLetters.append(wordToLetters[0])
        wordToLetters[0] = "" 
        x = 1
        EngToPL(''.join(wordToLetters))

    

EngToPL(word)



    

    