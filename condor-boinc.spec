Name:		condor-boinc
Version:	7.16.11
Release:	1%{?dist}
Summary:	HTCondor BOINC GAHP

License:	LGPLv3+
URL:		https://boinc.berkeley.edu/

# git archive --output boinc-client_release-7.16-7.16.11.tar.gz --prefix client_release-7.16-7.16.11/ client_release/7.16/7.16.11
Source0:	boinc-client_release-7.16-7.16.11.tar.gz

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
%setup -n client_release-7.16-7.16.11


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
* Tue Sep 22 2020 Tim Theisen <tim@cs.wisc.edu> - 7.16.11-1
- Initial version

