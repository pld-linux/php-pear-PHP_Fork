%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Fork
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Wrapper for pcntl_fork() with Java-like API
Summary(pl.UTF-8):	%{_pearname} - Wrapper dla pcntl_fork() z API zbliżonym do Javy
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fd79cedf8c57d074757d4362beab41bf
URL:		http://pear.php.net/package/PHP_Fork/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcntl)
Requires:	php(posix)
Requires:	php(shmop)
Requires:	php-pear >= 4:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_Fork class. Wrapper around the pcntl_fork() stuff with a API set
like Java language. Practical usage is done by extending this class,
and re-defining the run() method.

This way PHP developers can enclose logic into a class that extends
PHP_Fork, then execute the start() method that forks a child process.
Communications with the forked process is ensured by using a Shared
Memory Segment; by using a user-defined signal and this shared memory
developers can access to child process methods that returns a
serializable variable.

The shared variable space can be accessed with the two methods:
- void setVariable($name, $value)
- mixed getVariable($name)

$name must be a valid PHP variable name; $value must be a variable or
a serializable object.

Resources (db connections, streams, etc.) cannot be serialized and so
they're not correctly handled.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PHP_Fork. Wrapper dla zbioru funkcji pcntl_fork() i pochodnych z
API zbliżonym do języka Javy. Praktyczne zastosowanie polega na
rozszerzeniu tej klasy i przedefiniowaniu metody run().

Dzięki temu deweloper PHP może zamknąć warstwę logiczną wewnątrz klasy
rozszerzającej PHP_Fork, a następnie uruchomić metodę start() która
wywoła proces potomny. Komunikacja z nowo powstałym procesem jest
zapewniona za pomocą Segmentu Współdzielonej Pamięci (Shared Memory
Segment); używając zdefiniowanych przez użytkownika sygnałów i tejże
dzielonej pamięci deweloperzy mają dostęp do metod procesu potomnego,
które zwraca zmienną dająca się zserializować.

Dostęp do dzielonej przestrzeni zmiennych jest możliwy poprzez dwie
metody:
- void setVariable($name, $value)
- mixed getVariable($name)

$name musi być poprawną zmienną PHP; $value musi być zmienną lub
obiektem możliwym do serializacji.

Zasoby (połączenia z bazami danych, strumienie, itp) nie mogą być
zserializowane i jako takie nie są poprawnie obsługiwane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
