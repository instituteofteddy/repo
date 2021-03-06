%global project dde-calendar
%global repo %{project}

%global _commit d7e42a121b4b056f5c030fecbc601f4e0efb65be
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-calendar
Version:        1.0.3
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Calendar for Deepin Desktop Environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        %{url}/archive/%{_commit}/%{repo}-%{_shortcommit}.tar.gz

BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  deepin-tool-kit-devel
Provides:       %{repo}%{?_isa} = %{version}-%{release}

%description
Calendar for Deepin Desktop Environment

%prep
%setup -q -n %{repo}-%{_commit}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{repo}
%{_datadir}/%{repo}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.0.3-1.gitd7e42a1
- Update to 1.0.3
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.3-1
- Update to version 1.0.3
* Fri Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.2-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.2-1
- Initial package build
