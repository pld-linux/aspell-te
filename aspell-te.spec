Summary:	Telugu dictionary for aspell
Summary(pl.UTF-8):	Słownik telugu dla aspella
Name:		aspell-te
Version:	0.01
%define	subv	2
Release:	3
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/te/aspell6-te-%{version}-%{subv}.tar.bz2
# Source0-md5:	645f7f7204520552cddbe1c9ae64df2a
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telugu dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik telugu (lista słów) dla aspella.

%prep
%setup -q -n aspell6-te-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
