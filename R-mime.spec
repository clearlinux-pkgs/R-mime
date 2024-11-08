#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mime
Version  : 0.12
Release  : 103
URL      : https://cran.r-project.org/src/contrib/mime_0.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mime_0.12.tar.gz
Summary  : Map Filenames to MIME Types
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mime-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
derived from /etc/mime.types in UNIX-type systems.

%package lib
Summary: lib components for the R-mime package.
Group: Libraries

%description lib
lib components for the R-mime package.


%prep
%setup -q -c -n mime
cd %{_builddir}/mime

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641058666

%install
export SOURCE_DATE_EPOCH=1641058666
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mime
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mime
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mime
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mime || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mime/DESCRIPTION
/usr/lib64/R/library/mime/INDEX
/usr/lib64/R/library/mime/Meta/Rd.rds
/usr/lib64/R/library/mime/Meta/features.rds
/usr/lib64/R/library/mime/Meta/hsearch.rds
/usr/lib64/R/library/mime/Meta/links.rds
/usr/lib64/R/library/mime/Meta/nsInfo.rds
/usr/lib64/R/library/mime/Meta/package.rds
/usr/lib64/R/library/mime/NAMESPACE
/usr/lib64/R/library/mime/NEWS.Rd
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
/usr/lib64/R/library/mime/tests/mime.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mime/libs/mime.so
/usr/lib64/R/library/mime/libs/mime.so.avx2
/usr/lib64/R/library/mime/libs/mime.so.avx512
