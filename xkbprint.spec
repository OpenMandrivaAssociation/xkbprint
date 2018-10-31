Name:		xkbprint
Version:	1.0.4
Release:	5
Summary:	Print an XKB keyboard description
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xkbfile) >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xkbprint comman generates a printable or encapsulated PostScript
description of the XKB keyboard description specified by a file. 

%prep
%setup -q -n %{name}-%{version}

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xkbprint
%{_mandir}/man1/xkbprint.1*
