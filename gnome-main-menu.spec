Summary:	The GNOME Desktop Menu
Name:		gnome-main-menu
Version:	0.6.2
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	e0931ef4cee4f703bd078d59b9f32d40
URL:		http://www.gnome.org
BuildRequires:	NetworkManager-devel
BuildRequires:	avahi-devel
BuildRequires:	fam-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	gnutls-devel
BuildRequires:	intltool
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libgtop-devel
BuildRequires:	libidn
BuildRequires:	librsvg-devel
BuildRequires:	libwnck-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	python-devel
BuildRequires:	python-pygtk-gtk
BuildRequires:	scrollkeeper
Requires(pre):	filesystem
Requires(pre):	GConf2
Requires:	dbus-glib
Requires:	hal
Requires:	gnome-panel
Requires:	gnome-system-monitor
Requires:	gnome-terminal
Requires:	tango-icon-theme
Requires:	wireless-tools

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNOME Desktop Menu and Application Browser.

Authors:
Scott Reeves <sreeves@novell.com>
Jimmy Krehl <jimmyk@novell.com>

%package devel
Summary:	The GNOME Desktop Menu
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk2+-devel
Requires:	libgnomeui-devel
Requires:	libbonoboui-devel
Requires:	libglade2-devel
Requires:	librsvg-devel
Requires:	gnome-desktop-devel
Requires:	gnome-menus-devel
Requires:	glib2-devel
Requires:	pango-devel

%description devel
The GNOME Desktop Menu and Application Browser.

Authors:
Scott Reeves <sreeves@novell.com>
Jimmy Krehl <jimmyk@novell.com>

%prep
%setup -q

%build
autoreconf -f -i
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --sysconfdir=%{_sysconfdir}
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
%attr(755,root,root) %{_libexecdir}/main-menu
%attr(755,root,root) %{_bindir}/application-browser
%attr(755,root,root) %{_bindir}/control-center
%{_libdir}/bonobo/servers/GNOME_MainMenu.server
%attr(755,root,root) %{_libdir}/*.so.*
%{_desktopdir}/application-browser.desktop
%{_desktopdir}/control-center.desktop
%{_desktopdir}/main-menu-rug.desktop
%{_datadir}/gnome-2.0/ui/GNOME_MainMenu_ContextMenu.xml
%{_datadir}/gnome/autostart/application-browser.desktop

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
%{_libdir}/*.*a
%{_libdir}/*.so
%{_includedir}/slab
