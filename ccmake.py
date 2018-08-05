#!/usr/bin/env python3
from optparse import OptionParser
import os

TEM_DIR = 'templates'
LIB_DIR = 'lib'
EXE_DIR = 'exe'
F_NAME = 'CMakeLists.txt'
D_NAME = 'cmake'

P_REP = "@@P_NAME@@"
CPP_REP = "@@CPP_SOURCES@@"
HEA_REP = "@@HEA_SOURCES@@"
UI_REP = "@@UI_SOURCES@@"


def main():
    parser = OptionParser()

    parser.add_option(
        "-n", 
        "--name", 
        type="string",
        dest="name",
        help="Project name", 
        metavar="NAME"
    )

    parser.add_option(
        "-p", 
        "--path", 
        type="string",
        dest="path",
        #callback="get_ppath",
        help="Path to the code", 
        metavar="PATH"
    )

    parser.add_option(
        "-s", 
        "--source", 
        type="string", 
        dest="source",
        #callback="get_sdir",
        help="Relative directory of source code",
        #attr="src",
        metavar="SOURCE"
    )

    parser.add_option(
        "-e", 
        "--executable", 
        dest="executable",
        action="store_true",
        help="Project is a executable",
        default=False,
        metavar="EXECUTABLE"
    )

    parser.add_option(
        "-l", 
        "--library", 
        dest="library",
        action="store_true",
        help="Project is a library",
        default=False, 
        metavar="LIBRARY"
    )

    parser.add_option(
        "-v", 
        action="store_true", 
        dest="verbose",
        help="Be verbose",
        default=False,
        metavar="VERBOSE"    
    )

    (options, args) = parser.parse_args()

    if options.executable and options.library:
        parser.error("Options -l and -e are mutually exclusive")

    print(options)
    print(args)

    ppath = os.path.abspath( options.path )
    sdir = options.source

    # Check if exists
    if os.path.exists(ppath) and os.path.exists( os.path.join(ppath, sdir) ):
        # Get list of files in the project
        fcpp = list_cpp(ppath, sdir)
        fhpp = list_hpp(ppath, sdir)
        fui = list_ui(ppath, sdir)
        
        # read cmake file
        if options.executable:
            cmake_file = os.path.abspath( os.path.join('./', TEM_DIR, EXE_DIR, F_NAME) )
            cmake_dir = os.path.abspath( os.path.join('./', TEM_DIR, EXE_DIR, D_NAME) )
        if options.library:
            cmake_file = os.path.abspath( os.path.join('./', TEM_DIR, LIB_DIR, F_NAME) )
            cmake_dir = os.path.abspath( os.path.join('./', TEM_DIR, LIB_DIR, D_NAME) )
        
        # Read file in string
        fstr = read_cmake_file(cmake_file)
        # Change string
        fstr = fstr.replace( P_REP, options.name )
        fstr = fstr.replace( CPP_REP, '\n    '.join(fcpp))
        fstr = fstr.replace( HEA_REP, '\n    '.join(fhpp))
        fstr = fstr.replace( UI_REP, '\n    '.join(fui))    
        f = open('/tmp/CMakeLists.txt', 'wt', encoding='utf-8')
        f.write(fstr)
        f.close()

def get_ppath(ppath):
    pass

def get_spath(sdir):
    pass

def read_cmake_file(fpath):
    f = open(fpath,'r')
    return f.read()

def list_fwe(ppath, sdir, fext):
    import os
    flist = list()
    fpath = os.path.join(ppath, sdir)
    files = os.listdir(fpath)
    files.sort()
    for file in files:
        if file.endswith(fext):
            flist.append( sdir + '/' +file )
    return flist

def list_cpp(ppath, sdir):
    return list_fwe(ppath, sdir, 'cpp')

def list_hpp(ppath, sdir):
    return list_fwe(ppath, sdir, 'h')

def list_ui(ppath, sdir):
    return list_fwe(ppath, sdir, 'ui')

if __name__ == "__main__":
    main()