import os
import inspect

# FIX THIS in dependence of where this file is stored, in order to correctly locate the macros in Differential and Patches folder
# check also in samples.py
configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2018 folder
configurations = os.path.dirname(configurations) # EFT
configurations = os.path.dirname(configurations) # VBS, Differential & Patches level
configurations = os.path.dirname(configurations) # Configurations level

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

mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction = 'Autumn18_102X_nAODv6_Full2018v6'
mcSteps = 'MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6{var}'

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'

################################################
############ BASIC MC WEIGHTS ##################
################################################

mcCommonWeightNoMatch = 'SFweight'
#mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*59.74'
mcCommonWeight = 'SFweight*PromptGenLepMatch2l'

################################################
############### B-Tag  WP ######################
################################################

# Definitions in aliases.py

# SFweight += '*btagSF'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'
METFilter_FAKE = 'METFilter_FAKE'

################################################
############ DATA DECLARATION ##################
################################################

DataRun_2018 = [
    ['A','Run2018A-Nano25Oct2019-v1'] ,
    ['B','Run2018B-Nano25Oct2019-v1'] ,
    ['C','Run2018C-Nano25Oct2019-v1'] ,
    ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,
]

DataSets_2018 = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig_2018 = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}
###########################################
############  Reducible Bkg  ##############
###########################################

# # -------------------- mis-charge single-sample --------------------------------

# # DY , top, WW, HWW 
# files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
#         nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1') + \
#         nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_s-channel_ext1') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1') + \
#         nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu') + \
#         nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2NuPowheg_M125') + \
#         nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125')

# samples['mischarge'] = {
#     'name': files,
#     'weight': mcCommonWeight + '*chargeflip_w*1.3',  # SF=1.3 measured in Full2018_cr_mischarge (SS Z->ee region)
#     'FilesPerJob': 4
# }

# # DY weights
# DY_common_weight = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'
# addSampleWeight(samples,'mischarge','DYJetsToLL_M-50_ext2',DY_common_weight)
# addSampleWeight(samples,'mischarge','DYJetsToLL_M-10to50-LO_ext1',DY_common_weight)

# ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
# ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
# addSampleWeight(samples,'mischarge','DYJetsToLL_M-50_ext2',ptllDYW_NLO)
# addSampleWeight(samples,'mischarge','DYJetsToLL_M-10to50-LO_ext1',ptllDYW_LO)

# # top weights
# addSampleWeight(samples,'mischarge','TTTo2L2Nu','Top_pTrw')

# # WW weights
# WW_weight = 'nllW'
# addSampleWeight(samples,'mischarge','WWTo2L2Nu',WW_weight)

# WW_ewk_weight = '(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)' #filter tops and Higgs
# addSampleWeight(samples,'mischarge','WpWmJJ_EWK',WW_ewk_weight)

# ggWW_weight = '(1.53/1.4)' # updating k-factor
# addSampleWeight(samples,'mischarge','GluGluToWWToENEN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToENMN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToENTN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToMNEN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToMNMN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToMNTN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToTNEN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToTNMN',ggWW_weight)
# addSampleWeight(samples,'mischarge','GluGluToWWToTNTN',ggWW_weight)

# # HWW (ggH) weights
# addSampleWeight(samples,'mischarge','GluGluHToWWTo2L2NuPowheg_M125','Weight2MINLO')

# # -------------------- mis-charge single-sample --------------------------------

# ######## Vg ########  

# files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
#     nanoGetSampleFiles(mcDirectory, 'Zg')

# samples['Vg'] = {
#     'name': files,
#     'weight': mcCommonWeightNoMatch + '*(Gen_ZGstar_mass <= 0)',
#     'FilesPerJob': 3
# }
# # the following is needed in both v5 and v6
# addSampleWeight(samples, 'Vg', 'Zg', '0.448')

# ######## VgS ####### 

# files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
#         nanoGetSampleFiles(mcDirectory, 'Zg') + \
#         nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

# samples['VgS'] = {
#     'name': files,
#     'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#     'FilesPerJob': 3,
#     'subsamples': {
#       'L': 'gstarLow',
#       'H': 'gstarHigh'
#     }
# }
# addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
# addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0)*0.448')
# # applied gen level cut to cover mass from 0.1 to 4.0
# addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass < 4.0 )') 

# ######### VV #########
# files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext1') + \
#         nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
#         nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext1')
#         #nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
#         #nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')

# samples['ZZ'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 3
# }

# # not needed, os lepton charges, so it will be included in the mischarge sample that has to be added yet.
# # for the time being, we just remove it since it gives very small contributions
# # files = nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')
# # samples['WZTo2L2Q'] = {
# #     'name': files,
# #     'weight': mcCommonWeight,
# #     'FilesPerJob': 4
# # }

# files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_2Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_1Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
#         nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet')


# samples['WZ_QCD'] = {
#     'name': files,
#     'weight': mcCommonWeight+'*1.2',
#     'FilesPerJob': 3
# }

# #files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-60_EWK_4F')# + \
#         #nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To60_EWK_4F')

# files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')

# samples['WLLJJ_EWK'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 3
# }
# ########## VVV #########

# files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
#         nanoGetSampleFiles(mcDirectory, 'WZZ') + \
#         nanoGetSampleFiles(mcDirectory, 'WWZ') + \
#         nanoGetSampleFiles(mcDirectory, 'WWW')
        
# samples['VVV'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 3
# }

# ########## TTV #########

# files = nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
#         nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
#         nanoGetSampleFiles(mcDirectory, 'tZq_ll')
        
# samples['TTV'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 2
# }
# ########## DPS #########
# files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')

# samples['DPS'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 3
# }
# ###########################################
# #######  IRREDUCIBLE BACKGROUNDS  #########
# ###########################################

# files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')

# samples['WW_QCD'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 3
# }
###########################################
#############   SIGNALS  ##################
###########################################

# files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')

# samples['WpWp_EWK'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }

###########################################
#############  EFT samples  ###############
###########################################

# cW (old first sample) and sm sample position
EftDirectoryOld = '/afs/cern.ch/work/j/jixiao/public/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6'
# All EFT operators
EftDir = '/eos/user/j/jixiao/HWWnano3/eft/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6'

# SM Term
# files = nanoGetSampleFiles(EftDirectoryOld, 'SSWW_SM')
# samples['sm'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }

# cHbox # gives "bogus norm" problem
# linear term has negative events
files = nanoGetSampleFiles(EftDir, 'cHbox_int')
samples['linear_cHbox'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cHbox_bsm')
# samples['quadratic_cHbox'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cHDD # gives "bogus norm" problem
# linear term has negative events
files = nanoGetSampleFiles(EftDir, 'cHDD_int')
samples['linear_cHDD'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cHDD_bsm')
# samples['quadratic_cHDD'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cHq3
files = nanoGetSampleFiles(EftDir, 'cHq3_int')
samples['linear_cHq3'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cHq3_bsm')
# samples['quadratic_cHq3'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cHWB # gives "bogus norm" problem
# linear term has negative events
files = nanoGetSampleFiles(EftDir, 'cHWB_int')
samples['linear_cHWB'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cHWB_bsm')
# samples['quadratic_cHWB'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cHW
files = nanoGetSampleFiles(EftDir, 'cHW_int')
samples['linear_cHW'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
files = nanoGetSampleFiles(EftDir, 'cHW_bsm')
# samples['quadratic_cHW'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cll1
files = nanoGetSampleFiles(EftDir, 'cll1_int')
samples['linear_cll1'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
files = nanoGetSampleFiles(EftDir, 'cll1_bsm')
# samples['quadratic_cll1'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cqq11 # gives "bogus norm" problem
# linear term has negative events
files = nanoGetSampleFiles(EftDir, 'cqq11_int')
samples['linear_cqq11'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cqq11_bsm')
# samples['quadratic_cqq11'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cqq1 # gives "bogus norm" problem
# linear term has negative events
files = nanoGetSampleFiles(EftDir, 'cqq1_int')
samples['linear_cqq1'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cqq1_bsm')
# samples['quadratic_cqq1'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cqq31 # gives "bogus norm" problem
# linear term has negative events
files = nanoGetSampleFiles(EftDir, 'cqq31_int')
samples['linear_cqq31'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cqq31_bsm')
# samples['quadratic_cqq31'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cqq3 # gives "bogus norm" problem
# linear term has negative events
files = nanoGetSampleFiles(EftDir, 'cqq3_int')
samples['linear_cqq3'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cqq3_bsm')
# samples['quadratic_cqq3'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# cW
files = nanoGetSampleFiles(EftDir, 'cW_int')
samples['linear_cW'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
# files = nanoGetSampleFiles(EftDir, 'cW_bsm')
# samples['quadratic_cW'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1
# }

# # cHl1_int missing???

# ###########################################
# ################## FAKE ###################
# ###########################################
# #1389 files

# fakeDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__fakeW'

# samples['Fake_lep'] = {
#     'name': [],
#     'weight': 'METFilter_DATA*fakeW',
#     'weights': [],
#     'isData': ['all'],
#     'FilesPerJob': 17
# }

# for _, sd in DataRun_2018:
#     for pd in DataSets_2018:
#         files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
#         samples['Fake_lep']['name'].extend(files)
#         samples['Fake_lep']['weights'].extend([DataTrig_2018[pd]] * len(files))

# ###########################################
# ################## DATA ###################
# ###########################################

# dataDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6'

# samples['DATA'] = {
#     'name': [],
#     'weight': 'METFilter_DATA*LepWPCut',
#     'weights': [],
#     'isData': ['all'],
#     'FilesPerJob': 17
# }

# for _, sd in DataRun_2018:
#     for pd in DataSets_2018:
#         files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
#         samples['DATA']['name'].extend(files)
#         samples['DATA']['weights'].extend([DataTrig_2018[pd]] * len(files))

