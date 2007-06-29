%define version 1.4.6
%define release %mkrel 1

%define _requires_exceptions perl(Carp::Heavy)

%define build_h323	0
%{?_without_h323:	%global build_h323 0}
%{?_with_h323:		%global build_h323 1}

%define build_misdn	1
%{?_without_misdn:	%global build_misdn 0}
%{?_with_misdn:		%global build_misdn 1}

%define build_odbc	1
%{?_without_odbc:	%global build_odbc 0}
%{?_with_odbc:		%global build_odbc 1}

%define build_radius	1
%{?_without_radius:	%global build_radius 0}
%{?_with_radius:	%global build_radius 1}

%define build_tds	0
%{?_without_tds:	%global build_tds 0}
%{?_with_tds:		%global build_tds 1}

# SIP over TCP / TLS support: http://bugs.digium.com/view.php?id=4903
%define build_tcp	0
%{?_without_tcp:	%global build_tcp 0}
%{?_with_tcp:		%global build_tcp 1}

# this takes quite some time...
%define build_docs	0
%{?_without_docs:	%global build_docs 0}
%{?_with_docs:		%global build_docs 1}

Summary:	Asterisk PBX
Name:		asterisk
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Servers
URL:		http://www.asterisk.org/
Source0:	http://www.asterisk.org/html/downloads/%{name}-%{version}.tar.bz2
Source1:	asterisk.init
Source2:	asterisk.sysconfig
Source3:	http://www.asteriskdocs.org/modules/tinycontent/content/docbook/current/AsteriskDocs-html.tar.bz2
Patch0:		asterisk-1.4.0-mdv.diff
#Patch1:		asterisk-1.2.4-spandsp.diff
#Patch2:		asterisk-1.2.0-beta1-antibork_1.diff
#Patch3:		asterisk-1.2.5-antibork_2.diff
Patch4:		asterisk-1.4.0-beta3-freetds_mssql.diff
#Patch5:		asterisk-1.0.8-20050420-freetds-0.63.diff
#Patch8:		asterisk-1.0.8-20050420-h323_conf_fix.diff
# taken from the visdn-devel-20060315 tar ball
#Patch11:	asterisk-1.2.5-cap.diff
#Patch12:	asterisk-1.2-answer.diff
#Patch13:	asterisk-1.2-disconnect.diff
#Patch14:	asterisk-1.2.7.1-ppcfix.diff
#Patch15:	asterisk-1.2.7.1-metermaid.diff
Patch16:	asterisk-1.4.0-beta3-external_liblpc10_and_libilbc.diff
Patch17:	asterisk-1.4.0-beta3-no_mega_optimization.diff
Patch18:	asterisk-1.4.0-beta2-imap.diff
Patch19:	asterisk-1.4-app_fax.diff
Patch100:	asterisk-20061212-tcp.patch
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires:	mpg123
Requires:	asterisk-core-sounds
BuildRequires:	libtool
BuildRequires:	autoconf >= 1:2.60
BuildRequires:	automake1.9 >= 1.9.6
BuildRequires:	libalsa-devel
BuildRequires:	libcurl-devel
#BuildRequires:	gtk+1.2-devel
BuildRequires:	isdn4k-utils-devel
BuildRequires:	libgsm-devel
BuildRequires:	libiksemel-devel
BuildRequires:	libilbc-devel
BuildRequires:	libnbs-devel
BuildRequires:	libncurses-devel
BuildRequires:	libpri-devel >= 1.4.0
BuildRequires:	libspandsp-devel
BuildRequires:	libspeex-devel
BuildRequires:	libtermcap-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtonezone-devel >= 1.4.0
BuildRequires:	libzap-devel >= 1.0.1
BuildRequires:	lpc10-devel
BuildRequires:	libidn-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	imap-devel
BuildRequires:	krb5-devel
BuildRequires:	pam-devel
%if %{build_misdn}
BuildRequires:	libmisdn-devel >= 1:3.4
%endif
%if %{build_docs}
BuildRequires:	doxygen
%endif
BuildRequires:	newt-devel
BuildRequires:	oggvorbis-devel
%if %{build_h323}
#BuildRequires:	ooh323c-devel
#BuildRequires:	openh323-devel >= 1.15.3
%endif
## needed for smsq: popt-devel
BuildRequires:	libpopt-devel
#BuildRequires:	swig-devel
BuildRequires:	wget
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Asterisk is an Open Source PBX and telephony development platform that
can both replace a conventional PBX and act as a platform for developing
custom telephony applications for delivering dynamic content over a
telephone similarly to how one can deliver dynamic content through a
web browser using CGI and a web server.

Asterisk talks to a variety of telephony hardware including BRI, PRI, 
POTS, and IP telephony clients using the Inter-Asterisk eXchange
protocol (e.g. gnophone or miniphone).  For more information and a
current list of supported hardware, see www.asterisk.org.

%if %{build_misdn}
%package	chan_misdn
Summary:	This module adds mISDN support to the Asterisk PBX
Group:		System/Servers
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	chan_misdn
This module adds mISDN support to the Asterisk PBX. mISDN is the
(experimental) new ISDN4Linux stack, which adds support for
driving cards in NT mode and thus connecting an ISDN phone to your
computer.
%endif

%package	devel
Summary:	Header files for building Asterisk modules
Group:		Development/C

%description	devel
This package contains the development header files that are needed
to compile 3rd party modules.

%package	docs
Summary:	The Hitchhiker's Guide to Asterisk
Group:		Books/Howtos

%description	docs
The Hitchhiker's Guide to Asterisk

%package	plugins-fax
Summary:	FAX plugins for Asterisk
Group:		System/Servers
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-fax
This package contains FAX plugins for Asterisk:

* Trivial FAX Receive Application
* Trivial FAX Transmit Application
* Assign entered string to a given variable

%if %{build_odbc}
%package	plugins-odbc
Summary:	ODBC plugins for Asterisk
Group:		System/Servers
BuildRequires:	libunixODBC-devel
BuildRequires:	libtool-devel
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-odbc
This package contains ODBC plugins for Asterisk:

* ODBC Configuration
* Call Detail Recording for ODBC
* ODBC resource manager
%endif

%package	plugins-pgsql
Summary:	PostgreSQL plugins for Asterisk
Group:		System/Servers
BuildRequires:	postgresql-devel
BuildRequires:	zlib-devel
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-pgsql
This package contains PostgreSQL plugins for Asterisk:

* Simple PostgreSQL Interface
* Call Detail Recording for PostgreSQL

%if %{build_radius}
%package	plugins-radius
Summary:	Radiusclient plugins for Asterisk
Group:		System/Servers
BuildRequires:	radiusclient-ng-devel
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-radius
This package contains Radiusclient plugins for Asterisk:

* Call Detail Recording for Radius
%endif

%package	plugins-sqlite
Summary:	SQLite plugins for Asterisk
Group:		System/Servers
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-sqlite
This package contains SQLite plugins for Asterisk:

* Call Detail Recording for SQLite

%if %build_tds
%package	plugins-tds
Summary:	FreeTDS plugins for Asterisk
Group:		System/Servers
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}
BuildRequires:	freetds_mssql-devel >= 0.64

%description	plugins-tds
This package contains FreeTDS plugins for Asterisk:

* Call Detail Recording for FreeTDS
%endif

%package	plugins-osp
Summary:	Open Settlement Protocol for Asterisk
Group:		System/Servers
BuildRequires:	libosp-devel
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-osp
This package contains OSP (Open Settlement Protocol) support for Asterisk

%package	plugins-snmp
Summary:	Brief SNMP Agent / SubAgent support for Asterisk
Group:		System/Servers
Requires:	net-snmp
BuildRequires:	libnet-snmp-devel
BuildRequires:	tcp_wrappers-devel
BuildRequires:	openssl-devel
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-snmp
This package contains brief SNMP Agent / SubAgent support for Asterisk.

%package	plugins-jabber
Summary:	Jabber support for Asterisk
Group:		System/Servers
BuildRequires:	libgcrypt-devel
BuildRequires:	libgnutls-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libiksemel-devel
BuildRequires:	zlib-devel
Requires(post): %{name} = %{version}
Requires(preun): %{name} = %{version}

%description	plugins-jabber
This package contains Jabber support for Asterisk.

* res_jabber  - A resource for interfacing asterisk directly as a client or a
                component to a jabber compliant server.

* chan_gtalk  - brief Gtalk Channel Driver, until google/libjingle works with
                jingle spec.

%package	webvmail
Summary:	Web frontend to voicemail
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	webserver

%description	webvmail
This package contains the web frontend to voicemail.

WARNING:
IT USES A SETUID ROOT PERL SCRIPT, SO IF YOU DON'T LIKE THAT,
DO NOT INSTALL THIS PACKAGE!

%prep

%setup -q -a3

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type d -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;
		
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch0 -p1 -b .mdv
#patch1 -p1 -b .spandsp
#patch2 -p1 -b .antibork_1
#patch3 -p0 -b .antibork_2
%if %build_tds
%patch4 -p1 -b .freetds_mssql
%endif
#patch5 -p0 -b .freetds-0.63
#patch8 -p0 -b .h323_conf_fix
# visdn
#%patch11 -p1 -b .cap
#patch12 -p1 -b .answer
#patch13 -p1 -b .disconnect
%ifnarch %ix86
#patch14 -p1 -b .ppcfix
%endif
#patch15 -p0 -b .metermaid
%patch16 -p0 -b .external_liblpc10_and_libilbc
%patch17 -p0 -b .no_mega_optimization
%patch18 -p0 -b .imap
%patch19 -p0 -b .app_fax

%if %{build_tcp}
# SIP over TCP
%patch100 -p0 -b .tcp.patch
%endif

cat %{SOURCE1} > asterisk.init
cat %{SOURCE2} > asterisk.sysconfig

# lib64 fix
find -name "Makefile" | xargs perl -pi -e "s|/usr/lib|%{_libdir}|g"
perl -pi -e "s|/lib\b|/%{_lib}|g" configure*

# fix one convenient softlink
pushd docs-html
    ln -s book1.html index.html
popd

%build
rm -f configure
sh ./bootstrap.sh

echo "%{version}-%{release}" > .version

export ASTCFLAGS="%{optflags}"

%configure2_5x \
    --without-kde \
    --without-qt \
    --without-tinfo \
    --without-vpb \
    --without-pwlib \
%if !%{build_h323}
    --without-h323 \
%endif
    --with-imap=%{_prefix} \
    --with-asound=%{_prefix} \
    --with-curses=%{_prefix} \
    --with-gnutls=%{_prefix} \
    --with-gsm=%{_prefix} \
    --with-iksemel=%{_prefix} \
    --with-isdnnet=%{_prefix} \
%if %{build_misdn}
    --with-misdn=%{_prefix} \
%endif
    --with-nbs=%{_prefix} \
    --with-ncurses=%{_prefix} \
    --with-netsnmp=%{_prefix} \
    --with-newt=%{_prefix} \
%if %{build_odbc}
    --with-odbc=%{_prefix} \
%endif
    --with-ogg=%{_prefix} \
    --with-osptk=%{_prefix} \
    --with-oss=%{_prefix} \
    --with-popt=%{_prefix} \
    --with-postgres=%{_prefix} \
    --with-pri=%{_prefix} \
    --with-radius=%{_prefix} \
    --with-speex=%{_prefix} \
    --with-sqlite=%{_prefix} \
    --with-suppserv=%{_prefix} \
    --with-ssl=%{_prefix} \
%if %{build_tds}
    --with-tds_mssql=%{_prefix} \
%endif
    --with-termcap=%{_prefix} \
    --with-tonezone=%{_prefix} \
    --with-vorbis=%{_prefix} \
    --with-z=%{_prefix} \
    --with-zaptel=%{_prefix} \
    HTTPDIR="/var/www"

%make

%if %{build_docs}
%make progdocs
%endif

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}/var/www/{html,cgi-bin}

%makeinstall_std \
	ASTSBINDIR="%{_sbindir}" \
	HTTPDIR="/var/www"

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

install -d %{buildroot}/var/run/asterisk
install -d %{buildroot}/var/spool/asterisk
install -d %{buildroot}/var/spool/asterisk/outgoing

# install init scrips
install -d %{buildroot}%{_initrddir}
install -m0755 asterisk.init %{buildroot}%{_initrddir}/asterisk

# install sysconfig file
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -m0644 asterisk.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/asterisk

# fix logrotation
install -d %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/asterisk << EOF
/var/log/asterisk/console /var/log/asterisk/debug /var/log/asterisk/messages /var/log/asterisk/queue_log /var/log/asterisk/event_log /var/log/asterisk/cdr-csv/Master.csv {
    weekly
    rotate 5
    copytruncate
    compress
    notifempty
    missingok
    postrotate
    %{_sbindir}/asterisk -rx 'reload'
    endscript
}
EOF

touch %{name}-devel.filelist
%if %{build_docs}
    find doc/api/html -type f | sed 's/^/%doc /' | grep -v '\./%{name}-devel.filelist' > %{name}-devel.filelist
%endif

# fix ghost files
touch	%{buildroot}%{_localstatedir}/asterisk/astdb
touch	%{buildroot}/var/log/asterisk/console
touch	%{buildroot}/var/log/asterisk/debug
touch	%{buildroot}/var/log/asterisk/messages
touch	%{buildroot}/var/log/asterisk/queue_log
touch	%{buildroot}/var/log/asterisk/event_log
touch	%{buildroot}/var/log/asterisk/cdr-csv/Master.csv
touch	%{buildroot}/var/log/asterisk/h323_log

# Fix incorrect path in /etc/asterisk/asterisk.conf
perl -pi -e "s|astrundir => /var/run|astrundir => /var/run/asterisk|g" %{buildroot}/%{_sysconfdir}/asterisk/asterisk.conf
perl -pi -e "s|^libdir=.*|libdir=%{_libdir}|g" %{buildroot}%{_libdir}/pkgconfig/asterisk.pc
perl -pi -e "s|^varrundir=.*|varrundir=/var/run/asterisk|g" %{buildroot}%{_libdir}/pkgconfig/asterisk.pc

# TODO
# Add directory for ssl certs
#mkdir -p %{buildroot}%{_sysconfdir}/ssl/%{name}

# Remove unpackages files
rm -rf %{buildroot}%{_localstatedir}/asterisk/moh/.asterisk-moh-freeplay-wav

# use the stand alone asterisk-core-sounds package instead
rm -rf %{buildroot}%{_localstatedir}/asterisk/sounds

%pre
%_pre_useradd asterisk %{_localstatedir}/asterisk /bin/sh

%post
%create_ghostfile /var/log/asterisk/console asterisk asterisk 644
%create_ghostfile /var/log/asterisk/debug asterisk asterisk 644
%create_ghostfile /var/log/asterisk/messages asterisk asterisk 644
%create_ghostfile /var/log/asterisk/queue_log asterisk asterisk 644
%create_ghostfile /var/log/asterisk/event_log asterisk asterisk 644
%create_ghostfile /var/log/asterisk/cdr-csv/Master.csv asterisk asterisk 644
%create_ghostfile /var/log/asterisk/h323_log asterisk asterisk 644
echo "Adding setuid root to /usr/bin/mpg123, needed for MOH"
chmod u+s %{_bindir}/mpg123
%_post_service asterisk

%preun
if [ "$1" = 0 ]; then
    echo "Removing setuid root from /usr/bin/mpg123"
    chmod u-s %{_bindir}/mpg123
fi

# TODO
# generate the ldap.pem cert here instead of the initscript
#"/etc/ssl/asterisk/trustcerts.pem"
#"/etc/ssl/asterisk/trustdir"
#"/etc/ssl/asterisk/servercert.pem"
#"/etc/ssl/asterisk/serverkey.pem"
#"/etc/ssl/asterisk/dh512.pem"
#"/etc/ssl/asterisk/dh1024.pem"
#if [ ! -e %{_sysconfdir}/ssl/%{name}/ldap.pem ] ; then
#	if [ -x %{_datadir}/%{name}/gencert.sh ] ; then
#		echo "Generating self-signed certificate..."
#		pushd %{_sysconfdir}/ssl/%{name}/ > /dev/null
#		yes ""|%{_datadir}/%{name}/gencert.sh >/dev/null 2>&1
#		chmod 640 ldap.pem
#		chown root:ldap ldap.pem
#		popd > /dev/null
#	fi
#	echo "To generate a self-signed certificate, you can use the utility"
#	echo "%{_datadir}/%{name}/gencert.sh..."
#fi

%_preun_service asterisk

%postun
%_postun_userdel asterisk

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS ChangeLog CREDITS LICENSE README* apps/rpt_flow.pdf
%doc doc/*README* doc/*.txt contrib/init.d/rc.mandrake* contrib/asterisk-ices.xml
%doc contrib/scripts contrib/i18n.testsuite.conf contrib/README.festival
%attr(0755,root,root)					%{_initrddir}/asterisk
%attr(0644,root,root) %config(noreplace)		%{_sysconfdir}/logrotate.d/asterisk
%attr(0750,asterisk,asterisk) %dir			%{_sysconfdir}/asterisk
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/*.adsi
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/*.conf
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/extensions.ael
%attr(0644,root,root) %config(noreplace)		%{_sysconfdir}/sysconfig/asterisk
# TODO
#attr(0750,root,asterisk) %dir				%{_sysconfdir}/ssl/asterisk

# these are packaged as sub packages below
%if %{build_misdn}
%exclude						%{_sysconfdir}/asterisk/misdn.conf
%endif
%if %{build_odbc}
%exclude						%{_sysconfdir}/asterisk/*_odbc.conf
%endif
%if %{build_tds}
%exclude						%{_sysconfdir}/asterisk/*tds*.conf
%endif
%exclude						%{_sysconfdir}/asterisk/cdr_pgsql.conf
%exclude						%{_sysconfdir}/asterisk/gtalk.conf
%exclude						%{_sysconfdir}/asterisk/jabber.conf
%exclude						%{_sysconfdir}/asterisk/osp.conf
%exclude						%{_sysconfdir}/asterisk/res_snmp.conf
%exclude						%{_sysconfdir}/asterisk/*sql*.conf

%attr(0755,root,root)					%{_sbindir}/aelparse
%attr(0755,root,root)					%{_sbindir}/asterisk
%attr(0755,root,root)					%{_sbindir}/astgenkey
%attr(0755,root,root)					%{_sbindir}/astman
%attr(0755,root,root)					%{_sbindir}/autosupport
%attr(0755,root,root)					%{_sbindir}/muted
%attr(0755,root,root)					%{_sbindir}/rasterisk
%attr(0755,root,root)					%{_sbindir}/safe_asterisk
%attr(0755,root,root)					%{_sbindir}/smsq
%attr(0755,root,root)					%{_sbindir}/stereorize
%attr(0755,root,root)					%{_sbindir}/streamplayer

%attr(0755,root,root)		%dir			%{_libdir}/asterisk
%attr(0755,root,root)		%dir			%{_libdir}/asterisk/modules
%attr(0755,root,root)					%{_libdir}/asterisk/modules/app_*.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/cdr_*.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/chan_*.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/codec_*.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/format_*.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/func_*.so
#attr(0755,root,root)					%{_libdir}/asterisk/modules/func_callerid.so
#attr(0755,root,root)					%{_libdir}/asterisk/modules/func_enum.so
#attr(0755,root,root)					%{_libdir}/asterisk/modules/func_uri.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/pbx_*.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/res_*.so

# these are packaged as sub packages below
%if %{build_misdn}
%exclude						%{_libdir}/asterisk/modules/chan_misdn.so
%endif
%if %{build_odbc}
%exclude						%{_libdir}/asterisk/modules/*_odbc.so
%endif
%if %{build_tds}
%exclude						%{_libdir}/asterisk/modules/*tds*.so
%endif
%exclude						%{_libdir}/asterisk/modules/app_*fax.so
%exclude						%{_libdir}/asterisk/modules/app_osplookup.so
#exclude						%{_libdir}/asterisk/modules/app_sql_postgres.so
%exclude						%{_libdir}/asterisk/modules/cdr_pgsql.so
%exclude						%{_libdir}/asterisk/modules/cdr_radius.so
%exclude						%{_libdir}/asterisk/modules/cdr_sqlite.so
%exclude						%{_libdir}/asterisk/modules/chan_gtalk.so
%exclude						%{_libdir}/asterisk/modules/res_config_pgsql.so
%exclude						%{_libdir}/asterisk/modules/res_jabber.so
%exclude						%{_libdir}/asterisk/modules/res_snmp.so
%exclude						%{_libdir}/asterisk/modules/*sql*.so

#attr(0755,asterisk,asterisk)	%dir			%{_localstatedir}/asterisk
%attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/agi-bin
%attr(0755,root,root)					%{_localstatedir}/asterisk/agi-bin/*
%ghost							%{_localstatedir}/asterisk/astdb
%attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/firmware
%attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/firmware/iax
%attr(0755,root,root)					%{_localstatedir}/asterisk/firmware/iax/*.bin
%attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/images
%attr(0644,root,root)					%{_localstatedir}/asterisk/images/*.jpg
%attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/keys
%attr(0644,root,root)					%{_localstatedir}/asterisk/keys/*.pub
%attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/moh
%attr(0644,root,root)					%{_localstatedir}/asterisk/moh/*.wav
%doc							%{_localstatedir}/asterisk/moh/LICENSE-asterisk-moh-freeplay-wav
#attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/mohmp3
#attr(0644,root,root)					%{_localstatedir}/asterisk/mohmp3/*.mp3
%attr(0755,root,root)		%dir			%{_localstatedir}/asterisk/static-http
%attr(0644,root,root)					%{_localstatedir}/asterisk/static-http/*

%attr(0750,asterisk,asterisk)	%dir			/var/log/asterisk
%attr(0750,asterisk,asterisk)	%dir			/var/log/asterisk/cdr-csv
%attr(644,asterisk,asterisk)	%ghost			/var/log/asterisk/cdr-csv/Master.csv
%attr(0750,asterisk,asterisk)	%dir			/var/log/asterisk/cdr-custom
%attr(644,asterisk,asterisk)	%ghost			/var/log/asterisk/console
%attr(644,asterisk,asterisk)	%ghost			/var/log/asterisk/debug
%attr(644,asterisk,asterisk)	%ghost			/var/log/asterisk/event_log
%attr(644,asterisk,asterisk)	%ghost			/var/log/asterisk/h323_log
%attr(644,asterisk,asterisk)	%ghost			/var/log/asterisk/messages
%attr(644,asterisk,asterisk)	%ghost			/var/log/asterisk/queue_log
#attr(0750,asterisk,asterisk)	%dir			/var/log/asterisk/testreports

%attr(0750,asterisk,asterisk)	%dir			/var/run/asterisk

%attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/dictate
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/meetme
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/monitor
%attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/outgoing
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/system
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/tmp
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/vm
%attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/voicemail
%attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/voicemail/default
%attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/voicemail/default/1234
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/voicemail/default/1234/INBOX
%attr(0644,asterisk,asterisk)				/var/spool/asterisk/voicemail/default/1234/busy.gsm
%attr(0644,asterisk,asterisk)				/var/spool/asterisk/voicemail/default/1234/unavail.gsm
#attr(0750,asterisk,asterisk)	%dir			/var/spool/asterisk/voicemail/voicemail

							%{_mandir}/man8/asterisk.8*
							%{_mandir}/man8/astgenkey.8*
							%{_mandir}/man8/autosupport.8*
							%{_mandir}/man8/safe_asterisk.8*

%files devel -f %{name}-devel.filelist
%defattr(-,root,root)
%attr(0644,root,root)					%{_includedir}/asterisk/*.h
%attr(0644,root,root)					%{_includedir}/asterisk.h
#exclude						%{_includedir}/asterisk/defaults.h
							%{_libdir}/pkgconfig/asterisk.pc
#multiarch						%{multiarch_includedir}/asterisk/defaults.h

%files docs
%defattr(-,root,root)
%doc							docs-html/*

%if %{build_misdn}
%files chan_misdn
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/misdn.conf
%attr(0755,root,root)					%{_libdir}/asterisk/modules/chan_misdn.so
%endif

%files plugins-fax
%defattr(-,root,root)
#attr(0755,root,root)
%{_libdir}/asterisk/modules/app_*fax.so

%if %{build_odbc}
%files plugins-odbc
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/*_odbc.conf
%attr(0755,root,root)					%{_libdir}/asterisk/modules/*_odbc.so
%endif

%files plugins-pgsql
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/cdr_pgsql.conf
#attr(0755,root,root)					%{_libdir}/asterisk/modules/app_sql_postgres.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/cdr_pgsql.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/res_config_pgsql.so

%if %{build_radius}
%files plugins-radius
%defattr(-,root,root)
%attr(0755,root,root)					%{_libdir}/asterisk/modules/cdr_radius.so
%endif

%files plugins-sqlite
%defattr(-,root,root)
%attr(0755,root,root)					%{_libdir}/asterisk/modules/cdr_sqlite.so

%if %build_tds
%files plugins-tds
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/cdr_tds.conf
%attr(0755,root,root)					%{_libdir}/asterisk/modules/cdr_tds.so
%endif

%files plugins-osp
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/osp.conf
%attr(0755,root,root)					%{_libdir}/asterisk/modules/app_osplookup.so

%files plugins-snmp
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/res_snmp.conf
%attr(0755,root,root)					%{_libdir}/asterisk/modules/res_snmp.so

%files plugins-jabber
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/gtalk.conf
%attr(0644,asterisk,asterisk) %config(noreplace)	%{_sysconfdir}/asterisk/jabber.conf
%attr(0755,root,root)					%{_libdir}/asterisk/modules/chan_gtalk.so
%attr(0755,root,root)					%{_libdir}/asterisk/modules/res_jabber.so

%files webvmail
%defattr(-,root,root)
%attr(4755,root,root)					/var/www/cgi-bin/vmail.cgi
%attr(-,root,root)		%dir			/var/www/html/_asterisk
%attr(0644,root,root)					/var/www/html/_asterisk/animlogo.gif
%attr(0644,root,root)					/var/www/html/_asterisk/play.gif


