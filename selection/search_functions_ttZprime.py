#!/usr/bin/env python3
import ROOT
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection

def effevt(passCut,self,event):
 passCut = passCut+1
 self.out.passCut[0] = passCut
 self.out.eelumiWeight[0] = self.lumiWeight
 if self.isData:
  self.out.eegenWeight[0] = 1
 else:
  self.out.eegenWeight[0] = event.genWeight/abs(event.genWeight)
 self.out.effevt.Fill()


def selectMus(event,selectedMusIdx):
 muons = Collection(event, 'Muon') 
 for imu in range(event.nMuon):
  #print "mu idx pT |eta| ID Iso %s %s %s %s %s" % (imu,event.Muon_pt[imu],abs(event.Muon_eta[imu]),event.Muon_tightId[imu],event.Muon_pfRelIso04_all[imu])
  if not event.Muon_pt[imu]>=10: continue
  if not abs(event.Muon_eta[imu])<=2.4: continue
  if not event.Muon_looseId[imu]: continue
  if not event.Muon_pfRelIso04_all[imu]<=0.15: continue
  selectedMusIdx.append(imu)

def selectEles(event,selectedElesIdx):
 electrons = Collection(event, 'Electron') 
 for iele in range(event.nElectron):
  #print "mu idx pT |eta| ID Iso %s %s %s %s %s" % (imu,event.Muon_pt[imu],abs(event.Muon_eta[imu]),event.Muon_tightId[imu],event.Muon_pfRelIso04_all[imu])
  if not event.Electron_pt[iele]>=10: continue
  if not abs(event.Electron_eta[iele])<=2.4: continue
  if not event.Electron_deltaEtaSC[iele]<=2.5: continue
  if not event.Electron_cutBased[iele]==2: continue
  if not event.Electron_convVeto[iele]==1: continue
  selectedElesIdx.append(iele)

def selectJets(jetType,event,selectedJetsIdx):
 jets = Collection(event, 'Jet')
 for ijet in range(event.nJet):
  #print "jets idx pT eta phi ID %s %s %s %s %s" % (ijet,event.Jet_pt[ijet],abs(event.Jet_eta[ijet]),event.Jet_phi[ijet],event.Jet_jetId[ijet])
  #for imu in range(len(selectedMusIdx)):
   #print "dR(jet,mu) %s %s %s" % (ijet,imu,muons[selectedMusIdx[imu]].p4().DeltaR(jets[ijet].p4()))
  #Kinematic
  if not event.Jet_pt[ijet]>=20: continue
  if not abs(event.Jet_eta[ijet])<=5.0: continue
  if not (jetType==1 or jetType==2 or jetType==3):
   if not event.Jet_pt[ijet]>=30: continue
  if not jetType==4:
   if not abs(event.Jet_eta[ijet])<=2.4: continue 
  #ID
  if not event.Jet_jetId[ijet]>=2: continue
  #b-jet
  if jetType==2:
   if not event.Jet_btagCSVV2[ijet]>0.8838: continue #https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X 
  selectedJetsIdx.append(ijet)


def selectFatJets(jetType,event,selectedFatJetsIdx):
 fatjets = Collection(event, 'FatJet')
 for ifatjet in range(event.nFatJet):
  #print "fat jets idx pT eta phi ID msoftdrop tau2/tau1 %s %s %s %s %s %s %s" % (ifatjet,event.FatJet_pt[ifatjet],abs(event.FatJet_eta[ifatjet]),event.FatJet_phi[ifatjet],event.FatJet_jetId[ifatjet],event.FatJet_msoftdrop[ifatjet],event.FatJet_tau2[ifatjet]/event.FatJet_tau1[ifatjet])
  #Kinematic
  if not event.FatJet_pt[ifatjet]>=200: continue
  if not abs(event.FatJet_eta[ifatjet])<2.4: continue #This is the recommendation for all the fat jets (there are not reconstructed forward fat jets)
  if not (105<event.FatJet_msoftdrop[ifatjet] and event.FatJet_msoftdrop[ifatjet]<220): continue
  #ID
  #if not event.FatJet_jetId[ifatjet]>=2: continue
  #if(jetType==0):     #W-tagging
   #if not event.FatJet_pt[ifatjet]>=200: continue
   #if not (65<event.FatJet_msoftdrop[ifatjet] and event.FatJet_msoftdrop[ifatjet]<105): continue
   #if not event.FatJet_tau2[ifatjet]/event.FatJet_tau1[ifatjet]<0.55: continue
  #if(jetType==1):   #top-tagging
   #if not event.FatJet_pt[ifatjet]>=400: continue
   #if not (105<event.FatJet_msoftdrop[ifatjet] and event.FatJet_msoftdrop[ifatjet]<220): continue
   #if not event.FatJet_tau3[ifatjet]/event.FatJet_tau2[ifatjet]<0.81: continue
  selectedFatJetsIdx.append(ifatjet)


'''
def PartiallyMergedSelection(event,selectedWJetsIdx,selectedJetsIdx,JetsPartial,TopQuarksPartial):
 fatjets = Collection(event, 'FatJet')
 jets = Collection(event, 'Jet')
 TopQuarkPartial = ROOT.TLorentzVector(-99,-99,-99,-99)
 Jet1Partial = ROOT.TLorentzVector(-99,-99,-99,-99)
 Jet2Partial = ROOT.TLorentzVector(-99,-99,-99,-99)
 PartiallyMerged = False
 TopPtMin=20
 for ifatjet in range(len(selectedWJetsIdx)):
  for ijet in range(len(selectedJetsIdx)):
   if not (fatjets[selectedWJetsIdx[ifatjet]].p4() + jets[selectedJetsIdx[ijet]].p4()).Pt()> TopPtMin : continue 
   if not fatjets[selectedWJetsIdx[ifatjet]].p4().DeltaR(jets[selectedJetsIdx[ijet]].p4()) > 0.8: continue
   if not (fatjets[selectedWJetsIdx[ifatjet]].p4() + jets[selectedJetsIdx[ijet]].p4()).M() > 100: continue
   if not (fatjets[selectedWJetsIdx[ifatjet]].p4() + jets[selectedJetsIdx[ijet]].p4()).M() < 300: continue
   Jet1Partial=fatjets[selectedWJetsIdx[ifatjet]].p4()
   Jet2Partial=jets[selectedJetsIdx[ijet]].p4()
   TopPtMin= (fatjets[selectedWJetsIdx[ifatjet]].p4() + jets[selectedJetsIdx[ijet]].p4()).Pt()
   TopQuarkPartial = fatjets[selectedWJetsIdx[ifatjet]].p4() + jets[selectedJetsIdx[ijet]].p4()
   PartiallyMerged = True
 if PartiallyMerged:
  JetsPartial.append(Jet1Partial)  
  JetsPartial.append(Jet2Partial)  
  TopQuarksPartial.append(TopQuarkPartial)


def FullyMergedSelection(event,selectedTopJetsIdx,TopQuarksMerged):
 fatjets = Collection(event, 'FatJet')
 TopPtMin=400
 TopQuarkMerged = ROOT.TLorentzVector(-99,-99,-99,-99)
 FullyMerged = False
 for ifatjet in range(len(selectedTopJetsIdx)):
   if not (fatjets[selectedTopJetsIdx[ifatjet]].p4()).Pt()> TopPtMin : continue 
   TopPtMin = (fatjets[selectedTopJetsIdx[ifatjet]].p4()).Pt()
   TopQuarkMerged = fatjets[selectedTopJetsIdx[ifatjet]].p4() 
   FullyMerged = True
 if FullyMerged:
   TopQuarksMerged.append(TopQuarkMerged)
'''