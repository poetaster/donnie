#
# spec file for package libupnp
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011, Sascha Peilicke <saschpe@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
# tralala


%define lname libupnp6

Name:           libupnp
Version:        1.6.21
Release:        0
Summary:        Portable Universal Plug and Play (UPnP) SDK
License:        BSD-3-Clause
Group:          System/Libraries
Url:            https://sourceforge.net/projects/pupnp/
Source0:        https://downloads.sourceforge.net/pupnp/libupnp-%{version}.tar.bz2
Source42:       baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libtool
BuildRequires:  pkgconfig
#Patch:          libupnp-configure.patch

%description
The portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%package -n %lname 
Summary:        Portable Universal Plug and Play (UPnP) SDK
Group:          System/Libraries

%description -n %lname
The portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems

%package -n libupnp-devel
Summary:        Portable Universal Plug and Play (UPnP) SDK
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description -n libupnp-devel
The portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%prep
%setup -q
#%patch
%build
autoreconf -fiv
%configure --disable-samples --enable-ipv6 --disable-static
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -type f -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig -n %lname

%postun -p /sbin/ldconfig -n %lname

%files -n %lname
%defattr(-,root,root,-)
%doc ChangeLog NEWS README TODO
%{_libdir}/libixml.so.*
%{_libdir}/libthreadutil.so.*
%{_libdir}/libupnp.so.*

%files -n libupnp-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libupnp.pc
%{_libdir}/libixml.so
%{_libdir}/libthreadutil.so
%{_libdir}/libupnp.so
%{_includedir}/upnp/

%changelog
