#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Random-ISAAC
Summary:	Math::Random::ISAAC - Perl interface to the ISAAC PRNG algorithm
#Summary(pl.UTF-8):	
Name:		perl-Math-Random-ISAAC
Version:	1.004
Release:	1
License:	unrestricted
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46110b9a7bb96fe641bdfaf35bdafec5
URL:		http://search.cpan.org/dist/Math-Random-ISAAC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-NoWarnings >= 0.084
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As with other Pseudo-Random Number Generator (PRNG) algorithms like the
Mersenne Twister (see Math::Random::MT), this algorithm is designed to
take some seed information and produce seemingly random results as output.

However, ISAAC (Indirection, Shift, Accumulate, Add, and Count) has different
goals than these commonly used algorithms. In particular, it's really fast -
on average, it requires only 18.75 machine cycles to generate a 32-bit value.
This makes it suitable for applications where a significant amount of random
data needs to be produced quickly, such solving using the Monte Carlo method
or for games.

The results are uniformly distributed, unbiased, and unpredictable unless
you know the seed. The algorithm was published by Bob Jenkins in the late
90s and despite the best efforts of many security researchers, no feasible
attacks have been found to date.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Random/*.pm
%{perl_vendorlib}/Math/Random/ISAAC
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
