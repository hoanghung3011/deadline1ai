from cx_Freeze import setup, Executable

setup(name='Division of Labour', version='1.0', description='', executables=[Executable('src/main.py')], base='Win32Gui')