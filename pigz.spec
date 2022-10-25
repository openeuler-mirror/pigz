#spec from source code(%{name}-%{version}.tar.gz)
Name:     pigz
Version:  2.6
Release:  2
Summary:  pigz is a parallel implementation of gzip which utilizes multiple cores
License:  zlib
Source0:  http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
URL:      http://www.zlib.net/pigz

BuildRequires: zlib-devel gcc

%description
pigz, which stands for parallel implementation of gzip, is a fully functional replacement for gzip that
exploits multiple processors and multiple cores to the hilt when compressing data. pigz was written by
Mark Adler, and uses the zlib and pthread libraries.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build CFLAGS="%{optflags}"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mv pigz unpigz ${RPM_BUILD_ROOT}%{_bindir}
mv pigz.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

%check
make test

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*pigz

%files help
%{_mandir}/man1/pigz.1*

%changelog
* Tue Oct 25 2022 yanglongkang<yanglongkang@h-partners.com> - 2.6-2
- Type: bugfix
- ID: NA
- SUG: NA
- DESC: rebuild for next release

* Fri Dec 3 2021 guozhaorui<guozhaorui1@huawei.com> - 2.6-1
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: update version to 2.6

* Wed Dec 4 2019 shenyangyang<shenyangyang4@huawei.com> - 2.4-7
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: modify comments

* Wed Oct 9 2019 shenyangyang<shenyangyang4@huawei.com> - 2.4-6
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:modify spec according the spec in tarball

* Tue Sep 24 2019 shenyangyang<shenyangyang4@huawei.com> - 2.4-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add help package

* Fri Aug 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.4-4
- Package init

