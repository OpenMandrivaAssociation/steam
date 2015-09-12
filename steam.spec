%define debug_package %{nil}

Summary:	Steam Linux Client
Name:		steam
Version:	1.0.0.49
Release:	5
Group:		Games/Other
License:	Proprietary
URL:		https://github.com/ValveSoftware/steam-for-linux
Source0:	http://repo.steampowered.com/steam/pool/steam/s/steam/%{name}_%{version}.tar.gz
Requires:	alsa-lib
Requires:	awk
Requires:	coreutils
Requires:	curl
Requires:	dbus
Requires:	desktop-file-utils
Requires:	fonts-ttf-liberation
Requires:	gdk-pixbuf2.0
Requires:	gtk+2.0
Requires:	hicolor-icon-theme
Requires:	nss
Requires:	openal
Requires:	pulseaudio
Requires:	xterm
Requires:	zenity
# Libraries
Requires:	libfreetype6
Requires:	libgcrypt20
Requires:	libgl1
Requires:	libglu1
Requires:	libgdk_pixbuf2.0_0
Requires:	libgtk-x11_2.0_0
Requires:	liblcms2_2
Requires:	libpango1.0_0
Requires:	libpng16_16
Requires:	libSDL1.2_0
Requires:	libvorbis0
Requires:	libxtst6
ExclusiveArch:	%{ix86}

%description
Launcher for the Valve's Steam software distribution service.

%prep
%setup -q -n %{name}

%build
echo "Nothing to do"

%install
%makeinstall_std

%files
%doc %{_docdir}/*
%{_bindir}/steam*
%{_prefix}/lib/steam/bootstraplinux_ubuntu12_32.tar.xz
%{_datadir}/applications/steam.desktop
%{_datadir}/pixmaps/steam*.png
%{_iconsdir}/hicolor/*/apps/steam.*
%{_mandir}/man6/steam.6.*
