%define compat_python %{_bindir}/python2.4
%{!?python_sitelib: %define python_sitelib %(%{compat_python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           compat-python24-feedparser
Version:        4.1
Release:        6%{?dist}
Summary:        Parse RSS and Atom feeds in Python

Group:          Development/Languages
License:        BSD-ish
URL:            http://feedparser.org/
Source0:        http://download.sourceforge.net/feedparser/feedparser-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  compat-python24-devel

%description
Universal Feed Parser is a Python module for downloading and parsing 
syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91, 
Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0, 
Atom 0.3, Atom 1.0, and CDF feeds. It also parses several popular extension 
modules, including Dublin Core and Apple's iTunes extensions.


%prep
%setup -q -c
find -type f -exec sed -i 's/\r//' {} ';'
find -type f -exec chmod 0644 {} ';'


%build
CFLAGS="$RPM_OPT_FLAGS" %{compat_python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{compat_python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
cp -a docs html
rm -f html/examples/.ht*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README html
%{python_sitelib}/*


%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 4.1-6
- rebuild for new F11 features

* Sun Aug 10 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 4.1-5
- rebuild for RPM Fusion

* Thu Mar 27 2008 Jonathan Steffan <jonathansteffan a gmail.com> - 4.1-4
- Make a compat-python24 package,
  based on 4.1-3 from Fedora 8
