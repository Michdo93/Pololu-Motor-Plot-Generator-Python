#!/usr/bin/env python
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

discreteBins = 500  #We will use this number of bins for plotting and calculating all functions such as Torque, speed etc.
#Input part of the main function

print("Please enter the stall torque in oz-inch [17]")
StallTorque = input()

print("Please enter the stall current in mA [700]")
StallCurrent = input()

print("Please enter the rated voltage in Volts [6]")
RatedVoltage = input()

print("Please enter the free run currennt in mA [40]")
NoLoadCurrent = input()

print("Please enter the free run speed in RPM [290]")
NoLoadSpeed = input()

# StallTorque = input('Please enter the stall torque in oz-inch [17]: ');
# StallCurrent = input('Please enter the stall current in mA [700]: ');
# RatedVoltage = input('Please enter the rated voltage in Volts [6]: ');
# NoLoadCurrent = input('Please enter the free run currennt in mA [40]: ');
# NoLoadSpeed = input('Please enter the free run speed in RPM [290]: ');

#Some basic input error checking is here.
if not isinstance(StallTorque, (int, float)) or StallTorque is None:
    StallTorque = 17
    print('Using default value for StallTorque')

if not isinstance(StallCurrent, (int, float)) or StallCurrent is None:
    StallCurrent = 700
    print('Using default value for StallCurrent')

if not isinstance(RatedVoltage, (int, float)) or RatedVoltage is None:
    RatedVoltage = 6
    print('Using default value for RatedVoltage')

if not isinstance(NoLoadCurrent, (int, float)) or NoLoadCurrent is None:
    NoLoadCurrent = 40
    print('Using default value for NoLoadCurrent')

if not isinstance(NoLoadSpeed, (int, float)) or NoLoadSpeed is None:
    NoLoadSpeed = 290
    print('Using default value for NoLoadSpeed')

#Here we calculate basic stuff to get all the variables and outputs.
Resistance = RatedVoltage / (StallCurrent/1000)

#Torque line
TorqueLine = np.arange(0-(StallTorque/discreteBins), StallTorque, (StallTorque/discreteBins))
# TorqueLine = 0:(StallTorque/discreteBins):StallTorque

#Current Line
CurrentLine = np.arange(NoLoadCurrent, StallCurrent+1, (StallCurrent-NoLoadCurrent)/discreteBins)
# CurrentLine = NoLoadCurrent:(StallCurrent-NoLoadCurrent)/discreteBins:StallCurrent

#Speed Line
SpeedLine = np.arange(NoLoadSpeed, 0, ((0-NoLoadSpeed)/discreteBins))
# SpeedLine = NoLoadSpeed: (0-NoLoadSpeed)/discreteBins : 0

# Torque Constant in Torque per current is
SlopeOfTorqueVsCurrent = (StallCurrent - NoLoadCurrent) / (StallTorque)

#Output Mechanical Power in watts is Torque * Speed * 0.00074 watts
OutputPower = 0.00074 * TorqueLine * SpeedLine
# No @ because it is different between Matlab and matplotlib
# OutputPower = 0.00074 * TorqueLine .* SpeedLine

#Input Electrical Power to the motor is Voltage * Current
InputPower = CurrentLine * RatedVoltage / 1000
# We are dividing by 1000 as the input was in mA and we need power in Watts.


#Plot part of the functions    
#plt.subplot(2,2,1)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(np.array((0, StallTorque)), np.array((NoLoadSpeed, 0)), 'b-')
ax2.plot(np.array((0, StallTorque)), np.array((NoLoadCurrent, StallCurrent)), 'r-')
# [hAx, hLine1, hLine2] = plotyy([0 StallTorque], [NoLoadSpeed 0], [0 StallTorque], [NoLoadCurrent StallCurrent]);
#This is the TorqueLoad vs. Motor Speed graph

fig.suptitle('Torque vs. Speed & Torque vs. Current')
#title('Torque vs. Speed & Torque vs. Current')
ax1.set_xlabel('Torque (oz-in)')
# xlabel('Torque (oz-in)')
ax1.set_ylabel('Speed-RPM', color='b')
# ylabel(hAx(1), 'Speed-RPM')
ax2.set_ylabel('Current-mA', color='r')
# ylabel(hAx(2), 'Current-mA')

plt.figure(1)

#This is the plot of the Output Mechanical power in watts vs. Input
#Electrical power in Watts.
#plt.subplot(2,2,2)

# plotyy(X1, Y1, X2, Y2)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(TorqueLine, OutputPower, 'b-')
ax2.plot(TorqueLine, InputPower, 'r-')
# [h2Ax, h2Line1, h2Line2] = plotyy(TorqueLine, OutputPower, TorqueLine, InputPower)

ax1.set_xlabel('Torque (oz-in)')
# xlabel('Torque (oz-in)')
ax1.set_ylabel('OutputPower-watts', color='b')
# ylabel(h2Ax(1), 'OutputPower-watts')
ax2.set_ylabel('InputPower-watts', color='r')
# ylabel(h2Ax(2), 'InputPower-watts')
fig.suptitle('Torque vs. Output Power & Torque vs. Input Power')
# title('Torque vs. Output Power & Torque vs. Input Power')

plt.figure(2)

#This is the plot of the Power Efficiency of the motor.
#plt.subplot(2,2,3)

# plotyy(X1, Y1, X2, Y2)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

PowerEff = OutputPower / InputPower
# PowerEff = OutputPower ./ InputPower;
plt.plot(TorqueLine, PowerEff)
ax1.set_xlabel('Torque (oz-in)')
ax1.set_ylabel('Power Efficiency -nounit')
fig.suptitle('Power Efficiency of the motor')

plt.figure(3)

plt.show()

#Output information part of the function    
print('Slope of TorqueVsCurrent is %s. The recprocal is %s' % (SlopeOfTorqueVsCurrent, (1/SlopeOfTorqueVsCurrent)))

#Max Output Power is at
V,I = OutputPower.max(0),OutputPower.argmax(0)
# [V,I] = max(OutputPower)

print('Maximum output mechanical power is %s(watts).\nThis happens at the Torque load of %s(oz-in), with Current %s(mA)' % (OutputPower[I], TorqueLine[I], CurrentLine[I]))
print('Resistance of the motor is %s (ohms)' % Resistance)
