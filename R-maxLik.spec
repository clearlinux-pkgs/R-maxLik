#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-maxLik
Version  : 1.3.8
Release  : 27
URL      : https://cran.r-project.org/src/contrib/maxLik_1.3-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/maxLik_1.3-8.tar.gz
Summary  : Maximum Likelihood Estimation and Related Tools
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-dlm
Requires: R-miscTools
Requires: R-sandwich
BuildRequires : R-dlm
BuildRequires : R-miscTools
BuildRequires : R-sandwich
BuildRequires : buildreq-R

%description
optimization, and related tools.  It includes a unified way to call
   different optimizers, and classes and methods to handle the results from
   the ML viewpoint.  It also includes a number of convenience tools for testing
   and developing your own models.

%prep
%setup -q -c -n maxLik

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578694417

%install
export SOURCE_DATE_EPOCH=1578694417
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maxLik
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maxLik
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maxLik
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc maxLik || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/maxLik/CITATION
/usr/lib64/R/library/maxLik/DESCRIPTION
/usr/lib64/R/library/maxLik/INDEX
/usr/lib64/R/library/maxLik/Meta/Rd.rds
/usr/lib64/R/library/maxLik/Meta/features.rds
/usr/lib64/R/library/maxLik/Meta/hsearch.rds
/usr/lib64/R/library/maxLik/Meta/links.rds
/usr/lib64/R/library/maxLik/Meta/nsInfo.rds
/usr/lib64/R/library/maxLik/Meta/package.rds
/usr/lib64/R/library/maxLik/NAMESPACE
/usr/lib64/R/library/maxLik/NEWS
/usr/lib64/R/library/maxLik/R/maxLik
/usr/lib64/R/library/maxLik/R/maxLik.rdb
/usr/lib64/R/library/maxLik/R/maxLik.rdx
/usr/lib64/R/library/maxLik/help/AnIndex
/usr/lib64/R/library/maxLik/help/aliases.rds
/usr/lib64/R/library/maxLik/help/maxLik.rdb
/usr/lib64/R/library/maxLik/help/maxLik.rdx
/usr/lib64/R/library/maxLik/help/paths.rds
/usr/lib64/R/library/maxLik/html/00Index.html
/usr/lib64/R/library/maxLik/html/R.css
/usr/lib64/R/library/maxLik/tests/BFGSR.R
/usr/lib64/R/library/maxLik/tests/BFGSR.Rout.save
/usr/lib64/R/library/maxLik/tests/basicTest.R
/usr/lib64/R/library/maxLik/tests/basicTest.Rout.save
/usr/lib64/R/library/maxLik/tests/constraints.R
/usr/lib64/R/library/maxLik/tests/constraints.Rout.save
/usr/lib64/R/library/maxLik/tests/finalHessian.R
/usr/lib64/R/library/maxLik/tests/finalHessian.Rout.save
/usr/lib64/R/library/maxLik/tests/fitNormalDist_privateTest.Rout.save
/usr/lib64/R/library/maxLik/tests/methods.R
/usr/lib64/R/library/maxLik/tests/methods.Rout.save
/usr/lib64/R/library/maxLik/tests/numericGradient.R
/usr/lib64/R/library/maxLik/tests/numericGradient.Rout.save
/usr/lib64/R/library/maxLik/tests/parameters_privateTest.Rout.save
