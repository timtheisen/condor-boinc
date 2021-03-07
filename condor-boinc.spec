Name:		condor-boinc
Version:	7.16.16
Release:	1%{?dist}
Summary:	HTCondor BOINC GAHP

License:	LGPLv3+
URL:		https://boinc.berkeley.edu/

# git archive --output condor-boinc_7.16.16.orig.tar.gz --prefix condor-boinc-7.16.16/ client_release/7.16/7.16.16
Source0:	condor-boinc_7.16.16.orig.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	libcurl-devel
BuildRequires:	make
BuildRequires:	m4
BuildRequires:	libtool

%description
The BOINC GAHP for HTCondor

%prep
%setup -n condor-boinc-7.16.16


%build
./_autosetup && ./configure --disable-server --disable-client --disable-manager
make svn_version.h && cd lib && make && cd ../samples/condor && make


%install
mkdir -p %{buildroot}/usr/sbin
cp -p samples/condor/boinc_gahp %{buildroot}/usr/sbin


%files
%doc
/usr/sbin/boinc_gahp


%changelog
* Mon Feb 22 2021 Tim Theisen <tim@cs.wisc.edu> - 7.16.16-1
- Update to upstream version 7.16.16

* Tue Sep 22 2020 Tim Theisen <tim@cs.wisc.edu> - 7.16.11-1
- Initial version

