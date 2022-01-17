#!/usr/bin/env python3
import os, sys
import ROOT
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from search_variables_ttZprime import *
from search_functions_ttZprime import *

class declareVariables(search_variables):
 def __init__(self, name):
  super(declareVariables, self).__init__(name)

class Producer(Module):
 def __init__(self, **kwargs):
  #User inputs
  self.channel     = kwargs.get('channel') 
  self.isData      = kwargs.get('dataType')=='data'
  self.year        = kwargs.get('year') 
  self.maxNumEvt   = kwargs.get('maxNumEvt')
  self.prescaleEvt = kwargs.get('prescaleEvt')
  self.lumiWeight  = kwargs.get('lumiWeight')

  #Analysis quantities
  if self.year==2018:
   #Trigger 
   print "not yet"
  elif self.year==2017:
   #Trigger
   if self.channel=="mumu":
    self.trigger = lambda e: e.HLT_IsoMu24

  elif self.year==2016:
   #Trigger
   if self.channel=="mumu":
    self.trigger = lambda e: e.HLT_IsoMu24

  else:
   raise ValueError('Year must be above 2016 (included).')

  #ID
  
  #Corrections

  #Cut flow table
        
 def beginJob(self):
  print ("Here is beginJob")
  #pass
        
 def endJob(self):
  print ("Here is endJob")
  #pass
        
 def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
  print ("Here is beginFile")
  self.sumNumEvt = 0
  self.sumgenWeight = 0
  self.out = declareVariables(inputFile) 
  #pass
        
 def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):        
  print ("Here is endFile")
  self.out.sumNumEvt[0] = self.sumNumEvt
  self.out.sumgenWeight[0] = self.sumgenWeight
  self.out.evtree.Fill()
  self.out.outputfile.Write()
  self.out.outputfile.Close()
  #pass
        
 def analyze(self, event):
  """process event, return True (go to next module) or False (fail, go to next event)"""
  #For all events
  if(self.sumNumEvt>self.maxNumEvt and self.maxNumEvt!=-1): return False
  self.sumNumEvt = self.sumNumEvt+1
  if not self.isData: self.sumgenWeight = self.sumgenWeight+(event.genWeight/abs(event.genWeight))
  if not self.sumNumEvt%self.prescaleEvt==0: return False
  passCut = 0 

  #Primary vertex (loose PV selection)
  if not event.PV_npvs>0:             #total number of reconstructed primary vertices
   effevt(passCut,self,event)
   return False
  passCut = passCut+1 #passCut = 1

  #Trigger        
  if not self.trigger(event):
   effevt(passCut,self,event)
   return False
  passCut = passCut+1 #passCut = 2  

  #Muons
  #print "run:lumi:evt %s:%s:%s" % (event.run,event.luminosityBlock,event.event)
  muons = Collection(event, 'Muon')
  selectedMusIdx = []
  selectMus(event,selectedMusIdx) 
  if len(selectedMusIdx)>=1:        #the number of muon is less than 1(veto muon)
   effevt(passCut,self,event)
   return False
  passCut = passCut+1  #passCut = 3

  #Electrons
  electrons = Collection(event, 'Electron') 
  selectedElesIdx=[]
  selectEles(event,selectedElesIdx)
  if len(selectedElesIdx)>=1:     #the number of electron is less than 1(veto electron)
   effevt(passCut,self,event)
   return False
  passCut = passCut+1  #passCut = 4


  #Jet
  #1-> common jet
  #4-> Forward jet
  #2-> b-jet
  jets = Collection(event, 'Jet')
  selectedJetsIdx=[]
  selectJets(1,event,selectedJetsIdx) 
  selectedForwardJetsIdx=[]
  selectJets(4,event,selectedForwardJetsIdx) 
  selectedBJetsM=[]  
  selectJets(2,event,selectedJetsIdx) 
 
  #print len(selectedJetsIdx) 

  #FatJet
  #0-> W Jet
  #1-> Top Jet
  fatjets = Collection(event, 'FatJet')
  for ifatjet in range(event.nFatJet):
    self.out.FatJet_particleNetMD_QCD.push_back(event.FatJet_particleNetMD_QCD[ifatjet])
    self.out.FatJet_particleNetMD_Xbb.push_back(event.FatJet_particleNetMD_Xbb[ifatjet])
    self.out.FatJet_particleNetMD_Xcc.push_back(event.FatJet_particleNetMD_Xcc[ifatjet])
    self.out.FatJet_particleNetMD_Xqq.push_back(event.FatJet_particleNetMD_Xqq[ifatjet])
 

  '''
  #W tagger
  selectedWJetsIdx=[]
  selectFatJets(0,event,selectedWJetsIdx)
  
  
  #Top tagger
  selectedTopJetsIdx=[]
  selectFatJets(1,event,selectedTopJetsIdx)
  
  
  #select partially top
  JetsPartial=[]  
  TopQuarksPartial= []
  PartiallyMerged = False
  PartiallyMergedSelection(event,selectedWJetsIdx,selectedJetsIdx,JetsPartial,TopQuarksPartial)
  

  #select fully merged top
  TopQuarksMerged= []
  FullyMerged = False
  FullyMergedSelection(event,selectedTopJetsIdx,TopQuarksMerged)

  if (len(TopQuarksPartial)>=1):
     effevt(passCut,self,event)
     PartiallyMerged = True
  passCut = passCut+1  #passCut = 5


  if (len(TopQuarksMerged)>=1):
     effevt(passCut,self,event)
     FullyMerged = True 
  passCut = passCut+1  #passCut = 6

  #print FullyMerged
  #print PartiallyMerged
  
  if FullyMerged:
     PartiallyMerged = False

  if PartiallyMerged:
     FullyMerged = False 
  
 
  if not (FullyMerged or PartiallyMerged):
     return False


  if FullyMerged:
     TopQuark = TopQuarksMerged[0]    #read the leading top
     #print TopQuark.Pt()
     #print TopQuark.M()
      
  if PartiallyMerged:
     TopQuark = TopQuarksPartial[0]   #read the leading top
     #print TopQuark.Pt()
     #print TopQuark.M()
     #print JetsPartial[0].Pt()
     #print JetsPartial[1].Pt()
   '''
  #print "mu0 idx pT |eta| ID Iso %s %s %s %s %s" % (selectedMusIdx[0],event.Muon_pt[selectedMusIdx[0]],abs(event.Muon_eta[selectedMusIdx[0]]),event.Muon_tightId[selectedMusIdx[0]],event.Muon_pfRelIso04_all[selectedMusIdx[0]])
  #print "mu1 idx pT |eta| ID Iso %s %s %s %s %s" % (selectedMusIdx[1],event.Muon_pt[selectedMusIdx[1]],abs(event.Muon_eta[selectedMusIdx[1]]),event.Muon_tightId[selectedMusIdx[1]],event.Muon_pfRelIso04_all[selectedMusIdx[1]])
    
  print "run:lumi:evt %s:%s:%s" % (event.run,event.luminosityBlock,event.event)
  print "genWeights event.Pileup_nTrueInt %s %s" % (event.genWeight/abs(event.genWeight), event.Pileup_nTrueInt) 
  print ""
     
  #Event
  self.out.run[0] = event.run
  self.out.luminosityBlock[0] = event.luminosityBlock
  self.out.event[0] = event.event #& 0xffffffffffffffff


  #self.out.MuonPt[0] = event.Muon_pt[selectedMusIdx[0]]
  #self.out.ElectronPt[0] = event.Electron_pt[selectedElesIdx[0]]
  #self.out.JetsPt[0] = event.Jet_pt[selectedJetsIdx[0]]
  '''
  self.out.TopMass[0] = TopQuark.M()
  self.out.TopPt[0] = TopQuark.Pt()
  if FullyMerged:
    self.out.TopMassMerged[0] = TopQuarksMerged[0].M() 
    self.out.TopPtMerged[0] = TopQuarksMerged[0].Pt()

    self.out.TopMassPartial[0] = -99. 
    self.out.TopPtPartial[0] =  -99.
    self.out.Jet1PartialPt[0] = -99.
    self.out.Jet2PartialPt[0] = -99.
 
  if PartiallyMerged:
    self.out.TopMassMerged[0] = -99. 
    self.out.TopPtMerged[0] = -99.

    self.out.TopMassPartial[0] = TopQuarksPartial[0].M()
    self.out.TopPtPartial[0] = TopQuarksPartial[0].Pt()
    self.out.Jet1PartialPt[0] = JetsPartial[0].Pt()
    self.out.Jet2PartialPt[0] = JetsPartial[1].Pt()
   '''


  #Save tree
  self.out.Events.Fill() 
  return True
