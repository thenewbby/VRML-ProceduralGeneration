#!/usr/bin/python
import os
from random import randint

class Class1:
    """docstring for """
    posTree = []
    posLeaf = [0, 5, 0]
    scaleTree = [1, 1 ,1]
    colorLeaf = [0.443137,0.776471,0.443137]
    colorTrunk = [0.545098,0.270588,0.0745098]
    coordIndexLeaf = [0,13,12,-1,0,16,13,-1,0,15,16,-1,0,12,14,-1,0,14,15,-122,12,13,-1,23,14,12,-1,1,23,12,-1,1,12,22,-1,24,23,1,-1,25,24,1,-1,25,1,22,-1,36,25,22,-1,37,13,16,-1,38,23,24,-1,39,15,14,-1,40,24,25,-1,41,16,15,-1,6,14,23,-1,6,23,38,-1,6,39,14,-1,7,36,22,-1,7,22,13,-1,7,13,37,-1,8,41,15,-1,8,15,39,-1,9,16,41,-1,9,37,16,-1,10,24,40,-1,10,38,24,-1,11,25,36,-1,11,40,25,-1,20,41,8,-1,21,41,20,-1,21,9,41,-128,10,40,-1,29,28,40,-1,29,40,11,-1,30,7,37,-1,30,36,7,-1,31,36,30,-1,31,11,36,-1,31,29,11,-1,32,30,37,-1,32,37,9,-1,32,9,21,-1,33,6,38,-1,33,39,6,-1,34,33,38,-1,34,38,10,-1,34,10,28,-1,35,39,33,-1,35,8,39,-1,35,20,8,-1,2,28,29,-1,3,21,20,-1,4,33,34,-1,4,35,33,-1,5,31,30,-1,5,30,32,-1,18,32,21,-1,18,21,3,-1,18,5,32,-1,19,20,35,-1,19,3,20,-1,19,35,4,-1,26,17,2,-1,26,2,29,-1,26,29,31,-1,26,31,5,-1,26,5,18,-1,26,18,17,-1,17,18,3,-1,17,3,19,-1,27,17,19,-1,27,19,4,-1,27,4,34,-1,27,34,28,-1,27,28,2,-1,27,2,17,-1] #3
    pointIndexLeaf = [-1.0,1.61803398875,0.0,1.0,1.61803398875,0.0,1.0,-1.61803398875,0.0,-1.0,-1.61803398875,0.0,0.0,-1.0,-1.61803398875,0.0,-1.0,1.61803398875,0.0,1.0,-1.61803398875,0.0,1.0,1.61803398875,-1.61803398875,0.0,-1.0,-1.61803398875,0.0,1.0,1.61803398875,0.0,-1.0,1.61033988758,0.0,1.0,0,1.90213720110728,0,-0.587792720774946,1.53886132132858,0.951068600553639,-0.587792720774946,1.53886132132858,-0.951068600553639,-1.53886132132858,0.951068600553639,-0.587792720774946,-1.53886132132858,0.951068600553639,0.587792720774946,0,-1.90213720110728,0,-0.587792720774946,-1.53886132132858,0.951068600553639,-0.587792720774946,-1.53886132132858,-0.951068600553639,-1.53886132132858,-0.951068600553639,-0.587792720774946,-1.53886132132858,-0.951068600553639,0.587792720774946,0.587792720774946,1.53886132132858,0.951068600553639,0.587792720774946,1.53886132132858,-0.951068600553639,1.53886132132858,0.951068600553639,-0.587792720774946,1.53886132132858,0.951068600553639,0.587792720774946,0.587792720774946,-1.53886132132858,0.951068600553639,0.587792720774946,-1.53886132132858,-0.951068600553639,1.53886132132858,-0.951068600553639,-0.587792720774946,1.53886132132858,-0.951068600553639,0.587792720774946,0,0,1.90213720110728,0.951068600553639,-0.587792720774946,1.53886132132858,-0.951068600553639,-0.587792720774946,1.53886132132858,0,0,-1.90213720110728,0.951068600553639,-0.587792720774946,-1.53886132132858,-0.951068600553639,-0.587792720774946,-1.53886132132858,0.951068600553639,0.587792720774946,1.53886132132858,-0.951068600553639,0.587792720774946,1.53886132132858,0.951068600553639,0.587792720774946,-1.53886132132858,-0.951068600553639,0.587792720774946,-1.53886132132858,1.90213720110728,0,0,-1.90213720110728,0,0] #3
    spineTrunk = [0,0.5,0,0,1,0,0,1.5,0,0,2,0,0,2.5,0,0,3,0,0,3.5,0,0,4,0,0,4.5,0,0,5,0] #3
    scaleTrunk = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5] #2
    crossSection = [1,0,0.707106,-0.707106,0,-1,-0.707106,-0.707106,-1,0,-0.707106,0.707106,0,1,0.707106,0.707106,1,0] #2


    def __init__(self,X=0,Y=0,Z=0):
        self.posTree = [X,Y,Z]


    def toString(self):
        m = randint(0,3)

        stri = "Transform {\n"
        stri += "\ttranslation " + "  ".join(str(x) for x in self.posTree) + "\n"
        stri += "\tscale " + "  ".join(str(x) for x in self.scaleTree) + "\n"
        stri += "\tChildren [\n"

        for z in range(0,1):
            tempLeaf = self.pointIndexLeaf[:]
            tempSpineTrunk = self.spineTrunk[:]
            tempScale = [0.5,0.4,0.5]
            tempTranslation = [0,2.6,0]
            tempRotation = [z,0,-0.4,5]

            stri += "\t\tTransform {\n"
            stri += "\t\t\ttranslation " + "  ".join(str(x) for x in tempTranslation) + "\n"
            stri += "\t\t\trotation " + "  ".join(str(x) for x in tempRotation) + "\n"
            stri += "\t\t\tscale " + "  ".join(str(x) for x in tempScale) + "\n"
            stri += "\t\t\tChildren [\n"

            stri += "\t\t\t\tTransform {\n"
            stri += "\t\t\t\t\ttranslation " + "  ".join(str(x) for x in self.posLeaf) + "\n"
            stri += "\t\t\t\t\tChildren [\n"
            stri += "\t\t\t\t\t\tShape {\n"
            stri += "\t\t\t\t\t\t\tappearance Appearance {\n"
            stri += "\t\t\t\t\t\t\t\tmaterial Material {\n"
            stri += "\t\t\t\t\t\t\t\t\tdiffuseColor " + " ".join(str(x) for x in self.colorLeaf) + "\n"
            stri += "\t\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t\tgeometry IndexedFaceSet {\n"
            stri += "\t\t\t\t\t\t\t\tcoord Coordinate {\n"
            stri += "\t\t\t\t\t\t\t\t\tpoint [\n"
            stri += listStr3(tempLeaf,9 ) + "]\n"
            stri += "\t\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t\t\tcoordIndex [\n"
            stri += listStr3(self.coordIndexLeaf,8) + "]\n"
            stri += "\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t]\n"
            stri += "\t\t\t\t}\n"
            stri += "\t\t\t]\n"
            stri += "\t\t}\n"


        stri += "\t\tTransform {\n"
        stri += "\t\t\ttranslation " + "  ".join(str(x) for x in self.posLeaf) + "\n"
        stri += "\t\t\tChildren [\n"
        stri += "\t\t\t\tShape {\n"
        stri += "\t\t\t\t\tappearance Appearance {\n"
        stri += "\t\t\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\t\t\tdiffuseColor " + " ".join(str(x) for x in self.colorLeaf) + "\n"
        stri += "\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t\tgeometry IndexedFaceSet {\n"
        stri += "\t\t\t\t\t\tcoord Coordinate {\n"
        stri += "\t\t\t\t\t\t\tpoint [\n"
        stri += listStr3(self.pointIndexLeaf,7 ) + "]\n"
        stri += "\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t\tcoordIndex [\n"
        stri += listStr3(self.coordIndexLeaf,6) + "]\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t]\n"
        stri += "\t\t}\n"


        stri += "\t\tShape {\n"
        stri += "\t\t\tappearance Appearance {\n"
        stri += "\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\tdiffuseColor " + " ".join(str(x) for x in self.colorTrunk) + "\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t\tgeometry Extrusion {\n"
        stri += "\t\t\t\t\tccw TRUE\n"
        stri += "\t\t\t\t\tspine [\n"
        stri += listStr3(self.spineTrunk, 5) + "]\n"
        stri += "\t\t\t\t\tscale [\n"
        stri += listStr2(self.scaleTrunk, 5) + "]\n"
        stri += "\t\t\t\t\tcrossSection [\n"
        stri += listStr2(self.crossSection, 5) + "]\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t}\n"
        stri += "\t\t}\n"
        stri += "\t]\n"
        stri += "}\n"

        return stri



def listStr3(list, tab):
    ind = 0
    stri = "\t" * tab + " "
    for x in list:
        ind += 1
        if ind%3 == 0:
            stri += str(x) + ",\n" + "\t" * tab + " "
        else:
            stri += str(x) + " "
    return stri

def listStr2(list, tab):
    ind = 0
    stri = "\t" * tab + " "
    for x in list:
        ind += 1
        if ind%2 == 0:
            stri += str(x) + ",\n" + "\t" * tab + " "
        else:
            stri += str(x) + " "
    return stri

if __name__ == '__main__':
    myTree = Class1()
    print myTree.toString()
