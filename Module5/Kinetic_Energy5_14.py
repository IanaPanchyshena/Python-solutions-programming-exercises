# Kinetic_Energy5_14
# In physics, an object that is in motion is said to have kinetic energy.
# The following formula can be used to determine a moving object’s
# kinetic energy: KE=1\2*m(v**2)
# The variables in the formula are as follows:
# KE is the kinetic energy, m is the object’s mass in kilograms,
# and v is the object’s velocity in meters per second.
# Write a function named kinetic_energy that accepts an object’s mass
# (in kilograms) and velocity (in meters per second) as arguments.
# The function should return the amount of kinetic energy that the object has.

# Write a program that asks the user to enter values for mass and velocity,
# then calls the kinetic_energy function to get the object’s kinetic energy.

def main():
    mass=float(input('Enter values for mass in kilograms: '))
    velocity=float(input('Enter values for velocity in meters per second: '))

    kinetic_energy=get_kinetic_energy(mass,velocity)
    print('Kinetic energy is',format(kinetic_energy,'.2f'))

def get_kinetic_energy(mass,velocity):
    return 1/2*mass*velocity**2
    
main()
