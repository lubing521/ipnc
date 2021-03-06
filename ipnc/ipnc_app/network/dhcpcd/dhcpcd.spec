%define ver	1.3.22-pl4
%define rel	1
%define prefix	/usr

Summary:	DHCP Client Daemon.
Name:		dhcpcd
Version:	1.3.22pl4
Release:	%rel
Copyright:	GPL
Group:		Daemons/Networking
Source:		ftp://ftp.phystech.com/pub/%{name}-%{ver}.tar.gz
URL:		http://www.phystech.com/download
BuildRoot:	/var/tmp/%{name}-%{ver}-%{rel}-root
Packager:	Fill In As You Wish
Docdir:		%{prefix}/doc

%description
This package contains the development release of a DHCP Client 
Daemon for Linux kernels 2.0-2.5

Authors:
	Sergei Viznyuk	<sv@phystech.com>


%prep
%setup -q -n %{name}-%{ver}


%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
	CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix
else
	CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
fi

if [ "$SMP" != "" ]; then
	JSMP	= '"MAKE=make -k -j $SMP"'
fi

make ${JSMP};


%install
[ -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}

make DESTDIR=${RPM_BUILD_ROOT} install-strip
mkdir -p ${RPM_BUILD_ROOT}/etc/dhcpc


%clean
(PKGDIR=`pwd`; cd ..; rm -rf ${PKGDIR} ${RPM_BUILD_ROOT})


%files
%defattr (-, root, root)
/sbin/dhcpcd
%{prefix}/man/man8/*
%dir /etc/dhcpc
%doc ChangeLog
%doc COPYING
%doc INSTALL
%doc README
%doc *.lsm

