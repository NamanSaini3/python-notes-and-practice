 (x + y) * z  Jo kaam phela kara hn usko paranteesh () mai rak data hn or phela vohi hota hn 
 # Python Notes: Numbers, Variables, Basic Maths, Type Conversion

## 1. Variables me number store karna

Python me variable ek naam hota hai jo value ko point karta hai.

```python
x = 2
y = 3
z = 4
```

Yaha:

```text
x ----> 2
y ----> 3
z ----> 4
```

---

## 2. Addition

```python
x + y
```

Output:

```python
5
```

Reason:

```text
x = 2
y = 3

x + y = 2 + 3 = 5
```

---

## 3. Bracket aur multiplication

```python
(x + y) * z
```

Output:

```python
20
```

Reason:

```text
x = 2
y = 3
z = 4

(x + y) * z
= (2 + 3) * 4
= 5 * 4
= 20
```

Important:

```text
Bracket ke andar wala kaam pehle hota hai.
```

---

## 4. Integer + Float

```python
40 + 2.54
```

Output:

```python
42.54
```

Yaha:

```text
40     = int
2.54   = float
42.54  = float
```

Jab `int` aur `float` ka calculation hota hai, result mostly `float` me aata hai.

---

## 5. int() conversion

```python
int(2.56)
```

Output:

```python
2
```

Important:

```text
int() decimal ke baad wali value hata deta hai.
Ye round off nahi karta.
```

Example:

```python
int(2.56)  # 2
int(9.99)  # 9
int(5.10)  # 5
```

---

## 6. float() conversion

```python
float(40)
```

Output:

```python
40.0
```

Reason:

```text
float() integer ko decimal number bana deta hai.
```

Example:

```python
float(40)  # 40.0
float(5)   # 5.0
float(2)   # 2.0
```

---

## Final Summary

```text
x = 2, y = 3, z = 4

x + y = 5

(x + y) * z = 20

40 + 2.54 = 42.54

int(2.56) = 2

float(40) = 40.0
```

## Yaad Rakh

```text
int   = whole number / bina decimal wala number
float = decimal wala number

int()   = decimal hata deta hai
float() = number ko decimal form me convert karta hai

Bracket () ke andar wala calculation pehle hota hai.
```

# Python: `repr()`, `str()`, `print()`

## Example

```python
repr('chai')
# "'chai'"

str('chai')
# 'chai'

print('chai')
# chai
```

## Difference

```text
repr()  = developer/debug view
str()   = normal text view
print() = screen par clean output
```

## Important

```text
Quotes string ka part nahi hote.
Quotes Python ko batate hain ki ye text/string hai.
```

## Yaad Rakh

```text
repr('chai')  -> exact Python form dikhata hai
str('chai')   -> normal string banata hai
print('chai') -> quotes ke bina screen par dikhata hai
```




# Python: Chained Comparison

```python
1 == 2 < 3
```

Python isko aise read karta hai:

```python
1 == 2 and 2 < 3
```

Check:

```text
1 == 2  → False
2 < 3   → True
```

Result:

```text
False and True = False
```

## Yaad Rakh

```text
a == b < c

means:

a == b and b < c
```

`and` me final answer True tabhi hota hai jab dono conditions True ho.



# Python: `math.floor()` vs `math.trunc()`

```python
import math
```

## `math.floor()`

`floor()` hamesha **neeche wale nearest integer** par le jata hai.

```python
math.floor(3.5)    # 3
math.floor(-3.5)   # -4
math.floor(-3.6)   # -4
```

Important:

```text
Negative number me floor aur chhota number deta hai.
-3.5 ka floor = -4
```

---

## `math.trunc()`

`trunc()` bas **decimal part hata deta hai**.

```python
math.trunc(2.8)    # 2
math.trunc(-2.8)   # -2
```

Important:

```text
trunc() round nahi karta.
Bas decimal ke baad wali value cut karta hai.
```

---

## Yaad Rakh

```text
floor() = neeche jao
trunc() = decimal hatao
```

Example:

```python
math.floor(-2.8)   # -3
math.trunc(-2.8)   # -2
```






# Python: Binary, Octal, Hexadecimal Numbers

Python me number different base me likh sakte hain.

```python
0b1000   # binary
0o20     # octal
0xFF     # hexadecimal
```

## 1. Binary

```python
0b1000
```

Output:

```python
8
```

`0b` ka matlab binary hota hai.
Binary ka base `2` hota hai. Isme sirf `0` aur `1` use hote hain.

## 2. Octal

```python
0o20
```

Output:

```python
16
```

`0o` ka matlab octal hota hai.
Octal ka base `8` hota hai. Isme digits `0` se `7` tak hote hain.

## 3. Hexadecimal

```python
0xFF
```

Output:

```python
255
```

`0x` ka matlab hexadecimal hota hai.
Hexadecimal ka base `16` hota hai.

```text
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

## Yaad Rakh

```text
0b = binary      = base 2
0o = octal       = base 8
0x = hexadecimal = base 16
```

Python in sab ka output default me decimal me dikhata hai.

oct(65)
'0o101'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'

# Python: `int("number", base)`

`int()` ko base ke saath use karke kisi bhi number system ko decimal me convert kar sakte hain.

```python
int("1000", 2)   # 8
int("65", 8)     # 53
int("FF", 16)    # 255
```

## Format

```python
int("number", base)
```

## Base Meaning

```text
base 2  = binary
base 8  = octal
base 16 = hexadecimal
```

## Important

```text
Number string me hona chahiye.
```

```python
int("1000", 2)   # correct
int(1000, 2)     # wrong
```

