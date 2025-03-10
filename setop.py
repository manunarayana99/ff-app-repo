classA={"jayesh","shirisha","krish","nagesh","saurabh"}
classB={"sakshi","shrikant","sruthi","srishti"}
comp1={"jayesh":3.4,"sruthi":3.5,"sakshi":4.7}
comp2={"jayesh":12,"shirisha":13,"nagesh":14,"saurabh":15}
#Q1
print(classA and comp2.keys()-comp1.keys())
#Q2
print(comp1.keys() ^ comp2.keys())
#Q3
print((comp1.keys() and comp2.keys()) - classA)
#Q4
print(len(classA)+len(classB))
#Q5
print(len(comp1.keys() | comp2.keys()))
#Q6
print((comp1.keys() or comp2.keys()) - classA)
