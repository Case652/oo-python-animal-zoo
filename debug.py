from lib.animal import Animal
from lib.zoo import Zoo

# code here


# e.g.  
z3 = Zoo("Colordo Zoo", "Devner, CO")
z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
a7 = Animal( 'Lion', 75, 'Luke', z1 )
a6 = Animal( 'Lion', 75, 'Luke', z1 )
a5 = Animal( 'Bear', 75, 'Luke', z1 )
a5 = Animal( 'Bear', 75, 'Luke', z1 )
a5 = Animal( 'Dog', 75, 'Luke', z1 )
a5 = Animal( 'Cat', 75, 'Luke', z1 )
a5 = Animal( 'Cat', 75, 'Luke', z3 )





# ipdb allows us to stop our code & test stuff
import ipdb; ipdb.set_trace()
print( 'Thanks for visiting the zoo!' )