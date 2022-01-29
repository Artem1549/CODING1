
Var = input("Enter a number: ")

try:
    val = int(Var)
except ValueError:
    print("Input error")
    end = input("")

OE = int(Var) % 2
Result = ""
if OE == .0:
    Result = "Even"
else:
    Result = "Odd"

print (Result)

end = input("")
