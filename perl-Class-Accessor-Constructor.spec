%define upstream_name    Class-Accessor-Constructor
%define upstream_version 1.111590

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Support for an automated dirty flag in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Accessor::Complex)
BuildRequires:	perl(Class::Accessor::Installer)
BuildRequires:	perl(Data::Inherited)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.590-1mdv2011.0
+ Revision: 684738
- update to new version 1.111590

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.100.880-2
+ Revision: 654891
- rebuild for updated spec-helper

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.880-1mdv2011.0
+ Revision: 530232
- update to 1.100880

* Wed Mar 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.830-1mdv2010.1
+ Revision: 527172
- update to 1.100830

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 474739
- update to 0.08

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 444083
- import perl-Class-Accessor-Constructor


* Thu Sep 17 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist
