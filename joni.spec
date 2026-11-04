%bcond_with javadoc
Name:             joni
Version:          2.2.9
Release:          1
Summary:          Java port of Oniguruma regexp library 
Group:		  Development/Java
License:          MIT
URL:              https://github.com/jruby/%{name}
Source0:          https://github.com/jruby/joni/archive/refs/tags/joni-%{version}.tar.gz

BuildRequires:    jcodings

Requires:         java
Requires:         jcodings
Requires:         javapackages-filesystem

BuildArch:      noarch
BuildSystem:	maven
BuildOption(install):	--file-name %{name}


%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.

%if %{with javadoc}
%package javadoc

Summary:        Javadoc for %{name}
Requires:       javapackages-filesystem

%endif
%if %{with javadoc}
%description javadoc
API documentation for %{name}.

%endif
%prep
%setup -q -n joni-joni-%{version}

%files -f .mfiles
%doc LICENSE README.md

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc

%endif
