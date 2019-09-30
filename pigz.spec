Name:		pigz
Version:	2.4
Release:	5
Summary:	A parallel implementation of gzip which utilizes multiple cores
License:	Zlib
URL:		http://www.zlib.net/pigz/
Source0:	http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	ncompress zlib-devel gcc

%description
Pigz, which stands for parallel implementation of gzip, is a fully functional
replacement for gzip that exploits multiple processors and multiple cores to
the hilt when compressing data.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build CFLAGS="%{optflags}"

%install
install -p -D pigz %{buildroot}%{_bindir}/pigz
pushd %{buildroot}%{_bindir}
ln pigz unpigz
popd
install -p -D pigz.1 %{buildroot}%{_mandir}/man1/pigz.1

%check
make test

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*pigz

%files help
%{_mandir}/man1/pigz.1*

%changelog
* Tue Sep 24 2019 shenyangyang<shenyangyang4@huawei.com> - 2.4-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add help package

* Fri Aug 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.4-4
- Package init
