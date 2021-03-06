%global project go-lib
%global repo %{project}

%global _commit 44767e8c5463469d5fe09f7860db17fd2dfbdf9b
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-%{repo}
Version:        0.5.3
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Go bindings for Deepin Desktop Environment development

Group:          Development/Libraries
License:        GPLv3
URL:            https://github.com/linuxdeepin/go-lib
Source0:        %{url}/archive/%{_commit}/%{repo}-%{_shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  golang

%description
DLib is a set of Go bindings/libraries for DDE development.
Containing dbus (forking from guelfey), glib, gdkpixbuf, pulse and more.

%prep
%setup -q -n %{repo}-%{_commit}

%build

%install
install -d %{buildroot}%{gopath}/src/pkg.deepin.io/lib/
cp -r * %{buildroot}%{gopath}/src/pkg.deepin.io/lib/
rm -rf %{buildroot}%{gopath}/src/pkg.deepin.io/lib/debian

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{gopath}/src/pkg.deepin.io/lib/

%changelog
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.5.3-1.git44767e8
- Update to 0.5.3
* Sun Jul 12 2015 mosquito <sensor.wen@gmail.com> - 0.3.0-1.git98ac007
- Update to 0.3.0-1.git98ac007
* Mon Sep 29 2014 mosquito <sensor.wen@gmail.com> - 0.0.4git20140928-1
- Initial build
