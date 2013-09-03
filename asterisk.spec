%define _requires_exceptions perl(Carp::Heavy)
%define _disable_ld_no_undefined 1

%bcond_with	h323
%bcond_with	misdn
%bcond_with	odbc
%bcond_without	oss
%bcond_without	radius
%bcond_without	tds
%bcond_without	corosync

#define beta rc3

%define	major 1
%define libname %mklibname asteriskssl %{major}

Summary:	The Open Source PBX
Name:		asterisk
Version:	11.5.1
Release:	%mkrel %{?beta:0.0.%{beta}.}1
License:	GPLv2
Group:		System/Servers
URL:		http://www.asterisk.org/
Source0:	http://downloads.asterisk.org/pub/telephony/asterisk/%{?!beta:releases/}%{name}-%{version}%{?beta:-%{beta}}.tar.gz
Source1:	asterisk-logrotate
Source2:	%{name}-%{version}-menuselect.makedeps
Source3:	%{name}-%{version}-menuselect.makeopts
Source4:	g72x_install
Source5:	asterisk-mp3.tar.bz2
Source6:	asterisk.service
Source7:	asterisk-tmpfiles
# S8: svn checkout http://svn.digium.com/svn/asterisk-gui/trunk asterisk-gui
Source8:	asterisk-gui.tar.gz
Source100:	asterisk.rpmlintrc
Patch2:		0002-Modify-modules.conf-so-that-different-voicemail-modu.patch
Patch50:	asterisk-1.6.1-rc1-utils_pthread_fix.diff
Patch51:	asterisk-1.6.1-beta3-net-snmp_fix.diff
Patch52:	asterisk-1.6.1-beta3-ffmpeg_fix.diff
Patch53:	asterisk-external_liblpc10.diff
Patch57:	editline-include-missing-1.6.1-fix.diff
Patch58:	asterisk-neon-include-fix.patch
Patch59:	asterisk-11.1.0-lua_fix.diff
Requires:	mpg123
Requires:	asterisk-core-sounds, asterisk-moh
Requires(post): systemd
BuildRequires:	alsa-oss-devel
BuildRequires:	autoconf >= 1:2.60
BuildRequires:	automake1.9 >= 1.9.6
BuildRequires:	bison
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	dahdi-devel >= 2.0.0
BuildRequires:	ffmpeg-devel
BuildRequires:	flex
BuildRequires:	freetds-devel >= 0.64
BuildRequires:	gmime-devel
BuildRequires:	gsm-devel
BuildRequires:	pkgconfig(jack)
BuildRequires:	krb5-devel
BuildRequires:	libcap-devel
BuildRequires:	pkgconfig(libedit)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	gnutls-devel
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	pkgconfig(libical)
BuildRequires:	idn-devel
BuildRequires:	pkgconfig(iksemel)
BuildRequires:	pkgconfig(libilbc)
BuildRequires:	mysql-devel
BuildRequires:	nbs-devel
BuildRequires:	neon-devel
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pri-devel
BuildRequires:	ss7-devel
BuildRequires:	libtool-devel
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	zapata-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	lpc10-devel
BuildRequires:	lua-devel
%if %{with misdn}
BuildRequires:	isdn4k-utils-devel
BuildRequires:	isdn4net
BuildRequires:	misdn2-devel
%endif
BuildRequires:	pkgconfig(ncurses)
#BuildRequires:	ncurses-devel
BuildRequires:	net-snmp-devel
BuildRequires:	pkgconfig(libnewt)
%if %{with corosync}
BuildRequires:	pkgconfig(corosync)
%endif
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	openr2-devel
BuildRequires:	pkgconfig(libosptk)
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
BuildRequires:	srtp-devel
BuildRequires:	tcp_wrappers-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(uuid)
%if %{with odbc}
BuildRequires:	unixODBC-devel
%endif
BuildRequires:	usb-compat-devel
BuildRequires:	wget
BuildRequires:	zlib-devel
BuildRequires:	c-client-devel
%if %{with h323}
BuildRequires:	ooh323c-devel
BuildRequires:	openh323-devel >= 1.15.3
BuildRequires:	pwlib-devel
%endif

%description
Asterisk is a complete PBX in software. It runs on Linux and provides
all of the features you would expect from a PBX and more. Asterisk
does voice over IP in three protocols, and can interoperate with
almost all standards-based telephony equipment using relatively
inexpensive hardware.

%package -n	%{libname}
Summary:	The shared SSL library for Asterisk
Group:		System/Libraries

%description -n	%{libname}
The shared SSL library for Asterisk.

%package	addons
Summary:	Asterisk-addons metapackage
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Requires:	asterisk-plugins-mp3 = %{version}-%{release}
Requires:	asterisk-plugins-mysql = %{version}-%{release}
Requires:	asterisk-plugins-ooh323 = %{version}-%{release}
Requires:	asterisk-plugins-saycountpl = %{version}-%{release}

%description	addons
Contain this packages:
1. asterisk-plugins-mp3
2. asterisk-plugins-mysql
3. asterisk-plugins-ooh323
4. asterisk-plugins-saycountpl

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

%if %{with corosync}
%package	plugins-corosync
Summary:	Modules for Asterisk that use corosync
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}
Obsoletes:	asterisk-plugins-ais

%description	plugins-corosync
Modules for Asterisk that use corosync.
%endif

%package	plugins-alsa
Summary:	Modules for Asterisk that use Alsa sound drivers
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-alsa
Modules for Asterisk that use Alsa sound drivers.

%package	plugins-calendar
Summary:	Asterisk calendar support
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-calendar
Asterisk calendar support (ical, caldav, exchange, or ews)

%package	plugins-cel
Summary:	Asterisk Channel Event Logging
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-cel
Channel Event Logging is a mechanism to provide fine-grained event information
that can be used to generate billing information. Such event information can
be recorded to databases and files via pluggable backend modules.

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

%if %{with misdn}
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

%package	plugins-mobile
Summary:	Asterisk channel driver for bluetooth phones and headsets
Group:		System/Servers
BuildRequires:	bluez-devel
Requires:	%{_lib}bluez3
Requires:	asterisk = %{version}-%{release}

%description	plugins-mobile
Asterisk channel driver to allow Bluetooth cell/mobile phones to be
used as FXO devices, and headsets as FXS devices.

%package	plugins-mp3
Summary:	MP3 plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-mp3
This package contains MP3 support for Asterisk.

%package	plugins-mysql
Summary:	MySQL plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-mysql
This package contains MySQL plugins for Asterisk.

%if %{with odbc}
%package	plugins-odbc
Summary:	Applications for Asterisk that use ODBC (except voicemail)
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-odbc
Applications for Asterisk that use ODBC (except voicemail)
%endif

%package        plugins-ooh323
Summary:	Objective System's H323 for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-ooh323
Objective System's H323 for Asterisk.

%if %{with oss}
%package	plugins-oss
Summary:	Modules for Asterisk that use OSS sound drivers
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-oss
Modules for Asterisk that use OSS sound drivers.
%endif

%package	plugins-pktccops
Summary:	Modules for Asterisk that use the IETF COPS protocol on PacketCable
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-pktccops
It's a subset or a "profile" of the IETF COPS protocol, extended for
PacketCable specific usage. The IETF COPS RFC defines the extensions
mechanism and the PacketCable standard uses and respects them. For
example, IETF COPS defines an opaque field called "Client Specific
Decision Data" and the PacketCable Standard defines how to fill it.
Some IETF COPS messages are not used in the PC Standard (like SSC), so
is a subset.

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
Provides:	%{name}-plugins-postgresql = %{version}-%{release}

%description	plugins-pgsql
This package contains PostgreSQL plugins for Asterisk.

%if %{with radius}
%package	plugins-radius
Summary:	Radiusclient plugins for Asterisk
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-radius
This package contains Radiusclient plugins for Asterisk.
%endif

%package	plugins-saycountpl
Summary:	Modules for Asterisk that support the Polish grammar
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	plugins-saycountpl
Polish grammar has some funny rules for counting words.
for example 1 zloty, 2 zlote, 5 zlotych.
This application will take the words for 1, 2-4 and
5 and decide based on grammar rules which one
to use with the number you pass to it.
Example: SayCountPL(zloty,zlote,zlotych,122) will give: zlote


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

%if %{with tds}
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

%if %{with odbc}
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

%package	gui
Summary:	Asterisk GUI
Group:		System/Servers
Requires:	asterisk = %{version}-%{release}

%description	gui
Asterisk GUI is a framework for the creation of graphical interfaces for
configuring Asterisk. Some sample graphical interfaces for specific vertical
markets are included for reference or for actual use and extension.

%prep

%setup0 -q -n asterisk-%{version}%{?beta:-%{beta}} -a 5 -a 8

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type d -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;
		
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
	if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch2 -p1 -b .voicemail
##
%patch50 -p1 -b .pthread
%patch51 -p0 -b .net_snmp
%patch52 -p1 -b .ffmpeg
%patch53 -p0 -b .libplc10
%patch57 -p0 -b .editline
%patch58 -p1 -b .neon
%patch59 -p0 -b .lua

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
#find -name "Makefile" | xargs perl -pi -e "s|/usr/lib|%{_libdir}|g"
#perl -pi -e "s|/lib\b|/%{_lib}|g" configure* autoconf/*.m4
#perl -pi -e "s|/lib/|/%{_lib}/|g" configure*  autoconf/*.m4

%build

# if we are building for i386 promote the CPU arch to i486 for atomic operations support
%ifarch i386
%define optflags %{__global_cflags} -m32 -march=i486 -mtune=generic -fasynchronous-unwind-tables
%else
%define optflags %(rpm --target %{_target} --eval %%{optflags})
%endif

./bootstrap.sh

sed 's#localstatedir}/lib64#localstatedir}/lib#g' -i configure.ac

pushd menuselect/mxml
%configure2_5x
popd

pushd menuselect
%configure2_5x
popd 

pushd main/editline
%configure2_5x
popd

%configure2_5x \
	--localstatedir=/var \
	--with-asound=%{_prefix} \
	--with-bluetooth=%{_prefix} \
	--with-cap=%{_prefix} \
	--with-curses=%{_prefix} \
	--with-crypto=%{_prefix} \
	--with-dahdi=%{_prefix} \
	--with-avcodec=%{_prefix} \
	--with-gsm=%{_prefix} \
	--without-gtk2 \
	--with-gmime=%{_prefix} \
	--with-ical=%{_prefix} \
	--with-iconv=%{_prefix} \
	--with-iksemel=%{_prefix} \
	--with-imap=system \
	--with-inotify=%{_prefix} \
%if %{with odbc}
	--with-iodbc=%{_prefix} \
%else
	--without-iodbc \
%endif
	--with-jack=%{_prefix} \
	--without-kqueue \
	--with-ldap=%{_prefix} \
	--with-libcurl=%{_prefix} \
	--with-ltdl=%{_prefix} \
	--with-lua=%{_prefix} \
%if %{with misdn}
	--with-isdnnet=%{_prefix} \
	--with-misdn=%{_prefix} \
	--with-suppserv=%{_prefix} \
%else
	--without-isdnnet \
	--without-misdn \
	--without-suppserv \
%endif
	--with-mysqlclient=%{_prefix} \
	--with-nbs=%{_prefix} \
	--with-ncurses=%{_prefix} \
	--with-neon=%{_prefix} \
	--with-neon29=%{_prefix} \
	--with-netsnmp=%{_prefix} \
	--with-newt=%{_prefix} \
	--with-ogg=%{_prefix} \
%if %{with corosync}
	--with-cpg=%{_prefix} \
%else
	--without-cpg \
%endif
	--with-openr2=%{_prefix} \
	--with-osptk=%{_prefix} \
%if %{with oss}
	--with-oss \
%else
	--without-oss \
%endif
	--with-postgres=%{_prefix} \
	--with-popt=%{_prefix} \
	--with-portaudio=%{_prefix} \
	--with-pri=%{_prefix} \
	--with-radius=%{_prefix} \
	--with-resample=%{_prefix} \
%if %{with h323}
	--with-pwlib=%{_prefix} \
	--with-h323=%{_prefix} \
%else
	--without-pwlib \
	--without-h323 \
%endif
	--with-sdl=%{_prefix} \
	--with-SDL_image=%{_prefix} \
	--with-sounds-cache=%{_prefix} \
	--with-spandsp=%{_prefix} \
	--with-ss7=%{_prefix} \
	--with-speex=%{_prefix} \
	--with-speexdsp=%{_prefix} \
	--without-sqlite \
	--with-sqlite3=%{_prefix} \
	--with-srtp=%{_prefix} \
	--with-ssl=%{_prefix} \
	--with-tds=%{_prefix} \
	--with-timerfd=%{_prefix} \
	--without-tinfo \
	--with-tonezone=%{_prefix} \
%if %{with odbc}
	--with-unixodbc=%{_prefix} \
%else
	--without-unixodbc \
%endif
	--with-vorbis=%{_prefix} \
	--without-vpb \
	--without-x11 \
	--with-z=%{_prefix} \
	--with-ilbc=%{_prefix} \
	--with-libedit=%{_prefix} \

sed 's#localstatedir}/lib64#localstatedir}/lib#g' -i makeopts
#fix --no-undefined
sed -e 's/,--no-undefined -Wl//g' -i makeopts

# fix some weirdos
#GMIME_INCLUDE=`pkg-config --cflags gmime-2.6`
#perl -pi -e "s|^GMIME_INCLUDE=.*|GMIME_INCLUDE=$GMIME_INCLUDE|g" makeopts

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=FILE_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=/run/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_plain.so
mv apps/app_directory.so apps/app_directory_plain.so

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=IMAP_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=/run/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_imap.so
mv apps/app_directory.so apps/app_directory_imap.so

%if %{with odbc}
%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=ODBC_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=/run/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_odbc.so
mv apps/app_directory.so apps/app_directory_odbc.so
%endif

# so that these modules don't get built again during the install phase
touch apps/app_voicemail.o apps/app_directory.o
touch apps/app_voicemail.so apps/app_directory.so

pushd asterisk-gui
%configure2_5x
popd

%install
rm -rf %{buildroot}

ASTCFLAGS="%{optflags}" make install DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=/run/asterisk
ASTCFLAGS="%{optflags}" make samples DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=/run/asterisk

install -D -p -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/asterisk
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/asterisk.service
rm -f %{buildroot}%{_sbindir}/safe_asterisk
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf

#install -D -p -m 0644 contrib/editors/ael.vim %{buildroot}%{_datadir}/vim/syntax/ael.vim
#install -D -p -m 0644 contrib/editors/asteriskvm.vim %{buildroot}%{_datadir}/vim/syntax/asteriskvm.vim

rm %{buildroot}%{_libdir}/asterisk/modules/app_directory.so
rm %{buildroot}%{_libdir}/asterisk/modules/app_voicemail.so
install -D -p -m 0755 apps/app_directory_imap.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_imap.so %{buildroot}%{_libdir}/asterisk/modules/
%if %{with odbc}
install -D -p -m 0755 apps/app_directory_odbc.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_odbc.so %{buildroot}%{_libdir}/asterisk/modules/
%endif
install -D -p -m 0755 apps/app_directory_plain.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_plain.so %{buildroot}%{_libdir}/asterisk/modules/

# create some directories that need to be packaged
make installdirs DESTDIR=%{buildroot} ASTVARRUNDIR=/run/asterisk
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

rm -f %{buildroot}%{_sysconfdir}/asterisk/res_config_sqlite.conf

touch %{name}-devel.filelist

pushd asterisk-gui
%makeinstall_std
popd

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
%if !%{with odbc}
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/cdr_odbc.conf
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/cel_odbc.conf
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/func_odbc.conf
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/res_odbc.conf
%endif
%if !%{with misdn}
  rm -f %{buildroot}/%{_sysconfdir}/asterisk/misdn.conf
%endif
%if !%{with oss}
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
if [[ -e %{_libdir}/asterisk/modules/codec_g729.so ]]; then
  sh %{_docdir}/g72x_install
fi

%tmpfiles_create %{name}
%_post_service %{name}

%preun
if [ "$1" = 0 ]; then
	echo "Removing setuid root from /usr/bin/mpg123"
	chmod u-s %{_bindir}/mpg123
fi

# Remove the G72x stuff
rm -f /usr/share/doc/asterisk/README.g72x.txt
rm -f /usr/$LIBNAME/asterisk/modules/codec_g723.so
rm -f /usr/$LIBNAME/asterisk/modules/codec_g729.so
rm -f /usr/bin/g729_my_enc
rm -f /usr/bin/g729_my_dec
rm -f /usr/bin/astconv

%_preun_service %{name}

%postun
%_postun_userdel asterisk
gpasswd -d asterisk dialout 1>/dev/null

%pre plugins-dahdi
%{_sbindir}/usermod -a -G dahdi asterisk

%if %{with misdn}
%pre plugins-misdn
%{_sbindir}/usermod -a -G misdn asterisk
%endif

%pre plugins-mobile
if [[ -e %{_sysconfdir}/asterisk/mobile.conf ]] ; then
  mv -f %{_sysconfdir}/asterisk/{,chan_}mobile.conf
fi

%files -n %{libname}
%attr(0755,root,root) %{_libdir}/libasteriskssl.so.1

%files
%doc README* *.txt ChangeLog BUGS CREDITS configs
%doc doc/asterisk.sgml g72x_install
%doc contrib/realtime/mysql
%{_unitdir}/asterisk.service
%attr(0644,root,root) %{_tmpfilesdir}/%{name}.conf
%attr(0750,asterisk,asterisk) %dir %{_sysconfdir}/asterisk
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/acl.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adsi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/agents.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alarmreceiver.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/amd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/app_skel.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ccss.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_syslog.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_aliases.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli_permissions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/codecs.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/confbridge.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/config_test.conf
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
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/motif.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/musiconhold.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/muted.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phone.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phoneprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queuerules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queues.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_stun_monitor.conf
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
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/xmpp.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/asterisk
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
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_saycounted.so
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
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_syslog.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_agent.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_bridge.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_iax2.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_local.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_mgcp.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_motif.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_multicast_rtp.so
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
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_g719.so
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
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_sln.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_wav_gsm.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_wav.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_vox.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_aes.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_audiohookinherit.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_base64.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_blacklist.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_callcompletion.so
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
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_frame_trace.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_global.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_groupcount.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_hangupcause.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_iconv.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_jitterbuffer.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_lock.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_logic.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_math.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_md5.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_module.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_pitchshift.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_presencestate.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_rand.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_realtime.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_sha1.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_shell.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_sprintf.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_srv.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_strings.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_sysinfo.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_timeout.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_uri.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_version.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_volume.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_ael.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_config.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_dundi.so
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
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_format_attr_celt.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_format_attr_h263.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_format_attr_h264.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_format_attr_silk.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_http_post.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_http_websocket.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_limit.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_monitor.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_musiconhold.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_mutestream.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_phoneprov.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_realtime.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_rtp_asterisk.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_rtp_multicast.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_security_log.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_smdi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_speech.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_srtp.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_stun_monitor.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_timing_pthread.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_timing_timerfd.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_xmpp.so
%attr(0755,root,root) %{_sbindir}/aelparse
%attr(0755,root,root) %{_sbindir}/astcanary
%attr(0755,root,root) %{_sbindir}/astdb2bdb
%attr(0755,root,root) %{_sbindir}/astdb2sqlite3
%attr(0755,root,root) %{_sbindir}/asterisk
%attr(0755,root,root) %{_sbindir}/astgenkey
%attr(0755,root,root) %{_sbindir}/astman
%attr(0755,root,root) %{_sbindir}/autosupport
%attr(0755,root,root) %{_sbindir}/check_expr
%attr(0755,root,root) %{_sbindir}/check_expr2
%attr(0755,root,root) %{_sbindir}/conf2ael
%attr(0755,root,root) %{_sbindir}/muted
%attr(0755,root,root) %{_sbindir}/rasterisk
%attr(0755,root,root) %{_sbindir}/refcounter
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
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk/cdr-csv
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk/cdr-custom
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk
%attr(0770,asterisk,asterisk) %dir /var/spool/asterisk/monitor
%attr(0770,asterisk,asterisk) %dir /var/spool/asterisk/outgoing
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/tmp
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/voicemail
%attr(0640,asterisk,asterisk) %ghost /var/lib/asterisk/astdb
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/cdr-csv/Master.csv
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/console
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/debug
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/event_log
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/h323_log
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/messages
%attr(0640,asterisk,asterisk) %ghost /var/log/asterisk/queue_log
#%attr(0640,asterisk,asterisk) %{_datadir}/vim/syntax/ael.vim
#%attr(0640,asterisk,asterisk) %{_datadir}/vim/syntax/asteriskvm.vim

%files devel -f %{name}-devel.filelist
%dir %{_includedir}/asterisk
%dir %{_includedir}/asterisk/doxygen
%{_includedir}/asterisk.h
%{_includedir}/asterisk/*.h
%{_includedir}/asterisk/doxygen/*.h
%attr(0755,root,root) %{_libdir}/libasteriskssl.so

%files addons

%files firmware
%attr(0750,asterisk,asterisk) /var/lib/asterisk/firmware

%if %{with corosync}
%files plugins-corosync
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_corosync.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_corosync.so
%endif

%files plugins-alsa
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alsa.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_alsa.so

%files plugins-calendar
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/calendar.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_calendar.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_calendar_caldav.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_calendar_ews.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_calendar_exchange.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_calendar_icalendar.so

%files plugins-cel
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_custom.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_celgenuserevent.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cel_custom.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cel_manager.so

%files plugins-curl
%doc contrib/scripts/dbsep.cgi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dbsep.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_curl.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_curl.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_curl.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_curl.so

%files plugins-dahdi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/meetme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/chan_dahdi.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_flash.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_meetme.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_page.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dahdibarge.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_dahdiras.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_dahdi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_dahdi.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_timing_dahdi.so

%files plugins-fax
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_fax.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_fax.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_fax_spandsp.so

%files plugins-festival
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/festival.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_festival.so

%files plugins-ices
%doc contrib/asterisk-ices.xml
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_ices.so

%files plugins-jabber
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/gtalk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jabber.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jingle.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_gtalk.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_jingle.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_jabber.so

%files plugins-jack
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_jack.so

%files plugins-lua
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.lua
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_lua.so

%files plugins-ldap
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_ldap.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_ldap.so

%files plugins-minivm
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions_minivm.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/minivm.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_minivm.so

%if %{with misdn}
%files plugins-misdn
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/misdn.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_misdn.so
%endif

%files plugins-mobile
%doc configs/chan_mobile.conf.sample
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/chan_mobile.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_mobile.so

%files plugins-mp3
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_mp3.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_mp3.so

%files plugins-mysql
%doc contrib/realtime/mysql/*.sql
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/app_mysql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_mysql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_config_mysql.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_mysql.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_mysql.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_mysql.so

%if %{with odbc}
%files plugins-odbc
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/func_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_odbc.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_adaptive_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_odbc.so
%endif

%files plugins-ooh323
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ooh323.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_ooh323.so

%if %{with oss}
%files plugins-oss
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/oss.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_oss.so
%endif

%files plugins-osp
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_osplookup.so

%files plugins-pktccops
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_pktccops.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_pktccops.so

%files plugins-portaudio
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/console.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_console.so

%files plugins-pgsql
%doc contrib/realtime/postgresql/realtime.sql
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_pgsql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_pgsql.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_pgsql.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cel_pgsql.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_pgsql.so

%files plugins-radius
%attr(0755,root,root) %{_libdir}/asterisk/modules/cel_radius.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_radius.so

%files plugins-saycountpl
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_saycountpl.so

%files plugins-skinny
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/skinny.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_skinny.so

%files plugins-snmp
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_snmp.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_snmp.so

%files plugins-sqlite
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_sqlite3_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_sqlite3_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_config_sqlite3.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_sqlite3_custom.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cel_sqlite3_custom.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_sqlite3.so

%files plugins-speex
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_speex.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_speex.so

%files plugins-tds
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cel_tds.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_tds.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cel_tds.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_tds.so

%files plugins-unistim
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/unistim.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_unistim.so

%files plugins-voicemail
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/voicemail.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_vmcount.so

%files plugins-voicemail-imap
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_directory_imap.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_voicemail_imap.so

%if %{with odbc}
%files plugins-voicemail-odbc
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_directory_odbc.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_voicemail_odbc.so
%endif

%files plugins-voicemail-plain
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_directory_plain.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_voicemail_plain.so

%files gui
%doc asterisk-gui/LICENSE asterisk-gui/README asterisk-gui/developer_info
%dir %attr(0750,asterisk,asterisk) /var/lib/asterisk/gui_backups
%dir %attr(0750,asterisk,asterisk) /var/lib/asterisk/static-http
%dir %attr(0755,asterisk,asterisk) /var/lib/asterisk/static-http/config
%dir %attr(0755,asterisk,asterisk) /var/lib/asterisk/static-http/config/stylesheets
%dir %attr(0755,asterisk,asterisk) /var/lib/asterisk/static-http/config/images
%dir %attr(0755,asterisk,asterisk) /var/lib/asterisk/static-http/config/private
%dir %attr(0755,asterisk,asterisk) /var/lib/asterisk/static-http/config/private/bkps
%dir %attr(0755,asterisk,asterisk) /var/lib/asterisk/static-http/config/js
%dir %attr(0755,asterisk,asterisk) /var/lib/asterisk/scripts
#% attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/index.html
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/config/*.html
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/config/stylesheets/*
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/config/images/*
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/config/js/*
%attr(0755,asterisk,asterisk) /var/lib/asterisk/scripts/*
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/*.html
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/*.css
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/*.js
%attr(0644,asterisk,asterisk) /var/lib/asterisk/static-http/*.xml
