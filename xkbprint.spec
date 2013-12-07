Name:		xkbprint
Version:	1.0.3
Release:	5
Summary:	Print an XKB keyboard description
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
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
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xkbprint
%{_mandir}/man1/xkbprint.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 671329
- mass rebuild

* Mon Jan 10 2011 Thierry Vignaud <tv@mandriva.org> 1.0.3-1
+ Revision: 630845
- new release

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 608216
- rebuild

* Thu Nov 26 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 470365
- New version: 1.0.2

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 351038
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 226048
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154453
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 76532
- rebuild for 2008
- add a description
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

