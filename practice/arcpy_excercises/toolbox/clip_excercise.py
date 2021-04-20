#pyt to imitate clip
import arcpy

def clip(param_list):
    FC1 = param_list[0].valueAsText

class Toolbox(object):
    def __init__(self):
        self.label = "Bay_Hexation"
        self.alias = "Bay Hex"
        # List of tool classes associated with this toolbox
        self.tools = [Bay_Hexing]

class Bay_Hexing(object):
    def __init__(self):
        self.label = "Create Hexagons for Bay Polygon"
        self.description = "Create hexagon polygons for bay polygons that " + \
                           "are similar in size, clipped to and networked to" + \
                           " coastal NHDPlus catchments."

    def getParameterInfo(self):
        inFC = arcpy.Parameter(displayName = "Wrong Name 1",
                              name = "inPoly",
                              datatype = "GPFeatureLayer",
                              parameterType = "Required",
                              direction = "Input")
        clipFC = arcpy.Parameter(displayName = "Wrong Name 2",
                              name = "inPoly2",
                              datatype = "GPFeatureLayer",
                              parameterType = "Required",
                              direction = "Input")
        output = arcpy.Parameter(displayName = "Output",
                                 name = "outPoly",
                                 datatype = "DEFeatureClass",
                                 parameterType = "Required",
                                 direction = "Output")
        params = [inFC, output]
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, params):
        return

    def updateMessages(self, params):
        return

    def execute(self, params, messages):
        #try:
        clip(params)
        #except:
