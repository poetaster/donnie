Summary:        C++ wrapper for libupnp
Name:           libupnpp
Version:        0.15.2
Release:        0
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.lesbonscomptes.com/updmpdcli
Source0:        https://github.com/poetaster/donnie/raw/master/lib/libupnpp/libupnpp-0.15.2.tar.gz
Requires(pre):  shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires:  libupnp-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  expat-devel
BuildRequires:  libcurl-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
#BuildRequires:  systemd-units
BuildRoot:      %{_tmppath}/%{name}-build
Patch0:			compiler-flags.patch
Patch1:			increase-logging-level.patch
Patch2:			extra-debug-output.patch
Patch3:         include-functional.patch

%description
libupnpp is a C++ wrapper over libupnp. It exists mostly for supporting
upmpdcli and upplay

%prep
%setup -q
%patch0
# %patch1
# %patch2
%patch3

%build
./autogen.sh
CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot} STRIP=/bin/true INSTALL='install -p'
%{__rm} -f %{buildroot}%{_libdir}/libupnpp.a
%{__rm} -f %{buildroot}%{_libdir}/libupnpp.la

%post -p /sbin/ldconfig 

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_includedir}/libupnpp
%{_libdir}/libupnpp.so*
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri May 19 2017 J.F. Dockes <jf@dockes.org> - 0.15.2
- Linn Receiver issue
* Sun Oct 09 2016 J.F. Dockes <jf@dockes.org> - 0.15.1
- Added pkgconfig data
* Sun Sep 11 2016 J.F. Dockes <jf@dockes.org> - 0.15.0
- Add code to support embedded device. Small interface changes.
* Sun Feb 07 2016 J.F. Dockes <jf@dockes.org> - 0.14.1
- Fix bug leading to possible upmpdcli crash when radio service failed to
  init (e.g.: because of no python2)
* Fri Feb 05 2016 J.F. Dockes <jf@dockes.org> - 0.14.0
- No systematic broadcasting of state info
* Wed Dec 22 2015 J.F. Dockes <jf@dockes.org> - 0.13.1
- Help managing upmpdcli in SenderReceiver mode
* Mon Dec 14 2015 J.F. Dockes <jf@dockes.org> - 0.13.0
- Support more OpenHome services (Sender, Radio, Info). Songcast utils.
* Mon Aug 17 2015 J.F. Dockes <jf@dockes.org> - 0.12.1
- Make it easier to create pure openhome devices
* Tue May 05 2015 J.F. Dockes <jf@dockes.org> - 0.11.0
- Control side interface to the OpenHome receiver service
- API cleanups for a more stable ABI
- More complete implementation of OpenHome services to support pure
  OpenHome devices
* Sun Oct 12 2014 J.F. Dockes <jf@dockes.org> - 0.8.4
- Separation from upmpdcli
