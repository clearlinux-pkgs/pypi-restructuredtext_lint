#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-restructuredtext_lint
Version  : 1.4.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/48/9c/6d8035cafa2d2d314f34e6cd9313a299de095b26e96f1c7312878f988eec/restructuredtext_lint-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/9c/6d8035cafa2d2d314f34e6cd9313a299de095b26e96f1c7312878f988eec/restructuredtext_lint-1.4.0.tar.gz
Summary  : reStructuredText linter
Group    : Development/Tools
License  : Unlicense
Requires: pypi-restructuredtext_lint-bin = %{version}-%{release}
Requires: pypi-restructuredtext_lint-license = %{version}-%{release}
Requires: pypi-restructuredtext_lint-python = %{version}-%{release}
Requires: pypi-restructuredtext_lint-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)

%description
restructuredtext-lint
=====================
.. image:: https://travis-ci.org/twolfson/restructuredtext-lint.png?branch=master
:target: https://travis-ci.org/twolfson/restructuredtext-lint
:alt: Build Status

%package bin
Summary: bin components for the pypi-restructuredtext_lint package.
Group: Binaries
Requires: pypi-restructuredtext_lint-license = %{version}-%{release}

%description bin
bin components for the pypi-restructuredtext_lint package.


%package license
Summary: license components for the pypi-restructuredtext_lint package.
Group: Default

%description license
license components for the pypi-restructuredtext_lint package.


%package python
Summary: python components for the pypi-restructuredtext_lint package.
Group: Default
Requires: pypi-restructuredtext_lint-python3 = %{version}-%{release}

%description python
python components for the pypi-restructuredtext_lint package.


%package python3
Summary: python3 components for the pypi-restructuredtext_lint package.
Group: Default
Requires: python3-core
Provides: pypi(restructuredtext_lint)
Requires: pypi(docutils)

%description python3
python3 components for the pypi-restructuredtext_lint package.


%prep
%setup -q -n restructuredtext_lint-1.4.0
cd %{_builddir}/restructuredtext_lint-1.4.0
pushd ..
cp -a restructuredtext_lint-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656404804
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-restructuredtext_lint
cp %{_builddir}/restructuredtext_lint-1.4.0/UNLICENSE %{buildroot}/usr/share/package-licenses/pypi-restructuredtext_lint/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/restructuredtext-lint
/usr/bin/rst-lint

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-restructuredtext_lint/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
