# variables

# variables = {}

# 'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['nJet'] = {
    'name'  : 'Sum$(CleanJet_pt>30)',
    'range' : (4,0,4),
    'xaxis' : 'njets',
    'fold'  : 3
}

variables['mll'] = {
    'name'  : 'mll',
    'range' : (12,20.,500),
    'xaxis' : 'mll [GeV]',
    'fold'  : 3
}

variables['mllZ'] = {
    'name'  : 'wzeu_var[1]',
    'range' : (50,20.,180),
    'xaxis' : 'mll Z [GeV]',
    'fold'  : 3
}

variables['mlll'] = {
    'name'  : 'wzeu_var[2]',
    'range' : ([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200,250,300,350,400,450,500,550,600,650,700],),
    'xaxis' : 'mlll [GeV]',
    'fold'  : 3
}

variables['mee'] = {
    'name'  : 'wzeu_var[0]',
    'range' : (50,20.,180),
    'xaxis' : 'mee [GeV]',
    'fold'  : 3
}

variables['ptl1'] = {
    'name'  : 'Alt$(Lepton_pt[0],-9999.)',
    'range' : ([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,75,100,125,150,175,200,250,300,350],),
    'xaxis' : 'p_{T} 1st lep [GeV]',
    'fold'  : 3
}

variables['ptl1Z'] = {
    'name'  : 'wzeu_var[3]',
    'range' : ([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,75,100,125,150,175,200,250,300,350],),
    'xaxis' : 'p_{T} 1st lep Z [GeV]',
    'fold'  : 3
}

variables['ptl2'] = {
    'name'  : 'Alt$(Lepton_pt[1],-9999.)',
    'range' : ([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,75,100,150,200],),
    'xaxis' : 'p_{T} 2nd lep [GeV]',
    'fold'  : 3
}

variables['ptl2Z'] = {
    'name'  : 'wzeu_var[4]',
    'range' : ([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,75,100,150,200],),
    'xaxis' : 'p_{T} 2nd lep Z [GeV]',
    'fold'  : 3
}


variables['ptl3'] = {
    'name'  : 'Alt$(Lepton_pt[2],-9999.)',
    'range' : ([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,75,100,150,200,250],),
    'xaxis' : 'p_{T} 3rd lep [GeV]',
    'fold'  : 3
}

variables['ptlW'] = {
    'name'  : 'wzeu_var[5]',
    'range' : ([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,75,100,150,200,250],),
    'xaxis' : 'p_{T} lep W [GeV]',
    'fold'  : 3
}

variables['etal1'] = {
    'name'  : 'Alt$(Lepton_eta[0],-9999.)',
    'range' : (10,-2.5,2.5),
    'xaxis' : 'eta lep1',
    'fold'  : 3
}

variables['etal1Z'] = {
    'name'  : 'wzeu_var[6]',
    'range' : (10,-2.5,2.5),
    'xaxis' : 'eta lep1 Z',
    'fold'  : 3
}

variables['etal2'] = {
    'name'  : 'Alt$(Lepton_eta[1],-9999.)',
    'range' : (10,-2.5,2.5),
    'xaxis' : 'eta lep2',
    'fold'  : 3
}

variables['etal2Z'] = {
    'name'  : 'wzeu_var[7]',
    'range' : (10,-2.5,2.5),
    'xaxis' : 'eta lep2 Z',
    'fold'  : 3
}

variables['etal3'] = {
    'name'  : 'Alt$(Lepton_eta[2],-9999.)',
    'range' : (10,-2.5,2.5),
    'xaxis' : 'eta lep3',
    'fold'  : 3
}

variables['etalW'] = {
    'name'  : 'wzeu_var[8]',
    'range' : (10,-2.5,2.5),
    'xaxis' : 'eta lep W',
    'fold'  : 3
}

variables['mjj'] = {
    'name'  : 'mjj',
    'range' : ([300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700,720,740,760,780,800,1000,1250,1500,1750,2000,2500,3000],),
    'xaxis' : 'mjj [GeV]',
    'fold'  : 3
}

variables['ptj1'] = {
    'name'  : 'Alt$(CleanJet_pt[0],-9999.)',
    'range' : (54,30,300),
    'xaxis' : 'p_{T} 1st jet [GeV]',
    'fold'  : 3
}

variables['ptj2'] = {
    'name'  : 'Alt$(CleanJet_pt[1],-9999.)',
    'range' : (54,30,300),
    'xaxis' : 'p_{T} 2nd jet [GeV]',
    'fold'  : 3
}

variables['etaj1'] = {
    'name'  : 'Alt$(CleanJet_eta[0],-9999.)',
    'range' : (10,-5,5),
    'xaxis' : 'eta j1',
    'fold'  : 3
}

variables['etaj2'] = {
    'name'  : 'Alt$(CleanJet_eta[1],-9999.)',
    'range' : (10,-5,5),
    'xaxis' : 'eta j2',
    'fold'  : 3
}

variables['detajj'] = {
    'name'  : 'detajj',
    'range' : ([1.5,1.75,2,2.25,2.5,2.75,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5],),
    'xaxis' : 'deta jj',
    'fold'  : 3
}

variables['phi_j1'] = { 
    'name'  : 'Alt$(CleanJet_phi[0],-9999.)',
    'range' : (10,-3.141592,3.141592),
    'xaxis' : 'phi_j1',
    'fold'  : 3
}

variables['phi_j2'] = { 
    'name'  : 'Alt$(CleanJet_phi[1],-9999.)',
    'range' : (10,-3.141592,3.141592),
    'xaxis' : 'phi_j2',
    'fold'  : 3
}

variables['dphijj'] = {
    'name'  : 'dphijj',
    'range' : (10,0.0,3.141592),
    'xaxis' : 'dphi jj',
    'fold'  : 3
}

variables['met'] = {
    'name'  : 'MET_pt',
    'range' : ([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,175,200,225,250,275,300],),
    'xaxis' : 'met [GeV]', 
    'fold'  : 3
}

variables['Zlep1'] = {
    'name'  : 'zlep1',
    'range' : (40,-2.,2.),
    'xaxis' : 'Z^{lep}_{1}',
    'fold'  : 3
}

variables['Zlep2'] = {
    'name': 'zlep2',
    'range': (40,-2.,2.),
    'xaxis': 'Z^{lep}_{2}',
    'fold': 3
}
