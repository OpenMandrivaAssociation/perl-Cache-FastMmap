%define module  Cache-FastMmap
%define name	perl-%{module}
%define	modprefix Cache

%define version	1.25
%define release	%mkrel 1

Summary:	Uses an mmap'ed file to act as a shared memory interprocess cache
Name:		%name
Version:	%version
Release:	%release
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Storable)
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
A shared memory cache through an mmap'ed file. It's core is written in C for
performance. It uses fcntl locking to ensure multiple processes can safely
access the cache at the same time. It uses a basic LRU algorithm to keep the
most used entries in the cache.

%prep
%setup -q -n %{module}-%version

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %buildroot
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%perl_vendorarch/%{modprefix}
%perl_vendorarch/auto/%{modprefix}
%_mandir/*/*

%clean
rm -rf %buildroot



