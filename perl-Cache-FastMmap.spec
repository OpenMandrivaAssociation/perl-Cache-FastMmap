%define upstream_name    Cache-FastMmap
%define upstream_version 1.40

%define Werror_cflags %nil

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.40
Release:	1

Summary:	Uses an mmap'ed file to act as a shared memory interprocess cache
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Cache/Cache-FastMmap-1.40.tar.gz

BuildRequires:	perl(Storable)
BuildRequires:	perl-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
A shared memory cache through an mmap'ed file. It's core is written in C for
performance. It uses fcntl locking to ensure multiple processes can safely
access the cache at the same time. It uses a basic LRU algorithm to keep the
most used entries in the cache.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%perl_vendorarch/Cache
%perl_vendorarch/auto/Cache
%_mandir/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.360.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.360.0-2
+ Revision: 680710
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.360.0-1mdv2011.0
+ Revision: 595077
- update to new version 1.36

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.350.0-2mdv2011.0
+ Revision: 555689
- rebuild

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.350.0-1mdv2010.1
+ Revision: 510073
- update to 1.35

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.340.0-1mdv2010.0
+ Revision: 406256
- rebuild using %%perl_convert_version

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.34-1mdv2010.0
+ Revision: 387752
- update to new version 1.34

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2010.0
+ Revision: 373788
- update to new version 1.30

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2010.0
+ Revision: 371454
- new version

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.28-1mdv2009.0
+ Revision: 230268
- update to new version 1.28

* Thu Jun 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2009.0
+ Revision: 226194
- update to new version 1.27

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2009.0
+ Revision: 210846
- update to new version 1.26

* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2008.1
+ Revision: 162584
- update to new version 1.25

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.24-2mdv2008.1
+ Revision: 151356
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2008.1
+ Revision: 104512
- update to new version 1.24

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 1.23-1mdv2008.1
+ Revision: 101002
- update to new version 1.23

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2008.0
+ Revision: 98021
- update to new version 1.20
- update to new version 1.20

* Tue Aug 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2008.0
+ Revision: 72789
- update to new version 1.19

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2008.0
+ Revision: 46335
- update to new version 1.16


* Wed Feb 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-4mdv2007.0
+ Revision: 127228
- new version

* Wed Aug 09 2006 Scott Karns <scottk@mandriva.org> 1.09-4mdv2007.0
+ Revision: 54278
- Rebuild, spec file cleanup
- import perl-Cache-FastMmap-1.09-3mdk

* Sat May 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.09-3mdk
- Fix BuildRequires: perl-devel is needed

* Fri May 05 2006 Scott Karns <scottk@mandriva.org> 1.09-2mdk
- Fix BuildRequires
- Adjust Source URL to comply with Mandriva perl packaging policy

* Thu Jan 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.09-1mdk
- Initial MDV RPM


