%define dataversion 0.61

Summary:	Racing game based on Tux Racer
Name:		wherever-racer
Version:	0.1
Release:	%mkrel 5
License:	GPLv2+
Group:		Games/Sports
URL:		http://linuxprocess.tuxfamily.org/
Source:		%{name}-src-%{version}.tgz
Source1:	%{name}-data-%{version}.tgz
Source2:	%{name}-addon-%{version}.tgz
Source3:	%{name}-16x16.png
Source4:	%{name}-32x32.png
Source5:	%{name}-48x48.png
Patch0:		%{name}-0.1-gcc33.patch
Patch1:		%{name}-0.1-config.patch
Patch2:		%{name}-0.1-ia64.patch
BuildRequires:	libSDL_mixer-devel
BuildRequires:	libx11-static-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	esound-devel
BuildRequires:	mesaglu-devel
BuildRequires:	tcl
BuildRequires:	tcl-devel
BuildRequires:	texinfo
Conflicts:	tuxracer
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Wherever Racer is a simple OpenGL-based racing game featuring Tux.
The object of the game is to slide down a snow- and ice-covered mountain as
quickly as possible, avoiding the trees and rocks that will slow you down.
It is based on OpenRacer, a fork of Tux Racer, and offers the ability
to use themes, such as golf or open (set it in your ~/.tuxracer/options).

%prep

%setup -q -a 1 -a 2 -n tuxracer-%{dataversion}
%patch0 -p1 -b .gcc3.3
%patch1 -p1 -b .config
%patch2 -p1 -b .ia64

%build
%configure2_5x --with-data-dir=%{_gamesdatadir}/tuxracer/
%make

%install
rm -fr %{buildroot}
%makeinstall bindir=%{buildroot}%{_gamesbindir}

install -d %{buildroot}/%{_gamesdatadir}/tuxracer/

# get rid of .DS_Store Files created by Mac OS X Finder
rm -f tuxracer-data-%{dataversion}/courses/contrib/*/.DS_Store

tar c -C tuxracer-data-%{dataversion} . | tar x -C %{buildroot}/%{_gamesdatadir}/tuxracer/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Wherever Racer
Comment=A great racing game starring Tux
Exec=soundwrapper %{_gamesbindir}/tuxracer
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF

chmod -R a+rX %{buildroot}/%{_gamesdatadir}/tuxracer/ 

install -m644 %{SOURCE3} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE4} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE5} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%clean
rm -fr %{buildroot}

%post
%{update_menus}
%{update_icon_cache hicolor}

%postun
%{clean_menus}
%{clean_icon_cache hicolor}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README contrib
%doc %{_gamesdatadir}/tuxracer/README
%{_gamesbindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/tuxracer/
%{_iconsdir}/hicolor/*/apps/%{name}.png

