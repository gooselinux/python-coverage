%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# tracer.so is a private object, don't include it in the provides
%global _use_internal_dependency_generator 0
%global __find_provides /bin/sh -c "%{_rpmconfigdir}/find-provides | grep -v -E '(tracer.so)' || /bin/true"
%global __find_requires /bin/sh -c "%{_rpmconfigdir}/find-requires | grep -v -E '(tracer.so)' || /bin/true"

Name:			python-coverage
Summary:		Code coverage testing module for Python
Version:		3.0.1
Release:		2%{?dist}
License:		BSD and (MIT or GPLv2)
Group:			System Environment/Libraries
URL:			http://nedbatchelder.com/code/modules/coverage.html
Source0:		http://pypi.python.org/packages/source/c/coverage/coverage-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:		python-setuptools, python-devel
Requires:		python-setuptools

%description
Coverage.py is a Python module that measures code coverage during Python 
execution. It uses the code analysis tools and tracing hooks provided in the 
Python standard library to determine which lines are executable, and which 
have been executed.

%prep
%setup -q -n coverage-%{version}

find . -type f -exec chmod 0644 \{\} \;
sed -i 's/\r//g' README.txt

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/coverage
%{python_sitearch}/coverage/
%{python_sitearch}/coverage*.egg-info/

%changelog
* Mon Jun 28 2010 David Malcolm <dmalcolm@redhat.com> - 3.0.1-2
- require python-setuptools at run-time (556290)
- don't add tracer.so to the provides
- fix License metadata
- remove executable permissions from many files that don't need it

* Wed Aug 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0.1-1
- update to 3.0.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.85-2
- fix install invocation

* Wed May 6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.85-1
- Initial package for Fedora
