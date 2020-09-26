from deps import * # Importing all dependencies from deps.py
from config import enableAI, model

def ai(name, numGuess, root, base):
    if enableAI:

        execution_path = os.getcwd() # Gets the execution path

        prediction = ImagePrediction() # Init prediction variable
        prediction.setModelTypeAsResNet() # Set model type to ResNet
        prediction.setModelPath(os.path.join(execution_path, model)) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
        prediction.loadModel() # Loading selected model from config.py

        predictions, probabilities = prediction.predictImage((root + '\\' + name), result_count=numGuess) # AI engine calculates the image in a numGuess count of results

        try: # Create root/picture/predictions.csv file
            out = open((root + "\\" + base + "\\" + "predictions.csv"), 'w') # # Open root/picture/predictions.csv file
        except: pass # Pass if error / already exists

        print(
        "\nPredictions:" # Print title of Predictions
        )

        for eachPrediction, eachProbability in zip(predictions, probabilities): # Do the things below for each Prediction
        
            # Print each prediction and its probability

            print("    %s: %s%s" % ( # Prints Prediction: Probability%
                    str(eachPrediction), # Prediction name
                    str(round(eachProbability, 1)), # Prediction Percentage
                    str("%")
                )
            )

            out.write(str(eachPrediction) + '; ' + str(eachProbability) + '%\n') # Write each prediction and its probability to root/picture/predictions.csv

        out.close() # Close root/picture/predictions.csv file