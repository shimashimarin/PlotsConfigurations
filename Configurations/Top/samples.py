# samples

#samples = {}
    
#                    
#samples['DY']  = {    'name': ['latino_DYJetsToLL_M-50.root', 'latino_DYJetsToLL_M-10to50.root'],     #   file name    
                      #'weight' : 'baseW*puW',              #   weight/cut 
                      #'weights': ['GEN_weight_SM/abs(GEN_weight_SM) / 0.670032', 'GEN_weight_SM/abs(GEN_weight_SM) / 0.72760']                       #   additional cuts file dependent
                      ##'weights': ['0.66998', '0.72760'] ,                      #   additional cuts file dependent
                  #}

#samples['DY']  = {    'name': ['latino_DYJetsToLL_M-10to50.root'],     #   file name    
#                      'weight' : 'baseW*puW',              #   weight/cut 
                      #'weights': ['GEN_weight_SM/abs(GEN_weight_SM) / 0.670032', 'GEN_weight_SM/abs(GEN_weight_SM) / 0.72760']                       #   additional cuts file dependent
                      #'weights': ['0.66998', '0.72760'] ,                      #   additional cuts file dependent
#                  }

#samples['ttbar'] = {   'name': ['latino_TTJets.root'],         #   file name    
                       #'weight' : 'baseW',                     #   weight/cut 
                       ##'weights': ['0.33166']             #   additional cuts file dependent --> e.g. from +/- weights in MC
                       #'weights': ['GEN_weight_SM/abs(GEN_weight_SM) * 0.33166']             #   additional cuts file dependent --> e.g. from +/- weights in MC
                   #}



#samples['Wjets']  = {    'name': ['latino_WJetsToLNu.root'],     #   file name    
#                      'weight' : 'baseW*puW',              #   weight/cut 
#                      'weights': ['GEN_weight_SM/abs(GEN_weight_SM) / 0.683927 * 61526.7 / 20508.9']                       #   additional cuts file dependent
#                  }


#samples['FakeQCD']  = {    'name': ['latino_QCD_Pt-30to50_EMEnriched.root', 'latino_QCD_Pt-30toInf_DoubleEMEnriched.root', 'latino_QCD_Pt-50to80_EMEnriched.root', 'latino_QCD_Pt-15to20_MuEnrichedPt5.root'],     #   file name    
                      #'weight' : 'baseW*puW',              #   weight/cut 
                      #'weights': ['-', '-', '-', '-']                       #   additional cuts file dependent
                  #}


#samples['ttbar'] = {   'name': ['latino_TT.root'],         #   file name    
                       #'weight' : 'baseW',                 #   weight/cut 
                       ##'weights': ['0.33166']             #   additional cuts file dependent --> e.g. from +/- weights in MC
                       #'weights': ['1']                    #   additional cuts file dependent --> e.g. from +/- weights in MC
                   #}

samples['ttbar'] = {   'name': ['latino_TT_skim.root'],          
                       'weight' : 'baseW*puW',                
                       #'weights': ['GEN_weight_SM/abs(GEN_weight_SM) / 0.331907'],           
                       'weights': ['1']                   
                   }

#samples['top'] = {   'name': ['latino_ST_tW_top.root', 'latino_ST_tW_antitop.root', 'latino_ST_t-channel.root'],   
                       #'weight' : 'baseW*puW',                
                       #'weights': ['1', '1', 'GEN_weight_SM/abs(GEN_weight_SM) / 0.215131' ]            
                   #}


#samples['top'] = {   'name': ['latino_ST_t-channel.root'],   
#                       'weight' : 'baseW*puW',                
#                       'weights': ['GEN_weight_SM/abs(GEN_weight_SM) / 0.215131' ]            
#                   }


samples['WW']  = {    'name': ['latino_WWTo2L2Nu.root'],      
                      'weight' : 'baseW', #*puW manca!          
                  #    'weights': ['1']            
                  }

#samples['WZ']  = {    'name': ['latino_WZ.root'],      
#                      'weight' : '0.06630*puW',          
#                      'weights': ['1']            
#                  }

#samples['ZZ']  = {    'name': ['latino_ZZ.root'],      
                      #'weight' : '0.03184*puW',          
                      #'weights': ['1']            
                  #}



#samples['ggH']  = {    'name': ['latino_GluGluHToWWTo2L2Nu_M125_skim.root'],      
                  #    'weight' : 'baseW*puW',          
                  #    'weights': ['1']            
                 # }




###########################################
###########################################
###########################################


#samples['DATA']  = {    'name': ['latino_Run2015D_05Oct2015_MuonEG_0.root'],
                   #   'weight' : 'trigger',                              
                   #   'weights': ['1']            
                   #}

samples['DATA']  = {   'name': ['../data/5535pb/latino_Run2015D_05Oct2015_MuonEG_1.root', 
                                '../data/5535pb/latino_Run2015D_05Oct2015_DoubleEG_1.root',                                
                                '../data/5535pb/latino_Run2015D_05Oct2015_DoubleMuon_1.root',
                                '../data/5535pb/latino_Run2015D_05Oct2015_SingleElectron_1.root',
                                '../data/5535pb/latino_Run2015D_05Oct2015_SingleMuon_1.root',
                                '../data/5535pb/latino_Run2015D_05Oct2015_MuonEG_0.root', 
                                '../data/5535pb/latino_Run2015D_05Oct2015_DoubleEG_0.root',                                
                                '../data/5535pb/latino_Run2015D_05Oct2015_DoubleMuon_0.root',
                                '../data/5535pb/latino_Run2015D_05Oct2015_SingleElectron_0.root',
                                #'../data/5535pb/latino_Run2015D_05Oct2015_SingleMuon_0.root',
                                '../data/715pb/latino_Run2015D_PromptReco_MuonEG_3.root',
                                '../data/715pb/latino_Run2015D_PromptReco_MuonEG_2.root',
                                '../data/715pb/latino_Run2015D_PromptReco_MuonEG_1.root',
                                '../data/715pb/latino_Run2015D_PromptReco_MuonEG_0.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleEG_3.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleEG_2.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleEG_1.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleEG_0.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleMuon_0.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleMuon_1.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleMuon_2.root',
                                '../data/715pb/latino_Run2015D_PromptReco_DoubleMuon_3.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleElectron_0.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleElectron_1.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleElectron_2.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleElectron_3.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleMuon_0.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleMuon_1.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleMuon_2.root',
                                '../data/715pb/latino_Run2015D_PromptReco_SingleMuon_3.root' ],      

                       'weight' : 'trigger',
                       }

#samples['DATA']  = {   'name': ['dataB/latino_DoubleEG.root', 'dataB/latino_MuonEG.root', 'dataB/latino_SingleElectron.root', 'dataB/latino_SingleMu.root'],      
                       #'weight' : 'trigger',          
                  #}



# --inputDir=/media/data/amassiro/LatinoTrees/50ns/




