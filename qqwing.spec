#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Command-line Sudoku solver and generator
Summary(pl.UTF-8):	Uruchamiany z linii poleceń program do rozwiązywania i generowania Sudoku
Name:		qqwing
Version:	1.3.4
Release:	2
License:	GPL v2+
Group:		Applications/Games
#Source0Download: http://qqwing.com/download.html
Source0:	http://qqwing.com/%{name}-%{version}.tar.gz
# Source0-md5:	249dcfa8a1ca2d5cec5a81bcdbd017eb
URL:		http://qqwing.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QQwing is a command-line Sudoku puzzles solver and generator.

%description -l pl.UTF-8
QQwing to uruchamiany z linii poleceń program do rozwiązywania i
generowania łamigłówek Sudoku.

%package libs
Summary:	Library for Sudoku solving and generation
Summary(pl.UTF-8):	Biblioteka do rozwiązywania i generowania Sudoku
Group:		Libraries

%description libs
libqqwing is a C++ library for solving and generating Sudoku puzzles.

%description libs -l pl.UTF-8
libqqwing to biblioteka C++ do rozwiązywania i generowania łamigłówek
Sudoku.

%package devel
Summary:	Header files for qqwing library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki qqwing
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel

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

%post	libs -p /sbin/ldconfig
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
