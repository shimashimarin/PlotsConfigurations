# nuisances
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc_eft = [skey for skey in samples if 'quad_' in skey] + ['sm']
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake') and not skey in mc_eft]
except NameError:
    mc_eft = []
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()


################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2018',
#    'type': 'lnN',
#    'samples': dict((skey, '1.023') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc+mc_eft if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc+mc_eft if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc+mc_eft if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc+mc_eft if skey not in ['WW', 'top', 'DY'])
}

#### FAKES
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst_em',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc+mc_eft),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc+mc_eft), 
}



##### Electron Efficiency and energy scale  
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc+mc_eft), 
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    #'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VBS_ZV','VBS_VV_QCD']),
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'WJets']),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    #'AsLnN': '1'
}
#this is for the signals since they are in a different eos folder
nuisances['electronpt_VBS_ZV'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    #'samples': {"VBS_ZV":[1.,1.]},
    'samples': dict({"sm":[1.,1.]}.items() + dict((skey, ['1', '1']) for skey in mc_eft).items()),
    'folderUp': mcDirectory_private+'__ElepTup_suffix',
    'folderDown': mcDirectory_private+'__ElepTdo_suffix',
    #'AsLnN': '1'
}#add QCD_VV when ready


##### Muon Efficiency and energy scale  
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc+mc_eft),
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    #'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VBS_ZV','VBS_VV_QCD']),
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'WJets']),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    #'AsLnN': '1'
}
#this is for the signals
nuisances['muonpt_VBS_ZV'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    #'samples': {"VBS_ZV":[1.,1.]},
    'samples': dict({"sm":[1.,1.]}.items() + dict((skey, ['1', '1']) for skey in mc_eft).items()),
    'folderUp': mcDirectory_private+'__MupTup_suffix',
    'folderDown': mcDirectory_private+'__MupTdo_suffix',
    #'AsLnN': '1'
}#add QCD_VV when ready



##### Jet energy scale and reso for AK4
##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']
folderup = ""
folderdo = ""
folderup_signal = ""
folderdo_signal = ""

for js in jes_systs:
  if 'Absolute' in js: 
    folderup = makeMCDirectory('JESAbsoluteup_suffix')
    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
  elif 'BBEC1' in js:
    folderup = makeMCDirectory('JESBBEC1up_suffix')
    folderdo = makeMCDirectory('JESBBEC1do_suffix')
  elif 'EC2' in js:
    folderup = makeMCDirectory('JESEC2up_suffix')
    folderdo = makeMCDirectory('JESEC2do_suffix')
  elif 'HF' in js:
    folderup = makeMCDirectory('JESHFup_suffix')
    folderdo = makeMCDirectory('JESHFdo_suffix')
  elif 'Relative' in js:
    folderup = makeMCDirectory('JESRelativeup_suffix')
    folderdo = makeMCDirectory('JESRelativedo_suffix')
  elif 'FlavorQCD' in js:
    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')

  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      #'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VBS_ZV','VBS_VV_QCD']),
      'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'WJets']),
      'folderUp': folderup,
      'folderDown': folderdo,
#      'AsLnN': '1'
  }

#this is for signals
for js_VBS_ZV in jes_systs:
  if 'Absolute' in js_VBS_ZV: 
    folderup_signal = DirectorySMPeos+'__JESAbsoluteup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESAbsolutedo_suffix'
  elif 'BBEC1' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESBBEC1up_suffix'
    folderdo_signal = DirectorySMPeos+'__JESBBEC1do_suffix'
  elif 'EC2' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESEC2up_suffix'
    folderdo_signal = DirectorySMPeos+'__JESEC2do_suffix'
  elif 'HF' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESHFup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESHFdo_suffix'
  elif 'Relative' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESRelativeup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESRelativedo_suffix'
  elif 'FlavorQCD' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESFlavorQCDup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESFlavorQCDdo_suffix'
  """
  nuisances[js_VBS_ZV] = {
      'name': 'CMS_scale_'+js_VBS_ZV,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js_VBS_ZV+'up',
      'mapDown': js_VBS_ZV+'do',
      #'samples': {"VBS_ZV":[1.,1.]},
      'samples': {"sm":[1.,1.]},
      'folderUp': folderup_signal,
      'folderDown': folderdo_signal,
#      'AsLnN': '1'
  }#add QCD_VV when ready
  """
nuisances['JESTotal'] = {
    'name': 'CMS_scale_JESTotal',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JESup',
    'mapDown': 'JESdo',
    #'samples': {"VBS_ZV":[1.,1.]},
    'samples': dict({"sm":[1.,1.]}.items() + dict((skey, ['1', '1']) for skey in mc_eft).items()),
    'folderUp': mcDirectory_private+'__JESTotalup_suffix',
    'folderDown': mcDirectory_private+'__JESTotaldo_suffix',
}

##### Jet energy resolution
nuisances['JER'] = {
    'name': 'CMS_res_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    #'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VBS_ZV','VBS_VV_QCD']),
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'WJets']),
    'folderUp': makeMCDirectory('JERup_suffix'),
    'folderDown': makeMCDirectory('JERdo_suffix'),
#    'AsLnN': '1'
}

#this is for the signal
nuisances['JER_VBS_ZV'] = {
    'name': 'CMS_res_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    #'samples': {"VBS_ZV":[1.,1.]},
    'samples': dict({"sm":[1.,1.]}.items() + dict((skey, ['1', '1']) for skey in mc_eft).items()),
    'folderUp': mcDirectory_private+'__JERup_suffix',
    'folderDown': mcDirectory_private+'__JERdo_suffix',
#    'AsLnN': '1'
}#add QCD_VV when ready


# ##### Pileup
pu_syst = '(puWeightUp/puWeight)', '(puWeightDown/puWeight)'

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc+mc_eft),
#    'AsLnN': '1',
}





#####################
##### PS, QCD scale, UE 
#####################
#samples_PS = ['VBS_ZV','top','DY','VV','VVV','Vg','VgS','VBF-V','ggWW']  #add VBS_QCD_VV when ready on SMP eos
samples_PS = ['sm','top','DY','VV','VVV','Vg','VgS','VBF-V','ggWW']+mc_eft

for sample in samples_PS:
    nuisances['PS_ISR_'+sample]  = {
                    'name'  : 'CMS_PS_ISR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample : ['PSWeight[2]', 'PSWeight[0]'],
                    }
                }
    nuisances['PS_FSR_'+sample]  = {
                    'name'  : 'CMS_PS_FSR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample :  ['PSWeight[3]', 'PSWeight[1]'], 
                    }
                }
"""
#outdated ones.
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
        'ggWW'   : ['1.040233912070831*(nCleanGenJet==0) + 0.9611236379290876*(nCleanGenJet==1) + 0.9014289294088699*(nCleanGenJet==2) + 0.864310738090035*(nCleanGenJet>=3)', '0.9510305474211223*(nCleanGenJet==0) + 1.0433432942960381*(nCleanGenJet==1) + 1.1271383507266095*(nCleanGenJet==2) + 1.1885756983901514*(nCleanGenJet>=3)'],
        'WW'     : ['1.0005237869294796*(nCleanGenJet==0) + 1.0157425373134328*(nCleanGenJet==1) + 0.9644598124510606*(nCleanGenJet==2) + 0.9271488926223369*(nCleanGenJet>=3)', '0.9993553300024391*(nCleanGenJet==0) + 0.9806102300995024*(nCleanGenJet==1) + 1.042603303739856*(nCleanGenJet==2) + 1.0950369125887705*(nCleanGenJet>=3)'],
        'top'    : ['1.0020618369910668*(nCleanGenJet==0) + 1.0063081530771556*(nCleanGenJet==1) + 1.0094298425968304*(nCleanGenJet==2) + 0.9854207999040726*(nCleanGenJet>=3)', '0.9974340279269026*(nCleanGenJet==0) + 0.9920634820709106*(nCleanGenJet==1) + 0.988226385054923*(nCleanGenJet==2) + 1.017968568319235*(nCleanGenJet>=3)'],
        'DY'     : ['0.9998177685645392*(nCleanGenJet==0) + 1.0080838149428026*(nCleanGenJet==1) + 1.0057948912950987*(nCleanGenJet==2) + 0.9721358221196619*(nCleanGenJet>=3)', '1.0003244155266309*(nCleanGenJet==0) + 0.9897992135367016*(nCleanGenJet==1) + 0.9928782069009531*(nCleanGenJet==2) + 1.0348902921423981*(nCleanGenJet>=3)'],
        'VVV'    : ['1.0270826786253018*(nCleanGenJet==0) + 1.0198703447307862*(nCleanGenJet==1) + 1.0109191915514344*(nCleanGenJet==2) + 0.9838184220287978*(nCleanGenJet>=3)', '0.9661665482954546*(nCleanGenJet==0) + 0.9751744967838527*(nCleanGenJet==1) + 0.9859624782745712*(nCleanGenJet==2) + 1.0202995039288625*(nCleanGenJet>=3)'],
    },
    'AsLnN'      : '1',
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
        'ggWW'   : ['0.9910563426395067*(nCleanGenJet==0) + 1.0069894351287263*(nCleanGenJet==1) + 1.016616376034912*(nCleanGenJet==2) + 1.015902717074592*(nCleanGenJet>=3)', '1.0147395976461193*(nCleanGenJet==0) + 0.9860219489006646*(nCleanGenJet==1) + 0.9694680606617647*(nCleanGenJet==2) + 0.9489845115821678*(nCleanGenJet>=3)'],
        'WW'     : ['0.995462478372054*(nCleanGenJet==0) + 1.0052129975124378*(nCleanGenJet==1) + 1.008836750560578*(nCleanGenJet==2) + 0.9984120564941189*(nCleanGenJet>=3)', '1.008927720738437*(nCleanGenJet==0) + 0.995163868159204*(nCleanGenJet==1) + 0.9911024228315418*(nCleanGenJet==2) + 0.9763787172658678*(nCleanGenJet>=3)'],
        'top'    : ['0.9910899786333963*(nCleanGenJet==0) + 0.9990635702054794*(nCleanGenJet==1) + 1.002141744200183*(nCleanGenJet==2) + 1.0129742776372779*(nCleanGenJet>=3)', '1.0068843378231833*(nCleanGenJet==0) + 0.998988498438759*(nCleanGenJet==1) + 0.9952696584115224*(nCleanGenJet==2) + 0.9790955840673237*(nCleanGenJet>=3)'],
        'DY'     : ['0.9958763409773141*(nCleanGenJet==0) + 1.0041335498093422*(nCleanGenJet==1) + 1.0163363150953029*(nCleanGenJet==2) + 1.0296733670670226*(nCleanGenJet>=3)', '1.0066775262249232*(nCleanGenJet==0) + 0.9945601465681602*(nCleanGenJet==1) + 0.9662459619335311*(nCleanGenJet==2) + 0.9479423453563661*(nCleanGenJet>=3)'],
        'VVV'    : ['0.9809047855490748*(nCleanGenJet==0) + 0.9823641498350338*(nCleanGenJet==1) + 0.9976414629808243*(nCleanGenJet==2) + 1.0077953569413387*(nCleanGenJet>=3)', '1.035388723727876*(nCleanGenJet==0) + 1.0347339790465233*(nCleanGenJet==1) + 1.0017058788771533*(nCleanGenJet==2) + 0.9829344116371653*(nCleanGenJet>=3)'],
    },
    'AsLnN'      : '1',
}
"""
# # Theory nuisance: QCD scale
## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
#qcdscale_variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
#for sample in mc :
#    if sample == 'VBS_ZV' :
#        nuisances['QCD_scale_VBS'] = {
#            'name'  : 'QCDscale_'+sample,
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
#        }
for sample in mc+mc_eft:
    if sample == "ggWW": continue   #this sample apparently doesn't have LHE weights...
    if sample == "VBS_VV_QCD": continue   ##once SMP eos VBS_VV_QCD are ready comment out 
    nuisances['QCD_scale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
        }

# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet 
nuisances['UE']  = {
                'name'  : 'UE_CUET',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc+mc_eft),
}


####### Generic "cross section uncertainties"
"""
apply_on = {
    'top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}
"""
## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True
}

nuisances['VgStar'] = {
    'name': 'CMS_hww_VgStarScale',
    'type': 'lnN',
    'samples': {
        'VgS_L': '1.25'
    }
}

nuisances['VZ'] = {
    'name': 'CMS_hww_VZScale',
    'type': 'lnN',
    'samples': {
        'VgS_H': '1.16'
    }
}


####PDF syst, needs to be updated for signals
nuisances['pdf']  = {
               'name'  : 'pdf',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW'    : '1.05',
                   'WW'      : '1.04',
                   'Vg'      : '1.04',
                   'VZ'      : '1.04',
                   'VgS'     : '1.04',
                   'DY'      : '1.002', 
                   },
              }




## rate parameters
nuisances['Topnorm_boosted']  = {
               'name'  : 'Topnorm_boosted_2018',
               'samples'  : {
                   'top' : '1',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Boosted_topcr',
                   #'Boosted_SR_Ram',
                   'Boosted_SR_tight',
                   ]
              }

nuisances['Topnorm_resolved']  = {
               'name'  : 'Topnorm_resolved_2018',
               'samples'  : {
                   'top' : '1',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Resolved_topcr',
                   #'Resolved_SR_Ram',
                   'Resolved_SR_tight',
                   ]
              }              

nuisances['DYnorm_boosted']  = {
               'name'  : 'DYnorm_boosted_2018',
               'samples'  : {
                   'DY' : '1',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   #'Boosted_SR_Ram',
                   'Boosted_SR_tight',
                   'Boosted_DYcr',
                   ]
              }   

nuisances['DYnorm_resolved']  = {
               'name'  : 'DYnorm_resolved_2018',
               'samples'  : {
                   'DY' : '1',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   #'Resolved_SR_Ram',
                   'Resolved_SR_tight',
                   'Resolved_DYcr',
                   ]
              }   

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '1',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}


for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))
