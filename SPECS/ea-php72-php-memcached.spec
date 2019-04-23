%global scl_version ea-php72
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcached
Version: 3.0.2
Summary: php-memcached extension for %{scl_version}
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
License: MIT
Group: Programming/Languages
URL: https://pecl.php.net/package/memcached
Source: https://github.com/php-memcached-dev/php-memcached/archive/v3.0.2.tar.gz
Source1: memcached.ini

# should be no requires for building this package
#Requires: memcached
Requires: libmemcached
BuildRequires: libmemcached libmemcached-devel
BuildRequires: %{scl_version} %{scl_version}-php-cli

%description
This is the PECL memcached extension, using the libmemcached library to connect
to memcached servers.


%prep
%setup -n php-memcached-%{version}

%build
scl enable %{scl_version} phpize
scl enable %{scl_version} './configure --disable-memcached-sasl'
make

%install
make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/memcached.so
%config /%{ext_prefix}/%{conf_dir}/memcached.ini

%changelog
* Wed Mar  5 2017 Jack Hayhurst <jack@deleteos.com> - 2.2.7
- RPM actually building, fixed naming scheme to fit in with EA4

* Wed Mar  1 2017 Jack Hayhurst <jack@deleteos.com> - 2.2.7
- Initial spec file creation.
