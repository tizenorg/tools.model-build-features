%define release_prefix 1

Name:       model-build-features
Summary:    Model Build Feature configuration file for optimize packages-listing
Version:    0.5
Release:    %{release_prefix}
Group:      Development/System
Source:     %{name}-%{version}.tar.gz
License:    Apache 
URL:        http://www.tizen.org
BuildArch:  noarch
 
%description
Model Build Feature configuration file for optimize packages-listing

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
cp default/macros.modelbuildfeatures.default  default/macros.modelbuildfeatures
%if "%{?tizen_profile_name}" == "mobile"
cp default/macros.modelbuildfeatures.m0  default/macros.modelbuildfeatures
%endif 
%if "%{?tizen_profile_name}" == "wearable"
cp default/macros.modelbuildfeatures.b2  default/macros.modelbuildfeatures
%endif 

install -m 644 default/macros.modelbuildfeatures %{buildroot}%{_sysconfdir}/rpm



%files
%defattr(-,root,root,-)
%{_sysconfdir}/rpm/macros.modelbuildfeatures

