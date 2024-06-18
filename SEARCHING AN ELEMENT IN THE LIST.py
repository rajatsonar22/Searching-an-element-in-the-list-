# Practical no 4
# SEARCHING TEH ELEM:
print(""">>> IT SEARCHES THE ELEMENT IN THE LIST IF IT IS THERE IT WILL
      GIVE OUTPUT AS FOUND OTHERWISE NOT FOUND FROM THE GIEVEN LIST 
      mylist = [1, 2, "sachin", 4, "FYCE",6]
      AND SEARCHES THE ELEMENT n = "tyce" """)
print("")#...space
def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return True
        return False

mylist = [1, 2, "sachin", 4, "FYCE",6]
n = "tyce"

if search(mylist,n):
    print("---FOUND")
else:
    print("---NOT FOUND")
