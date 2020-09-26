# -*- coding: utf-8 -*-
# WhatsDisPic?

from deps import *
from config import * # User configuration - Local file (config.py)

clear = lambda: os.system('cls') # Define clear() as cls

yes = ['y', 'yes'] # YES Synonyms
no = ['n', 'no'] # NO Synonyms

execution_path = os.getcwd() # Gets the execution path

prediction = ImagePrediction() # Init prediction variable
prediction.setModelTypeAsResNet() # Set model type to ResNet
prediction.setModelPath(os.path.join(execution_path, model)) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
prediction.loadModel() # Loading selected model from config.py

dominantColor = "" # Init dominantColor variable
pattern = "" # Init pattern variable

for root, dirs, files in os.walk(root, topdown=False):
    clear()
    for name in [fi for fi in files if fi.lower().endswith(tuple(fileTypes))]:
        # Split file up into base.ext

        base, ext = os.path.splitext(name) # File name base.ext
        
        # Getting image size

        im = Image.open(root + '\\' + name) # Opening root/picture.ext
        width, height = im.size # Taking the width of that pictures
        im.close() # Closing the opened image root/picture.ext

        # Getting colors

        color_thief = ColorThief(root + '\\' + name) # Getting image's color-properties
        dominantColor = color_thief.get_color(quality = 1) # Getting the image dominant color
        predictions, probabilities = prediction.predictImage((root + '\\' + name), result_count=numGuess) # AI engine calculates the image in a numGuess count of results

        # Creating image directory

        try: # Try making the root/picture/
            os.mkdir(root + "\\" + base) # Create directory for image root/picture/
        except: pass # Pass, if error/already exists

        # Making a image with the dominant color

        ima = Image.new("RGB", (width, height), (dominantColor)) # Creating a image base with dominant color
        ima.save(root + "\\" + base + "\\" + "dominantColor" + ext) # Saves the dominant color image in root/picture/dominant.ext
        ima.close() # Close dominant image

        # Moving original image to the image folder and call it original.ext

        try: # Try move image from root/picture.ext to root/picture/original.ext
            shutil.move((root + "\\" + name), (root + "\\" + base + "\\original" + ext))
        except: # If error
            ask_continue = input("Failed at moving file " + name + ", do you want to continue? (no/yes)")
            if ask_continue in no: exit() # Exit program if answered no
            elif ask_continue in yes: # Do statement if answered yes
                try:
                    shutil.move((root + "\\" + name), (root + "\\" + base + "-failed" + ext)) # Rename root/picture.ext to root/picture-failed.ext
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

        # Create root/picture/predictions.csv file

        try: # Try to open a new CSV file
            out = open((root + "\\" + base + "\\" + "predictions.csv"), 'w') # Opening a CSV file
        except: pass # Pass if error / already exists
        
        # Printing some properties about the image

        print(
            "Image Name: %s" % str(name) + # Prints name of image
            "\nDominant Color: %s" % str(dominantColor) + # Prints Dominant color
            "\nImage Palette: %s" % str(pattern) + # Prints Image Palette
            "\nPredictions:" # Print title of Predictions
        )

        for eachPrediction, eachProbability in zip(predictions, probabilities): # Do the things below for each Prediction

            # Print each prediction and its probability

            print("    %s: %s%" % ( # Prints Prediction: Probability%
                    str(eachPrediction), # Prediction name
                    str(round(eachProbability, 1)) # Prediction Percentage
                )
            )

            # Clear Console

            clear()

            # Write each prediction and its probability to root/picture/predictions.csv
            
            out.write(str(eachPrediction) + '; ' + str(eachProbability) + '%\n') # Write each prediction to the CSV file

        # Close root/picture/predictions.csv file

        out.close() # Close .csv file