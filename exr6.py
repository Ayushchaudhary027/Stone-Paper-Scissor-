
import random
x=["stone","paper","scissor"]
p=0
c=0
a=0
b=10
print("We will play stone paper scissor game\n")
while a<=b:
     player = input("Enter your choice with respest to this game\ns for stone\np for paper\nc for scisssor\n")
     comp = random.choice(x)
     print("Computer's choice is ",comp)
     if player=="s":
        if comp=="paper":
            c+=1
            print("computer wins =",c)
        elif comp=="scissor":
            p += 1
            print("PLayer wins = ",p)
        else:
            print("Match tied")
     elif player=="p":
        if comp == "scissor":
            c+=1
            print("Computer wins = ",c)
        elif comp=="stone":
            p += 1
            print("PLayer wins = ",p)
        else:
            print("Match tied")
     elif player=="c":
         if comp == "stone":
             c+=1
             print("Computer wins = ",c)
         elif comp == "paper":
             p+=1
             print("PLayer wins = ",p)
         else:
             print("Match tied")
     else:
         print("enter the correct value\n")
     a += 1
     print(f"number of chances left is {a} out of {b}\n\n")

print("Game over\n")

if c<p:
    print("Congrats you win\n")
elif c==p:
    print("match tied\n")
else:
    print("Computer wins , better luck next time\n")

print(f"your point is {p} and computer point is {c}\n")

