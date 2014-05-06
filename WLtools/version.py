# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# metadata definition used by setup.py and others

_wltools_version_ = "0.1.0"
_wltools_name_ = "wltools"
_wltools_copyright_ = '2014, N. Cibirka de Oliveira'
_wltools_requires_ = ['numpy', 'minuit']
_wltools_provides_ = ['wltools']
_wltools_package_dir_ = {'wltools': '/WLtools'}
_wltools_packages_ = ['WLtools', 'WLtools.profiles']
_wltools_updated_ = '2013-02-15'
_wltools_long_description_ = 'Weak lensing fitting tools'
_wltools_author_ = 'Nathália Cibirka de Oliveira'
_wltools_author_email_ = 'nathcibirka@gmail.com'
_wltools_license_ = "GPLv2"
_wltools_url_ = 'https://github.com/nathcibirka/WLtools'
_wltools_download_url_ = 'https://github.com/wschoenell/magal/archive/%s-%s.tar.gz' % (_wltools_name_,
                                                                                       _wltools_version_)
_wltools_platform_ = "GNU/Linux"
_wltools_classifiers_ = ['Development Status :: 4 - Beta',
                         'Environment :: Console',
                         'Intended Audience :: Science/Research',
                         'Intended Audience :: Developers',
                         'License :: OSI Approved :: GNU General Public License (GPL)',
                         'Natural Language :: English',
                         'Natural Language :: Portuguese (Brazilian)',
                         'Operating System :: POSIX :: Linux',
                         'Programming Language :: Python',
                         'Topic :: Scientific/Engineering :: Astronomy']