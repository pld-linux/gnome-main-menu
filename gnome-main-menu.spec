Summary:	The GNOME Desktop Menu
Summary(pl.UTF-8):	Menu dla środowiska GNOME
Name:		gnome-main-menu
Version:	0.9.16
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-main-menu/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	c52c95536dadd64d08d566f8aafc2da2
URL:		http://en.opensuse.org/GNOME_Main_Menu
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	gnutls-devel
BuildRequires:	hal-devel
BuildRequires:	intltool
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libgtop-devel
BuildRequires:	libidn-devel
BuildRequires:	libiw-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	libwnck2-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	python-devel
BuildRequires:	python-pygtk-gtk
BuildRequires:	scrollkeeper
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	dbus-glib
Requires:	gnome-panel
Requires:	gnome-system-monitor
Requires:	gnome-terminal
Requires:	hal
Requires:	tango-icon-theme
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Main Menu is a convenient menu accessible from a button in the
desktop panel. It is different from conventional menus, in that it
lists a user's favourite and recent Applications, Documents and Places
in one useful interface. Additionally it provides a search bar that
allows a user to search for applications and documents from the menu
itself.

%description -l pl.UTF-8
Menu i przeglądarka aplikacji dla środowiska GNOME.

%package devel
Summary:	Header files for GNOME Desktop Menu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki menu środowiska GNOME
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel
Requires:	gnome-desktop-devel
Requires:	gnome-menus-devel
Requires:	gtk+2-devel
Requires:	libbonoboui-devel
Requires:	libglade2-devel
Requires:	libgnomeui-devel
Requires:	librsvg-devel
Requires:	pango-devel

%description devel
Header files for GNOME Desktop Menu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki menu środowiska GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__libtoolize}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/autostart
install application-browser/etc/application-browser.desktop $RPM_BUILD_ROOT%{_datadir}/gnome/autostart/
sed -i "/^Exec=/ s/application-browser *$/application-browser -h/" $RPM_BUILD_ROOT%{_datadir}/gnome/autostart/application-browser.desktop

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/en_IGID

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install slab.schemas
%gconf_schema_install control-center.schemas
%gconf_schema_install application-browser.schemas
%scrollkeeper_update_post
/sbin/ldconfig

%preun
%gconf_schema_uninstall slab.schemas
%gconf_schema_uninstall control-center.schemas
%gconf_schema_uninstall application-browser.schemas

%postun
%scrollkeeper_update_postun
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/slab.schemas
%{_sysconfdir}/gconf/schemas/control-center.schemas
%{_sysconfdir}/gconf/schemas/application-browser.schemas
%attr(755,root,root) %{_bindir}/application-browser
%attr(755,root,root) %{_bindir}/control-center
%attr(755,root,root) %{_libexecdir}/main-menu
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/bonobo/servers/GNOME_MainMenu.server
%{_desktopdir}/application-browser.desktop
%{_desktopdir}/control-center.desktop
%{_desktopdir}/gnome-screensaver-lock.desktop
%{_desktopdir}/gnome-session-kill.desktop
%{_datadir}/gnome-main-menu
%{_datadir}/gnome-2.0/ui/GNOME_MainMenu_ContextMenu.xml
%{_datadir}/gnome/autostart/application-browser.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/slab
%{_pkgconfigdir}/*.pc

# static? (if exists)
#%{_libdir}/*.a
