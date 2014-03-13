//**************************************************************************
//This macro maps Ped cell status onto a crate view of the electronics
//the color is an indicator of how many cells on a channel are bad
//**************************************************************************
#include <RAT/DB.hh>
#include <RAT/DBTable.hh>
#include <RAT/Log.hh>
#include <RAT/BitManip.hh>
#include <iostream>
#include <fstream>
#include <string>
#include <TFitter.h>
#include <TPaveText.h>
#include <TGraph.h>
#include <TStyle.h>
#include <TFile.h>
#include <TLegend.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TH2F.h>

using namespace RAT;

int main(int argc, char* argv[])
{

  //Check if the number of arguments is what we expect
   if ( argc != 3 ) // argc should be 2 for correct execution
   {   // We print argv[0]: it is the program name
      std::cout<<"usage: "<< argv[0]  << " <tslope ratdb>" << " < output-dir>\n";
      return -1; // exit
   }

   gStyle->SetOptTitle(0);
   gStyle->SetOptStat(0);    

   const char* filename1 = argv[1];
   const char* outputDir = argv[2];

   RAT::DB* ratdb;
   // load ratdb tables
   std::cout << "Load DB from "<< filename1 << "..." << std::endl;
   ratdb = RAT::DB::Get();
   ratdb->Load(filename1);

   std::vector<int> fCellStatus;
//   std::vector<float> fQHS;
//   std::vector<float> fQHL;
//   std::vector<float> fQLX;
//   std::vector<float> fTAC;
   DBLinkPtr PDST_DB = DB::Get()->GetLink( "ECA_PDST"); 
   try
   {
      fCellStatus = PDST_DB->GetIArray("pdst_status");
//      fQHS = PDST_DB->GetFArrayFromD("pdst_qhs");
//      fQHL = PDST_DB->GetFArrayFromD("pdst_qhl");
//      fQLX = PDST_DB->GetFArrayFromD("pdst_qlx");
//      fTAC = PDST_DB->GetFArrayFromD("pdst_tac");
   }
   catch( RAT::DBNotFoundError &e ) 
   { 
      RAT::Log::Die( "Can't open TSLP DB stuffs" );
   }
   ratdb->Clear();

   const int numch = 9728;
//   TH1F* fQHShist = new TH1F("pdst_qhs", filename1, 400, 0., 1800);
//   TH1F* fQHLhist = new TH1F("pdst_qhl", filename1, 400, 0., 1800);
//   TH1F* fQLXhist = new TH1F("pdst_qlx", filename1, 400, 0., 1800);
//   TH1F* fTAChist = new TH1F("pdst_tac", filename1, 600, 0., 2600);

   int chpercrate = 512;
   int cardpercrate = 16;
   int chpercard = 32;

   TH2F* crate0;
   TH2F* crate1;
   TH2F* crate2;
   TH2F* crate3;
   TH2F* crate4;
   TH2F* crate5;
   TH2F* crate6;
   TH2F* crate7;
   TH2F* crate8;
   TH2F* crate9;
   TH2F* crate10;
   TH2F* crate11;
   TH2F* crate12;
   TH2F* crate13;
   TH2F* crate14;
   TH2F* crate15;
   TH2F* crate16;
   TH2F* crate17;
   TH2F* crate18;

   //loop over status word bits
   for(int ibit = 0; ibit < 32; ibit ++)
   {
      int statusBit = ibit;
      crate0 = new TH2F("crate0", "crate0", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate1 = new TH2F("crate1", "crate1", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate2 = new TH2F("crate2", "crate2", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate3 = new TH2F("crate3", "crate3", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate4 = new TH2F("crate4", "crate4", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate5 = new TH2F("crate5", "crate5", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate6 = new TH2F("crate6", "crate6", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate7 = new TH2F("crate7", "crate7", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate8 = new TH2F("crate8", "crate8", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate9 = new TH2F("crate9", "crate9", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate10 = new TH2F("crate10", "crate10", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate11 = new TH2F("crate11", "crate11", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate12 = new TH2F("crate12", "crate12", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate13 = new TH2F("crate13", "crate13", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate14 = new TH2F("crate14", "crate14", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate15 = new TH2F("crate15", "crate15", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate16 = new TH2F("crate16", "crate16", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate17 = new TH2F("crate17", "crate17", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);
      crate18 = new TH2F("crate18", "crate18", cardpercrate,0, cardpercrate, chpercard, 0, chpercard);

      BitManip* fBits = new BitManip();
      int numcells = 155648;
      int icell = -1;
      for(int i=0; i < numcells; i++){
         icell++;
         int lcn = BitManip::GetLCN(icell);
         int card = BitManip::GetCard(lcn);
         int current_crate = BitManip::GetCrate(lcn);
         //if(fQHS[i] == -9999.0)
         //if((fQHS[i] == 0.0) && (fQHL[i] == 0.0) && (fQLX[i] == 0.0) && (fTAC[i] == 0.0))
         if(fBits->BitManip::TestBit(fCellStatus[i],statusBit))   
         {
            if(current_crate == 0) crate0->Fill(card, lcn%32);
            if(current_crate == 1) crate1->Fill(card, lcn%32);
            if(current_crate == 2) crate2->Fill(card, lcn%32);
            if(current_crate == 3) crate3->Fill(card, lcn%32);
            if(current_crate == 4) crate4->Fill(card, lcn%32);
            if(current_crate == 5) crate5->Fill(card, lcn%32);
            if(current_crate == 6) crate6->Fill(card, lcn%32);
            if(current_crate == 7) crate7->Fill(card, lcn%32);
            if(current_crate == 8) crate8->Fill(card, lcn%32);
            if(current_crate == 9) crate9->Fill(card, lcn%32);
            if(current_crate == 10) crate10->Fill(card, lcn%32);
            if(current_crate == 11) crate11->Fill(card, lcn%32);
            if(current_crate == 12) crate12->Fill(card, lcn%32);
            if(current_crate == 13) crate13->Fill(card, lcn%32);
            if(current_crate == 14) crate14->Fill(card, lcn%32);
            if(current_crate == 15) crate15->Fill(card, lcn%32);
            if(current_crate == 16) crate16->Fill(card, lcn%32);
            if(current_crate == 17) crate17->Fill(card, lcn%32);
            if(current_crate == 18) crate18->Fill(card, lcn%32);
         } //if qhs==0
       }//for loop

      TCanvas* cp0 = new TCanvas();
      cp0->Divide(10,2);

      crate0->SetNdivisions(16,"X");
      crate1->SetNdivisions(16,"X");
      crate2->SetNdivisions(16,"X");
      crate3->SetNdivisions(16,"X");
      crate4->SetNdivisions(16,"X");
      crate5->SetNdivisions(16,"X");
      crate6->SetNdivisions(16,"X");
      crate7->SetNdivisions(16,"X");
      crate8->SetNdivisions(16,"X");
      crate9->SetNdivisions(16,"X");
      crate10->SetNdivisions(16,"X");
      crate11->SetNdivisions(16,"X");
      crate12->SetNdivisions(16,"X");
      crate13->SetNdivisions(16,"X");
      crate14->SetNdivisions(16,"X");
      crate15->SetNdivisions(16,"X");
      crate16->SetNdivisions(16,"X");
      crate17->SetNdivisions(16,"X");
      crate18->SetNdivisions(16,"X");
   
      cp0->cd(1);
      crate0->Draw("COLZ");
      cp0->cd(2);
      crate1->Draw("COLZ");
      cp0->cd(3);
      crate2->Draw("COLZ");
      cp0->cd(4);
      crate3->Draw("COLZ");
      cp0->cd(5);
      crate4->Draw("COLZ");
      cp0->cd(6);
      crate5->Draw("COLZ");
      cp0->cd(7);
      crate6->Draw("COLZ");
      cp0->cd(8);
      crate7->Draw("COLZ");
      cp0->cd(9);
      crate8->Draw("COLZ");
      cp0->cd(10);
      crate9->Draw("COLZ");
      cp0->cd(11);
      crate10->Draw("COLZ");
      cp0->cd(12);
      crate11->Draw("COLZ");
      cp0->cd(13);
      crate12->Draw("COLZ");
      cp0->cd(14);
      crate13->Draw("COLZ");
      cp0->cd(15);
      crate14->Draw("COLZ");
      cp0->cd(16);
      crate15->Draw("COLZ");
      cp0->cd(17);
      crate16->Draw("COLZ");
      cp0->cd(18);
      crate17->Draw("COLZ");
      cp0->cd(19);
      crate18->Draw("COLZ");
   

      char buff[20];
      //sprintf(buff, "_Bit_%d", statusBit);
      if(statusBit < 10) sprintf(buff, "-0%d", statusBit);
      else sprintf(buff, "-%d", statusBit);
      std::string bitinfo(buff); 
      std::string rdbname(filename1);
      int end = rdbname.find("ratdb");
      int begin = rdbname.find("PDST_");
      std::string runNo = rdbname.substr(begin, end-begin-1);
      std::cout << "runNo = " << runNo << std::endl;
      std::cout << "begin = " << begin << " end = " << end << std::endl;
      std::string cellstat = bitinfo;
      if(statusBit == 0) cellstat.assign("Overall Status");
      if(statusBit == 1) cellstat.assign("QHS Bad");
      if(statusBit == 2) cellstat.assign("QHS Width Bad");
      if(statusBit == 3) cellstat.assign("QHS Outside Limits From Prev Run");
      if(statusBit == 4) cellstat.assign("QHL Bad");
      if(statusBit == 5) cellstat.assign("QHL Width Bad");
      if(statusBit == 6) cellstat.assign("QHL Width Bad");
      if(statusBit == 7) cellstat.assign("QLX Bad");
      if(statusBit == 8) cellstat.assign("QLX Width Bad");
      if(statusBit == 9) cellstat.assign("QLX Outside Limits From Prev Run");
      if(statusBit == 10) cellstat.assign("TAC Ped Bad");
      if(statusBit == 11) cellstat.assign("TAC Ped Width Bad");
      if(statusBit == 12) cellstat.assign("TAC Ped Outside Limits From Prev Run");
      if(statusBit == 13) cellstat.assign("Too Few Events");
      if(statusBit == 14) cellstat.assign("Zero Events");
      if(statusBit == 15) cellstat.assign("Overall Channel Status");
      if(statusBit == 16) cellstat.assign("MB ID check");
      if(statusBit == 17) cellstat.assign("DB ID check");
      if(statusBit == 18) cellstat.assign("QHS Any Values Bad");
      if(statusBit == 19) cellstat.assign("QHL Any Values Bad");
      if(statusBit == 20) cellstat.assign("QLX Any Values Bad");
      if(statusBit == 21) cellstat.assign("TAC Ped Any Values Bad");
      if(statusBit == 22) cellstat.assign("Any Ped Values Bad");
      if(statusBit == 23) cellstat.assign("Any Width Values Bad");
      if(statusBit == 24) cellstat.assign("Any Diff From Prev Run Values Bad");
      if(statusBit == 25) cellstat.assign("Sequencer Disabled");
      if(statusBit == 26) cellstat.assign("Too Few Events on Channel");
      if(statusBit == 27) cellstat.assign("Zero Events on Channel");

      cp0->cd(20);
      TPaveText* pt = new TPaveText(0.04, .1, 0.95, .8);
      pt->SetFillColor(0);
      pt->AddText(runNo.c_str());
      pt->AddText(cellstat.c_str());
      pt->Draw();
   
      cp0->Update();

       //quality of pdf saved this way is not good
       //there are lots of rando grid lines everywhere.
//      std::string title = runNo + bitinfo + std::string(".png");
      std::string title = std::string("pdst-flag") + bitinfo + std::string(".png");
      std::string fullpath = std::string(outputDir) + std::string("/") + title;
      cp0->SaveAs(fullpath.c_str());

  }//status bit loop

}
