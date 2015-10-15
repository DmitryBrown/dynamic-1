#!/usr/bin/env python
"""
    DYNAMIC: A simple Python 2 program for experiments with dynamical systems
    Copyright 2015 Robert Paul Sanders

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    ---------------------------------------------------------------------------

    Created: 15 Oct 2015
    Author: Robert Paul Sanders
    Last Edited: 15 Oct 2015
    Tested on: Python 2.7.10 :: Anaconda 2.3.0 (64-bit) running on SUSE Linux
    Recommended for: Recent Python 2 only

    ---------------------------------------------------------------------------
"""

import matplotlib.pyplot as plt
import numpy as np

def generateics(command):
    """
    """
    return

def simulate(command):
    """
    """
    return

def analysis(command):
    """
    """
    # plt.plot() commands 
    return

def setVariable(command):
    return

def main():
    print "Dynamic v0.0"
    print "Copyright 2015 Robert Paul Sanders"
    print "For full license details see: http://www.gnu.org/licenses/gpl-3.0.txt"
    print ""
    while True:
        command = raw_input("> ")
        command = command.split()
        mode = command[0]

        # applying command word to arguments via an associated function
        # one function per command word and one command word per line
        if mode=="exit" or mode=="quit": return
        if mode=="generateics": generateics(command)
        if mode=="simulate": simulate(command)
        if mode=="analysis": analysis(command)
        if mode=="set": setVariable(command)

if __name__ == "__main__":
    main()

