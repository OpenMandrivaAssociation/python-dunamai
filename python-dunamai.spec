%define module dunamai

Name:		python-dunamai
Version:	1.26.1
Release:	1
Summary:	Dynamic version generation
License:	MIT
Group:		Development/Python
URL:		https://dunamai.readthedocs.io/
# upstream repo		https://github.com/mtkennerly/dunamai/
Source0:	https://github.com/mtkennerly/dunamai/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
Dynamic version generation

%files
%doc README.md
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
