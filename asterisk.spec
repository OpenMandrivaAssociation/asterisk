%define	name	asterisk
%define	version	1.6.2.2
%define release	%mkrel 1

%define _requires_exceptions perl(Carp::Heavy)
%define _disable_ld_no_undefined 1

%define build_h323	0
%{?_without_h323:	%global build_h323 0}
%{?_with_h323:		%global build_h323 1}

# not compatible >=kernel-2.6.25 Using instead asterisk-chan_lcr
%define build_misdn	0
%{?_without_misdn:	%global build_misdn 0}
%{?_with_misdn:		%global build_misdn 1}

%define build_odbc	0
%{?_without_odbc:	%global build_odbc 0}
%{?_with_odbc:		%global build_odbc 1}

%define build_oss	1
%{?_without_oss:	%global build_oss 0}
%{?_with_oss:		%global build_oss 1}

%define build_radius	1
%{?_without_radius:	%global build_radius 0}
%{?_with_radius:	%global build_radius 1}

%define build_tds	1
%{?_without_tds:	%global build_tds 0}
%{?_with_tds:		%global build_tds 1}

# this takes quite some time and adds roughly 200mb of html...
%define build_docs	0
%{?_without_docs:	%global build_docs 0}
%{?_with_docs:		%global build_docs 1}

#define beta 4

Summary:	The Open Source PBX
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		System/Servers
URL:		http://www.asterisk.org/
Source0:	http://downloads.asterisk.org/pub/telephony/asterisk/%{name}-%{version}%{?beta:-rc%{beta}}.tar.gz
Source1:	asterisk-logrotate
Source2:	menuselect.makedeps
Source3:	menuselect.makeopts
Source4:	g72x_install
Patch1:		0001-Modify-init-scripts-for-better-Fedora-compatibility.patch
Patch2:		0002-Modify-modules.conf-so-that-different-voicemail-modu.patch
Patch4:		0004-Use-pkgconfig-to-check-for-Lua.patch
Patch5:		0005-Revert-changes-to-pbx_lua-from-rev-126363-that-cause.patch
Patch6:		0006-Build-using-external-libedit.diff
Patch7:		0007-Use-pkgconfig-to-check-for-Gmime-2.2.patch
#Patch8:		0008-libusb-check.diff
Patch50:	asterisk-1.6.1-rc1-utils_pthread_fix.diff
Patch51:	asterisk-1.6.1-beta3-net-snmp_fix.diff
Patch52:	asterisk-1.6.1-beta3-ffmpeg_fix.diff
Patch53:	asterisk-external_liblpc10_and_libilbc.diff
#Patch54:	asterisk-1.6.1-beta3-pwlib_and_openh323_fix.diff
#Patch55:	AST_PBX_KEEPALIVE-1.6.1-fix.diff
Patch56:	strlcpy-strlcat-1.6.1-fix.diff
Patch57:	editline-include-missing-1.6.1-fix.diff
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires:	mpg123
Requires:	asterisk-core-sounds, asterisk-moh
BuildRequires:	%{_lib}alsa2-devel
BuildRequires:	autoconf >= 1:2.60
BuildRequires:	automake1.9 >= 1.9.6
BuildRequires:	bison
BuildRequires:	bluez-devel
BuildRequires:	curl-devel
BuildRequires:	dahdi-devel >= 2.0.0
BuildRequires:	ffmpeg-devel
BuildRequires:	flex
BuildRequires:	freetds-devel >= 0.64
BuildRequires:	libgmime2.2-devel
BuildRequires:	gmime2.2-utils
BuildRequires:	gsm-devel
BuildRequires:	gtk-devel
BuildRequires:	gtk2-devel
BuildRequires:	jackit-devel
BuildRequires:	krb5-devel
BuildRequires:	libcap-devel
BuildRequires:	libedit-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libgnutls-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libgsm-devel
BuildRequires:	%mklibname hoard
BuildRequires:	libidn-devel
BuildRequires:	libiksemel-devel
BuildRequires:	libilbc-devel
BuildRequires:	libnbs-devel
BuildRequires:	libogg-devel
#BuildRequires:	libosp-devel >= 3.5.0
BuildRequires:	libpopt-devel
BuildRequires:	libpri-devel >= 1.4.8
BuildRequires:	libss7-devel >= 1.0.2
BuildRequires:	libtool
BuildRequires:	libtool-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libzap-devel >= 1.0.1
BuildRequires:	lm_sensors-devel
BuildRequires:	lpc10-devel
BuildRequires:	%{_lib}lua-devel
%if %{build_misdn}
BuildRequires:	isdn4k-utils-devel
BuildRequires:	isdn4net
BuildRequires:	misdn2-devel
%endif
BuildRequires:	ncurses-devel
BuildRequires:	net-snmp-devel
BuildRequires:	newt-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	openais-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	osptk-devel >= 3.5.0
BuildRequires:	pam-devel
BuildRequires:	perl-devel
BuildRequires:	portaudio-devel >= 19
BuildRequires:	postgresql-devel
BuildRequires:	radiusclient-ng-devel
BuildRequires:	resample-devel
BuildRequires:	SDL_image-devel
BuildRequires:	spandsp-devel
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel
BuildRequires:	tcp_wrappers-devel
BuildRequires:	termcap-devel
BuildRequires:	tiff-devel
%if %{build_odbc}
BuildRequires:	unixODBC-devel
%endif
#BuildRequires:	usb1.0-devel
BuildRequires:	%{_lib}usb-compat0.1-devel
BuildRequires:	wget
BuildRequires:	zlib-devel
%if %mdkversion < 200900
BuildRequires:	imap-devel
%else
BuildRequires:	c-client-devel
%endif
%if %{build_h323}
BuildRequires:	ooh323c-devel
BuildRequires:	openh323-devel >= 1.15.3
BuildRequires:	pwlib-devel
%endif
%if %{build_docs}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Asterisk is a complete PBX in software. It runs on Linux and provides
all of the features you would expect from a PBX and more. Asterisk
does voice over IP in three protocols, and can interoperate with
almost all standards-based telephony equipment using relatively
inexpensive hardware.

%package	firmware
Summary:	Firmware for the Digium S101I (IAXy)
Group:		System/Servers
License:	Redistributable, no modification permitted
Requires:	asterisk = %{version}-%{release}

%description	firmware
Firmware for the Digium S101I (IAXy).

%package	devel
Summary:	Header files for building Asterisk modules
Group:		Development/C

%description	devel
This package contains the development header files that are needed
to compile 3rd party modules.

%package	plugins-ais
Summary:	Modules for Asterisk that use OpenAIS
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-ais
Modules for Asterisk that use OpenAIS.

%package	plugins-alsa
Summary:	Modules for Asterisk that use Alsa sound drivers
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-alsa
Modules for Asterisk that use Alsa sound drivers.

%package	plugins-curl
Summary:	Modules for Asterisk that use cURL
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-curl
Modules for Asterisk that use cURL.

%package	plugins-dahdi
Summary:	Modules for Asterisk that use DAHDI
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	dahdi-tools >= 2.0.0

%description	plugins-dahdi
Modules for Asterisk that use DAHDI.

%package	plugins-fax
Summary:	FAX plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-fax
This package contains FAX plugins for Asterisk.

%package	plugins-festival
Summary:	Festival application for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	festival

%description	plugins-festival
Application for the Asterisk PBX that uses Festival to convert text to speech.

%package	plugins-ices
Summary:	Stream audio from Asterisk to an IceCast server
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	ices

%description	plugins-ices
Stream audio from Asterisk to an IceCast server.

%package	plugins-jabber
Summary:	Jabber support for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-jabber
This package contains Jabber support for Asterisk.

%package	plugins-jack
Summary:	JACK resources for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-jack
JACK resources for Asterisk.

%package	plugins-lua
Summary:	Lua resources for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-lua
Lua resources for Asterisk.

%package	plugins-ldap
Summary:	LDAP resources for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-ldap
LDAP resources for Asterisk.

%if %{build_misdn}
%package	plugins-misdn
Summary:	This module adds mISDN support to the Asterisk PBX
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-misdn
This module adds mISDN support to the Asterisk PBX. mISDN is the
(experimental) new ISDN4Linux stack, which adds support for
driving cards in NT mode and thus connecting an ISDN phone to your
computer.
%endif

%package	plugins-minivm
Summary:	MiniVM applicaton for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-minivm
MiniVM application for Asterisk.

%if %{build_odbc}
%package	plugins-odbc
Summary:	Applications for Asterisk that use ODBC (except voicemail)
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-odbc
Applications for Asterisk that use ODBC (except voicemail)
%endif

%if %{build_oss}
%package	plugins-oss
Summary:	Modules for Asterisk that use OSS sound drivers
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-oss
Modules for Asterisk that use OSS sound drivers.

%package	plugins-usbradio
Summary:	USB radio channel for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-usbradio
USB radio channel for Asterisk.
%endif

%package	plugins-portaudio
Summary:	Modules for Asterisk that use the portaudio library
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-portaudio
Modules for Asterisk that use the portaudio library.

%package	plugins-pgsql
Summary:	PostgreSQL plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-pgsql
This package contains PostgreSQL plugins for Asterisk.

%if %{build_radius}
%package	plugins-radius
Summary:	Radiusclient plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-radius
This package contains Radiusclient plugins for Asterisk.
%endif

%package	plugins-skinny
Summary:	Modules for Asterisk that support the SCCP/Skinny protocol
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-skinny
Modules for Asterisk that support the SCCP/Skinny protocol.

%package	plugins-snmp
Summary:	Brief SNMP Agent / SubAgent support for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	net-snmp

%description	plugins-snmp
This package contains brief SNMP Agent / SubAgent support for Asterisk.

%package	plugins-speex
Summary:	SPEEX plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-speex
This package contains SPEEX plugins for Asterisk.

%package	plugins-sqlite
Summary:	SQLite plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-sqlite
This package contains SQLite plugins for Asterisk.

%if %{build_tds}
%package	plugins-tds
Summary:	FreeTDS plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-tds
This package contains FreeTDS plugins for Asterisk.
%endif

%package	plugins-osp
Summary:	Open Settlement Protocol for Asterisk
Group:		System/Servers

%description	plugins-osp
This package contains OSP (Open Settlement Protocol) support for Asterisk.

%package	plugins-unistim
Summary:	Unistim channel for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-unistim
Unistim channel for Asterisk.

%package	plugins-voicemail
Summary:	Common Voicemail Modules for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	asterisk-plugins-voicemail-implementation = %{version}-%{release}
Requires:	sox
Requires:	sendmail-command

%description	plugins-voicemail
Common Voicemail Modules for Asterisk.

%package	plugins-voicemail-imap
Summary:	Store voicemail on an IMAP server
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	asterisk-plugins-voicemail = %{version}-%{release}
Provides:	asterisk-plugins-voicemail-implementation = %{version}-%{release}

%description	plugins-voicemail-imap
Voicemail implementation for Asterisk that stores voicemail on an IMAP
server.

%if %{build_odbc}
%package	plugins-voicemail-odbc
Summary:	Store voicemail in a database using ODBC
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	asterisk-plugins-voicemail = %{version}-%{release}
Provides:	asterisk-plugins-voicemail-implementation = %{version}-%{release}

%description	plugins-voicemail-odbc
Voicemail implementation for Asterisk that uses ODBC to store
voicemail in a database.
%endif

%package	plugins-voicemail-plain
Summary:	Store voicemail on the local filesystem
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	asterisk-plugins-voicemail = %{version}-%{release}
Provides:	asterisk-plugins-voicemail-implementation = %{version}-%{release}

%description	plugins-voicemail-plain
Voicemail implementation for Asterisk that stores voicemail on the
local filesystem.

%prep

%setup0 -q -n asterisk-%{version}%{?beta:-rc%{beta}}

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type d -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;
		
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
	if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch1 -p1 -b .init
%patch2 -p1 -b .voicemail
#%patch4 -p1 -b .lua
##%patch5 -p1 -b .pbx_lua
###%patch6 -p1 -b .libedit
#%patch7 -p1 -b .gmime-2_2
##%patch8 -p1 -b .libusb
##
%patch50 -p1 -b .pthread
%patch51 -p0 -b .net_snmp
%patch52 -p1 -b .ffmpeg
%patch53 -p0 -b .libplc10
##%patch54 -p0 -b .pwlib
#%patch56 -p0 -b .strlcpy
%patch57 -p0 -b .editline

cp %{SOURCE2} menuselect.makedeps
cp %{SOURCE3} menuselect.makeopts
cp %{SOURCE4} g72x_install

# Fixup makefile so sound archives aren't downloaded/installed
%{__perl} -pi -e 's/^all:.*$/all:/' sounds/Makefile
%{__perl} -pi -e 's/^install:.*$/install:/' sounds/Makefile

# convert comments in one file to UTF-8
mv main/fskmodem.c main/fskmodem.c.old
iconv -f iso-8859-1 -t utf-8 -o main/fskmodem.c main/fskmodem.c.old
touch -r main/fskmodem.c.old main/fskmodem.c
rm main/fskmodem.c.old

chmod -x contrib/scripts/dbsep.cgi

# lib64 fix
find -name "Makefile" | xargs perl -pi -e "s|/usr/lib|%{_libdir}|g"
perl -pi -e "s|/lib\b|/%{_lib}|g" configure* autoconf/*.m4
perl -pi -e "s|/lib/|/%{_lib}/|g" configure*  autoconf/*.m4

%build

# if we are building for i386 promote the CPU arch to i486 for atomic operations support
%ifarch i386
%define optflags %{__global_cflags} -m32 -march=i486 -mtune=generic -fasynchronous-unwind-tables -Werror-implicit-function-declaration
%else
%define optflags %(rpm --eval %%{optflags}) -Werror-implicit-function-declaration
%endif

#rm -f autoconf/ast_prog_sed.m4
./bootstrap.sh

pushd menuselect/mxml
%configure2_5x
popd

pushd menuselect
%configure2_5x
popd 

pushd main/editline
%configure2_5x
popd

export CFLAGS="%{optflags} `gmime-config --cflags`"

%configure \
	--localstatedir=/var \
	--with-asound=%{_prefix} \
	--with-execinfo=%{_prefix} \
	--with-cap=%{_prefix} \
	--with-curl=%{_prefix} \
	--with-curses=%{_prefix} \
	--with-crypto=%{_prefix} \
	--with-dahdi=%{_prefix} \
	--with-avcodec=%{_prefix} \
	--with-gsm=%{_prefix} \
	--with-gtk2=%{_prefix} \
	--with-gmime=%{_prefix} \
	--with-hoard=%{_prefix} \
	--with-iconv=%{_prefix} \
	--with-iksemel=%{_prefix} \
	--with-imap=system \
	--with-inotify=%{_prefix} \
%if %{build_odbc}
	--with-iodbc=%{_prefix} \
%else
	--without-iodbc \
%endif
	--with-jack=%{_prefix} \
	--with-ldap=%{_prefix} \
	--with-ltdl=%{_prefix} \
	--with-lua=%{_prefix} \
%if %{build_misdn}
	--with-isdnnet=%{_prefix} \
	--with-misdn=%{_prefix} \
	--with-suppserv=%{_prefix} \
%else
	--without-isdnnet \
	--without-misdn \
	--without-suppserv \
%endif
	--with-nbs=%{_prefix} \
	--with-ncurses=%{_prefix} \
	--with-netsnmp=%{_prefix} \
	--with-newt=%{_prefix} \
	--with-ogg=%{_prefix} \
	--with-osptk=%{_prefix} \
%if %{build_oss}
	--with-oss \
%else
	--without-oss \
%endif
	--with-postgres=%{_prefix} \
	--with-popt=%{_prefix} \
	--with-portaudio=%{_prefix} \
	--with-pri=%{_prefix} \
	--with-resample=%{_prefix} \
	--with-spandsp=%{_prefix} \
	--with-ss7=%{_prefix} \
%if %{build_h323}
	--with-pwlib=%{_prefix} \
	--with-h323=%{_prefix} \
%else
	--without-pwlib \
	--without-h323 \
%endif
	--with-radius=%{_prefix} \
	--with-sdl=%{_prefix} \
	--with-SDL_image=%{_prefix} \
	--with-openais=%{_prefix} \
	--with-speex=%{_prefix} \
	--with-speexdsp=%{_prefix} \
	--without-sqlite \
	--with-sqlite3=%{_prefix} \
	--with-ssl=%{_prefix} \
	--with-tds=%{_prefix} \
	--with-termcap=%{_prefix} \
	--without-tinfo \
	--with-tonezone=%{_prefix} \
%if %{build_odbc}
	--with-unixodbc=%{_prefix} \
%else
	--without-unixodbc \
%endif
	--with-usb=%{_prefix} \
	--with-vorbis=%{_prefix} \
	--without-vpb \
	--with-x11=%{_prefix} \
	--with-z=%{_prefix} \
	--with-timerfd=%{_prefix}
#urpmf --files openr2.h
#	--with-openr2=%{_prefix} \

# fix some weirdos
GMIME_INCLUDE=`gmime-config --cflags`
perl -pi -e "s|^AIS_INCLUDE=.*|AIS_INCLUDE=-I/usr/include/openais|g" makeopts
perl -pi -e "s|^GMIME_INCLUDE=.*|GMIME_INCLUDE=$GMIME_INCLUDE|g" makeopts

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=FILE_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=/var/run/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_plain.so
mv apps/app_directory.so apps/app_directory_plain.so

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=IMAP_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=/var/run/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_imap.so
mv apps/app_directory.so apps/app_directory_imap.so

%if %{build_odbc}
%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=ODBC_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=/var/run/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_odbc.so
mv apps/app_directory.so apps/app_directory_odbc.so
%endif

# so that these modules don't get built again during the install phase
touch apps/app_voicemail.o apps/app_directory.o
touch apps/app_voicemail.so apps/app_directory.so

%if %{build_docs}
ASTCFLAGS="%{optflags}" make progdocs DEBUG= OPTIMIZE= ASTVARRUNDIR=/var/run/asterisk NOISY_BUILD=1

# fix dates so that we don't get multilib conflicts
find doc/api/html -type f -print0 | xargs --null touch -r ChangeLog
%endif

%install
rm -rf %{buildroot}

ASTCFLAGS="%{optflags}" make install DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=/var/run/asterisk
ASTCFLAGS="%{optflags}" make samples DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=/var/run/asterisk

install -D -p -m 0755 contrib/init.d/rc.redhat.asterisk %{buildroot}%{_initrddir}/asterisk
install -D -p -m 0644 contrib/sysconfig/asterisk %{buildroot}%{_sysconfdir}/sysconfig/asterisk
install -D -p -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/asterisk
install -D -p -m 0644 doc/asterisk-mib.txt %{buildroot}/var/lib/snmp/mibs/ASTERISK-MIB.txt
install -D -p -m 0644 doc/digium-mib.txt %{buildroot}/var/lib/snmp/mibs/DIGIUM-MIB.txt

rm %{buildroot}%{_libdir}/asterisk/modules/app_directory.so
rm %{buildroot}%{_libdir}/asterisk/modules/app_voicemail.so
install -D -p -m 0755 apps/app_directory_imap.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_imap.so %{buildroot}%{_libdir}/asterisk/modules/
%if %{build_odbc}
install -D -p -m 0755 apps/app_directory_odbc.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_odbc.so %{buildroot}%{_libdir}/asterisk/modules/
%endif
install -D -p -m 0755 apps/app_directory_plain.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_plain.so %{buildroot}%{_libdir}/asterisk/modules/

# create some directories that need to be packaged
mkdir -p %{buildroot}/var/lib/asterisk/moh
mkdir -p %{buildroot}/var/lib/asterisk/sounds
mkdir -p %{buildroot}/var/lib/asterisk
mkdir -p %{buildroot}/var/log/asterisk/cdr-custom
mkdir -p %{buildroot}/var/spool/asterisk/monitor
mkdir -p %{buildroot}/var/spool/asterisk/outgoing

# We're not going to package any of the sample AGI scripts
rm -f %{buildroot}/var/lib/asterisk/agi-bin/*

# Don't package the sample voicemail user
rm -rf %{buildroot}/var/spool/asterisk/voicemail/default

# Don't package example phone provision configs
rm -rf %{buildroot}/var/lib/asterisk/phoneprov/*

# these are compiled with -O0 and thus include unfortified code.
rm -rf %{buildroot}%{_sbindir}/hashtest
rm -rf %{buildroot}%{_sbindir}/hashtest2

touch %{name}-devel.filelist
%if %{build_docs}
	find doc/api/html -name \*.map -size 0 -delete
	find doc/api/html -type f | sed 's/^/%doc /' | grep -v '\./%{name}-devel.filelist' > %{name}-devel.filelist
%endif

# fix ghost files
touch %{buildroot}/var/lib/asterisk/astdb
touch %{buildroot}/var/log/asterisk/console
touch %{buildroot}/var/log/asterisk/debug
touch %{buildroot}/var/log/asterisk/messages
touch %{buildroot}/var/log/asterisk/queue_log
touch %{buildroot}/var/log/asterisk/event_log
touch %{buildroot}/var/log/asterisk/cdr-csv/Master.csv
touch %{buildroot}/var/log/asterisk/h323_log

# remove unused files
%if !%{build_odbc}
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/cdr_odbc.conf
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/func_odbc.conf
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/res_odbc.conf
%endif
%if !%{build_misdn}
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/misdn.conf
%endif
%if !%{build_oss}
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/oss.conf
%endif

%pre
%_pre_useradd asterisk /var/lib/asterisk /bin/sh
gpasswd -a asterisk dialout 1>/dev/null

%post
%create_ghostfile /var/lib/asterisk/astdb asterisk asterisk 640
%create_ghostfile /var/log/asterisk/console asterisk asterisk 640
%create_ghostfile /var/log/asterisk/debug asterisk asterisk 640
%create_ghostfile /var/log/asterisk/messages asterisk asterisk 640
%create_ghostfile /var/log/asterisk/queue_log asterisk asterisk 640
%create_ghostfile /var/log/asterisk/event_log asterisk asterisk 640
%create_ghostfile /var/log/asterisk/cdr-csv/Master.csv asterisk asterisk 640
%create_ghostfile /var/log/asterisk/h323_log asterisk asterisk 640
echo "Adding setuid root to /usr/bin/mpg123, needed for MOH"
chmod u+s %{_bindir}/mpg123
[[ -e %{_libdir}/asterisk/modules/codec_g729.so ]] && sh %{_docdir}/g72x_install
%_post_service asterisk

%preun
if [ "$1" = 0 ]; then
	echo "Removing setuid root from /usr/bin/mpg123"
	chmod u-s %{_bindir}/mpg123
fi
# Remove the G72x stuff
rm -rf /usr/share/doc/asterisk/README.g72x.txt
rm -rf /usr/$LIBNAME/asterisk/modules/codec_g723.so
rm -rf /usr/$LIBNAME/asterisk/modules/codec_g729.so
rm -rf /usr/bin/g729_my_enc
rm -rf /usr/bin/g729_my_dec
rm -rf /usr/bin/astconv

%_preun_service asterisk

%postun
%_postun_userdel asterisk
gpasswd -d asterisk dialout 1>/dev/null

%pre plugins-dahdi
%{_sbindir}/usermod -a -G dahdi asterisk

%if %{build_misdn}
%pre plugins-misdn
%{_sbindir}/usermod -a -G misdn asterisk
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README* *.txt ChangeLog BUGS CREDITS configs
%doc doc/asterisk.sgml doc/backtrace.txt doc/callfiles.txt
%doc doc/externalivr.txt doc/macroexclusive.txt doc/manager_1_1.txt
%doc doc/modules.txt doc/PEERING doc/queue.txt doc/rtp-packetization.txt
%doc doc/siptls.txt doc/smdi.txt doc/sms.txt doc/speechrec.txt
%doc doc/ss7.txt doc/video.txt
%doc g72x_install
%{_initrddir}/asterisk
%attr(0750,asterisk,asterisk) %dir %{_sysconfdir}/asterisk
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adsi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adtranvofr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/agents.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alarmreceiver.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/amd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_aliases.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_permissions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/codecs.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dnsmgr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dsp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dundi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/enum.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extconfig.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.ael
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/features.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/followme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/h323.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/http.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iax.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iaxprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/indications.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/logger.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/mgcp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/modules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/musiconhold.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/muted.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phone.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phoneprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queuerules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queues.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/rpt.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/rtp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/say.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip_notify.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sla.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/smdi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/telcordia-1.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/udptl.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/users.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/vpb.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/asterisk
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/asterisk
%dir %{_libdir}/asterisk
%dir %{_libdir}/asterisk/modules
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_adsiprog.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_alarmreceiver.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_amd.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_authenticate.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_cdr.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_chanisavail.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_channelredirect.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_chanspy.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_confbridge.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_controlplayback.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_db.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dial.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dictate.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_directed_pickup.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_disa.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dumpchan.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_echo.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_exec.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_externalivr.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_followme.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_forkcdr.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_getcpeid.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_image.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_ivrdemo.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_macro.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_milliwatt.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_mixmonitor.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_morsecode.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_mp3.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_nbscat.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_originate.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_parkandannounce.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_playback.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_playtones.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_privacy.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_queue.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_readexten.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_readfile.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_read.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_record.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_rpt.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_sayunixtime.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_senddtmf.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_sendtext.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_setcallerid.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_skel.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_sms.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_softhangup.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_speech_utils.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_stack.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_system.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_talkdetect.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_test.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_transfer.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_url.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_userevent.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_waitforring.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_waitforsilence.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_waituntil.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_verbose.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_while.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_zapateller.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/bridge_builtin_features.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/bridge_multiplexed.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/bridge_simple.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/bridge_softmix.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_csv.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_custom.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_manager.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_agent.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_bridge.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_iax2.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_local.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_mgcp.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_nbs.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_phone.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_sip.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_adpcm.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_alaw.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_a_mu.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_g722.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_g726.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_gsm.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_ilbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_lpc10.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_resample.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_ulaw.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_g723.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_g726.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_g729.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_gsm.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_h263.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_h264.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_ilbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_jpeg.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_ogg_vorbis.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_pcm.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_siren14.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_siren7.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_sln16.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_sln.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_wav_gsm.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_wav.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_vox.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_audiohookinherit.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_aes.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_base64.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_blacklist.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_callerid.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_cdr.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_channel.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_config.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_cut.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_db.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_devstate.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_dialgroup.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_dialplan.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_enum.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_env.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_extstate.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_global.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_groupcount.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_iconv.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_lock.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_logic.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_math.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_md5.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_module.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_rand.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_realtime.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_sha1.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_shell.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_sprintf.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_strings.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_sysinfo.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_timeout.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_uri.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_version.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_volume.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_ael.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_config.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_dundi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_gtkconsole.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_loopback.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_realtime.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_spool.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_adsi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_ael_share.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_agi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_clialiases.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_clioriginate.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_convert.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_crypto.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_http_post.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_limit.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_monitor.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_musiconhold.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_phoneprov.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_realtime.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_smdi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_speech.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_timing_pthread.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_timing_timerfd.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/test_dlinklists.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/test_heap.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/test_sched.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/test_skel.so
%attr(0755,root,root) %{_sbindir}/aelparse
%attr(0755,root,root) %{_sbindir}/astcanary
%attr(0755,root,root) %{_sbindir}/asterisk
%attr(0755,root,root) %{_sbindir}/astgenkey
%attr(0755,root,root) %{_sbindir}/astman
%attr(0755,root,root) %{_sbindir}/autosupport
#%attr(0755,root,root) %{_sbindir}/check_expr
%attr(0755,root,root) %{_sbindir}/conf2ael
%attr(0755,root,root) %{_sbindir}/muted
%attr(0755,root,root) %{_sbindir}/rasterisk
%attr(0755,root,root) %{_sbindir}/refcounter
%attr(0755,root,root) %{_sbindir}/safe_asterisk
%attr(0755,root,root) %{_sbindir}/smsq
%attr(0755,root,root) %{_sbindir}/stereorize
%attr(0755,root,root) %{_sbindir}/streamplayer
%{_mandir}/man8/asterisk.8*
%{_mandir}/man8/astgenkey.8*
%{_mandir}/man8/autosupport.8*
%{_mandir}/man8/safe_asterisk.8*
%attr(0750,asterisk,asterisk) %dir /var/lib/asterisk
%attr(0750,asterisk,asterisk) %dir /var/lib/asterisk/agi-bin
%attr(0750,asterisk,asterisk) /var/lib/asterisk/documentation
%attr(0750,asterisk,asterisk) /var/lib/asterisk/images
%attr(0750,asterisk,asterisk) /var/lib/asterisk/keys
%attr(0750,asterisk,asterisk) /var/lib/asterisk/phoneprov
%attr(0750,asterisk,asterisk) /var/lib/asterisk/static-http
%attr(0750,asterisk,asterisk) %dir /var/lib/asterisk/moh
%attr(0750,asterisk,asterisk) %dir /var/lib/asterisk/sounds
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk/cdr-csv
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk/cdr-custom
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk
%attr(0770,asterisk,asterisk) %dir /var/spool/asterisk/monitor
%attr(0770,asterisk,asterisk) %dir /var/spool/asterisk/outgoing
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/tmp
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/voicemail
%attr(0755,asterisk,asterisk) %dir /var/run/asterisk
%attr(0640,asterisk,asterisk) %ghost /var/lib/asterisk/astdb
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/cdr-csv/Master.csv
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/console
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/debug
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/event_log
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/h323_log
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/messages
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/queue_log

%files devel -f %{name}-devel.filelist
%defattr(-,root,root,-)
%doc doc/CODING-GUIDELINES doc/datastores.txt doc/modules.txt doc/valgrind.txt
%dir %{_includedir}/asterisk
%{_includedir}/asterisk.h
%{_includedir}/asterisk/*.h

%files firmware
%defattr(-,root,root,-)
%attr(0750,asterisk,asterisk) /var/lib/asterisk/firmware

%files plugins-ais
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ais.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_ais.so

%files plugins-alsa
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alsa.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_alsa.so

%files plugins-curl
%defattr(-,root,root,-)
%doc contrib/scripts/dbsep.cgi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dbsep.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_curl.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_curl.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_curl.so

%files plugins-dahdi
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/meetme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/chan_dahdi.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_flash.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_meetme.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_page.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dahdibarge.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dahdiras.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dahdiscan.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_dahdi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_dahdi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_timing_dahdi.so

%files plugins-fax
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_fax.so

%files plugins-festival
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/festival.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_festival.so

%files plugins-ices
%defattr(-,root,root,-)
%doc contrib/asterisk-ices.xml
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_ices.so

%files plugins-jabber
%defattr(-,root,root,-)
%doc doc/jabber.txt doc/jingle.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/gtalk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jabber.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jingle.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_gtalk.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_jingle.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_jabber.so

%files plugins-jack
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_jack.so

%files plugins-lua
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.lua
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_lua.so

%files plugins-ldap
%defattr(-,root,root,-)
%doc doc/ldap.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_ldap.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_ldap.so

%files plugins-minivm
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions_minivm.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/minivm.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_minivm.so

%if %{build_misdn}
%files plugins-misdn
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/misdn.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_misdn.so
%endif

%if %{build_odbc}
%files plugins-odbc
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/func_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_odbc.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_adaptive_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_odbc.so
%endif

%if %{build_oss}
%files plugins-oss
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/oss.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_oss.so

%files plugins-usbradio
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/usbradio.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_usbradio.so
%endif

%files plugins-osp
%defattr(-,root,root)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_osplookup.so

%files plugins-portaudio
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/console.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_console.so

%files plugins-pgsql
%defattr(-,root,root,-)
%doc contrib/scripts/realtime_pgsql.sql
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_pgsql.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_pgsql.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_pgsql.so

%files plugins-radius
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_radius.so

%files plugins-skinny
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/skinny.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_skinny.so

%files plugins-snmp
%defattr(-,root,root,-)
%doc doc/asterisk-mib.txt
%doc doc/digium-mib.txt
%doc doc/snmp.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_snmp.conf
%attr(0644,root,root) /var/lib/snmp/mibs/ASTERISK-MIB.txt
%attr(0644,root,root) /var/lib/snmp/mibs/DIGIUM-MIB.txt
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_snmp.so

%files plugins-sqlite
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_sqlite3_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_config_sqlite.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_sqlite3_custom.so

%files plugins-speex
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_speex.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_speex.so

%files plugins-tds
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_tds.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_tds.so

%files plugins-unistim
%defattr(-,root,root,-)
%doc doc/unistim.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/unistim.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_unistim.so

%files plugins-voicemail
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/voicemail.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_vmcount.so

%files plugins-voicemail-imap
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_directory_imap.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_voicemail_imap.so

%if %{build_odbc}
%files plugins-voicemail-odbc
%defattr(-,root,root,-)
%doc doc/voicemail_odbc_postgresql.txt
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_directory_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_voicemail_odbc.so
%endif

%files plugins-voicemail-plain
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_directory_plain.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_voicemail_plain.so
