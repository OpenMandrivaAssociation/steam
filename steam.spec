%define debug_package %{nil}

Summary:	Steam Linux Client
Name:		steam
Version:	1.0.0.61
Release:	1
Group:		Games/Other
License:	Proprietary
URL:		https://github.com/ValveSoftware/steam-for-linux
Source0:	http://repo.steampowered.com/steam/pool/steam/s/steam/%{name}_%{version}.tar.gz

# Input devices seen as joysticks:
Source8:	https://raw.githubusercontent.com/denilsonsa/udev-joystick-blacklist/master/after_kernel_4_9/51-these-are-not-joysticks-rm.rules
# First generation Nvidia Shield controller seen as mouse:
Source9:	https://raw.githubusercontent.com/cyndis/shield-controller-config/master/99-shield-controller.rules

Patch0:		steam-use-our-own-libraries.patch
# Make Steam Controller usable as a GamePad:
# https://steamcommunity.com/app/353370/discussions/0/490123197956024380/
Patch1:		%{name}-controller-gamepad-emulation.patch

Requires:	alsa-lib
Requires:	awk
Requires:	coreutils
Requires:	diffutils
Requires:	curl >= 7.63.0
# (tpg) see https://github.com/ValveSoftware/csgo-osx-linux/issues/1925
# failed to dlopen engine_client.so error=/usr/lib64/libldap_r-2.4.so.2: version `OPENLDAP_2.4_2' not found
Requires:	%{_lib}ldap2.4_2 >= 2.4.46-4
Requires:	dbus
Requires:	desktop-file-utils
Requires:	fonts-ttf-liberation
Requires:	gdk-pixbuf2.0
Requires:	gtk+2.0
Requires:	gnutar
Requires:	hicolor-icon-theme
Requires:	nss
Requires:	openal
Requires:	pulseaudio
Requires:	xterm
Requires:	xz
Requires:	zenity
# Libraries
Requires:	libcurl4 >= 7.63.0
# https://github.com/ValveSoftware/steam-for-linux/issues/4795
Requires:	libdbusmenu-gtk2_4
Requires:	libdbus-glib-1_2
Requires:	libfreetype6
Requires:	libgconf2_4
Requires:	libgcrypt20
Requires:	libgl1
Requires:	libglu1
Requires:	libgdk_pixbuf2.0_0
Requires:	libgtk-x11_2.0_0
Requires:	liblcms2_2
Requires:	libpango1.0_0
Requires:	libpng16_16
Requires:	libpulseaudio0
Requires:	libSDL1.2_0
Requires:	libstdc++6
Requires:	libvorbis0
Requires:	libxtst6
Requires:	libdri-drivers
Requires:	libopenal1
Requires:	libsm6
Requires:	libice6
Requires:	libxcb-dri2_0
Requires:	libxcb-glx0
Requires:	libva1
Requires:	libvdpau1
ExclusiveArch:	%{x86_64}

%description
Launcher for the Valve's Steam software distribution service.

%prep
%autosetup -n %{name} -p1

%build
# Strip out broken outdated crap from the bootstrap environment
# and make the launcher script use gtar (--checkpoint=1 is a gtar
# specific option)
mkdir TMP
cd TMP
tar xf ../bootstraplinux_ubuntu12_32.tar.xz
sed -i -e 's,tar --blocking,gtar --blocking,g' steam.sh
rm -rf	ubuntu12_32/steam-runtime/i386/lib/i386-linux-gnu/libgcc_s* \
	ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu/lib*
tar cf ../bootstraplinux_ubuntu12_32.tar *
cd ..
xz -f bootstraplinux_ubuntu12_32.tar
rm -rf TMP

%install
%make_install

# Rename steamdeps, it's not working on non-Debian based distros
mv -f %{buildroot}%{_bindir}/steamdeps %{buildroot}%{_bindir}/steamdeps.save
install -D -m644 lib/udev/rules.d/60-steam-input.rules %{buildroot}%{_udevrulesdir}/60-steam-input.rules

install -m 644 -p lib/udev/rules.d/* \
    %{SOURCE8} %{SOURCE9} %{buildroot}%{_udevrulesdir}/

%files
%doc %{_docdir}/*
%{_bindir}/steam*
%{_prefix}/lib/steam/bootstraplinux_ubuntu12_32.tar.xz
%{_datadir}/applications/steam.desktop
%{_datadir}/pixmaps/steam*.png
%{_iconsdir}/hicolor/*/apps/steam.*
%{_mandir}/man6/steam.6.*
%{_udevrulesdir}/*.rules
