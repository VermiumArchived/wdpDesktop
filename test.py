from imageai.Prediction import ImagePrediction
from colorthief import ColorThief
import os
from PIL import Image

execution_path = os.getcwd()

file = "./images/hund.png"

numGuess = 10

fileTypes = ['.png', '.jpg', '.bmp', '.webp', '.jpeg']

clear = lambda: os.system('cls')

color_thief = ColorThief(file)
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=6)

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5")) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
prediction.loadModel()

#predictions, probabilities = prediction.predictImage(os.path.join(file), result_count=numGuess)
#clear()
#print("Dominant Color: %s" % str(dominant_color))
#print("Palette: %s" % str(palette))
#print("Predictions:")
#for eachPrediction, eachProbability in zip(predictions, probabilities):
#    print("    %s: %s" % (str(eachPrediction), str(round(eachProbability, 1))) + "%")

root = './images'

for root, dirs, files in os.walk(root, topdown=False):
    clear()

    for name in [fi for fi in files if fi.lower().endswith(tuple(fileTypes))]:
        im = Image.open(root + "\\" + name)
        width, height = im.size
        img = Image.open(root + "\\" + name)
        predictions, probabilities = prediction.predictImage((root + "\\" + name), result_count=numGuess)
        print("Image Name: %s" % str(name))
        print("Dominant Color: %s" % str(dominant_color))
        print("Palette: %s" % str(palette))
        print("Predictions:")
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print("    %s: %s" % (str(eachPrediction), str(round(eachProbability, 1))) + "%")
            img.save(root + "\\" + str(eachPrediction) + "-" + str(name))