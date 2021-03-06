%define name bladeenc
%define version 0.94.2
%define release 1

Summary: BladeEnc is a free cross-platform MP3 encoder released under the LGPL
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL
Group: Multimedia/Sound
Source: %{name}-%{version}-src-stable.tar.gz
URL: http://bladeenc.mp3.no
BuildRoot: %{_tmppath}/%{name}-buildroot

%description 
BladeEnc was started by Tord Jansson as a project to make a decent, free
encoder for high-bitrate MP3 encoding, heavily based on the ISO source code
for a reference encoder. Since then it has developed into a free software
project (Open Source) with many contributors.

%prep
%setup -q

%configure

%build

%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%attr(0755,root,root) %{_bindir}/bladeenc
%doc  AUTHORS COPYING ChangeLog README bladeenc.html

%changelog
* Fri Jan 26 2001 Jean Robertson <jean@cc.mcgill.ca>
- first spec file 


 
