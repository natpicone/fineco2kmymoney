#!/usr/bin/python
# Importer script to convert Fineco xls files into QIF files,
# for use, among others, by gnucash.
# 
# Antonino Sabetta - antonino.sabetta@isti.cnr.it
# (C) - 2009
#
# This is based on Jelmer Vernooij's script
# for PostBank mijn.postbank.nl .csv files.
# Jelmer Vernooij <jelmer@samba.org>, 2007

import csv, sys, os


##
#
#
def usage():
    print "Usage: ....."
    sys.exit(-1)

##
#
#
def wrong_format():
    print "Unrecognized format in input file."
    sys.exit(-1)

##
#
#
def check_input_file():
    line = rows.next()
    line = rows.next()
    line = rows.next()
    assert line == ['Risultato ricerca movimenti']
    
    line = rows.next()
    assert line == ['DataOperazione','Data Valuta','Entrate','Uscite','Descrizione','Causale']


##
# begin main program
#
if len(sys.argv) < 2:
    usage

try:
    #print "converting XLS to CSV"
    os.system("rm out.csv")
    os.system("xls2csv " + sys.argv[1] + "> out.csv")
except:
    usage

try:
    csvfile = open("out.csv")
except IOError:
    print "Error reading CSV file"
    sys.exit(-1)

rows = csv.reader(csvfile,delimiter=',')

try:
    check_input_file
except AssertionError:
    wrong_format

print '!Type:Bank\n'

for l in rows:
    if "/" not in l[0]:
        #print "skipping"
        continue
    else:
        p = l[0].split("/")
        print "D%s/%s/%s" % (p[0], p[1], p[2]) # you can easily get month-day-year here...
        # print 'D%s/%s/%s' % (l[0][4:6], l[0][6:8], l[0][0:4]) # date
    if l[2] == '':
        print 'T-%s' % l[3] # negative amount
    else:
        print 'T%s' % l[2]  # positive amount
    print 'P%s' % l[4] # payee / description
    print 'M%s %s' % (l[5], l[4]) # comment
    print '^\n' # end transaction
