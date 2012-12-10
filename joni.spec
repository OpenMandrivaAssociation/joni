%define gcj_support 0


Name:           joni
Version:        1.1.3
Release:        %mkrel 0.1.svn7235.3
Summary:        Java regular expression library
Group:          Development/Java
License:        MIT
URL:            http://jruby.codehaus.org/
# The source for this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
#   svn export -r 7235 http://svn.codehaus.org/jruby/joni/trunk/ joni-1.0.3
#   tar -cjf joni-1.0.3.tar.bz2 joni-1.0.3
Source0:          %{name}-%{version}.tar.bz2
Patch0:           joni-set-java-5_0-target-and-source.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  java-rpmbuild >= 1.5
BuildRequires:  ant
BuildRequires:  jpackage-utils
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel >= 1.0.31
%endif
Requires:       java >= 1.5
Requires:       jpackage-utils
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.


%prep
%setup -q
%patch0 -p0

%build
%ant build


%install
rm -rf %{buildroot}

# jars
install -d -m 755 %{buildroot}%{_javadir}
# install unversioned jar as per Java Packaging Guidelines
install -m 644 target/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

%{gcj_compile}


%post
%{update_gcjdb}


%postun
%{clean_gcjdb}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc pom.xml
%{_javadir}/%{name}.jar
%{gcj_files}


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-0.1.svn7235.3mdv2011.0
+ Revision: 612510
- the mass rebuild of 2010.1 packages

* Thu Feb 25 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.1.3-0.1.svn7235.2mdv2010.1
+ Revision: 510955
- update to 1.1.3

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-0.3.svn7235.2mdv2010.0
+ Revision: 429644
- rebuild

* Thu Aug 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.3-0.3.svn7235.1mdv2009.0
+ Revision: 271715
- new svn snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Sat Jun 07 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.2-0.4.3mdv2009.0
+ Revision: 216570
- disable gcj dependency

* Fri May 30 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.2-0.4.2mdv2009.0
+ Revision: 213568
- remove useless patch
- new snapshot for the new jruby

* Mon Apr 28 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.2-0.4.1mdv2009.0
+ Revision: 197993
- import joni


