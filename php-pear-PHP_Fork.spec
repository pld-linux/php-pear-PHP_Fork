%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Fork
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
URL:		http://pear.php.net/package/PHP_Fork/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

$name must be a valid PHP variable name;
$value must be a variable or a serializable object.

Resources (db connections, streams, etc.) cannot be serialized and so
they're not correctly handled.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PHP_Fork. Wrapper dla zbioru funkcji pcntl_fork() i pochodnych z
API zbli¿onym do jêzyka Javy. Praktyczne zastosowanie polega na
rozszerzeniu tej klasy i przedefiniowaniu metody run().

Dziêki temu deweloper PHP mo¿e zamkn±æ warstwê logiczn± wewn±trz klasy
rozszerzaj±cej PHP_Fork, a nastêpnie uruchomiæ metodê start() która
wywo³a proces potomny. Komunikacja z nowo powsta³ym procesem jest
zapewniona za pomoc± Segmentu Wspó³dzielonej Pamiêci (Shared Memory
Segment); u¿ywaj±c zdefiniowanych przez u¿ytkownika sygna³ów i tej¿e
dzielonej pamiêci deweloperzy maj± dostêp do metod procesu potomnego,
które zwraca zmienn± daj±ca siê zserializowaæ.

Dostêp do dzielonej przestrzeni zmiennych jest mo¿liwy poprzez dwie
metody:
- void setVariable($name, $value)
- mixed getVariable($name)

$name musi byæ poprawn± zmienn± PHP;
$value musi byæ zmienn± lub obiektem mo¿liwym do serializacji.

Zasoby (po³±czenia z bazami danych, strumienie, itp) nie mog± byæ
zserializowane i jako takie nie s± poprawnie obs³ugiwane.

Ta klasa ma w PEAR status: %{_status}.

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
