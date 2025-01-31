# variables

#variables = {}
'''
variables['VARIABLE']  = {  
          'name': 'expression',        # variable expression as one would use in TTree::Draw. Also 2D expression works e.g. var1:var2    
          'range' : range:             # anything that a TH1 can digest van be put here: 
                                       # a 3-valued tuple is interpreted as (nbins, xmin, xmax).
                                       # a 6-valued tuple is interpreted as (nbinsx, xmin, xmax, nbinsy, ymin, ymax)
                                       # a ([list]) is interpreted as a vector of bin edges
                                       # a ([list],[list],) is interpreted as a 2D vector of bin edges (mind the comma before the closing ")")
          'xaxis' : 'DR_{ll}',         # x axis name, human readable name, what goes into h->GetXaxis()->SetTitle()
          'fold' : NUMBER,             # 0 -> no underflow/overflow folding. 1 -> fold underflow in the first bin. 2-> fold overflow in the last bin. 3 -> fold both underflow and overflow.
          'divideByBinWidth': VALUE,   #OPTIONAL, whether to divide (1) or not (0) the bin content by the bin width (for variable bin size histograms). Default is 0
} 
'''

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

#
# leptons
#
"""
variables['pt_lep']  = {   'name': 'Lepton_pt',
                        'range' : (30,0.,200),
                        'xaxis' : 'p_{T} lep [GeV]',
                        'fold'  : 0
                        }
"""

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,25.,200),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3
                        }
variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,20.,200),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3
                        }

variables['eta1']  = {   'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range' : (30,-2.5,2.5),
                        'xaxis' : '#eta 1st lep',
                        'fold' :3
                        }

variables['eta2']  = {   'name': 'Alt$(Lepton_eta[1],-9999.)',
                        'range' : (30,-2.5,2.5),
                        'xaxis' : '#eta 2nd lep',
                        'fold' : 3
                        }

variables['mll-peak']  = {   'name': 'mll',            #   variable name    
                        'range' : (30,76.,106.),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }


#
# VBS jet AK4
#

variables['nCleanJetNotFat']  = {
                        'name': 'nCleanJetNotFat',     
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets (cleaned)',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['VBS_jet_eta1'] = {  'name': 'Alt$(CleanJet_eta[vbs_jet_0],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 1st VBS jet',
                        'fold' : 3
                        }
variables['VBS_jet_eta2'] = {  'name': 'Alt$(CleanJet_eta[vbs_jet_1],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 2nd VBS jet',
                        'fold' : 3
                        }

variables['VBS_jet_pt1']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_0],-9999.)',            #   variable name    
                        'range' : (30,80,400),    #   variable range
                        'xaxis' : 'p_{T} 1st VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['VBS_jet_pt2']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_1],-9999.)',            #   variable name    
                        'range' : (30,30,200),    #   variable range
                        'xaxis' : 'p_{T} 2nd VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }

#
# V- jet(s) #

variables['V_jet_eta1'] = {  'name': 'Alt$(CleanJet_eta[v_jet_0],-9999.)',
                        'range': (30,-2.5,2.5),
                        'xaxis': '#eta 1st V jet',
                        'fold' : 3
                        }
variables['V_jet_eta2'] = {  'name': 'Alt$(CleanJet_eta[v_jet_1],-9999.)',
                        'range': (30,-2.5,2.5),
                        'xaxis': '#eta 2nd V jet',
                        'fold' : 3
                        }

variables['V_jet_pt1']  = {   'name': 'Alt$(CleanJet_pt[v_jet_0],-9999.)',            #   variable name    
                        'range' : (50,30,200),    #   variable range
                        'xaxis' : 'p_{T} 1st V jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['V_jet_pt2']  = {   'name': 'Alt$(CleanJet_pt[v_jet_1],-9999.)',            #   variable name    
                        'range' : (30,30,100),    #   variable range
                        'xaxis' : 'p_{T} 2nd V jet [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['Vjet_mass'] = { 'name': 'Alt$(Vjet_mass,-9999.)',            #   variable name    
                        'range' : (30,65,105),    #   variable range
                        'xaxis' : 'V-jet mass [GeV]',  #   x axis name
                        'fold' : 3
                        }



# Fat Jet

variables['nFatJet']  = {
                        'name': 'nCleanFatJet',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets w/ p_{T}>200 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['FatJet_pt']  = {
                        'name': 'CleanFatJet_pt',     
                        'range' : (30,200,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJet_eta'] = {'name': 'CleanFatJet_eta',
                           'range' : (25,-2.5,2.5),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 3
                           }
                                                                                                                        
variables['FatJet_tau21'] = {   'name': 'CleanFatJet_tau21',
                        'range' : (50,0,1),
                        'xaxis' : '#tau_{21}',
                        'fold' : 0
                        }


# new variables

variables['mjj_max']  = {   'name': 'mjj_max',            #   variable name    
                        'range' : (20,350,4000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['detajj_mjjmax']  = {   'name': 'detajj_mjjmax',            #   variable name    
                           'range' : (12,1.0,8.0),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :3
                           }

variables['dphijj_mjjmax']  = {   'name': 'dphijj_mjjmax',            #   variable name    
                           'range' : (8,0,3.14),    #   variable range
                           'xaxis' : '#Delta #phi jj',  #   x axis name
                           'fold' :3
                           }


variables['mjj_binned']  = {   'name': 'mjj_max',            #   variable name    
                        'range' : ([350.,500., 750., 1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000.],),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        }

#Zeppenfeld variables
"""
variables['Zlep_1'] = {   'name': '( Lepton_eta[0]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{l1}', 
                        'fold' : 3
                        }

variables['Zlep_2'] = {   'name': '( Lepton_eta[1]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{l2}', 
                        'fold' : 3
                        }
"""

variables['Zlep_ll'] = {   'name': '  ( Lepton_eta[0]+Lepton_eta[1]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) ) /detajj_mjjmax',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{ll}', 
                        'fold' : 3
                        }

