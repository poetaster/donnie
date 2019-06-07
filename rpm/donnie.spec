# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       donnie

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libixml|libthreadutil|libupnp|libupnpp.*$
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    UPnP Controller with built in Player
Version:    0.8
Release:    1
Group:      Applications/Multimedia
License:    MIT
URL:        https://github.com/wdehoog/donnie
Source0:    %{name}-%{version}.tar.gz
Source1:    %{name}-rpmlintrc
Source100:  donnie.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   mpris-qt5
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  libupnpp >= 0.15.1
BuildRequires:  mpris-qt5-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils

%description
UPnP control point and player for Sailfish OS


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/translations
# >> files
%changelog
* Fri Jun 7 2019 Willem-Jan de Hoog <wdehoog@exalondelft.nl> 0.8
- Translations update (de,es,ru)

* Fri Oct 20 2017 Willem-Jan de Hoog <wdehoog@exalondelft.nl> 0.7
- Translatable, added Spanish translation
- Option to resume
- Many Fixes
- Include required shared libraries in package

* Fri Oct 6 2017 Willem-Jan de Hoog <wdehoog@exalondelft.nl> 0.6
- Browse, Search, Play local and Play in Remote Renderer

* Thu Apr 13 2017 Willem-Jan de Hoog <wdehoog@exalondelft.nl> 0.0.1
- initial upload
# << files
