import numpy as np #Loads the numpy library for numerical operations (mathtools for Python)
import matplotlib.pyplot as plt #Loads the matplotlib library for plotting (like graph paper)

def x(t): #Defines the x position as a function of time
    return 8-6*t+t**2 #The equation for x position, * means multiply, ** means power, return means give back this value, now when i plug in a time t it will give back the x position
def v(t): #Defines velocity as a function od time
    return -6+2*t #The equation for velocity, derived from the position function by taking the derivative
def a(t): #Defines acceleration as a function of time
    return 2+0*t #The equation for acceleration, derived from the velocity function by taking the derivative
t= np.linspace(0,6,500) #Creates 500 evenly spaced time values from 0 to 6, more spaces means smoother curves

# Now for position vs time
plt.figure() #Creates a new figure for the plot
plt.plot(t,x(t)) #Plots time on the x-axis and x position on the y-axis
plt.axhline(0, color="black") #Adds a horizontal line at y=0 for reference
plt.axvline(0, color="black") #Adds a vertical line at x=0 for reference

plt.scatter([0,2,3,4], x(np.array([0,2,3,4]))) #Adds dots at specific time points (0,2,3,4) to show positions at those times,

plt.xlabel("Time (s)") #Labels the x-axis
plt.ylabel("x position (m)") #Labels the y-axis
plt.title("Position vs Time") #Adds a title to the plot
plt.grid() #Adds a grid to the plot for better readability


# Now for velocity
plt.figure() #Creates a new figure for the next plot
plt.plot(t,v(t)) #Plots time on the x-axis and velocity on the y-axis
plt.axhline(0, color="black") #Adds a horizontal line at y=0 for reference
plt.axvline(0, color="black") #Adds a vertical line at x=0 for reference
plt.xlabel("Time (s)") #Labels the x-axis
plt.ylabel("Velocity (m/s)") #Labels the y-axis
plt.title("Velocity vs Time") #Adds a title to the plot
plt.grid(True) #Adds a grid to the plot for better readability


# Now for acceleration
plt.figure() #Creates a new figure for the next plot
plt.plot(t,a(t)) #Plots time on the x-axis and acceleration on the y-axis
plt.axhline(0, color="black") #Adds a horizontal line at y=0 for reference
plt.axvline(0, color="black") #Adds a vertical line at x=0 for reference
plt.xlabel("Time (s)") #Labels the x-axis
plt.ylabel("Acceleration (m/s²)") #Labels the y-axis
plt.title("Acceleration vs Time") #Adds a title to the plot
plt.grid(True) #Adds a grid to the plot for better readability
plt.show() #Displays the plot