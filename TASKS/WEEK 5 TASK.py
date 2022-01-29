print("Enter a word")
word = input()


def wordtoNato(word):
    nato = {"a":"alfa", "b":"bravo", "c":"charlie", "d":"delta", "e":"echo", "f":"foxtrot", "g":"golf", "i":"india", "h":"hotel", "j":"juliett", "k":"kilo", "l":"lima", "m":"mike", "n":"november", "o":"oscar", "p":"papa", "q":"quebec", "r":"romeo", "s":"sierra", "t":"tango", "u":"uniform", "v":"victor", "w":"whiskey", "x":"x-ray", "y":"yankee", "z":"zulu"}
    listoflet = list(word)
 
    for x in listoflet:
        print(nato[x])
 
wordtoNato(word)

print("Enter a NATO Phonetic Alphabet words with a space.")
natoalf = input()

def Natotoword(natoalf):
    nato2 = {"alfa":"a", "bravo":"b", "charlie":"c", "delta":"d", "echo":"e", "foxtrot":"f", "golf":"g",  "india":"i", "hotel":"h", "juliett":"j", "kilo":"k", "lima":"l", "mike":"m", "november":"n", "oscar":"o", "papa":"p", "quebec":"q", "romeo":"r", "sierra":"s", "tango":"t", "uniform":"u", "victor":"v", "whiskey":"w", "x-ray":"x", "yankee":"y", "zulu":"z"}
    listofword = list(natoalf.split(" "))
    
    for x in listofword:
        try:
            print(nato2[x], end = '')
        except:
            print("") 

    print("")

Natotoword(natoalf)

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetlist = list(alphabet)

print("Enter word to encrypt: ")
word = input()
wordlist = list(word)

for x in wordlist:
    if (x == " "):
        print(" ", end='')
    else:
        p = 0
        for q in alphabetlist:
            if(x == q):
                if((p+7)<20):
                    print(alphabetlist[p+7], end='')
                else:
                    print(alphabetlist[p-19], end='')
            p += 1
    
print("")


