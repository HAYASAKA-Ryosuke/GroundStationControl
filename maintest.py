class testmain(unittest.TestCase):

    #def testorbit(self):
    #    orbitinfo = Orbitcalc.Orbitcalc(gslat='43', gslon='141', gselev='50')
    #    orbitinfo.SatInfo('iss',
    #                  '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
    #                  '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
    #                  '437.234', 'FM')
    #    satlat, satlon, satfreq = orbitinfo.CalcObserve()
    #    print satlat
    #    print satlon
    #    print satfreq

    def testradioIC910(self):
        ic910= radio.Radio("IC910","Sub","CW")
        ic910.connect("/dev/ttyUSB0")
        #print radio.getfreq()
        #radio.getmode()
        ic910.changefreq(437.38590)
        #print "Sub FM"
        #radio.chengemode("Sub","FM")
        print "Sub CW"
        ic910.changemode("Sub","CW")
        #print "Main FM"
        #radio.chengemode("Main","FM")
        #print "Main CW"
        #radio.chengemode("Main","CW")
        ic910.close()
    #def testradioIC910(self):
    #    ic910 = radio.Radio("IC910","Sub","CW")
    #    ic910.connect("/dev/ttyUSB0")
    #    #print radio.getfreq()
    #    #radio.getmode()
    #    ic910.chengemode("Sub","FM")
    #    ic910.chengefreq(437.4801)
    #    #print "Sub FM"
    #    ic910.chengemode("Sub","CW")
    #    ic910.chengefreq(437.5801)
    #    #print "Sub FM"
    #    #print "Sub CW"
    #    #radio.chengemode("Sub","CW")
    #    #print "Main FM"
    #    #radio.chengemode("Main","FM")
    #    #print "Main CW"
    #    #radio.chengemode("Main","CW")
    #    ic910.close()
unittest.main()