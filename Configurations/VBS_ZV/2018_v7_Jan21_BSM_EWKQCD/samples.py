
import os 
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()
################################################
################# SKIMS ########################
################################################ 

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
dataReco = 'Run2018_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

fakeReco = 'Run2018_102X_nAODv7_Full2018v7'
fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirSMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

def makeMCDirectorySMPeos(var=''):
    if var:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
mcDirectorySMPeos = makeMCDirectorySMPeos() #this was added just for signals 
DirectorySMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

################################################
############# PRIVATE directory ################
################################################

mcDirectory_private = '/eos/user/r/ribrusa/nanoAOD-post/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
           }


#########################################
############ MC COMMON ##################
#########################################

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
quadReweight = '0.5*(LHEReweightingWeight[1]+LHEReweightingWeight[2]-2*LHEReweightingWeight[0])'

###########################################
#############   SIGNALS  ##################
###########################################

#######VBS EW: only ZV processes

### SM EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_SM') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_SM') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_SM') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_SM') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_SM') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_SM')

samples['sm'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 20,
}

### EFTNeg cHDD EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cHDD_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cHDD_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cHDD_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cHDD_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cHDD_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cHDD_SM_LI_QU')

samples['sm_lin_quad_cHDD'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cHDD'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

### EFTNeg cHWB EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cHWB_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cHWB_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cHWB_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cHWB_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cHWB_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cHWB_SM_LI_QU')

samples['sm_lin_quad_cHWB'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cHWB'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

### EFTNeg cll1 EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cll1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cll1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cll1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cll1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cll1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cll1_SM_LI_QU')

samples['sm_lin_quad_cll1'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cll1'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

### EFTNeg cHl1 EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cHl1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cHl1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cHl1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cHl1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cHl1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cHl1_SM_LI_QU')

samples['sm_lin_quad_cHl1'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cHl1'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

### EFTNeg cHl3 EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cHl3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cHl3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cHl3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cHl3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cHl3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cHl3_SM_LI_QU')

samples['sm_lin_quad_cHl3'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cHl3'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

### EFTNeg cHq1 EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cHq1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cHq1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cHq1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cHq1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cHq1_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cHq1_SM_LI_QU')

samples['sm_lin_quad_cHq1'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cHq1'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

### EFTNeg cHq3 EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cHq3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cHq3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cHq3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cHq3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cHq3_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cHq3_SM_LI_QU')

samples['sm_lin_quad_cHq3'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cHq3'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

### EFTNeg cW EWK + QCD

files = nanoGetSampleFiles(mcDirectory_private, 'ZWm_cW_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWp_cW_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZ_cW_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWmQCD_cW_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZWpQCD_cW_SM_LI_QU') + \
        nanoGetSampleFiles(mcDirectory_private, 'ZZQCD_cW_SM_LI_QU')

samples['sm_lin_quad_cW'] = {
   'name': files,
   'weight': mcCommonWeight,
   'FilesPerJob': 10,
}
samples['quad_cW'] = {
   'name': files,
   'weight': mcCommonWeight + '*' + quadReweight,
   'FilesPerJob': 10,
}

###########################################
#############  BACKGROUNDS  ###############
###########################################

########## irreducible VBS QCD 

#samples['VBS_VV_QCD'] = {
#    'name':   nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J_QCD') 
#             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J_QCD')
#             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J_QCD')
#             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_ZTo2L_QCD')
#             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu_QCD')
#             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J_QCD')
#             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J_QCD')
#             +nanoGetSampleFiles(mcDirectory, 'ZTo2L_ZTo2J_QCD')              
#             +nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L_QCD'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 7
#}

########## DY #### consider using HT binned after Davide's studies.
#Beware! we have to correct the cross section here
###### DY #######

useDYtt = False
#weights updated to 2018
ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


if useDYtt:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
        'FilesPerJob': 4,
    }
    addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)


else:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-200to400') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-400to600') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-600toInf') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')
        #nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-70to100') + \ available
#here M-10to50-LO_ext1 are available

    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + "*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                         Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )",
        'FilesPerJob': 4,
        'EventsPerJob' : 70000,
    }

    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext2', 'DY_NLO_pTllrw * (LHE_HT < 100)')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO', 'DY_LO_pTllrw * (LHE_HT < 100)')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200',  'DY_LO_pTllrw * 1.000')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400',  'DY_LO_pTllrw * 0.999')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600',  'DY_LO_pTllrw * 0.990')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800',  'DY_LO_pTllrw * 0.975')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200',  'DY_LO_pTllrw * 0.907')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500',  'DY_LO_pTllrw * 0.833')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf',  'DY_LO_pTllrw * 1.015')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-100to200',  'DY_LO_pTllrw')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-200to400',  'DY_LO_pTllrw')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-400to600',  'DY_LO_pTllrw')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-600toInf',  'DY_LO_pTllrw')

###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1') + \
    nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic') + \
    nanoGetSampleFiles(mcDirectory,'TTZjets') + \
    nanoGetSampleFiles(mcDirectory,'TTWjets')
#this one gives compilatio error with "topGenPt", need to understand why
#these two samples can be considered outside the category "top" to solve this issue...

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','ST_t-channel_top_ext1',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")

######WJets#####

files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf') 
# nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO') + \

samples['WJets'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 2
}

#addSampleWeight(samples,'WJets', 'WJetsToLNu-LO', '(LHE_HT < 70)')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT100_200', '0.993') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT200_400', '1.002') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT400_600', '1.009') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT600_800', '1.120') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT800_1200', '1.202') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT1200_2500', '1.332') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT2500_inf', '4.200') 

###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop'),
    'weight': mcCommonWeight, #+ '*nllW',
    'FilesPerJob': 3
}


# k-factor 1.4 already taken into account in XSWeight
files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

samples['ggWW'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 2
}
######## Vg ########

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(mcDirectory,'ZGToLLG'),
                    'weight' : mcCommonWeightNoMatch +'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 6,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }
#the following baseW correction is needed in v5 and should be removed in v6
#addSampleWeight(samples,'Vg','ZGToLLG','0.448')


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'ZGToLLG')
                                 + nanoGetSampleFiles(mcDirectory,'WZTo3LNu_mllmin01'),
                      'weight' : mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 6,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#0.448 needed in v5 and should be removed in v6
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') #*0.448
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 2
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


########VBF-V##########

files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50')

samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}
###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))



##########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 120
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
