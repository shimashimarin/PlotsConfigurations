# configuration file

treeName= 'Events'

date = '_feb10'

version = '_v0'

tag = 'VBS_SS'  + date + version


# used by mkShape to define output directory for root files
outputDir = 'rootFile' + '_' +  tag

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
samplesFile = 'samples.py'

# file with list of samples
plotFile = 'plot_sr_group.py'

# luminosity to normalize to (in 1/fb)
lumi = 41.53 

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plots' + '_' + tag

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards' + '_' + tag

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
