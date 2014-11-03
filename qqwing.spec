#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Command-line Sudoku solver and generator
Name:		qqwing
Version:	1.3.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://qqwing.com/%{name}-%{version}.tar.gz
# Source0-md5:	2d5541e89b82202c63ef18e49d99aa52
URL:		http://qqwing.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QQwing is a command-line Sudoku solver and generator.

%package libs
Summary:	Library for Sudoku solving and generation
Group:		Libraries

%description libs
libqqwing is a C++ library for solving and generating Sudoku puzzles.

%package devel
Summary:	Header files for qqwing library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki qqwing
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for qqwing library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki qqwing.

%package static
Summary:	Static qqwing library
Summary(pl.UTF-8):	Statyczna biblioteka qqwing
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static qqwing library.

%description static -l pl.UTF-8
Statyczna biblioteka qqwing.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/qqwing
%{_mandir}/man1/qqwing.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqqwing.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqqwing.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqqwing.so
%{_includedir}/qqwing.hpp
%{_pkgconfigdir}/qqwing.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libqqwing.a
%endif
