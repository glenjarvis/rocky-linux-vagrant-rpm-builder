Name:           fizz-buzz
Version:        1.0.0
Release:        1%{?dist}
Summary:        A simple demo executable to show how RPM packaging works
BuildArch:      noarch

License:        MIT
URL:            https://github.com/glenjarvis/rocky-linux-vagrant-rpm-builder
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:  
Requires:       platform-python

%description
This simple "fizzbuzz" program is now bundled as a RPM to demonstrate how
rpm-builder works.


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp fizz $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/fizz
#%license add-license-file-here
#%doc add-docs-here


%changelog
* Sat Feb 13 2021 vagrant
- Initial example created
