
print("Enter 3 integers:")
num1 = int(input())
num2 = int(input()) 
num3 = int(input())
SumOfNum = 0

for i in range(num1,num2):
  
    if i % num3 == 0:
        SumOfNum += i

print(SumOfNum)

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
ii = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0 
z = 0

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0
K = 0
L = 0
M = 0
N = 0
O = 0
P = 0
Q = 0
R = 0
S = 0
T = 0
U = 0
V = 0
W = 0
X = 0
Y = 0 
Z = 0

print("Input text:")
text = input()
for i in text:
    if i == "a":
        a += 1
    elif i == "b":
        b += 1
    elif i == "c":
        c += 1
    elif i == "d":
        d += 1
    elif i == "e":
        e += 1
    elif i == "f":
        f += 1
    elif i == "g":
        g += 1
    elif i == "h":
        h += 1
    elif i == "i":
        ii += 1
    elif i == "j":
        j += 1
    elif i == "k":
        k += 1
    elif i == "l":
        l += 1
    elif i == "m":
        m += 1
    elif i == "n":
        n += 1
    elif i == "o":
        o += 1
    elif i == "p":
        p += 1
    elif i == "q":
        q += 1
    elif i == "r":
        r += 1
    elif i == "s":
        s += 1
    elif i == "t":
        t += 1
    elif i == "u":
        u += 1
    elif i == "v":
        v += 1
    elif i == "w":
        w += 1
    elif i == "x":
        x += 1
    elif i == "y":
        y += 1
    elif i == "z":
        z += 1
    elif i == "A":
        A += 1
    elif i == "b":
        B += 1
    elif i == "c":
        C += 1
    elif i == "d":
        D += 1
    elif i == "e":
        E += 1
    elif i == "f":
        F += 1
    elif i == "g":
        G += 1
    elif i == "h":
        H += 1
    elif i == "i":
        I += 1
    elif i == "j":
        J += 1
    elif i == "k":
        K += 1
    elif i == "l":
        L += 1
    elif i == "m":
        M += 1
    elif i == "n":
        N += 1
    elif i == "o":
        O += 1
    elif i == "p":
        P += 1
    elif i == "q":
        Q += 1
    elif i == "r":
        R += 1
    elif i == "s":
        S += 1
    elif i == "t":
        T += 1
    elif i == "u":
        U += 1
    elif i == "v":
        V += 1
    elif i == "w":
        W += 1
    elif i == "x":
        X += 1
    elif i == "y":
        Y += 1
    elif i == "z":
        Z += 1

print("a: " + str(a))
print("b: " + str(b))
print("c: " + str(c))
print("d: " + str(d))
print("e: " + str(e))
print("f: " + str(f))
print("g: " + str(g))
print("h: " + str(h))
print("i: " + str(i))
print("j: " + str(j))
print("k: " + str(k))
print("l: " + str(l))
print("m: " + str(m))
print("n: " + str(n))
print("o: " + str(o))
print("p: " + str(p))
print("q: " + str(q))
print("r: " + str(r))
print("s: " + str(s))
print("t: " + str(t))
print("u: " + str(u))
print("v: " + str(v))
print("w: " + str(w))
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))

print("A: " + str(A))
print("B: " + str(B))
print("C: " + str(C))
print("D: " + str(D))
print("E: " + str(E))
print("F: " + str(F))
print("G: " + str(G))
print("H: " + str(H))
print("I: " + str(I))
print("J: " + str(J))
print("K: " + str(K))
print("L: " + str(L))
print("M: " + str(M))
print("N: " + str(N))
print("O: " + str(O))
print("P: " + str(P))
print("Q: " + str(Q))
print("R: " + str(R))
print("S: " + str(S))
print("T: " + str(T))
print("U: " + str(U))
print("V: " + str(V))
print("W: " + str(W))
print("X: " + str(X))
print("Y: " + str(Y))
print("Z: " + str(Z))





try:
    num = int(input("Enter an integer number to be divided: "))
except ValueError:
    print("Input error")  

try:
    divnum = int(input("Enter an integer number to divide by: "))
except ValueError:
    print("Input error")  


while True:
    num = num - divnum
    print("- " + str(divnum))
    if num < divnum:
        rem = num
        break

print("Remainder: " + str(num))


