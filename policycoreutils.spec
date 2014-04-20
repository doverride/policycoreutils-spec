%global libauditver     2.1.3
%global libsepolver     2.1.9
%global libselinuxver   2.2.1

Name:           policycoreutils
Version:        2.3
Release:        0.1.rc1%{?dist}
Summary:        Core set of utilities needed to use SELinux

License:        GPLv2
URL:            http://www.selinuxproject.org
Source0:        http://userspace.selinuxproject.org/releases/2.3-rc1/policycoreutils-%{version}-rc1.tar.gz
Patch0:         makefile.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libsepol-devel >= %{libsepolver} libselinux-devel >= %{libselinuxver} audit-libs-devel >=  %{libauditver} gettext coreutils make
Requires:       libsepol libselinux audit-libs

%description
Security-enhanced Linux (SELinux) is a reference implementation of the
Flask security architecture for flexible mandatory access control. The
Flask architecture provides general support for the enforcement of many
kinds of mandatory access control policies, including those based on
the concepts of Type Enforcement®, Role-based Access Control, and
Multi-level Security.

%prep   
%setup -qn policycoreutils-%{version}-rc1
%patch0 -p1

%build
/usr/bin/make clean
/usr/bin/make LSPP_PRIV=y SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fPIE" LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now" all


%install
/usr/bin/rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_bindir}
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_sbindir}
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_mandir}/man1
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_mandir}/man5
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_mandir}/man8
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}/
/usr/bin/cp COPYING ${RPM_BUILD_ROOT}%{_usr}/share/doc/%{name}/

/usr/bin/make LSPP_PRIV=y  DESTDIR="${RPM_BUILD_ROOT}" SBINDIR="%{buildroot}%{_sbindir}" LIBDIR="%{buildroot}%{_libdir}" install


%clean
/usr/bin/rm -rf ${RPM_BUILD_ROOT}


%files
%{_bindir}/secon
%{_sbindir}/load_policy
%{_sbindir}/restorecon
%{_sbindir}/setfiles
%{_sbindir}/sestatus
%{_mandir}/man1/secon.1.gz
%{_mandir}/man5/sestatus.conf.5.gz
%{_mandir}/man8/load_policy.8.gz
%{_mandir}/man8/restorecon.8.gz
%{_mandir}/man8/setfiles.8.gz
%{_mandir}/man8/sestatus.8.gz
%config(noreplace) %{_sysconfdir}/sestatus.conf
%doc %{_usr}/share/doc/%{name}



%changelog
* Sun Apr 20 2014 "Dominick Grift <dac.override@gmail.com>" - 2.3-0.1.rc1
- Initial core set of utilities needed to use SELinux RPM spec file
