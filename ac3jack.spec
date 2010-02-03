%define name	ac3jack
%define version	2.0.3
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Jack audio to ac3 surround converter
Version: 	%{version}
Release: 	%{release}

Source0:	http://www.essej.net/ac3jack/%{name}-%{version}.tar.gz
Patch0:		%{name}-2.0.3-mdv-fix-gcc4.4.patch
URL:		http://www.essej.net/ac3jack/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	jackit-devel
BuildRequires:	libsndfile-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	aften-static-devel
BuildRequires:	libsigc++1.2-devel
BuildRequires:	liblo-devel
BuildRequires:	libxml2-devel
BuildRequires:	libwxgtk-devel
BuildRequires:	libboost-devel

%description
ac3jack is a tool for creating an AC-3 (Dolby Digital) multichannel stream
from its JACK input ports. Using this tool, an AC-3 stream (up to 5.1
channels) is created in real time and either written to a file or streamed to
standard output.

When streamed to stdout and piped through the ALSA tool ac3dec -C, the AC-3
stream can be passed out the SPDIF port on your audio interface for connection
to a multichannel surround receiver. In this way, you can achieve full 5.1
surround mixing and monitoring of your JACK applications with a single digital
cable, and no need for hardware supporting discrete outputs and inputs.

AC-3 is a compressed audio stream, so quality will suffer somewhat, but it is
the price you pay for easy surround sound. After all, if it is good enough for
DVD and film soundtracks, it must be OK.

%prep
%setup -q
%patch0 -p1 -b .gcc44

%build
%configure
%make
										
%install
rm -rf %{buildroot}
%makeinstall

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Ac3jack
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=
Terminal=false
Type=Application
Categories=Audio;X-MandrivaLinux-Sound;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
