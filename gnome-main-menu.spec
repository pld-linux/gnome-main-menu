# TODO
# - lock screen fails (but mate own lock screen launches xscreensaver okay)
#   ** (main-menu:9293): WARNING **: error launching file:///usr/share/applications/mate-screensaver-lock.desktop [Fai
Summary:	The GNOME Desktop Menu
Summary(pl.UTF-8):	Menu dla środowiska GNOME
Name:		gnome-main-menu
Version:	1.8.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	c93b26d9ab7d68209e3e716c69b0c37b
URL:		http://en.opensuse.org/GNOME_Main_Menu
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool
BuildRequires:	libgtop-devel
BuildRequires:	libiw-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	mate-control-center-devel >= 1.5.2
BuildRequires:	mate-desktop-devel >= 1.8.0
BuildRequires:	mate-panel-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
#Requires:	dbus-glib
Requires:	glib2 >= 1:2.26.0
#Requires:	gnome-panel
#Requires:	gnome-terminal
#Requires:	hal
Requires:	mate-system-monitor
#Requires:	tango-icon-theme
#Requires:	wireless-tools
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
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/application-browser
%attr(755,root,root) %{_bindir}/trigger-panel-run-dialog
%attr(755,root,root) %{_libdir}/main-menu
%{_mandir}/man1/application-browser.1*
%{_desktopdir}/application-browser.desktop
%{_desktopdir}/mate-screensaver-lock.desktop
%{_desktopdir}/mate-session-logout.desktop
%{_desktopdir}/mate-session-shutdown.desktop
%{_desktopdir}/trigger-panel-run-dialog.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.mate.panel.applet.GNOMEMainMenuFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.gnome-main-menu.application-browser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.gnome-main-menu.gschema.xml
%{_datadir}/mate-control-center/*.xbel
%{_datadir}/mate-control-center/empty.*
%{_datadir}/mate-panel/applets/org.mate.GNOMEMainMenu.mate-panel-applet
