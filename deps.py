import os
import sys
from config import root # User configuration - Local file (config.py)

try:
    os.mkdir(root) 
except: pass # Create ./images

try:
    os.mkdir(root + "\\toDo") 
except: pass # Create ./images/toDo

try:
    os.mkdir(root + "\\failed")
except: pass # Create ./images/failed

try:
    os.mkdir(root + "\\completed")
except: pass # Create ./images/completed

try:
    os.mkdir("./models")
except: pass # Create ./models

clear = lambda: os.system('cls') # Define clear() as cls

yes = ['y', 'yes'] # Yes values
no = ['n', 'no'] # No values

try:
    import tensorflow
    from imageai.Prediction import ImagePrediction
    from PIL import Image, ImageColor
    from colorthief import ColorThief
    ask_auto = ""
except:
    clear()
    ask_auto = input("Do you wan't automatic install of packages? (no/yes)")

try:
    import tensorflow
except ImportError:
    clear()
    if ask_auto in no:
        sys.exit("""You need tensorflow!
    install it from http://pypi.python.org/pypi/tensorflow
    or run pip install tensorflow.""")
    elif ask_auto in yes:
        print("Trying to Install required module: tensorflow\n")
        os.system('python -m pip install tensorflow')
        import tensorflow

try:
    from imageai.Prediction import ImagePrediction
except ImportError:
    clear()
    if ask_auto in no:
        sys.exit("""You need imageai!
    install it from http://pypi.python.org/pypi/imageai
    or run pip install imageai.""")
    elif ask_auto in yes:
        print("Trying to Install required module: imageai\n")
        os.system('python -m pip install imageai')
        from imageai.Prediction import ImagePrediction

try:
    from PIL import Image, ImageColor
except ImportError:
    clear()
    if ask_auto in no:
        sys.exit("""You need PIL!
    install it from http://pypi.python.org/pypi/PIL
    or run pip install PIL""")
    elif ask_auto in yes:
        print("Trying to Install required module: PIL\n")
        os.system('python -m pip install PIL')
        from PIL import Image, ImageColor

try:
    from colorthief import ColorThief
except ImportError:
    clear()
    if ask_auto in no:
        sys.exit("""You need colorthief!
    install it from http://pypi.python.org/pypi/colorthief
    or run pip install colorthief.""")
    elif ask_auto in yes:
        print("Trying to Install required module: colorthief\n")
        os.system('python -m pip install colorthief')
        from colorthief import ColorThief