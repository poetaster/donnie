Summary:       Library for interfacing Music Player Daemon
Name:          libmpdclient
Version:       2.11
Release:       6%{?dist}
License:       BSD
URL:           http://www.musicpd.org/
Group:         System Environment/Libraries
Source0:       http://www.musicpd.org/download/libmpdclient/2/libmpdclient-%{version}.tar.xz
#Source1:       http://www.musicpd.org/download/libmpdclient/2/libmpdclient-%{version}.tar.xz.sig

# tralala

BuildRequires: doxygen

%package devel
Summary: Header files for developing programs with %{name}
Requires: %{name} = %{version}-%{release}
Group: Development/Libraries

%description
A stable, documented, asynchronous API library for interfacing MPD
in the C, C++ & Objective C languages.

%description devel
%{name}-devel is a sub-package which contains header files and
libraries for developing programs with %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__sed} -i -e "s,doc/api/html/\*.gif,,g" Makefile
%{__make} DESTDIR="$RPM_BUILD_ROOT" install
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name} _doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README NEWS
%{_libdir}/libmpdclient.so.2*

%files devel
%doc _doc/html
%{_datadir}/vala/vapi/libmpdclient.vapi
%{_libdir}/libmpdclient.so
%{_libdir}/pkgconfig/libmpdclient.pc
%{_includedir}/mpd/

%changelog
* Thu Mar 21 2017 wdehoog
- copied spec file from fedora project
