# Polulu-Motor-Plot-Generator-Python

The original Matlab Code you can find [here](https://de.mathworks.com/matlabcentral/fileexchange/54695-polulu-motor-plot-generator).

It is still in process and not working. The problems are described on stackoverflow:
https://stackoverflow.com/questions/65483128/converting-the-polulu-motor-plot-generator-from-matlab-to-matplotlib

Pololu sells dc motors used in differential drive robots. Plot useful info using their datasheet

The website of Pololu or several (small) DC motor manufacturers generally only supply very few parameters such as stall torque, stall current, rated voltage etc. To get more information about the motor behaviour, these parameter values can be combined and analyzed.
This script does the same. The input is similar to the link here (https://www.pololu.com/product/2380/specs)
The output curves and methodology is similar to the link here (https://www.pololu.com/product/2380/faqs)
Re-written to include all units as per the feedback from users.
Calculation guide is at http://www.micromo.com/technical-library/dc-motor-tutorials/motor-calculations
