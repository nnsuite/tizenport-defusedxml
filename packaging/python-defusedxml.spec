Name:           python-defusedxml
Version:        0.5
Release:        0
Summary:        XML bomb protection for Python stdlib modules
License:        Python
URL:            https://bitbucket.org/tiran/defusedxml
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.

%prep
%setup -q
cp %{SOURCE1001} .

%build
/usr/bin/python2 setup.py build

%install
/usr/bin/python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%manifest %{name}.manifest
%{python_sitelib}/*
%exclude %{python_sitelib}/defusedxml/*.pyc

%changelog
