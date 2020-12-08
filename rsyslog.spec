#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rsyslog
Version  : 8.2012.0
Release  : 20
URL      : https://github.com/rsyslog/rsyslog/archive/v8.2012.0/rsyslog-8.2012.0.tar.gz
Source0  : https://github.com/rsyslog/rsyslog/archive/v8.2012.0/rsyslog-8.2012.0.tar.gz
Summary  : An enhanced multi-threaded syslogd with a focus on security and reliability
Group    : Development/Tools
License  : Apache-2.0 CDDL-1.0 GPL-3.0 LGPL-3.0
Requires: rsyslog-bin = %{version}-%{release}
Requires: rsyslog-lib = %{version}-%{release}
Requires: rsyslog-license = %{version}-%{release}
Requires: rsyslog-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : docutils
BuildRequires : flex
BuildRequires : iproute2
BuildRequires : json-c
BuildRequires : json-c-dev
BuildRequires : libestr
BuildRequires : libestr-dev
BuildRequires : libfastjson
BuildRequires : libfastjson-dev
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error
BuildRequires : libgpg-error-dev
BuildRequires : liblogging
BuildRequires : liblogging-dev
BuildRequires : libtool
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libestr)
BuildRequires : pkgconfig(libfastjson)
BuildRequires : pkgconfig(liblogging-stdlog)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libpq)
BuildRequires : pkgconfig(librabbitmq)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : valgrind
BuildRequires : zlib
BuildRequires : zlib-dev

%description


%package bin
Summary: bin components for the rsyslog package.
Group: Binaries
Requires: rsyslog-license = %{version}-%{release}

%description bin
bin components for the rsyslog package.


%package lib
Summary: lib components for the rsyslog package.
Group: Libraries
Requires: rsyslog-license = %{version}-%{release}

%description lib
lib components for the rsyslog package.


%package license
Summary: license components for the rsyslog package.
Group: Default

%description license
license components for the rsyslog package.


%package man
Summary: man components for the rsyslog package.
Group: Default

%description man
man components for the rsyslog package.


%prep
%setup -q -n rsyslog-8.2012.0
cd %{_builddir}/rsyslog-8.2012.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607385908
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --enable-gnutls \
--enable-imfile \
--enable-imjournal \
--enable-impstats \
--enable-imptcp \
--enable-inet \
--enable-mail \
--enable-omjournal \
--enable-omprog \
--enable-omstdout
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1607385908
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rsyslog
cp %{_builddir}/rsyslog-8.2012.0/COPYING %{buildroot}/usr/share/package-licenses/rsyslog/654d5ed6dd2d6ab7904d4047cde6345730f9d174
cp %{_builddir}/rsyslog-8.2012.0/COPYING.ASL20 %{buildroot}/usr/share/package-licenses/rsyslog/a0e4cbb52a11ad6dd1e4d27c0bd948eb2abc0188
cp %{_builddir}/rsyslog-8.2012.0/COPYING.LESSER %{buildroot}/usr/share/package-licenses/rsyslog/1e2bf763a406378034f0722de926e819c31ed211
cp %{_builddir}/rsyslog-8.2012.0/contrib/omhiredis/COPYING %{buildroot}/usr/share/package-licenses/rsyslog/d2773a247962f107e65362fbb37d20cdf979d0ff
cp %{_builddir}/rsyslog-8.2012.0/contrib/omhiredis/COPYING_LESSER %{buildroot}/usr/share/package-licenses/rsyslog/75b8e4445cd2df277d34b4ee6f5b1c06fca7cc91
cp %{_builddir}/rsyslog-8.2012.0/solaris/cddllicense.txt %{buildroot}/usr/share/package-licenses/rsyslog/95df6148dd543173d4a3aedb646fc703e5bed82c
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rsyslogd

%files lib
%defattr(-,root,root,-)
/usr/lib64/rsyslog/fmhash.so
/usr/lib64/rsyslog/fmhttp.so
/usr/lib64/rsyslog/imfile.so
/usr/lib64/rsyslog/imjournal.so
/usr/lib64/rsyslog/imklog.so
/usr/lib64/rsyslog/immark.so
/usr/lib64/rsyslog/impstats.so
/usr/lib64/rsyslog/imptcp.so
/usr/lib64/rsyslog/imtcp.so
/usr/lib64/rsyslog/imudp.so
/usr/lib64/rsyslog/imuxsock.so
/usr/lib64/rsyslog/lmcry_gcry.so
/usr/lib64/rsyslog/lmnet.so
/usr/lib64/rsyslog/lmnetstrms.so
/usr/lib64/rsyslog/lmnsd_gtls.so
/usr/lib64/rsyslog/lmnsd_ptcp.so
/usr/lib64/rsyslog/lmregexp.so
/usr/lib64/rsyslog/lmtcpclt.so
/usr/lib64/rsyslog/lmtcpsrv.so
/usr/lib64/rsyslog/lmzlibw.so
/usr/lib64/rsyslog/mmexternal.so
/usr/lib64/rsyslog/omjournal.so
/usr/lib64/rsyslog/ommail.so
/usr/lib64/rsyslog/omprog.so
/usr/lib64/rsyslog/omstdout.so
/usr/lib64/rsyslog/omtesting.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rsyslog/1e2bf763a406378034f0722de926e819c31ed211
/usr/share/package-licenses/rsyslog/654d5ed6dd2d6ab7904d4047cde6345730f9d174
/usr/share/package-licenses/rsyslog/75b8e4445cd2df277d34b4ee6f5b1c06fca7cc91
/usr/share/package-licenses/rsyslog/95df6148dd543173d4a3aedb646fc703e5bed82c
/usr/share/package-licenses/rsyslog/a0e4cbb52a11ad6dd1e4d27c0bd948eb2abc0188
/usr/share/package-licenses/rsyslog/d2773a247962f107e65362fbb37d20cdf979d0ff

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/rsyslog.conf.5
/usr/share/man/man8/rsyslogd.8
