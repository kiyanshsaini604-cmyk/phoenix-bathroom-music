Name:           phoenix-device
Version:        0.1.0
Release:        1%{?dist}
Summary:        Phoenix bathroom voice music device firmware and system services

License:        MIT
URL:            https://github.com/kiyanshsaini604-cmyk/phoenix-bathroom-music
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
Requires:       python3
Requires:       python3-vosk
Requires:       python3-requests
Requires:       python3-numpy
Requires:       python3-pillow

%description
Phoenix is a dedicated bathroom voice music device. This package contains
the device-side firmware, service modules, configuration helpers, and
tests for the Phoenix project.

The device acts as a Subsonic-compatible client for a self-hosted music
server and uses a local-first voice pipeline for wake-word and
speech-recognition handling.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{python3_sitelib}/phoenix
%{python3_sitelib}/phoenix-*.egg-info

%changelog
* Mon Mar 21 2026 Builder <builder@example.com> - 0.1.0-1
- Initial package
