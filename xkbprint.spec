Name:		xkbprint
Version:	1.0.6
Release:	2
Summary:	Print an XKB keyboard description
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile) >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
The xkbprint comman generates a printable or encapsulated PostScript
description of the XKB keyboard description specified by a file. 

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xkbprint
%doc %{_mandir}/man1/xkbprint.1*
