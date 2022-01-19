void test(){ 
  gROOT->Reset();
  gStyle->SetCanvasColor(0);
  gStyle->SetFrameBorderMode(0);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1,0);
  gStyle->SetTitleX(0.5); //title X location 
  gStyle->SetTitleY(0.96); //title Y location 
  gStyle->SetPaintTextFormat(".2f");
  gErrorIgnoreLevel = kError;
  using namespace std; 

  TCanvas *c1 = new TCanvas("c1","test",800,600);
    
  //Open the root files
  TFile* fqcd0  = new TFile("QCD_HT50to100.root");
  TFile* fqcd1  = new TFile("QCD_HT100to200.root");
  TFile* fqcd2  = new TFile("QCD_HT200to300.root");
  TFile* fqcd3  = new TFile("QCD_HT300to500.root");
  TFile* fqcd4  = new TFile("QCD_HT500to700.root");
  TFile* fqcd5  = new TFile("QCD_HT700to1000.root");
  TFile* fqcd6  = new TFile("QCD_HT1000to1500.root");
  TFile* fqcd7  = new TFile("QCD_HT1500to2000.root");
  TFile* fqcd8  = new TFile("QCD_HT2000toInf.root");

  //Define the weight of each samples
  float LUMI  = 41500.0; 

  float wQCD0 = (19380000*LUMI/26243010);       //QCD_HT50to100
  float wQCD1 = (19380000*LUMI/54381393);      //QCD_HT100to200
  float wQCD2 = (1710000*LUMI/42714435);     //QCD_HT200to300            
  float wQCD3 = (348000*LUMI/43429979);     //QCD_HT300to500           
  float wQCD4 = (32100*LUMI/36194860);     //QCD_HT500to700            
  float wQCD5 = (6830*LUMI/32934816);    //QCD_HT700to1000           
  float wQCD6 = (1210*LUMI/10186734);   //QCD_HT1000to1500      
  float wQCD7 = (120*LUMI/7701876);   //QCD_HT1500to2000      
  float wQCD8 = (25.3*LUMI/4112573);  //QCD_HT2000toInf 

  //Get the tree
  TTree *Tree_qcd0 = (TTree*)fqcd0->Get("Events");
  TTree *Tree_qcd1 = (TTree*)fqcd1->Get("Events");
  TTree *Tree_qcd2 = (TTree*)fqcd2->Get("Events");
  TTree *Tree_qcd3 = (TTree*)fqcd3->Get("Events");
  TTree *Tree_qcd4 = (TTree*)fqcd4->Get("Events");
  TTree *Tree_qcd5 = (TTree*)fqcd5->Get("Events");
  TTree *Tree_qcd6 = (TTree*)fqcd6->Get("Events");
  TTree *Tree_qcd7 = (TTree*)fqcd7->Get("Events");
  TTree *Tree_qcd8 = (TTree*)fqcd8->Get("Events");

  //Define the histogram
  int nbins=100;
  float low =0.0,up =1.0;

  TH1F *njets_qcd0    = new TH1F("njets_qcd0",      "", nbins,low,up );
  TH1F *njets_qcd1   = new TH1F("njets_qcd1",     "", nbins,low,up );
  TH1F *njets_qcd2   = new TH1F("njets_qcd2",     "", nbins,low,up );
  TH1F *njets_qcd3   = new TH1F("njets_qcd3",     "", nbins,low,up );
  TH1F *njets_qcd4   = new TH1F("njets_qcd4",     "", nbins,low,up );
  TH1F *njets_qcd5   = new TH1F("njets_qcd5",     "", nbins,low,up );
  TH1F *njets_qcd6   = new TH1F("njets_qcd6",     "", nbins,low,up );
  TH1F *njets_qcd7   = new TH1F("njets_qcd7",     "", nbins,low,up );
  TH1F *njets_qcd8   = new TH1F("njets_qcd8",     "", nbins,low,up );

  //TH1F *background = new TH1F("","",nbins,low,up);
  TH1F *QCD = new TH1F("","",nbins,low,up);
  //set the selection cuts
  //const char *cut = "NumSelLeps==0";
  //const char *cut = "NumSelLeps==0&&HT>900&&NumSelJets>=9&&NumSelBJetsT>=3"; 

  //Draw branch to histogram with cuts
  Tree_qcd0->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd0");
  Tree_qcd1->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd1");
  Tree_qcd2->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd2");
  Tree_qcd3->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd3");
  Tree_qcd4->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd4");
  Tree_qcd5->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd5");
  Tree_qcd6->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd6");
  Tree_qcd7->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd7");
  Tree_qcd8->Draw("FatJet_particleNetMD_Xbb+FatJet_particleNetMD_Xcc+FatJet_particleNetMD_Xqq>>njets_qcd8");

  

  for(int j=1; j<nbins+1; j++){
    njets_qcd0->SetBinContent(j,wQCD0*njets_qcd0->GetBinContent(j));
    njets_qcd1->SetBinContent(j,wQCD1*njets_qcd1->GetBinContent(j));
    njets_qcd2->SetBinContent(j,wQCD2*njets_qcd2->GetBinContent(j));
    njets_qcd3->SetBinContent(j,wQCD3*njets_qcd3->GetBinContent(j));
    njets_qcd4->SetBinContent(j,wQCD4*njets_qcd4->GetBinContent(j));
    njets_qcd5->SetBinContent(j,wQCD5*njets_qcd5->GetBinContent(j));
    njets_qcd6->SetBinContent(j,wQCD6*njets_qcd6->GetBinContent(j));
    njets_qcd7->SetBinContent(j,wQCD7*njets_qcd7->GetBinContent(j));
    njets_qcd8->SetBinContent(j,wQCD8*njets_qcd8->GetBinContent(j));

    //float nsig = njets_sig->GetBinContent(j);
    //float bkg0 = njets_bkg0->GetBinContent(j);
    float qcd = njets_qcd0->GetBinContent(j)+njets_qcd1->GetBinContent(j)+njets_qcd2->GetBinContent(j)+njets_qcd3->GetBinContent(j)+njets_qcd4->GetBinContent(j)+njets_qcd5->GetBinContent(j)+njets_qcd6->GetBinContent(j)+njets_qcd7->GetBinContent(j)+njets_qcd8->GetBinContent(j);
    QCD->SetBinContent(j,qcd);
    //background->SetBinContent(j,bkg0+bkg1);
  }    

 

  
  //njets_sig->SetLineColor(1);
  QCD->SetLineColor(2);
  //njets_bkg0->SetLineColor(3);

  //double nsig  =njets_sig->Integral();
  //double nbkg0 =njets_bkg0->Integral();
  //double nbkg1 =QCD->Integral();
  //std::cout<<"TTTT: "<<nsig <<std::endl;
  //std::cout<<"TT  : "<<nbkg0<<std::endl;
  //std::cout<<"QCD : "<<nbkg1<<std::endl;
  //std::cout<<"Sensitivity : "<<nsig/sqrt(nsig+nbkg0+nbkg1)<<std::endl;

  //njets_sig->Scale(1/nsig);
  //njets_bkg0->Scale(1/nbkg0);
  //QCD->Scale(1/nbkg1);

  
  QCD->Draw("hist");
  QCD->GetXaxis()->SetTitle("P");
  //QCD->GetYaxis()->SetTitle("Normalize to unit");
  
  
  //njets_sig->Draw("histsame");
  //njets_bkg0->Draw("histsame");
  /*
  TExec *setex1 = new TExec("setex1","gStyle->SetErrorX(0.5)");
  setex1->Draw();
  m_h1_signal->Draw("E2Same");
  TExec *setex2 = new TExec("setex2","gStyle->SetErrorX(0)");
  setex2->Draw();
  //hs402->Draw("histSAME");
  */
  TLegend *leg = new TLegend(.52, .62, .92, .82,NULL,"brNDC");
  //leg->AddEntry(njets_sig, "TTTT","l");
  leg->AddEntry(QCD, "QCD","l");
  //leg->AddEntry(njets_bkg0, "TTbar","l");
  leg->SetBorderSize(0);
  leg->SetLineColor(19);
  leg->SetLineStyle(1);
  leg->SetLineWidth(1);
  leg->SetFillColor(19);
  leg->SetFillStyle(0);
  leg->Draw();
  c1->SaveAs("QCD.pdf");
  c1->Draw("");
  //c1->SaveAs(NAME+".pdf");

  return;
}
    
