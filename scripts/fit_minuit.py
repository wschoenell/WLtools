from __future__ import division

from profiles import gamma_nfw
import numpy as np
from astropy import constants as const
import minuit
from astropy.cosmology import Planck13 as cosmo
import pyfits as pf

#dt = dtype=np.dtype(
#            [('e1', np.float), ('e2', np.float), ('m', np.float), ('Ra', np.float), ('Dec', np.float), ('galaxies_x', np.float), ('galaxies_y', np.float),
#             ('galaxies_r', np.float), ('z_phot', np.float), ('err_z_phot', np.float), ('weight_LF', np.float),
#             ('Sigma_c', np.float), ('factor_gal', np.float), ('R_gal', np.float)])
#
#
#data = np.loadtxt('compare_new.cat', dtype=dt)

data = pf.open('compare.fits')[1].data



class nfw(object):

    def __init__(self, data):
        self.data = data

    def chi2(self, r, c):
        k = gamma_nfw(r, c, self.data['R_gal_1'], self.data['factor_gal_1'], self.data['galaxies_x_1'], self.data['galaxies_y_1'], self.data['galaxies_r_1'])
        chi2 = np.sum(((k[0] - self.data['e1_c'])**2)*self.data['weight_LF_1']) + np.sum(((k[1] - self.data['e2_c'])**2)*self.data['weight_LF_1'])
        return chi2

model = nfw(data[data['R_gal_1'] < 4])

m = minuit.Minuit(model.chi2, limit_r = (.1, 10.), limit_c = (.1, 15.)) #, r=1.9, c=3.5)

print 'Starting minuit'
m.migrad()
print 'End: r = %3.2f and c = %3.2f' % (m.values['r'], m.values['c'])