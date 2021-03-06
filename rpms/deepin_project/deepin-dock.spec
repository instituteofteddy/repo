%global project dde-dock
%global repo %{project}

%global _commit a88259093ebcbe8dc0f8517908139ab0ee025476
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-dock
Version:        4.0.8
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Deepin desktop-environment - Dock module
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-dock
Source0:        %{url}/archive/%{_commit}/%{repo}-%{_shortcommit}.tar.gz

BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXtst-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
#Requires:       deepin-daemon
#Requires:       deepin-menu
#Requires:       deepin-qt-dbus-factory
#Requires:       deepin-qt5integration

Provides:       %{repo}%{?_isa} = %{version}-%{release}
Obsoletes:      %{repo}%{?_isa} < %{version}-%{release}

%description
Deepin desktop-environment - Dock module

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}

%prep
%setup -q -n %{repo}-%{_commit}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

%ifarch x86_64
sed -i '/target.path/s|lib|%{_lib}|' plugins/*/*.pro
sed -i 's|lib|%{_lib}|' frame/controller/dockpluginloader.cpp
%endif

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{repo}
%{_libdir}/%{repo}/
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service

%files devel
%{_includedir}/%{repo}/

%changelog
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.8-1.gita882590
- Update to 4.0.8
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.7-1
- Update to version 4.0.7 and renamed to deepin-dock
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.6-1
- Update to version 4.0.6
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build
