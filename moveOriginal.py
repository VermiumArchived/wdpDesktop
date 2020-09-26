from deps import * # Importing all dependencies from deps.py

yes = ['y', 'yes'] # YES Synonyms
no = ['n', 'no'] # NO Synonyms

def moveOriginal(name, root, base, ext):
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