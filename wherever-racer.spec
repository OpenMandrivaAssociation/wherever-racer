%define dataversion 0.61

Summary:	Wherever Racer
Name:		wherever-racer
Version:	0.1
Release:	%mkrel 4
License:	GPL
Group:		Games/Sports
URL:		http://linuxprocess.tuxfamily.org/downloads.php
Source:		%{name}-src-%{version}.tgz
Source1:	%{name}-data-%{version}.tgz
Source2:	%{name}-addon-%{version}.tgz
Source3:	%{name}-16x16.png
Source4:	%{name}-32x32.png
Source5:	%{name}-48x48.png
Patch0:		%{name}-0.1-gcc33.patch.bz2
Patch1:		%{name}-0.1-config.patch.bz2
Patch2:		%{name}-0.1-ia64.patch.bz2
BuildRequires:	SDL_mixer-devel
BuildRequires:	libx11-static-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	esound-devel
BuildRequires:	libMesaGLU-devel
BuildRequires:	tcl tcl-devel
BuildRequires:	texinfo
Conflicts:	tuxracer
BuildRoot:	%_tmppath/%name-%version-%release-root

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
# not needed anymore, code is now fixed for OpenGL 1.3
#export CC="gcc -DGLX_GLXEXT_LEGACY"
%configure --with-data-dir=%_gamesdatadir/tuxracer/

%make

%install
rm -fr %buildroot

%makeinstall bindir=$RPM_BUILD_ROOT%_gamesbindir

install -d %buildroot/%_gamesdatadir/tuxracer/

# get rid of .DS_Store Files created by Mac OS X Finder
rm -f tuxracer-data-%dataversion/courses/contrib/*/.DS_Store

tar c -C tuxracer-data-%dataversion . | tar x -C %buildroot/%_gamesdatadir/tuxracer/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Wherever Racer
Comment=A great racing game starring Tux
Exec=soundwrapper %_gamesbindir/tuxracer
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Sports;Game;SportsGame;
EOF

install -d %buildroot/%_menudir
cat <<EOF > %buildroot/%_menudir/%name
?package(%{name}):command="soundwrapper %_gamesbindir/tuxracer" \
		  icon="%{name}.png" \
		  needs="x11" \
		  section="Amusement/Sports" \
		  title="Tuxracer"\
		  longtitle="A great racing game starring Tux" \
		  xdg="true"
EOF

chmod -R a+rX %buildroot/%_gamesdatadir/tuxracer/ 

install -m644 %{SOURCE3} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE4} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE5} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean
rm -fr %buildroot

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README contrib
#
#
#
%_gamesbindir/*
#
#
#
%_menudir/*
%{_datadir}/applications/mandriva-%{name}.desktop
#
#
#
%dir %_gamesdatadir/tuxracer/
%doc %_gamesdatadir/tuxracer/README
%_gamesdatadir/tuxracer/*.tcl*
#
#
%dir %_gamesdatadir/tuxracer/courses/
%_gamesdatadir/tuxracer/courses/course_idx.tcl*
#
%dir %_gamesdatadir/tuxracer/courses/bumpy_ride/
%_gamesdatadir/tuxracer/courses/bumpy_ride/*
#
%dir %_gamesdatadir/tuxracer/courses/bunny_hill/
%_gamesdatadir/tuxracer/courses/bunny_hill/*
#
%dir %_gamesdatadir/tuxracer/courses/common/
%_gamesdatadir/tuxracer/courses/common/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/
%dir %_gamesdatadir/tuxracer/courses/contrib/60_herrings_half_pipe/
%_gamesdatadir/tuxracer/courses/contrib/60_herrings_half_pipe/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/bigasjump/
%_gamesdatadir/tuxracer/courses/contrib/bigasjump/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/BronzeSet/
%_gamesdatadir/tuxracer/courses/contrib/BronzeSet/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/Candy_Lane/
%_gamesdatadir/tuxracer/courses/contrib/Candy_Lane/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/canyon/
%_gamesdatadir/tuxracer/courses/contrib/canyon/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/deadman/
%_gamesdatadir/tuxracer/courses/contrib/deadman/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/Desperation/
%_gamesdatadir/tuxracer/courses/contrib/Desperation/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/downhill_fear/
%_gamesdatadir/tuxracer/courses/contrib/downhill_fear/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/flatcourse/
%_gamesdatadir/tuxracer/courses/contrib/flatcourse/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/goldenset/
%_gamesdatadir/tuxracer/courses/contrib/goldenset/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/halfpipe/
%_gamesdatadir/tuxracer/courses/contrib/halfpipe/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/hamburger_hill/
%_gamesdatadir/tuxracer/courses/contrib/hamburger_hill/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/hazzard_valley/
%_gamesdatadir/tuxracer/courses/contrib/hazzard_valley/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/hey_tux/
%_gamesdatadir/tuxracer/courses/contrib/hey_tux/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/ice_canyon/
%_gamesdatadir/tuxracer/courses/contrib/ice_canyon/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/ice_labyrinth/
%_gamesdatadir/tuxracer/courses/contrib/ice_labyrinth/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/ice_pipeline/
%_gamesdatadir/tuxracer/courses/contrib/ice_pipeline/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/ingos_speedway/
%_gamesdatadir/tuxracer/courses/contrib/ingos_speedway/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/in_search_of_vodka/
%_gamesdatadir/tuxracer/courses/contrib/in_search_of_vodka/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/ive_got_a_woody/
%_gamesdatadir/tuxracer/courses/contrib/ive_got_a_woody/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/jools_big_mountain/
%_gamesdatadir/tuxracer/courses/contrib/jools_big_mountain/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/milos_castle/
%_gamesdatadir/tuxracer/courses/contrib/milos_castle/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/mount_herring/
%_gamesdatadir/tuxracer/courses/contrib/mount_herring/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/mount_satan/
%_gamesdatadir/tuxracer/courses/contrib/mount_satan/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/nebula/
%_gamesdatadir/tuxracer/courses/contrib/nebula/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/nevada/
%_gamesdatadir/tuxracer/courses/contrib/nevada/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/next_step/
%_gamesdatadir/tuxracer/courses/contrib/next_step/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/pdna/
%_gamesdatadir/tuxracer/courses/contrib/pdna/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/penguins_cant_fly/
%_gamesdatadir/tuxracer/courses/contrib/penguins_cant_fly/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/ramps/
%_gamesdatadir/tuxracer/courses/contrib/ramps/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/rock_n_roll/
%_gamesdatadir/tuxracer/courses/contrib/rock_n_roll/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/sentinel_towers/
%_gamesdatadir/tuxracer/courses/contrib/sentinel_towers/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/skull_mountain/
%_gamesdatadir/tuxracer/courses/contrib/skull_mountain/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/snow_run_1/
%_gamesdatadir/tuxracer/courses/contrib/snow_run_1/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/snow_run_2/
%_gamesdatadir/tuxracer/courses/contrib/snow_run_2/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/snow_valley/
%_gamesdatadir/tuxracer/courses/contrib/snow_valley/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/The_long_ride/
%_gamesdatadir/tuxracer/courses/contrib/The_long_ride/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/the_narrow_way/
%_gamesdatadir/tuxracer/courses/contrib/the_narrow_way/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/Tidy/
%_gamesdatadir/tuxracer/courses/contrib/Tidy/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/twin_paths/
%_gamesdatadir/tuxracer/courses/contrib/twin_paths/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/twists/
%_gamesdatadir/tuxracer/courses/contrib/twists/*
#
%dir %_gamesdatadir/tuxracer/courses/contrib/wild_ride/
%_gamesdatadir/tuxracer/courses/contrib/wild_ride/*
#
%dir %_gamesdatadir/tuxracer/courses/frozen_river/
%_gamesdatadir/tuxracer/courses/frozen_river/*
#
%dir %_gamesdatadir/tuxracer/courses/path_of_daggers/
%_gamesdatadir/tuxracer/courses/path_of_daggers/*
#
%dir %_gamesdatadir/tuxracer/courses/twisty_slope/
%_gamesdatadir/tuxracer/courses/twisty_slope/*
#
#
%dir %_gamesdatadir/tuxracer/fonts/
%_gamesdatadir/tuxracer/fonts/*
#
#
%dir %_gamesdatadir/tuxracer/music/
%_gamesdatadir/tuxracer/music/*
#
#
%dir %_gamesdatadir/tuxracer/sounds/
%_gamesdatadir/tuxracer/sounds/*
#
#
%dir %_gamesdatadir/tuxracer/textures/
%_gamesdatadir/tuxracer/textures/*
#
#
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
