from distutils.core import setup

from wltools.version import _wltools_version_, _wltools_packages_, _wltools_url_, _wltools_license_, _wltools_author_, \
    _wltools_author_email_, _wltools_long_description_

setup(
    name='WLtools',
    version=_wltools_version_,
    packages=_wltools_packages_,
    url=_wltools_url_,
    license=_wltools_license_,
    author=_wltools_author_,
    author_email=_wltools_author_email_,
    description=_wltools_long_description_
)
