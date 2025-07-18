Summary:	Utility for icon theme generation
Summary(pl.UTF-8):	Narzędzie do generowania motywów ikon
Name:		icon-slicer
Version:	0.3
Release:	3
License:	MIT
Group:		Development/Tools
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	5c5374d4f265b0abe4daef1d03f87104
Patch0:		%{name}-0.3-attachpoints.patch
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
icon-slicer is a utility for generating icon themes and libXcursor
cursor themes.

%description -l pl.UTF-8
icon-slicer to narzędzie do generowania motywów ikon oraz motywów
kursorów libXcursor.

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/icon-slicer
