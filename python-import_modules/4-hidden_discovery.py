#!/usr/bin/python3
import importlib.machinery as mach

if __name__ == "__main__":
    module_name = 'hidden_4'
    module_file = './hidden_4.pyc'
    hidden_module = mach.SourcelessFileLoader(
        module_name, module_file).load_module()
    names = dir(hidden_module)
    for name in names:
        if not name.startswith('__'):
            print(name)
