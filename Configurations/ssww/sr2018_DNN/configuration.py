# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_sr2018_DNN'

tag = 'VBS_SS'+date


# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date

# file with TTree aliases
aliasesFile = 'aliases_plot.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts_plot.py'
#cutsFile = 'cuts_forPlots.py'

# file with list of samples
samplesFile = 'samples_plot.py'

# file with list of samples
plotFile = 'plot.py'

# luminosity to normalize to (in 1/fb)
lumi =59.74 

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plotVBS'+date


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'+date


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'total_nuisances.py'
