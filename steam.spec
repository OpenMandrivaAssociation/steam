Summary:	Steam Linux Client
Name:		steam
Version:	1.0.0.45
Release:	4
Group:		Games/Other
License:	Proprietary
URL:		https://github.com/ValveSoftware/steam-for-linux
Source0:	http://repo.steampowered.com/steam/pool/steam/s/steam/%{name}_%{version}.tar.gz
Requires:	zenity
Requires:	libgl1
Requires:	curl
BuildArch:	noarch

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
