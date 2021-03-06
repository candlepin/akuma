%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: akuma
Summary: akuma daemonizer
Group: Internet/Applications
License: MIT
Version: 1.7
Release: 3%{?dist}
URL: http://java.net/projects/akuma
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: x86_64 i686

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: jna
Requires: java >= 0:1.6.0
#Requires: bouncycastle
%define __jar_repack %{nil}

%description
akuma

%prep
%setup -q

%build
ant -Dlibdir=/usr/share/java clean package

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT/usr/share/java/
install -m 644 dist/lib/akuma.jar $RPM_BUILD_ROOT/usr/share/java/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/java/akuma.jar


%changelog
* Mon Mar 26 2012 Chris Duryee (beav) <cduryee@redhat.com>
- use x86_64 and i686 (cduryee@redhat.com)

* Wed Mar 21 2012 Chris Duryee (beav) <cduryee@redhat.com>
- use x86_64 for now, and remove version from jar filename (cduryee@redhat.com)

* Mon Feb 27 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Mon Feb 27 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Mon Feb 27 2012 Chris Duryee <cduryee@redhat.com> 1.7
- initial setup
