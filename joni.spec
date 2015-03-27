%{?_javapackages_macros:%_javapackages_macros}
Name:             joni
Version:          2.1.5
Release:          1
Summary:          Java port of Oniguruma regexp library 
Group:		  Development/Java
License:          MIT
URL:              http://github.com/jruby/%{name}
Source0:          https://github.com/jruby/joni/archive/2.1.5.tar.gz#/%{name}-%{version}.tar.gz
Patch1:           joni-remove-useless-wagon-dependency.patch

BuildRequires:    java-devel
BuildRequires:    jcodings
BuildRequires:    jpackage-utils
BuildRequires:    junit
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin

BuildRequires:    objectweb-asm4

Requires:         java
Requires:         jcodings
Requires:         jpackage-utils
Requires:         objectweb-asm4

BuildArch:      noarch


%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.

%package javadoc

Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p0

# fixes rpmlint warning about wrong-file-end-of-line-encoding
sed -i -e 's|\r||' test/org/joni/test/TestC.java
sed -i -e 's|\r||' test/org/joni/test/TestU.java
sed -i -e 's|\r||' test/org/joni/test/TestA.java

%mvn_file : %{name}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc MANIFEST.MF

%files javadoc -f .mfiles-javadoc
