Name:		ac3jack
Summary:	Jack audio to ac3 surround converter
Version:	2.0.3
Release:	8

Source0:	http://www.essej.net/ac3jack/%{name}-%{version}.tar.gz
Patch0:		%{name}-2.0.3-mdv-fix-gcc4.4.patch
Patch1:		ac3jack-2.0.3-boost-mt.patch
URL:		http://www.essej.net/ac3jack/
License:	GPLv2+
Group:		Sound
BuildRequires:	jackit-devel
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	ffmpeg-devel
BuildRequires:	aften-static-devel
BuildRequires:	libsigc++1.2-devel
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	wxgtku-devel
BuildRequires:	boost-devel

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
%patch1 -p0 -b .boost
touch AUTHORS ChangeLog

sed -i -e 's/TIME_UTC/TIME_UTC_/g' src/alsa_spdif_writer.cpp src/file_writer.cpp
sed -i '25a\#include "string.h"' src/ringbuffer.hpp

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

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


%changelog
* Sat Mar 31 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.0.3-8
+ Revision: 788432
- Build for boost 1.49
- Don't buildrequire the 32bit version of libsndfile-devel on 64bit

* Thu Jan 19 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0.3-7
+ Revision: 762341
- Rebuild against utf8 wxGTK2.8

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 2.0.3-6
+ Revision: 644447
- rebuild for new boost

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 2.0.3-5mdv2011.0
+ Revision: 572119
- rebuild for new boost

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 2.0.3-4mdv2011.0
+ Revision: 566095
- rebuild for new boost

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 2.0.3-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 2.0.3-2mdv2010.1
+ Revision: 500121
- more fixes for gcc 4.4
- link against boost-mt
- rebuild for new boost

* Sun Nov 08 2009 Jérôme Brenier <incubusss@mandriva.org> 2.0.3-1mdv2010.1
+ Revision: 463219
- update to new version 2.0.3
- BR modified accordingly
- fix build with gcc 4.4 (Patch0)
- drop no more needed ffmpeg includes patch
- add menu entry
- fix license tag

* Mon Oct 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-8mdv2010.0
+ Revision: 454238
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.1.2-4mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 21 2007 Stefan van der Eijk <stefan@mandriva.org> 0.1.2-4mdv2008.0
+ Revision: 54302
- Import ac3jack



* Mon Jun 26 2006 Lenny Cartier <lenny@mandriva.com> 0.1.2-4mdv2007.0
- rebuild

* Fri Mar 31 2006 Austin Acton <austin@mandriva.org> 0.1.2-3mdk
- Rebuild

* Tue Nov 08 2005 Austin Acton <austin@mandriva.org> 0.1.2-2mdk
- Rebuild

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 0.1.2-1mdk
- 0.1.2

* Wed Jan 14 2004 Austin Acton <aacton@yorku.ca> 0.1.1-1mdk
- initial package
