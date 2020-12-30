# Pololu-Motor-Plot-Generator-Python

The original Matlab Code you can find [here](https://de.mathworks.com/matlabcentral/fileexchange/54695-polulu-motor-plot-generator).

Pololu sells dc motors used in differential drive robots. Plot useful info using their datasheet

The website of Pololu or several (small) DC motor manufacturers generally only supply very few parameters such as stall torque, stall current, rated voltage etc. To get more information about the motor behaviour, these parameter values can be combined and analyzed.
This script does the same. The input is similar to the link here (https://www.pololu.com/product/2380/specs)
The output curves and methodology is similar to the link here (https://www.pololu.com/product/2380/faqs)
Re-written to include all units as per the feedback from users.
Calculation guide is at http://www.micromo.com/technical-library/dc-motor-tutorials/motor-calculations

## MATLAB vs. Python (matplotlib + numpy)

On the left side you can see the MATLAB code in action and on the right side the Python Code. The MATLAB functions The MATLAB code is commented out in the Python code, so you can learn to translate MATLAB codes into Python. Also helpful are the NumPy for Matlab users guides from [Numpy](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) and [mathesaurus](http://mathesaurus.sourceforge.net/matlab-numpy.html).

![matlab_vs_matplotlib_comparison](https://github.com/Michdo93/Polulu-Motor-Plot-Generator-Python/blob/main/work.PNG?raw=true)

## Usage

It was tested and written in/with:

Python Version: 3.6.8
Numpy Version: 1.16.4
Matplotlib Version: 3.1.0

Please you have to make sure that you use nearly this versions!

At first you have to clone the repository:

```
git clone https://github.com/Michdo93/Pololu-Motor-Plot-Generator-Python.git
```

Then you can run it:

```
cd Pololu-Motor-Plot-Generator-Python
python3 motorPlot.py
```

After closing all three windows you can see the
* Slope of TorqueVSCurrent
  * recprocal of it
* maximum output of the mechanical power in watts
  * its Torque load in oz-in
  * it current in mA
* Resistance of the motor in ohm
