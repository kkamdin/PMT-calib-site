#! /usr/bin/env python

import ROOT
import rat
import sys
import argparse

#Handle command line arguments
ap = argparse.ArgumentParser(description='Read a root file and spit out png files of all histograms')
ap.add_argument('file', help='the root file to read in')
args = ap.parse_args()

if not (args.pythonsrc):
    ap.error("No output specified for ratdb to py file transformation")

histoFile = ROOT.TFile(args.file)
ROOT.histoFile.Open()
ROOT.histoFile.ls()

TH1F.histo1 = histoFile.Get("fPedestal1")
c1 = TCanvas('', 'c1', 500, 600)
TH1F.histo1.Draw()


