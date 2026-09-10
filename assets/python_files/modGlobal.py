"""
 #Created 28/07/2026 By Roger Wiliams
 
 globals vars
 
 taken from temperature project and modified for this project

"""

#VARS

#folder paths
CNST_STR_DATA_ROOTPATH = "/assets/csv"
CNST_STR_DATA_PATH = CNST_STR_DATA_ROOTPATH + "/Data"
CNST_STR_DATA_EXTRACTEDPATH = CNST_STR_DATA_ROOTPATH +"/ExtractedFiles"
CNST_STR_DATA_ORIGINALPATH = CNST_STR_DATA_ROOTPATH +"/OriginalFiles"
CNST_STR_DATA_WORKINGPATH = CNST_STR_DATA_ROOTPATH +"/WorkingFiles"
CNST_STR_DATA_CLEANEDPATH = CNST_STR_DATA_ROOTPATH +"/CleanedFiles"
CNST_STR_DATA_VISUALISATIONPATH = CNST_STR_DATA_ROOTPATH +"/VisualisationFiles"
CNST_STR_PIPELINESPATH = "assets/pipelines"

#need these two modified paths as ML for some reason does not like the /assets prefix
CNST_STR_MLPIPELINESPATH = "assets/pipelines"
CNST_STR_MLREPORTIMAGESPATH = "reports/images"


#file name appenders
CNST_STR_FILENAME_APPEND_CLEANED = "_Cleaned"
CNST_STR_FILENAME_APPEND_WORKING = "_Working"
CNST_STR_FILENAME_APPEND_VISUALISATION = "_Visualisation"

#constant for project directory
CNST_STR_PROJECT_DIR = "Spotify-Music-Trend-Analysis"

#file path constants
CNST_STR_CLEANFILENAME = "spotifydataset_Cleaned.csv"
CNST_STR_FILENAME = "spotifydataset.csv"
CNST_STR_RAWFILEFORETL = "spotifydataset.csv"


#default container size for tabs
CNST_INT_CONTAINTER_HEIGHT = 800
CNST_INT_INNER_CONTAINTER_HEIGHT = 780

dfWorking = None