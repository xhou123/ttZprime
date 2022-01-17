#!/usr/bin/env python
#Insert dataset you want to analyze
#The format is that of a list of array in python
#Eeach array has 8 entries
#0. "year": year of the dataset
#1. "datasetFlag": may stands for "SigMC", "BkgMC", the name of the dataset (e.g. "JetHT", "MET")
#2. "processName": a shortcut of the datasetName. If a dataset is an "ext", add this label and its number (e.g. DYJetsToLL_M-50_HT-100to200ext1) 
#3. "datasetName": the datasetName
#4. xSec in pb
#5. The total number of events of the dataset. To find it, use the command: dasgoclient --query="file dataset=dataset name | sum(file.nevents)". For data you should run 1 time and see the num as in data we filter the evt with the json file (to make sure you run over all evt see e.g. the tot num of files processed) 
#6. "sumgenWeight": the  sum of the genWeight of a MC dataset. Set 0 for data dataset.
#7. Label containing the analyses that need to analyze the dataset 
#Note
#1. The order of insertion of each year is first Data and then MC and must respect to avoid problems in the analysis chain
#2. The first time your run you do not know what the value of sumgenWeight is. So you need to be careful that your run over the entire dataset to get this value (see the num of files or the tot num of abs evt). Up to then, set sumgenWeight = 1 

datasets_info = [
#####
##   Year: 2017
#####
#####
##   Type:data
#####   


#####
##   Type:MC
#####  
#ZprimetoTT
#[2017,"BkgMC","ZprimeToTT","/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAOD-106X_mc2017_realistic_v6-v1/NANOAODSIM",1,192535,1,"ttZprime"],
#####
##   Background
#####
#TTTT
#[2017,"BkgMC","TTTT","/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",0.012,10351000,1,"ttZprime"],
#TT
#[2017,"BkgMC","TTToHadronic","/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",377.96,232999999,1,"ttZprime"],
[2017,"BkgMC","TTToSemiLeptonic","/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",365.34,346052000,1,"ttZprime"],
'''
[2017,"BkgMC","TTTo2L2Nu","/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",88.29,106724000,1,"ttZprime"],
#QCD
[2017,"BkgMC","QCD_HT50to100","/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",19380000,26243010,1,"ttZprime"],
[2017,"BkgMC","QCD_HT100to200","/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",19380000,5.4381393e+07,1,"ttZprime"],
[2017,"BkgMC","QCD_HT200to300","/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",1710000,42714435,1,"ttZprime"],
[2017,"BkgMC","QCD_HT300to500","/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",348000,43429979,1,"ttZprime"],
[2017,"BkgMC","QCD_HT500to700","/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",32100,36194860,1,"ttZprime"],
[2017,"BkgMC","QCD_HT700to1000","/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",6830,32934816,1,"ttZprime"],
[2017,"BkgMC","QCD_HT1000to1500","/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",1210,1.0186734e+07,1,"ttZprime"],
[2017,"BkgMC","QCD_HT1500to2000","/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",120,7701876,1,"ttZprime"],
[2017,"BkgMC","QCD_HT2000toInf","/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",25.3,4.112573e+06,1,"ttZprime"],
#TT+X
[2017,"BkgMC","TTGJets","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",3.697,3534208,1,"ttZprime"],
[2017,"BkgMC","ttHJetTobb","/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",0.2934,9579021,1,"ttZprime"],
[2017,"BkgMC","ttZJets","/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",0.2151,31791131,1,"ttZprime"],
[2017,"BkgMC","ttWJets","/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",0.4793,27662138,1,"ttZprime"],
#tZq
[2017,"BkgMC","tZq_ll","/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",0.0758,9530000,1,"ttZprime"],
#ST
[2017,"BkgMC","ST_t-channel_top_4f_InclusiveDecay","/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",136.02,1.29903e+08,1,"ttZprime"],
[2017,"BkgMC","ST_t-channel_antitop_4f_inclusiveDecays","/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",80.95,69793000,1,"ttZprime"],
#####
##   Year: 2016
#####
#####
##   Type:data
#####   


#####
##   Type:MC
#####  
#####
##   Background
#TTTT
[2016,"BkgMC","TTTT","/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",0.012,4.544e+06,1,"ttZprime"],
#TT
[2016,"BkgMC","TTToHadronic","/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",377.96,1.07067e+08,1,"ttZprime"],
[2016,"BkgMC","TTToSemiLeptonic","/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",365.34,1.44722e+08,1,"ttZprime"],
[2016,"BkgMC","TTTo2L2Nu","/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",88.29,4.3546e+07,1,"ttZprime"],
#QCD
[2016,"BkgMC","QCD_HT50to100","/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",19380000,1.1197186e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT100to200","/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",19380000,7.3506112e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT200to300","/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",1710000,4.3280518e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT300to500","/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",348000,1.6747056e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT500to700","/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",32100,1.4212819e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT700to1000","/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",6830,1.3750537e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT1000to1500","/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",1210,1.2254238e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT1500to2000","/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",120,9.376965e+06,1,"ttZprime"],
[2016,"BkgMC","QCD_HT2000toInf","/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",25.3,4.867995e+06,1,"ttZprime"],
#TT+X
[2016,"BkgMC","TTGJets","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",3.697,1.41623e+06,1,"ttZprime"],
[2016,"BkgMC","ttHJetTobb","/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",0.2934,5.231575e+06,1,"ttZprime"],
[2016,"BkgMC","ttHJetToNonbb","/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",0.2151,4.94125e+06,1,"ttZprime"],
#tZq
[2016,"BkgMC","tZq_ll","/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",0.0758,3.967e+06,1,"ttZprime"],
#ST
[2016,"BkgMC","ST_t-channel_top_4f_InclusiveDecay","/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",136.02,6.3073e+07,1,"ttZprime"],
[2016,"BkgMC","ST_t-channel_antitop_4f_inclusiveDecays","/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",80.95,3.0609e+07,1,"ttZprime"],
#####
#TTTT_APV
[2016,"BkgMC","TTTT_APV","/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",0.012,4.233e+06,1,"ttZprime"],
#TT_APV
[2016,"BkgMC","TTToHadronic_APV","/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",377.96,9.7823e+07,1,"ttZprime"],
[2016,"BkgMC","TTToSemiLeptonic_APV","/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",365.34,1.38169e+08,1,"ttZprime"],
[2016,"BkgMC","TTTo2L2Nu_APV","/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",88.29,4.1364e+07,1,"ttZprime"],
#QCD_APV
[2016,"BkgMC","QCD_HT50to100_APV","/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",19380000,3.816514e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT100to200_APV","/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",19380000,7.3633197e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT200to300_APV","/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",1710000,5.2222889e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT300to500_APV","/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",348000,5.2647947e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT500to700_APV","/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",32100,5.8385287e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT700to1000_APV","/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",6830,4.5459115e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT1000to1500_APV","/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",1210,1.4081307e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT1500to2000_APV","/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",120,1.0247757e+07,1,"ttZprime"],
[2016,"BkgMC","QCD_HT2000toInf_APV","/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",25.3,5.080758e+06,1,"ttZprime"],
#TT+X_APV
[2016,"BkgMC","ttZJets_APV","/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",0.618,1.7127765e+07,1,"ttZprime"],
[2016,"BkgMC","TTGJets_APV","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",3.697,1.511805e+06,1,"ttZprime"],
[2016,"BkgMC","ttHJetTobb_APV","/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",0.2934,5.087191e+06,1,"ttZprime"],
[2016,"BkgMC","ttHJetToNonbb_APV","/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",0.2151,4.824845e+06,1,"ttZprime"],
#tZq_APV
[2016,"BkgMC","tZq_ll_APV","/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",0.0758,3.955e+06,1,"ttZprime"],
#ST_APV
[2016,"BkgMC","ST_t-channel_top_4f_InclusiveDecay_APV","/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",136.02,5.5961e+07,1,"ttZprime"],
[2016,"BkgMC","ST_t-channel_antitop_4f_inclusiveDecays_APV","/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM",80.95,3.1024e+07,1,"ttZprime"],
#####
##   Year: 2018
#####
#####
##   Type:data
#####   


#####
##   Type:MC
#####  
#####
##   Background
#####
#TTTT
[2018,"BkgMC","TTTT","/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",0.012,13058000,1,"ttZprime"],
#TT
[2018,"BkgMC","TTToHadronic","/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",377.96,334206000,1,"ttZprime"],
[2018,"BkgMC","TTToSemiLeptonic","/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",365.34,476408000,1,"ttZprime"],
[2018,"BkgMC","TTTo2L2Nu","/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",88.29,145020000,1,"ttZprime"],
#QCD
[2018,"BkgMC","QCD_HT50to100","/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",19380000,38599389,1,"ttZprime"],
[2018,"BkgMC","QCD_HT100to200","/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",19380000,8.4434559e+07,1,"ttZprime"],
[2018,"BkgMC","QCD_HT200to300","/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",1710000,57336623,1,"ttZprime"],
[2018,"BkgMC","QCD_HT300to500","/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",348000,6.1609663e+07,1,"ttZprime"],
[2018,"BkgMC","QCD_HT500to700","/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",32100,49184771,1,"ttZprime"],
[2018,"BkgMC","QCD_HT700to1000","/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",6830,48506751,1,"ttZprime"],
[2018,"BkgMC","QCD_HT1000to1500","/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",1210,1.4394786e+07,1,"ttZprime"],
[2018,"BkgMC","QCD_HT1500to2000","/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",120,10411831,1,"ttZprime"],
[2018,"BkgMC","QCD_HT2000toInf","/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",25.3,5374711,1,"ttZprime"],
#TT+X
[2018,"BkgMC","TTGJets","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",3.697,4437068,1,"ttZprime"],
[2018,"BkgMC","ttHJetTobb","/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",0.2934,10020658,1,"ttZprime"],
[2018,"BkgMC","ttHJetToNonbb","/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",0.2151,9852567,1,"ttZprime"],
[2018,"BkgMC","ttZJets","/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",0.2151,32793815,1,"ttZprime"],
[2018,"BkgMC","ttWJets","/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",0.4793,27686862,1,"ttZprime"],
#tZq
[2018,"BkgMC","tZq_ll","/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",0.0758,11916000,1,"ttZprime"],
#ST
[2018,"BkgMC","ST_t-channel_top_4f_InclusiveDecay","/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",136.02,178336000,1,"ttZprime"],
[2018,"BkgMC","ST_t-channel_antitop_4f_inclusiveDecays","/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",80.95,9.5627e+07,1,"ttZprime"],
'''






 
]
