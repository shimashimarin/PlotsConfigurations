import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017_v6
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
btag_algo="deepflav"#deepcsv

eleWP = 'mvaFall17V1Iso_WP90'
muWP = 'cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'CountGenJet',
    'samples': mc
}

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2017']['NLO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    #'expr': '1',
    'expr': '('+DYrew['2017']['LO'].replace('x', 'gen_ptll')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}

# B tagging
if btag_algo == "deepcsv":
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
    }
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'
    }  
elif btag_algo == "deepflav":
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0521) == 0'
    }
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0521) >= 1'
    }

# Flavour definitions

aliases['SameFlav'] = {
    'expr': '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
    'samples': mc
}

aliases['DiffFlav'] = {
    'expr': 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'samples': mc
}

# CR definitions

aliases['topcr'] = {
#    'expr': 'mtw2>30 && mll>50 && ((zeroJet && !bVeto) || bReq)'
    'expr': 'mll>50 && ((zeroJet && !bVeto) || bReq)'
}

aliases['dycr'] = {
    'expr': 'mth<60 && bVeto'
}

aliases['wwcr'] = {
    'expr': 'mth>60 && mtw2>30 && mll>100 && bVeto'
}

# SR definition

aliases['sr'] = {
#    'expr': 'mth>60 && mtw2>30 && bVeto'
    'expr': 'mth>60 && bVeto'
}

aliases['centralVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 30 && CleanJet_eta > TMath::Min(CleanJet_eta[0], CleanJet_eta[1]) && CleanJet_eta < TMath::Max(CleanJet_eta[0], CleanJet_eta[1]) && abs(CleanJet_eta - CleanJet_eta[0]) > 1 && abs(CleanJet_eta - CleanJet_eta[1]) > 1) == 0'        
}

aliases['lowZ'] = {
    'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) < 1'
}

aliases['highZ'] = {
    'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) >= 1'
}

#B tag scale factors
if btag_algo=="deepcsv":
    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
   
    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['btagSF'] = {
        'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
        'samples': mc
    }
    
    for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:


        for targ in ['bVeto', 'bReq']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)
    
            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)
    
        aliases['btagSF%sup' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
            'samples': mc
        }
    
        aliases['btagSF%sdown' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
            'samples': mc
        }

elif btag_algo=="deepflav":
    btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepFlavour_94XSF_V4_B_F.csv' % os.getenv('CMSSW_BASE')
    
    aliases['Jet_btagSF_deepflav_shape'] = {
        'linesToAdd': [
            'gSystem->Load("libCondFormatsBTauObjects.so");',
            'gSystem->Load("libCondToolsBTau.so");',
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L %s/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+' % os.getenv('CMSSW_BASE')
        ],
        'class': 'BtagSF',
        'args': (btagSFSource,'central','deepjet'),
        'samples': mc
    }
    
    
    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['btagSF'] = {
        'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
        'samples': mc
    }
    
    for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
        aliases['Jet_btagSF_deepflav_shape_up_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'up_' + shift,'deepjet'),
            'samples': mc
        }
        aliases['Jet_btagSF_deepflav_shape_down_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'down_' + shift,'deepjet'),
            'samples': mc
        }
    
        for targ in ['bVeto', 'bReq']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_up_%s' % shift)
    
            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_down_%s' % shift)
    
        aliases['btagSF%sup' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
            'samples': mc
        }
    
        aliases['btagSF%sdown' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
            'samples': mc
        }

## puWeight with no division by eras
aliases['puWeight_noeras'] = {
    'class': 'PuWeightNoEras',
    'args': ( '2017','{}/src/PlotsConfigurations/Configurations/patches/PU_profiles_yearly.root'.format(os.getenv('CMSSW_BASE'))),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libPhysicsToolsNanoAODTools.so")',
        '.L %s/src/PlotsConfigurations/Configurations/patches/puWeight_noeras.cc+' % os.getenv('CMSSW_BASE')
    ],
    'samples':mc
}

#### redifine SFweight2l to include the NEW pu weight with noeras
#formulas['SFweight2l'] = 'event.puWeight*\
#                          event.TriggerEffWeight_2l*\
#                          event.Lepton_RecoSF[0]*\
#                          event.Lepton_RecoSF[1]*\
#                          event.EMTFbug_veto \
#                          if event.nLepton > 1 else 0.'

aliases['SFweight2l_noeras'] = {
  'expr': ' * '.join(['puWeight_noeras', 'TriggerEffWeight_2l' , 'Lepton_RecoSF[0]','Lepton_RecoSF[1]','EMTFbug_veto' ]),  
  'samples' : mc
}
 
# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l_noeras', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF', 'PrefireWeight']),
    'samples': mc
}
# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}

