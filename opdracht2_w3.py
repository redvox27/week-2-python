class stack:
    def __init__(self):

        self.elements = []

    def  is_empty(self):
        if self.elements == [] :
            print("elements is leeg ")
        else:
            return False

    def addToList(self,value):
        self.elements.append(value)

    def peek(self):
        print("last element in list is: ",self.elements[-1])

    def pop(self):
        print("the following element has been removed: ",self.elements[-1])

        self.elements.remove(self.elements[-1])


    def getSize(self):
        if self.elements == [] :
            print("de lijst is leeg ")

        else:
            print("lenght of the list is: ",len(self.elements))


