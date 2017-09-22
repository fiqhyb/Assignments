###this program simulates a person driving from point A to point B###
import time
def main():
    print("Driving Simulator 1.4\nMade by Fiqhy Bismadhika\n########################")

##important variables or inputs
    name    =input("Enter the person's name:").title()
    while not name.isalpha():
        print("Name can only contains letters without any spaces")
        name=input("Enter the person's name:")
    initvel = u =0
    print("=>Initial velocity is 0 m/s")
   #initvel = u =int(input("Enter the amount of initial velocity(m/s):"))
    speedlim= l = 60
    print("=>Speed limit is 60 m/s")
   #speedlim= l =int(input("Enter the amount of speed limit(m/s):"))
    t_spent = t =(int(input("Enter the amount of time spent(s)      :")))
    acc     = a =(int(input("Enter the amount of acceleration(m/s2) :")))
    dis     = d =(int(input("Enter the amount of distance(m)        :")))

    print(name + " is driving to the destination...")
###################################################

##equations
    v=u+a*t
    s=u*t+(a/2)*(t**2) or t/2*(v+u)
    v2=u**2+2*a*s

    def driving():
        print(name+" has stopped driving")
####################################################

##output
    print("Loading output...")
    for i in range(t + 1):
        time.sleep(1)
        k = int((a/2)*(i**2) / 10)
        print("Duration:", i, ("sec"), "Distance:", "*" * k,"(",(a/2)*(i**2),"m"")")

##conditions
    if v>l:
        print(name+" went over the speed limit, max speed was ",(v)," m/s")
    else:
        print(name+" did not go over the speed limit, max speed was ",(v)," m/s")
    time.sleep(3)
    if s>=d:
        print(name+" reached the destination, reached ",int(s)," m")
    else:
        print(name+" did not reach the destination, reached ",int(s)," m")

    def end():
        print("Simulation is complete")
    time.sleep(3),end()
main()
while True:
    rest=input("Press r to restart and q to quit")
    if rest =="r":
        main()
    elif rest =="q":
        quit()