%define upstream_name    Class-Accessor-Constructor
%define upstream_version 1.100880

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Support for an automated dirty flag in
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::Accessor::Complex)
BuildRequires: perl(Class::Accessor::Installer)
BuildRequires: perl(Data::Inherited)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module generates accessors for your class in the same spirit as the
Class::Accessor manpage does. While the latter deals with accessors for
scalar values, this module provides accessor makers for rather flexible
constructors.

The accessor generators also generate documentation ready to be used with
the Pod::Generated manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


