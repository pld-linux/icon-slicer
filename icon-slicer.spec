Summary:	Utility for icon theme generation
Name:		icon-slicer
Version:	0.3
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	5c5374d4f265b0abe4daef1d03f87104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildPrereq:	gtk+2-devel
BuildPrereq:	popt

%description
icon-slicer is a utility for generating icon themes and libXcursor
cursor themes.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/icon-slicer
