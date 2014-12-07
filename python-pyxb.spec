%define	module	PyXB

Name:		python-pyxb
Version:	1.2.4
Release:	2
Source0:	https://github.com/pabigot/pyxb/archive/%{module}-%{version}.tar.gz
Summary:	Python XML Schema Bindings
License:	Apache
Group:		Development/Python
Url:		http://pyxb.sourceforge.net/
BuildArch:	noarch
BuildRequires:	python-devel

%description
PyXB is a pure Python package that generates Python source
code for classes that correspond to data structures defined by
XMLSchema.

%prep
%setup -q -n pyxb-%{module}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
 
%files
%doc doc/* LICENSE NOTICE README.txt examples/*
%{python_sitelib}/*
%{_bindir}/pyx*
