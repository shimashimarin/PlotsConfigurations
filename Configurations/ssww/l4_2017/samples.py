import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
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

#mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'
mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6/'
mcDir_private='/eos/user/j/jixiao/HWWnano3/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction = 'Autumn18_102X_nAODv6_Full2018v6'
mcSteps = 'MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6{var}'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'SFweight'
mcCommonWeight = 'SFweight*PromptGenLepMatch4l'
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['B','Run2017B-Nano1June2019-v1'] ,
    ['C','Run2017C-Nano1June2019-v1'] ,
    ['D','Run2017D-Nano1June2019-v1'] ,
    ['E','Run2017E-Nano1June2019-v1'] ,
    ['F','Run2017F-Nano1June2019-v1'] ,
]
DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']
DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}
###########################################
############  Reducible Bkg  ##############
###########################################
### Signal
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
samples['WpWp_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### Interference
# need:
# WpWpJJ_Interference_TuneCUETP8M1_13TeV-madgraph-pythia8
# WLLJJ_WToLNu_Interference_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8
#files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_Interference')
#samples['WpWpJJ_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_Interference')
#samples['WLLJJ_WToLNu_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

### WW QCD
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### WZ QCD
files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet')
samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.2',
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu')
samples['WZ_QCD_AMCNLO'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['WZ_QCD_mllmin01'] = {
    'name': files,
    'weight': mcCommonWeight+'*(Gen_ZGstar_mass > 4)',
    'FilesPerJob': 4
}

### ZZ
# need:
# ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8
# ZZJJTo4L_QCD_TuneCP5_13TeV-madgraph-pythia8
# GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8
# GluGluToContinToZZTo4tau:ggZZ4t_CP5
# ggZZ2e2t
files = nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')
samples['ZZTo4L_ext2'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ggZZ2m2t_CP5') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2m') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2t_v3') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4m_ext2')
samples['ggZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### TVX
# need:
# TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8
# TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8
# TTWJetsToQQ_TuneTuneCP5_13TeV-amcatnloFXFX-madspin-pythia8

files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll')
samples['TVX'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### Vg
# need: 
# LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# old: WGJJ Zg
files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

files = nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['VgS1'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS1', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS1', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

### Wrong-sign
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')
samples['WW'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop')
samples['Top'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

# MIT: 
# DY0JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY1JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY2JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY3JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY0JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY1JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY2JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY3JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
ptllDYW_NLO = '(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')
samples['DY'] = {
    'name': files,
    'weight': 'mcCommonWeight_os*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
        Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 17,
}
# need:
# GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV714_pythia8
# # not found: VBFHToZZTo4L_M125_13TeV_powheg2_JHUGenV714_pythia8
# VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8
files = nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125') + \
        nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125') + \
        nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125')
samples['Higgs'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}
# Others
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')
samples['DPS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW') + \
        nanoGetSampleFiles(mcDirectory, 'WWG') 
samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
################## FAKE ###################
###########################################
#1389 files
samples['Fake_lep'] = {
    'name': [],
    'weight': 'METFilter_DATA*fakeW*(Alt$(Lepton_pdgId[0],-9999)*Alt$(Lepton_pdgId[1],9999)>0)',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}
for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__fakeW/', pd + '_' + sd)
        samples['Fake_lep']['name'].extend(files)
        samples['Fake_lep']['weights'].extend([DataTrig[pd]] * len(files))
###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut*(Alt$(Lepton_pdgId[0],-9999)*Alt$(Lepton_pdgId[1],9999)>0)',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6/', pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
