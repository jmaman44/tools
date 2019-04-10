import re

#Node Class
class ScaffNode:
    def __init__(self,data,ind):
        #Class Attributes
        self.order = ind
        self.name = re.search(r'NODE_\d+',data).group(0)
        self.NodeLength = int(re.search(r'(?<=th_)\d+',data).group(0))
        self.start = int(re.search(r'(?<=:)\d+',data).group(0))
        self.stop = int(re.search(r'(?<=-)\d+',data).group(0))
        self.span = self.stop - self.start + 1

        def getNumber():
            return int(re.search(r'\d+',self.name).group(0))

#Scaffold Class
class Scaffold:
        def __init__(self,data):
            #Class Attributes
            RegName = re.search(r'Scaffold_\d+',data)
            NodeData = data[RegName.span()[1]:]
            self.name = RegName.group(0)
            ind = 1
            self.nodes = [ScaffNode(InData,NodeData.index(InData)) for InData in NodeData.split("...")]
            self.links = []
            loc = 0
            for nd in self.nodes:
                loc += nd.span
                self.links.append(loc)
            self.length = self.links.pop()

            def getNumber():
                return int(re.search(r'\d+',self.name).group(0))

#Generate array for Scaffold name and location
def getLookUp(ln):
    scaf = Scaffold(ln)
    return [scaf.name + ":" + str(lk) for lk in scaf.links]

#Make file Scaffold names and locations
def Run():
    #input file name
    filename = "scaffolds_V3.fasta.links"
    finarr = []
    with open(filename) as f:
        line = 1
        while(line):
            line = f.readline()
            try:
                finarr += getLookUp(line)
            except AttributeError:
                continue
    f.close()
    #output file name
    g = open("outfile.txt","w+")
    g.write("\n".join(finarr))
    g.close()

    
Run()
