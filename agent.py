import objgraph
from flask import Response
import uuid
import time
import gc
from pympler.asizeof import asizeof

class Agent:

    stringCount = 0
    global isWaiting
    global startTime
    global endTime


    def __init__(self):
        self.stringCount = 0
        self.startTime = 0
        self.isWaiting = False
        self.endTime = 0

    def startRequestTimer(self):
        if not self.isWaiting:
            self.startTime = time.time()
            self.isWaiting = True


    def stopRequestTimer(self):
        if not self.isWaiting:
            print ('ERROR! Must have a running timer (startRequestTimer()) before stopping it.')
        else:
            self.endTime = time.time()
            self.isWaiting = False
            print ('{} {} {}'.format("Request took: ", self.endTime - self.startTime, " ms."))


    def countStrings(self):
        self.stringCount = 0
        cellObjs = objgraph.by_type('cell')
        for cell in cellObjs:
            if(cell.cell_contents is not None and objgraph._get_obj_type(cell.cell_contents) == str):
                self.stringCount += 1
        return self.stringCount


    def getMemoryUsed(self):
        #Kinda hacky, but for each object in the garbage collection, get it's size and add to a running sum.
        #using pympler's asizeOf instead of sys.sizeOf to remove GC's overhead from count. (https://stackoverflow.com/questions/34787327/pympler-asizeof-vs-sys-getsizeof)
        print ("{} {} {}".format("Total memory used: ", sum([asizeof(o) for o in gc.get_objects()]), " bytes"))

    def addRequestID(self, res):
        response = aResponse(res)
        return response



#Creating a new response class that handles the response and adds an ID (UUID) to it.
# Extending Flask's response class so they can do all the under the hood stuff in process_request after
# main's @app.after_request finishes.
class aResponse(Response):
    id = 0
    response = None
    def __init__(self, res):
        self.response = res
        self.id = uuid.uuid4()

    def getId(self):
        return self.id