%define name	ac3jack
%define version	0.1.2
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	Jack audio to ac3 surround converter
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://essej.net/ac3jack/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig
BuildRequires:	ffmpeg-devel jackit-devel
BuildRequires:	libsndfile-devel

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

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{_bindir}/%name
%{_mandir}/man1/*
