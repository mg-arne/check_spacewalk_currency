Name:           nagios-plugins-spacewalk-currency
Version:        0.5.0
Release:        1%{?dist}
Summary:        A Nagios / Icinga plugin for checking patch currency of hosts managed by Spacewalk

Group:          Applications/System
License:        GPL
URL:            https://github.com/stdevel/check_spacewalk_currency
Source0:        nagios-plugins-spacewalk-currency-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:
Requires:       python-requests

%description
This package contains a Nagios / Icinga plugin for checking patch currency of hosts managed by Spacewalk, Red Hat Satellite 5.x or SUSE Manager.

Check out the GitHub page for further information: https://github.com/stdevel/check_spacewalk_currency

%prep
%setup -q

%build
#change /usr/lib64 to /usr/lib if we're on i686
%ifarch i686
sed -i -e "s/usr\/lib64/usr\/lib/" check_spacewalk_currency.cfg
%endif

%install
install -m 0755 -d %{buildroot}%{_libdir}/nagios/plugins/
install -m 0755 check_spacewalk_currency.py %{buildroot}%{_libdir}/nagios/plugins/check_spacewalk_currency
%if 0%{?el7}
        install -m 0755 -d %{buildroot}%{_sysconfdir}/nrpe.d/
        install -m 0755 check_spacewalk_currency.cfg  %{buildroot}%{_sysconfdir}/nrpe.d/check_spacewalk_currency.cfg
%else
        install -m 0755 -d %{buildroot}%{_sysconfdir}/nagios/plugins.d/
        install -m 0755 check_spacewalk_currency.cfg  %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_spacewalk_currency.cfg
%endif



%clean
rm -rf $RPM_BUILD_ROOT

%files
%if 0%{?el7}
        %config %{_sysconfdir}/nrpe.d/check_spacewalk_currency.cfg
%else
        %config %{_sysconfdir}/nagios/plugins.d/check_spacewalk_currency.cfg
%endif
%{_libdir}/nagios/plugins/check_spacewalk_currency


%changelog
* Fri Oct 14 2016 Christian Stankowic <info@stankowic-development.net> - 0.5.0-1
- First release
