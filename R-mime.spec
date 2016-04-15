#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mime
Version  : 0.4
Release  : 21
URL      : http://cran.r-project.org/src/contrib/mime_0.4.tar.gz
Source0  : http://cran.r-project.org/src/contrib/mime_0.4.tar.gz
Summary  : Map Filenames to MIME Types
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mime-lib
BuildRequires : clr-R-helpers

%description
# mime
[![Build Status](https://travis-ci.org/yihui/mime.svg)](https://travis-ci.org/yihui/mime)

%package lib
Summary: lib components for the R-mime package.
Group: Libraries

%description lib
lib components for the R-mime package.


%prep
%setup -q -c -n mime

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library mime
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mime


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mime/DESCRIPTION
/usr/lib64/R/library/mime/INDEX
/usr/lib64/R/library/mime/Meta/Rd.rds
/usr/lib64/R/library/mime/Meta/hsearch.rds
/usr/lib64/R/library/mime/Meta/links.rds
/usr/lib64/R/library/mime/Meta/nsInfo.rds
/usr/lib64/R/library/mime/Meta/package.rds
/usr/lib64/R/library/mime/NAMESPACE
/usr/lib64/R/library/mime/NEWS
/usr/lib64/R/library/mime/R/mime
/usr/lib64/R/library/mime/R/mime.rdb
/usr/lib64/R/library/mime/R/mime.rdx
/usr/lib64/R/library/mime/help/AnIndex
/usr/lib64/R/library/mime/help/aliases.rds
/usr/lib64/R/library/mime/help/mime.rdb
/usr/lib64/R/library/mime/help/mime.rdx
/usr/lib64/R/library/mime/help/paths.rds
/usr/lib64/R/library/mime/html/00Index.html
/usr/lib64/R/library/mime/html/R.css
/usr/lib64/R/library/mime/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mime/libs/mime.so
