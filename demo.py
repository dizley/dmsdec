'''
Created on Nov 6, 2014

@author: Disley
'''

import dmsdec

if __name__ == '__main__':
    location = ('50 3 58.76N', '5 42 53.1W')
    print(location)
    dec_location = dmsdec.dms2dec(location)
    print(dec_location)
    print(dmsdec.dec2dms(dec_location, ','))
    print(dmsdec.dms2dec(dmsdec.dec2dms(dec_location)))