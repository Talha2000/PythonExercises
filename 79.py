
subject = ["I", "You"]
verb = ["Play", "Love"]
Object = ["Hockey", "Football"]
def GenSentence():

    for i in subject:
        for j in verb:
            for k in Object:
                print("{} {} {}".format(i, j, k))

GenSentence()
