import re 
txt="Jh_h3aa_aaa4KKabbbb"
txt2="Hello, world."
txt3="CamelSnakeCamelSnake"
txt4="camel_snake_camel_snake"
#1
match1=r"ab*"
x1=re.search(match1, txt)
print(x1.group(0))

#2
match2=r"abb|bbb"
x2=re.search(match2, txt)
print(x2.group(0))

#3
pattern3=r"[a-z]+_[a-z]+"
prog3=re.compile(pattern3)
iter3=prog3.finditer(txt)
for i in iter3:
    print(i.group(0))
    
#4
pattern4=r"[A-Z][a-z]+"
prog4=re.compile(pattern4)
iter4=prog4.finditer(txt)
for i in iter4:
    print(i.group(0))

#5
match5=r"a.*b"
x5=re.search(match5,txt)
print(x5.group(0))

#6
match6=r"[\s,.]"
x6=re.sub(match6,':',txt2)
print(x6)

#7
x7=re.sub(r'_([a-zA-Z])', lambda match:match.group(1).upper(),txt4)
print(x7)

#8
words=[]
match8=r"[A-Z][a-z]*"
prog8=re.compile(match8)
iter8=prog8.finditer(txt3)
for i in iter8:
    words.append(i)
for i in words:
    print(i.group(0))

#9
x9=re.sub(r"([a-z])([A-Z])",r"\1 \2",txt3)
print(x9)

#10
x10=re.sub(r"([a-z])([A-Z])",r"\1_\2",txt3).lower()
print(x10)



