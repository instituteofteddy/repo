%global _commit 20e36728822c43fb9a2abb1012770426c9e13959
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-tool-kit
Version:        0.2.1
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Base development tool of all C++/Qt Developer work on Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-tool-kit
Source0:        %{url}/archive/%{_commit}/%{name}-%{_shortcommit}.tar.gz

BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libXrender-devel
BuildRequires:  startup-notification-devel
BuildRequires:  xcb-util-devel

%description
Base development tool of all C++/Qt Developer work on Deepin

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}

%prep
%setup -q -n %{name}-%{_commit}
sed -i 's|lrelease|lrelease-qt5|g' tool/translate_generation.sh
sed -i -E '/test|examples/d' dtk.pro

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%files
%doc README.md Specification.md
%{_libdir}/lib*.so.*
%{_datadir}/dtkwidget/translations/*.qm

%files devel
%{_includedir}/libdtk-1.0/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1.git20e3672
- Update to 0.2.1
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.1-1
- Updated package to 0.2.1
* Thu Jan 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.0-2
- Split the package to main and devel
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.0-1
- Updated package to 1.7
* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.7-1
- Updated package to 1.7
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.6-1
- Initial package build
