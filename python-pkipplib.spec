%define		module	pkipplib

Summary:	Module for preparing IPP requests
Summary(pl.UTF-8):	Moduł do przygotowywania zleceń IPP
Name:		python-%{module}
Version:	0.07
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://www.pykota.com/software/pkipplib/download/tarballs/%{module}-%{version}.tar.gz
# Source0-md5:	6e59a148f6ebf7c4344a7a2f1c2aea3c
URL:		http://www.pykota.com/software/pkipplib/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkipplib is a Python library which can prepare IPP requests
with the help of a somewhat high level API. These requests
can then be sent to an IPP printer or print server (e.g. CUPS).
This library can also parse IPP answers received, and create
high level Python objects from them.
Both of these actions can be done through an IPPRequest class
and its instance methods.
Finally, a CUPS class can be leveraged to easily deal with
CUPS print servers.

%description -l pl.UTF-8
pkpgcounter jest biblioteką umożliwiającą przygotowywanie zleceń IPP,
jak również parsowania odpowiedzi IPP i tworzenie na ich podstaiw
obiektów pythona.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pksubscribe
%dir %{py_sitescriptdir}/pkipplib
%{py_sitescriptdir}/pkipplib/*.py[co]
%{py_sitescriptdir}/*.egg-info
