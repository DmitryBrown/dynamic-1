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
    Last Edited: 10 Nov 2015
    Tested on: Python 2.7.10 :: Anaconda 2.3.0 (64-bit) running on SUSE Linux
    Recommended for: Recent Python 2 only, any system
    
    ---------------------------------------------------------------------------
"""

import os
import struct

gadget = ()

def read_gadget(filename):
    """ Reads particle data stored in GADGET format. """
    s = os.path.getsize(filename)
    f = open(filename, "rb")
    
    # here we read the header
    header = struct.unpack('IIIIIIddddddddiiiiiddddiiiiiiiii', f.read(180))
    space = struct.unpack('i'*19, f.read(256-180))
    n = sum(header[:6])

    print "Loading..."
    print header
    print "Number of particles: ", n
    
    # read basic data
    positions = struct.unpack('f'*3*n, f.read(n*3*4))
    print "positions: ", len(positions)
    velocities = struct.unpack('f'*3*n, f.read(n*3*4))
    print "velocities: ", len(velocities)
    identifications = struct.unpack('i'*n, f.read(n*4))
    print "identifications: ", len(identifications)
    masses = struct.unpack('f'*n, f.read(n*4))
    print "masses: ", len(masses)
    energy = struct.unpack('f'*header[5], f.read(4*header[5]))
    print "energy: ", len(energy)
    density = struct.unpack('f'*header[5], f.read(4*header[5]))
    print "density: ", len(density)
    # we can't assume the rest exist

    readsize = 256+(len(positions)+len(velocities)+len(identifications)+len(masses)+len(energy)+len(density))*4

    if readsize != s:
        print "Read data does not match file size: "+str(readsize)+"/"+str(s)
    else:
        print "Read data matches file size."


    gadget = (header, positions, velocities, identifications, masses, energy, density)
    
    f.close()
    return gadget

def write_gadget(filename):
    """ Writes particle data in GADGET format. """
    f = open(filename, "wb")
    
    f.write(header)
    f.close()
    return

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

def output_data_stats():
    """ Prints useful information about the loaded data. """
    print gadget
    return

def read_script(filename):
    """ Alternative input format. Takes commands as a script. """
    f = open(filename, "r")
    for line in f.readlines():
        if interpret_line(line) == 1:
            break
    f.close()
    return

def interpret_line(line):
    """ Since the input is line based as a script or as commands, I abstract
    them through this function that deals with the effects of one line.
    """
    command = line.split()

    # applying command word to arguments via an associated function
    # one function per command word and one command word per line
    if command[0]=="exit" or command[0]=="quit": return 1
    if command[0]=="generateics": generateics(command)
    if command[0]=="simulate": simulate(command)
    if command[0]=="analysis": analysis(command)
    if command[0]=="set": setVariable(command)
    if command[0]=="load": gadget = read_gadget(command[1])
    if command[0]=="save": gadget = write_gadget(command[1])
    if command[0]=="statdata": output_data_stats()
    
    return 0

def main():
    print "Dynamic v0.0"
    print "Copyright 2015 Robert Paul Sanders"
    print "For full license details see: http://www.gnu.org/licenses/gpl-3.0.txt"
    print ""
    while True:
        if interpret_line(raw_input("> ")) == 1:
            break

if __name__ == "__main__":
    main()
