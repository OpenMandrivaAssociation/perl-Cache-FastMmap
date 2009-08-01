%define upstream_name    Cache-FastMmap
%define upstream_version 1.34

%define Werror_cflags %nil

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Uses an mmap'ed file to act as a shared memory interprocess cache
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Storable)
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
%{__make} OPTIMIZE="%{optflags}"

%check
%{__make} test

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
