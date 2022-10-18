from enum import Enum

class CellType(Enum):
    EMPTY = 1
    EVENT = 2


class Cell:
    def __init__(self):
        pass

    def getType(self):
        pass

    def getName(self):
        return ""
    
    def setName(self, newName):
        self.name = newName

    def compareName(self, name):
        return False

class Empty(Cell):
    def __init__(self):
        super().__init__()

    def getType(self):
        return CellType.EMPTY

class EventCell(Cell):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def getType(self):
        return CellType.EVENT

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def compareName(self, name):
        if self.name == name:
            return True
        return False


class Day:
    def __init__(self):
        self.cells = [Empty()]*96 #List of Cell(), 96 elements of Cell()
    
    def getIndex(self, name:str):
        """Inputs a string and returns a list of index showing the segments of the wanted cell.\n
        Returns a list of int
        """
        indexList = []
        for i in range(len(self.cells)):
            if self.cells.compareName(name):
                indexList.append(i)

        return indexList
    
    def getTimesFromName(self, name:str):
        """Inputs a string and returns a list of times showing the time of each segment from the wanted name: Good for display\n
        Returns a list of str"""
        timeList = []
        indexList = self.getIndex(name)
        for segment in indexList:
            timeList.append(f"{(segment)//4}:{(segment)%4}")

    def getTimesIndex(self):
        """Returns a list of index, giving the segments needed to interrupt user."""
        lastCellName = ""
        notify = []
        for i in range(len(self.cells)):
            if self.cells[i].getType() != CellType.EMPTY:
                if not self.cells[i].compareName(lastCellName):
                    lastCellName = self.cells[i].getName()
                    notify.append(i)
                
            else:
                lastCellName = ""

        return notify

    def generateSegment(self, startTime: str, endTime: str, cell: Cell):
        """Modifies cells (list) such that the wanted cell occupies the inputted time interval"""
        startIndex = self.getIndex(startTime)
        endIndex = self.getIndex(endTime)
        changeCells = list(range(startIndex,endIndex))
        for index in changeCells:
            self.cells[index] = cell
        
    def getNotify(self):
        """Inputs a list of index, returns a list of string indicating the times of that segment that needs to be notified."""
        times = []
        for segment in self.getTimesIndex():
            times.append((Day.getTime(segment),self.cells[segment].getName()))
        return times
        
    def setup(self, listOfCells:list):
        self.cells = listOfCells
    
    def save(self):
        finalString = ""
        for x in self.cells:
            if x.getType() == CellType.EMPTY:
                finalString += "-;"
            else:
                finalString += x.getName() +";"
        finalString = finalString[:-1]
        return finalString

    @staticmethod
    def getTimes(indexList:list):
        """Inputs a list of index, returns a list of string indicating the times of that segment that needs to be notified."""
        times = []
        for segment in indexList:
            times.append(Day.getTime(segment))

    @staticmethod
    def getTime(index:int):
        """Inputs a int, indicating the time segment and returns the time of that segment in str"""
        return f"{(index)//4}:{((index)%4)*15:02d}"

    @staticmethod
    def getIndex(segmentTime:str):
        """Inputs a string of the segmented time in the format of HH:MM, returns an integer referring to which segment it belongs to."""
        temp = segmentTime.split(":")
        hour = int(temp[0])
        minutes = int(temp[1])
        return hour*4+minutes//15

    

    

class Week:
    def __init__(self):
        self.days = []
        for x in range(7):
            self.days.append(Day())

    def loadData(self, inputStr: str):
        daysList = inputStr.split("\n")
        for x in range(len(self.days)):
            temp = daysList[x].split(";")
            newList = []
            for y in range(len(temp)):
                if temp[y] == "-":
                    newList.append(Empty())
                else:
                    newList.append(EventCell(temp[y]))
            self.days[x].setup(newList)
    
    def saveData(self):
        """Take the schedule data and put it into a string, returns a string to that can be written into a txt file."""
        finalString = ""
        for x in self.days:
            finalString += x.save()+"\n"
        return finalString



