%define debug_package %{nil}

Summary:	Steam Linux Client
Name:		steam
Version:	1.0.0.52
Release:	3
Group:		Games/Other
License:	Proprietary
URL:		https://github.com/ValveSoftware/steam-for-linux
Source0:	http://repo.steampowered.com/steam/pool/steam/s/steam/%{name}_%{version}.tar.gz
Patch0:		steam-use-our-own-libraries.patch
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
Requires:	xz
Requires:	zenity
# Libraries
Requires:	libcurl4
Requires:	libdbus-glib-1_2
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
Requires:	libstdc++6
Requires:	libvorbis0
Requires:	libxtst6
Requires:	libdri-drivers
# Add some restricted package to Suggests
Suggests:	libtxc-dxtn
ExclusiveArch:	%{ix86}

%description
Launcher for the Valve's Steam software distribution service.

%prep
%setup -q -n %{name}
%apply_patches

%build
echo "Nothing to do"

%install
%makeinstall_std

# Rename steamdeps, it's not working on non-Debian based distros
mv -f %{buildroot}%{_bindir}/steamdeps %{buildroot}%{_bindir}/steamdeps.save
install -D -m644 lib/udev/rules.d/99-steam-controller-perms.rules %{buildroot}%{_udevrulesdir}/99-steam-controller-perms.rules

%files
%doc %{_docdir}/*
%{_bindir}/steam*
%{_prefix}/lib/steam/bootstraplinux_ubuntu12_32.tar.xz
%{_datadir}/applications/steam.desktop
%{_datadir}/pixmaps/steam*.png
%{_iconsdir}/hicolor/*/apps/steam.*
%{_mandir}/man6/steam.6.*
%{_udevrulesdir}/99-steam-controller-perms.rules
