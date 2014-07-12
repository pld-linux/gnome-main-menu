# TODO
# - lock screen fails (but mate own lock screen launches xscreensaver okay)
#   ** (main-menu:9293): WARNING **: error launching file:///usr/share/applications/mate-screensaver-lock.desktop [Fai
#
# Conditional build:
%bcond_without	caja	# Caja (MATE file manager) extension
#
Summary:	The GNOME/MATE Desktop Menu
Summary(pl.UTF-8):	Menu dla środowiska GNOME/MATE
Name:		gnome-main-menu
Version:	1.8.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	c93b26d9ab7d68209e3e716c69b0c37b
URL:		http://en.opensuse.org/GNOME_Main_Menu
BuildRequires:	NetworkManager-devel >= 0.8.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	cairo-devel
%{?with_caja:BuildRequires:	caja-devel >= 1.5.0}
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtk-doc-automake >= 1.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgtop-devel
BuildRequires:	libiw-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	mate-control-center-devel >= 1.5.2
BuildRequires:	mate-desktop-devel >= 1.8.0
BuildRequires:	mate-panel-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	glib2 >= 1:2.26.0
Requires:	gtk+2 >= 2:2.18
Requires:	mate-control-center >= 1.5.2
Requires:	mate-panel
Requires:	mate-panel
Requires:	mate-system-monitor
# for mate-screensaver-lock
Suggests:	mate-screensaver
# for mate-session-logout, mate-session-shutdown
Suggests:	mate-session-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/mate-panel

%description
GNOME Main Menu is a convenient menu for GNOME/MATE desktop
environments accessible from a button in the desktop panel. It is
different from conventional menus, in that it lists a user's favourite
and recent Applications, Documents and Places in one useful interface.
Additionally it provides a search bar that allows a user to search for
applications and documents from the menu itself.

%description -l pl.UTF-8
GNOME Main Menu to wygodne menu dla środowisk GNOME/Mate, dostępne z
poziomu przycisku w panelu pulpitu. Różni się tym od konwencjonalnych
menu, że wyświetla ulubione i ostatnio używane przez użytkownika
aplikacje, dokumenty i miejsca w jednym, użytecznym interfejsie.
Dodatkowo udostępnia pasek wyszukiwania, pozwalający użytkownikowi
wyszukać aplikacje i dokumenty z menu.

%package -n caja-extension-main-menu
Summary:	Main Menu extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie Main Menu dla zarządcy plików Caja (ze środowiska MATE)
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	caja >= 1.5.0

%description -n caja-extension-main-menu
Main Menu extension for Caja (MATE file manager).

%description -n caja-extension-main-menu -l pl.UTF-8
Rozszerzenie Main Menu dla zarządcy plików Caja (ze środowiska MATE).

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_caja:--enable-caja-extension} \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%if %{with caja}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/libcaja-main-menu.la
%endif

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
%attr(755,root,root) %{_libexecdir}/main-menu
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
%{_datadir}/mate-control-center/applications.xbel
%{_datadir}/mate-control-center/documents.xbel
%{_datadir}/mate-control-center/places.xbel
%{_datadir}/mate-control-center/system-items.xbel
%{_datadir}/mate-control-center/empty.ots
%{_datadir}/mate-control-center/empty.ott
%{_datadir}/mate-panel/applets/org.mate.GNOMEMainMenu.mate-panel-applet

%if %{with caja}
%files -n caja-extension-main-menu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-main-menu.so
%endif
