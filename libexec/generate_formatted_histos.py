#! /usr/bin/env python

import ROOT
from ROOT import TH1F, TFile, TCanvas, TDirectory, gDirectory
import rat
import sys
import argparse

#set batch mode so no canvases pop up
ROOT.gROOT.SetBatch()

#Handle command line arguments
ap = argparse.ArgumentParser(description='Read a root file and spit out png files of all histograms')
ap.add_argument('--file', help='the root file to read in')
ap.add_argument('--outputDir', help='the output directory where you dump the image files')
args = ap.parse_args()

#check if arguments are actually given
if not (args.outputDir):
	ap.error("No output directory specified for where to dump image files")
if not (args.file):
	ap.error("no file provided")

#open TFile where ECA histograms are hidden
histoFile = ROOT.TFile(args.file)
print "ROOT file to read and reformat is ", args.file
#get iterible list (i.e can't loop over histos in TFile)
histoFile.cd()
dirList = gDirectory.GetListOfKeys()

#loop over histograms and save each as an png file
for key in dirList:
	histo = key.ReadObj()
	#print histo.ClassName(), histo.GetName()
	c1 = TCanvas()
	histo.Draw()
	mystring = args.outputDir +"/" + histo.GetName() + ".png"
	c1.SaveAs(mystring)


