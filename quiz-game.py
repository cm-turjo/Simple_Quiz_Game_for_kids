print("Welcome to My Computer Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("The Game quits")
    quit()

print("Okay! Let's play :) ")

ans_count=0

answer = input("What does CPU Stand for? ")

if answer.lower() == "central processing unit":
    print("Correct! ")
    ans_count+=1
else:
    print("You got Wrong!")
    print(" Correct Answer is: CPU- Central Processing Unit")

answer = input("What does GPU Stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct! ")
    ans_count += 1
else:
    print("You got Wrong!")
    print("Correct Answer is: Graphics Processing Unit")

answer = input("What does PSU Stand for? ")

if answer.lower() == "power supply unit":
    print("Correct! ")
    ans_count += 1
else:
    print("You got Wrong!")
    print("Correct Answer is PSU-Power Supply Unit")

answer = input("What does RAM Stand for? ")

if answer.lower() == "random access memory":
    print("Correct! ")
    ans_count += 1
else:
    print("You got Wrong!")
    print("Correct Answer is: Random Access Memory")

answer = input("What does ROM Stand for? ")

if answer.lower() == "read only memory":
    print("Correct! ")
    ans_count += 1
else:
    print("You got Wrong!")
    print("Correct Answer is: Read Only Memory")


print("Thank you for playing this game!")
print('Your Score is ' + str(ans_count) + "/5")
