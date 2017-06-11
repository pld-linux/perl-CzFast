#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	CzFast
Summary:	CzFast - Perl module for Czech charsets manipulation
Summary(pl.UTF-8):	CzFast - moduł Perla do manipulacji czeskimi zestawami znaków
Name:		perl-CzFast
Version:	0.10
Release:	13
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TR/TRIPIE/%{pnam}-%{version}.tar.gz
# Source0-md5:	03f8221f66f181f8c08c121c4707e2d9
Source1:	%{pnam}.3pm
URL:		http://search.cpan.org/dist/CzFast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CzFast is a Perl module for Czech charsets manipulation. It uses
character tables created by Jaromir Dolecek for the Csacek project
(http://www.csacek.cz/).

%description -l pl.UTF-8
CzFast jest modułem Perla do manipulacji czeskimi zestawami znaków.
Korzysta on z tablic przekodowań utworzonych przez Jaromira Dolecka
na potrzeby projektu Csacek (http://www.csacek.cz/).

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/cs/man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_mandir}/man3/CzFast.3pm* $RPM_BUILD_ROOT%{_mandir}/cs/man3
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/CzFast.pm
%dir %{perl_vendorarch}/auto/CzFast
%attr(755,root,root) %{perl_vendorarch}/auto/CzFast/CzFast.so
%{_mandir}/man3/*
%lang(cs) %{_mandir}/cs/man3/*
