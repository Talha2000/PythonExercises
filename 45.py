class American(object):
    @staticmethod
    def printNationality():
        print("America")

# first_American = American()         # this will not run if @staticmethod does not decorates the function.
# first_American.printNationality()     # Because the class has no instance.


American.printNationality()      # this will run even though the @staticmethod
                                 # does not decorate printNationality()

