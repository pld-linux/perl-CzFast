#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pnam	CzFast
Summary:	CzFast - Perl module for Czech charsets manipulation
Summary(pl):	CzFast - modu³ Perla do manipulacji czeskimi zestawami znaków
Name:		perl-CzFast
Version:	0.10
Release:	3
License:	GPL 1+ / Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/T/TR/TRIPIE/%{pnam}-%{version}.tar.gz
Source1:	%{pnam}.3pm
URL:		http://www.cpan.org/authors/id/T/TR/TRIPIE/%{pnam}-%{version}.readme
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CzFast is a Perl module for Czech charsets manipulation. It uses
character tables created by Jaromir Dolecek for the Csacek project
(http://www.csacek.cz).

%description -l pl
CzFast jest modu³em Perla do manipulacji czeskimi zestawami znaków.
Korzysta on z tablic przekodowañ utworzonych przez Jaromira Dolecka
na potrzeby projektu Csacek (http://www.csacek.cz).

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

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
%{perl_vendorarch}/auto/CzFast/CzFast.bs
%attr(755,root,root) %{perl_vendorarch}/auto/CzFast/CzFast.so
%{_mandir}/man3/*
%lang(cs) %{_mandir}/cs/man3/*
