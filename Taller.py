class student:
    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.gradez = []
        s.isPassed = "NO"
        s.honor = "?"

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        if not self.gradez:
            return 0

        t = 0
        for x in self.gradez:
            t += x

        avg = t / len(self.gradez)
        return avg

    def checkHonor(self):
        if self.calcaverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        if 0 <= index < len(self.gradez):
            del self.gradez[index]
        else:
            print("Invalid index")

    def report(self):
        print("ID: " + str(self.id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + str(self.calcaverage()))


def startrun():
    a = student("x", "Jorge")
    a.addGrades(100)
    a.addGrades(50)
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(1)
    a.report()


startrun()