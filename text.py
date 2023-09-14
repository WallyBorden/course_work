def calculatePotential(height)
    potential= 1000*9.8*height
    return potential

def calculateKinetic(velocityx,velocityy)
    kinetic=.5*1000*((velocityx**2+velocityy**2)**.5)
    return kinetic

def calculateTotalenergy(height, velocityx, velcotyy)
    total_energy=calculatePotential(height) + calculateKinetic(velocityx,velocityy)
    return total_energy
