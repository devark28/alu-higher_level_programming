#!/usr/bin/python3
import sys
import py_compile
py_compile.compile(sys.argv[1], cfile=sys.argv[1] + "c")
