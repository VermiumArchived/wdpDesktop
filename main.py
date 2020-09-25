# -*- coding: utf-8 -*-
# WhatsDisPic?

__author__ = "Vermium Sifell, Temerold"
__copyright__ = "MIT License - (© 2020 Zyner)"
__version__ = "dev"
__email__ = "support@vermium.se, support@Temerold.se"
__status__ = "In development"


# ./images/toDo - files to transcode
# ./images/failed - files that have had failed
# ./images/completed - files that have successfully completed

from config import * # User configuration - Local file (config.py)

import os
import sys
import shutil
from time import sleep

from deps import *

clear = lambda: os.system('cls') # Define clear() as cls

yes = ['y', 'yes'] # YES Synonyms
no = ['n', 'no'] # NO Synonyms

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, model)) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
prediction.loadModel()

dominant_color = ""
pattern = ""
run = True

for root, dirs, files in os.walk(root, topdown=False):
    clear()
    for name in [fi for fi in files if fi.lower().endswith(tuple(fileTypes))]:
        base, ext = os.path.splitext(name)
        
        im = Image.open(root + '\\' + name) # Opening ./images/picture.ext
        
        width, height = im.size # Taking the width of that pictures
        im.close() # Closing the opened image ./images/picture.ext
        color_thief = ColorThief(root + '\\' + name) # Getting image's color-properties
        dominant_color = color_thief.get_color(quality = 1) # Getting the image dominant color
        predictions, probabilities = prediction.predictImage((root + '\\' + name), result_count=numGuess) # AI engine calculates the image in a numGuess count of results
        
        print(
            "Image Name: %s" % str(name) + # Prints name of image
            "\nDominant Color: %s" % str(dominant_color) + # Prints Dominant color
            "\nPredictions:" # Print title of Predictions
        )

        try: # Try making the ./images/picture/
            os.mkdir(root + "\\" + base) # Create directory for image ./images/picture/
        except: pass # Pass, if error/already exists

        ima = Image.new("RGB", (width, height), (dominant_color)) # Creating a image base with dominant color

        ima.save(root + "\\" + base + "\\" + "dominantColor" + ext) # Saves the dominant color image in ./images/picture/dominant.ext

        ima.close() # Close dominant image

        try: # Try move image from ./images/picture.ext to ./images/picture/original.ext
            shutil.move((root + "\\" + name), (root + "\\" + base + "\\original" + ext))
        except: # If error
            ask_continue = input("Failed at moving file " + name + ", do you want to continue? (no/yes)")
            if ask_continue in no: exit() # Exit program if answered no
            elif ask_continue in yes: # Do statement if answered yes
                try:
                    shutil.move((root + "\\" + name), (root + "\\" + base + "-failed" + ext)) # Rename ./images/picture.ext to ./images/picture-failed.ext
                except:
                    secs = 10 # Timer set for 10 seconds
                    for sec in range(secs - 1):
                        clear() # Clear console
                        print(
                            "Couldn't rename file to %s-failed%s" % (base, ext) + # Prints Couldn't rename file to picture-failed.ext
                            "\n Closing program in %s seconds." % secs # Prints closing in x secs
                        )
                        secs -= 1 # Remove 1 second from timer
                        sleep(1) # Wait 1 second
                    exit() # Exit program

        try: # Try to open a new CSV file
            out = open((root + "\\" + base + "\\" + "predictions.csv"), 'w') # Opening a CSV file
        except: pass # Pass if error / already exists
        
        for eachPrediction, eachProbability in zip(predictions, probabilities): # Do the things below for each Prediction
            print( 
                "    %s: %s" % ( # Prints Prediction: Probability
                    str(eachPrediction), # Prediction name
                    str(round(eachProbability, 1)) # Prediction Percentage
                ) +
                "%" # Add a percentage symbol after Prediction: Probability
            )
            clear()
            out.write(str(eachPrediction) + '; ' + str(eachProbability) + '%\n') # Write each prediction to the CSV file

        out.close() # Close .csv file
