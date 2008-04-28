


%define gcj_support 1

Name:           joni
Version:        1.0.2
Release:        %mkrel 0.4.1
Summary:        Java regular expression library
Group:          Development/Java
License:        MIT
URL:            http://jruby.codehaus.org/
# The source for this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
#   svn export http://svn.codehaus.org/jruby/joni/tags/1.0.2/ joni-1.0.2
#   tar -cjf joni-1.0.2.tar.bz2 joni-1.0.2
Source0:        %{name}-%{version}.tar.bz2
Patch0:         joni-set-java-5_0-target-and-source.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  java-rpmbuild >= 1.5
BuildRequires:  ant
BuildRequires:  jpackage-utils
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel >= 1.0.31
%endif
Requires:       java >= 1.5
Requires:       jpackage-utils
Requires(post):   java-gcj-compat >= 1.0.31
Requires(postun): java-gcj-compat >= 1.0.31

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
