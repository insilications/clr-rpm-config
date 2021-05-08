#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-rpm-config
Version  : 224
Release  : 295
URL      : file:///aot/build/clearlinux/packages/clr-rpm-config/clr-rpm-config-224.tar.gz
Source0  : file:///aot/build/clearlinux/packages/clr-rpm-config/clr-rpm-config-224.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-avx-tools
Requires: clr-python-timestamp
BuildRequires : clr-avx-tools
BuildRequires : clr-python-timestamp

%description
No detailed description available

%prep
%setup -q -n clr-rpm-config
cd %{_builddir}/clr-rpm-config

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620516391
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1620516391
rm -rf %{buildroot}
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/rpm
ln -s clr %{buildroot}/usr/lib/rpm/unknown
ln -s clr %{buildroot}/usr/lib/rpm/generic
ln -s clr %{buildroot}/usr/lib/rpm/redhat
ln -s clr %{buildroot}/usr/lib/rpm/koji
ln -s clr %{buildroot}/usr/lib/rpm/pc
rm -f %{buildroot}/usr/lib/rpm/clr/perl.prov
ln -s /usr/lib/rpm/perl.prov %{buildroot}/usr/lib/rpm/clr/perl.prov
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/rpm/clr/LICENSE
/usr/lib/rpm/clr/VERSION
/usr/lib/rpm/clr/auto_path.tcl
/usr/lib/rpm/clr/brp-compress
/usr/lib/rpm/clr/brp-create-abi
/usr/lib/rpm/clr/brp-fix-pyc-reproducibility
/usr/lib/rpm/clr/brp-implant-ident-static
/usr/lib/rpm/clr/brp-java-repack-jars
/usr/lib/rpm/clr/brp-python-bytecompile
/usr/lib/rpm/clr/brp-python-hardlink
/usr/lib/rpm/clr/brp-redhat
/usr/lib/rpm/clr/brp-sparc64-linux
/usr/lib/rpm/clr/brp-strip
/usr/lib/rpm/clr/brp-strip-comment-note
/usr/lib/rpm/clr/brp-strip-shared
/usr/lib/rpm/clr/brp-strip-static-archive
/usr/lib/rpm/clr/brp-strip-static-lto
/usr/lib/rpm/clr/cmake.prov
/usr/lib/rpm/clr/config.guess
/usr/lib/rpm/clr/config.sub
/usr/lib/rpm/clr/dist.sh
/usr/lib/rpm/clr/find-provides
/usr/lib/rpm/clr/find-provides.d/firmware.prov
/usr/lib/rpm/clr/find-provides.d/modalias.prov
/usr/lib/rpm/clr/find-provides.debuginfo
/usr/lib/rpm/clr/find-provides.ksyms
/usr/lib/rpm/clr/find-provides.libtool
/usr/lib/rpm/clr/find-provides.pkgconfig
/usr/lib/rpm/clr/find-requires
/usr/lib/rpm/clr/find-requires.ksyms
/usr/lib/rpm/clr/find-requires.libtool
/usr/lib/rpm/clr/find-requires.pkgconfig
/usr/lib/rpm/clr/macros
/usr/lib/rpm/clr/mvn.prov
/usr/lib/rpm/clr/perl.prov
/usr/lib/rpm/clr/perl.req
/usr/lib/rpm/clr/rpmrc
/usr/lib/rpm/clr/rpmsort
/usr/lib/rpm/clr/so_symlink.req
/usr/lib/rpm/clr/symset-table
/usr/lib/rpm/fileattrs/cmake.attr
/usr/lib/rpm/fileattrs/elfoptimized.attr
/usr/lib/rpm/fileattrs/mingw.attr
/usr/lib/rpm/fileattrs/mvn.attr
/usr/lib/rpm/fileattrs/openmpi.attr
/usr/lib/rpm/fileattrs/perl.attr
/usr/lib/rpm/fileattrs/so_symlink.attr
/usr/lib/rpm/generic
/usr/lib/rpm/koji
/usr/lib/rpm/pc
/usr/lib/rpm/redhat
/usr/lib/rpm/unknown
