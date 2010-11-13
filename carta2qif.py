#!/usr/bin/python
# Importer script to convert Fineco Credit Card xls files into QIF files,
# for use, among others, by gnucash.
# 
# Based on the fineo2qif.py script by
# Antonino Sabetta - antonino.sabetta@isti.cnr.it
# (C) - 2009
#
# Modified by Marco Aicardi - marco [a] aicardi d0t org
#
# Released under GPLv3 License - www.gnu.org/licenses/g...
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
    assert line == ['Data operazione','Data Registrazione','Descrizione Operazione','Tipo spesa','Tipo rimborso','Importo in euro'] 

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
    print 'T-%s' % l[5] # negative amount 
    print 'P%s' % l[2] # payee / description
    print 'M%s' % l[2] # comment 
    print '^\n' # end transaction
