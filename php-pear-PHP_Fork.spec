%include	/usr/lib/rpm/macros.php
%define         _class          PHP
%define         _subclass       Fork
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Wrapper for pcntl_fork() with Java-like API
Summary(pl):	%{_pearname} - Wrapper dla pcntl_fork() z API zbli¿onym do Javy
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8ecf5ea9cdde0ab2d6d962d380d63323
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_Fork class. Wrapper around the pcntl_fork() stuff with a API set
like Java language. Practical usage is done by extending this class,
and re-defining the run() method.
[see basic example]

This way PHP developers can enclose logic into a class that extends
PHP_Fork, then execute the start() method that forks a child process.
Communications with the forked process is ensured by using a Shared
Memory Segment; by using a user-defined signal and this shared memory
developers can access to child process methods that returns a
serializable variable.

The shared variable space can be accessed with the two methods:
- void setVariable($name, $value)
- mixed getVariable($name)

$name must be a valid PHP variable name;
$value must be a variable or a serializable object.

Resources (db connections, streams, etc.) cannot be serialized and so
they're not correctly handled.

This class has in PEAR status: %{_status}.

#%description -l pl
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
