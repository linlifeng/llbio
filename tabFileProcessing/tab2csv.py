#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
"""
SYNOPSIS
    Convert a Orange tab formated file to comma-separed value(csv) file.
DESCRIPTION
    
    A utility tool to convert tab like files.
EXAMPLES
    
    python tab2csv.py filename.tab filename.csv
EXIT STATUS
    
    0 program exit normal
    1 program had problem on execution
AUTHOR
    Theofilis George <theofilis.g@gmail.com>
LICENSE
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
VERSION
    1
"""

import sys, os, traceback, optparse
import time
import re

def main():
    global options, args

    with open(args[0], 'r') as myfile:
        with  open(args[1],"w") as f:

            for line in myfile.readlines():
                data = line.strip().split()
                f.write("{0}".format(data[0]))
                for w in data[1:]:
                    f.write(",{0}".format(w))
                print >>f,"\n" % (),



if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print time.asctime()
        main()
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)