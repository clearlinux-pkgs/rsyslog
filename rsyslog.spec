#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rsyslog
Version  : 8.1904.0
Release  : 5
URL      : https://github.com/rsyslog/rsyslog/archive/v8.1904.0.tar.gz
Source0  : https://github.com/rsyslog/rsyslog/archive/v8.1904.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 LGPL-3.0
Requires: rsyslog-bin = %{version}-%{release}
Requires: rsyslog-lib = %{version}-%{release}
Requires: rsyslog-license = %{version}-%{release}
Requires: rsyslog-man = %{version}-%{release}
Requires: rsyslog-services = %{version}-%{release}
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
Requires: rsyslog-services = %{version}-%{release}

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


%package services
Summary: services components for the rsyslog package.
Group: Systemd services

%description services
services components for the rsyslog package.


%prep
%setup -q -n rsyslog-8.1904.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555364375
export LDFLAGS="${LDFLAGS} -fno-lto"
%autogen --disable-static --enable-imjournal
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1555364375
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rsyslog
cp COPYING %{buildroot}/usr/share/package-licenses/rsyslog/COPYING
cp COPYING.ASL20 %{buildroot}/usr/share/package-licenses/rsyslog/COPYING.ASL20
cp COPYING.LESSER %{buildroot}/usr/share/package-licenses/rsyslog/COPYING.LESSER
cp contrib/omhiredis/COPYING %{buildroot}/usr/share/package-licenses/rsyslog/contrib_omhiredis_COPYING
cp contrib/omhiredis/COPYING_LESSER %{buildroot}/usr/share/package-licenses/rsyslog/contrib_omhiredis_COPYING_LESSER
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
/usr/lib64/rsyslog/imjournal.so
/usr/lib64/rsyslog/imklog.so
/usr/lib64/rsyslog/immark.so
/usr/lib64/rsyslog/imtcp.so
/usr/lib64/rsyslog/imudp.so
/usr/lib64/rsyslog/imuxsock.so
/usr/lib64/rsyslog/lmcry_gcry.so
/usr/lib64/rsyslog/lmnet.so
/usr/lib64/rsyslog/lmnetstrms.so
/usr/lib64/rsyslog/lmnsd_ptcp.so
/usr/lib64/rsyslog/lmregexp.so
/usr/lib64/rsyslog/lmtcpclt.so
/usr/lib64/rsyslog/lmtcpsrv.so
/usr/lib64/rsyslog/lmzlibw.so
/usr/lib64/rsyslog/mmexternal.so
/usr/lib64/rsyslog/omtesting.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rsyslog/COPYING
/usr/share/package-licenses/rsyslog/COPYING.ASL20
/usr/share/package-licenses/rsyslog/COPYING.LESSER
/usr/share/package-licenses/rsyslog/contrib_omhiredis_COPYING
/usr/share/package-licenses/rsyslog/contrib_omhiredis_COPYING_LESSER

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/rsyslog.conf.5
/usr/share/man/man8/rsyslogd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rsyslog.service
