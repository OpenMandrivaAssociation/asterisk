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

%define build_tds	1
%{?_without_tds:	%global build_tds 0}
%{?_with_tds:		%global build_tds 1}

# this takes quite some time and adds roughly 200mb of html...
%define build_docs	0
%{?_without_docs:	%global build_docs 0}
%{?_with_docs:		%global build_docs 1}

Summary:	Asterisk PBX
Name:		asterisk
Version:	1.4.21.1
Release:	%mkrel 2
License:	GPL
Group:		System/Servers
URL:		http://www.asterisk.org/
Source0:	http://www.asterisk.org/html/downloads/%{name}-%{version}.tar.gz
Source1:	asterisk.init
Source2:	asterisk.sysconfig
Patch0:		asterisk-mdv.diff
Patch4:		asterisk-freetds.diff
Patch16:	asterisk-external_liblpc10_and_libilbc.diff
Patch17:	asterisk-1.4.0-beta3-no_mega_optimization.diff
Patch18:	asterisk-imap.diff
Patch19:	asterisk-1.4-app_fax.diff
Patch20:	asterisk-chan_sip-content-length.diff
Patch21:	asterisk-autoconf262.diff
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
BuildRequires:	isdn4k-utils-devel
BuildRequires:	libgsm-devel
BuildRequires:	libiksemel-devel
BuildRequires:	libilbc-devel
BuildRequires:	libnbs-devel
BuildRequires:	libncurses-devel
BuildRequires:	libpri-devel >= 1.4.0
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
BuildRequires:	spandsp-devel
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
BuildRequires:	freetds-devel >= 0.64

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
BuildRequires:	perl-devel
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

%setup -q

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type d -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;
		
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch0 -p1 -b .mdv

%if %build_tds
%patch4 -p0 -b .freetds
%endif

%patch16 -p1 -b .external_liblpc10_and_libilbc
%patch17 -p0 -b .no_mega_optimization
%patch18 -p0 -b .imap
%patch19 -p0 -b .app_fax
%patch20 -p0 -b .content_length
%patch21 -p0

cat %{SOURCE1} > asterisk.init
cat %{SOURCE2} > asterisk.sysconfig

# lib64 fix
find -name "Makefile" | xargs perl -pi -e "s|/usr/lib|%{_libdir}|g"
perl -pi -e "s|/lib\b|/%{_lib}|g" configure* acinclude.m4
perl -pi -e "s|/lib/|/%{_lib}/|g" configure* acinclude.m4

# temporary hack
cp %{_includedir}/spandsp/plc.h include/asterisk/

%build
%serverbuild

rm -f configure
sh ./bootstrap.sh

echo "%{version}-%{release}" > .version

export ASTCFLAGS="$CFLAGS"

%configure2_5x \
    --localstatedir=/var/lib \
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
rm -rf %{buildroot}

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
    create 0640 asterisk asterisk
    weekly
    rotate 5
    copytruncate
    compress
    notifempty
    missingok
    postrotate
	%{_sbindir}/asterisk -rx 'logger reload' >/dev/null 2>/dev/null || true
    endscript
}
EOF

touch %{name}-devel.filelist
%if %{build_docs}
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

# Fix incorrect path in /etc/asterisk/asterisk.conf
perl -pi -e "s|astrundir => /var/run|astrundir => /var/run/asterisk|g" %{buildroot}/%{_sysconfdir}/asterisk/asterisk.conf
perl -pi -e "s|^libdir=.*|libdir=%{_libdir}|g" %{buildroot}%{_libdir}/pkgconfig/asterisk.pc
perl -pi -e "s|^varrundir=.*|varrundir=/var/run/asterisk|g" %{buildroot}%{_libdir}/pkgconfig/asterisk.pc

# Remove unpackages files
rm -rf %{buildroot}/var/lib/asterisk/moh/.asterisk-moh-freeplay-wav

# use the stand alone asterisk-core-sounds package instead
rm -rf %{buildroot}/var/lib/asterisk/sounds

%pre
%_pre_useradd asterisk /var/lib/asterisk /bin/sh

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
%_post_service asterisk

%preun
if [ "$1" = 0 ]; then
    echo "Removing setuid root from /usr/bin/mpg123"
    chmod u-s %{_bindir}/mpg123
fi

%_preun_service asterisk

%postun
%_postun_userdel asterisk

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS ChangeLog CREDITS LICENSE README* apps/rpt_flow.pdf
%doc doc/*README* doc/*.txt contrib/init.d/rc.mandrake* contrib/asterisk-ices.xml
%doc contrib/scripts contrib/i18n.testsuite.conf contrib/README.festival
%attr(0755,root,root) %{_initrddir}/asterisk
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/asterisk
%attr(0750,asterisk,asterisk) %dir %{_sysconfdir}/asterisk
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/*.adsi
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/*.conf
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.ael
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/asterisk
%attr(0755,root,root) %{_sbindir}/aelparse
%attr(0755,root,root) %{_sbindir}/asterisk
%attr(0755,root,root) %{_sbindir}/astgenkey
%attr(0755,root,root) %{_sbindir}/astman
%attr(0755,root,root) %{_sbindir}/autosupport
%attr(0755,root,root) %{_sbindir}/muted
%attr(0755,root,root) %{_sbindir}/rasterisk
%attr(0755,root,root) %{_sbindir}/safe_asterisk
%attr(0755,root,root) %{_sbindir}/smsq
%attr(0755,root,root) %{_sbindir}/stereorize
%attr(0755,root,root) %{_sbindir}/streamplayer
%attr(0755,root,root) %dir %{_libdir}/asterisk
%attr(0755,root,root) %dir %{_libdir}/asterisk/modules
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_*.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_*.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_*.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/codec_*.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/format_*.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/func_*.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/pbx_*.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_*.so
%attr(0755,root,root) %dir /var/lib/asterisk/agi-bin
%attr(0755,root,root) /var/lib/asterisk/agi-bin/*
%ghost /var/lib/asterisk/astdb
%attr(0755,root,root) %dir /var/lib/asterisk/firmware
%attr(0755,root,root) %dir /var/lib/asterisk/firmware/iax
%attr(0755,root,root) /var/lib/asterisk/firmware/iax/*.bin
%attr(0755,root,root) %dir /var/lib/asterisk/images
%attr(0644,root,root) /var/lib/asterisk/images/*.jpg
%attr(0755,root,root) %dir /var/lib/asterisk/keys
%attr(0644,root,root) /var/lib/asterisk/keys/*.pub
%attr(0755,root,root) %dir /var/lib/asterisk/moh
%attr(0644,root,root) /var/lib/asterisk/moh/*.wav
%doc /var/lib/asterisk/moh/LICENSE-asterisk-moh-freeplay-wav
%attr(0755,root,root) %dir /var/lib/asterisk/static-http
%attr(0644,root,root) /var/lib/asterisk/static-http/*
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk/cdr-csv
%attr(644,asterisk,asterisk) %ghost /var/log/asterisk/cdr-csv/Master.csv
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk/cdr-custom
%attr(644,asterisk,asterisk) %ghost /var/log/asterisk/console
%attr(644,asterisk,asterisk) %ghost /var/log/asterisk/debug
%attr(644,asterisk,asterisk) %ghost /var/log/asterisk/event_log
%attr(644,asterisk,asterisk) %ghost /var/log/asterisk/h323_log
%attr(644,asterisk,asterisk) %ghost /var/log/asterisk/messages
%attr(644,asterisk,asterisk) %ghost /var/log/asterisk/queue_log
%attr(0750,asterisk,asterisk) %dir /var/run/asterisk
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/outgoing
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/voicemail
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/voicemail/default
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/voicemail/default/1234
%attr(0644,asterisk,asterisk) /var/spool/asterisk/voicemail/default/1234/busy.gsm
%attr(0644,asterisk,asterisk) /var/spool/asterisk/voicemail/default/1234/unavail.gsm
%{_mandir}/man8/asterisk.8*
%{_mandir}/man8/astgenkey.8*
%{_mandir}/man8/autosupport.8*
%{_mandir}/man8/safe_asterisk.8*

# these are packaged as sub packages below
%exclude %{_sysconfdir}/asterisk/cdr_pgsql.conf
%exclude %{_sysconfdir}/asterisk/gtalk.conf
%exclude %{_sysconfdir}/asterisk/jabber.conf
%exclude %{_sysconfdir}/asterisk/osp.conf
%exclude %{_sysconfdir}/asterisk/res_snmp.conf
%exclude %{_sysconfdir}/asterisk/*sql*.conf
%if %{build_misdn}
%exclude %{_sysconfdir}/asterisk/misdn.conf
%exclude %{_libdir}/asterisk/modules/chan_misdn.so
%endif
%if %{build_odbc}
%exclude %{_sysconfdir}/asterisk/*_odbc.conf
%exclude %{_libdir}/asterisk/modules/*_odbc.so
%endif
%if %{build_tds}
%exclude %{_sysconfdir}/asterisk/*tds*.conf
%exclude %{_libdir}/asterisk/modules/*tds*.so
%endif
%exclude %{_libdir}/asterisk/modules/app_*fax.so
%exclude %{_libdir}/asterisk/modules/app_osplookup.so
%exclude %{_libdir}/asterisk/modules/cdr_pgsql.so
%exclude %{_libdir}/asterisk/modules/cdr_radius.so
%exclude %{_libdir}/asterisk/modules/cdr_sqlite.so
%exclude %{_libdir}/asterisk/modules/chan_gtalk.so
%exclude %{_libdir}/asterisk/modules/res_config_pgsql.so
%exclude %{_libdir}/asterisk/modules/res_jabber.so
%exclude %{_libdir}/asterisk/modules/res_snmp.so
%exclude %{_libdir}/asterisk/modules/*sql*.so

%files devel -f %{name}-devel.filelist
%defattr(-,root,root)
%attr(0644,root,root) %{_includedir}/asterisk/*.h
%attr(0644,root,root) %{_includedir}/asterisk.h
%{_libdir}/pkgconfig/asterisk.pc

%if %{build_misdn}
%files chan_misdn
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/misdn.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_misdn.so
%endif

%files plugins-fax
%defattr(-,root,root)
%{_libdir}/asterisk/modules/app_*fax.so

%if %{build_odbc}
%files plugins-odbc
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/*_odbc.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/*_odbc.so
%endif

%files plugins-pgsql
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_pgsql.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_config_pgsql.so

%if %{build_radius}
%files plugins-radius
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_radius.so
%endif

%files plugins-sqlite
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_sqlite.so

%if %build_tds
%files plugins-tds
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_tds.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/cdr_tds.so
%endif

%files plugins-osp
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/app_osplookup.so

%files plugins-snmp
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_snmp.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_snmp.so

%files plugins-jabber
%defattr(-,root,root)
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/gtalk.conf
%attr(0644,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jabber.conf
%attr(0755,root,root) %{_libdir}/asterisk/modules/chan_gtalk.so
%attr(0755,root,root) %{_libdir}/asterisk/modules/res_jabber.so

%files webvmail
%defattr(-,root,root)
%attr(4755,root,root) /var/www/cgi-bin/vmail.cgi
%attr(-,root,root) %dir /var/www/html/_asterisk
%attr(0644,root,root) /var/www/html/_asterisk/animlogo.gif
%attr(0644,root,root) /var/www/html/_asterisk/play.gif
