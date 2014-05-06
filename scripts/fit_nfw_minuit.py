from __future__ import division

import sys

import numpy as np
import pyfits as pf

from WLtools.profiles.nfw import gamma_nfw
import minuit


data = pf.open(sys.argv[1])[1].data


class nfw(object):
    def __init__(self, data):
        self.data = data

    def chi2(self, r, c):
        k = gamma_nfw(r, c, self.data['R_gal_1'], self.data['factor_gal_1'], self.data['galaxies_x_1'],
                      self.data['galaxies_y_1'], self.data['galaxies_r_1'])
        chi2 = np.sum(((k[0] - self.data['e1_c']) ** 2) * self.data['weight_LF_1']) + np.sum(
            ((k[1] - self.data['e2_c']) ** 2) * self.data['weight_LF_1'])
        return chi2


model = nfw(data[data['R_gal_1'] < 4])

m = minuit.Minuit(model.chi2, limit_r=(.1, 10.), limit_c=(.1, 15.))

print 'Starting minuit'
m.migrad()
print 'End: r = %3.2f and c = %3.2f' % (m.values['r'], m.values['c'])