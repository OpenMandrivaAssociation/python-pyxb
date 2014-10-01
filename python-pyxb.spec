%define	module	PyXB

Name:		python-pyxb
Version:	1.2.4
Release:	0.2.gitc494ba3
Source0:	http://downloads.sourceforge.net/project/pyxb/pyxb/%{version}/%{module}-%{version}.tar.gz
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
%setup -q -n %{module}-%{version}
find . -name .gitignore -exec rm {} \;

# remove "-DEV" from version
sed -i 's|\(%{version}\)-DEV|\1|' setup.py doc/conf.py pyxb/__init__.py

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
 
%files
%doc doc/* LICENSE NOTICE README.txt examples/*
%{python_sitelib}/*
%{_bindir}/pyx*

