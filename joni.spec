%{?_javapackages_macros:%_javapackages_macros}
Name:             joni
Version:          2.1.3
Release:          1.2
Summary:          Java port of Oniguruma regexp library 
Group:		  Development/Java
License:          MIT
URL:              http://github.com/jruby/%{name}
Source0:          https://github.com/jruby/%{name}/archive/%{version}.tar.gz/%{name}-%{version}.tar.gz
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

%changelog
* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 1.1.9-3
- Start using xmvn.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.9-1
- Updated to version 1.1.9.
- Switched from ant to maven.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> - 1.1.3-8
- add maven pom
- adapt to current guideline

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.3-4
- fixed end of line encoding rpmlint warning
- removed uneccessary deps

* Wed Feb 17 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.3-3
- removed gcj bits
- updated package to conform to guidelines based on feedback
- corrected source url

* Fri Jan 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.3-2
- Unorphaned / updated package

* Fri Mar 6 2009 Conrad Meyer <konrad@tylerc.org> - 1.1.3-1
- Bump to 1.1.3.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Conrad Meyer <konrad@tylerc.org> - 1.1.2-1
- Bump to 1.1.2.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 1.1.1-1
- Bump to 1.1.1.

* Sun Aug 31 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-1
- Official 1.0.3 release.

* Sat Jul 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-0.3.svn7235
- Build AOT bits.

* Sat Jul 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-0.2.svn7235
- Bump revision because of stupid packager's mistake.

* Sat Jul 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-0.1.svn7235
- Bump to trunk version of joni for JRuby 1.1.3.
- Switch to noarch for fc10 and up.

* Sat Apr 5 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.2-4
- Compile AOT bits.

* Sun Mar 16 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.2-3
- Bump to 1.0.2.
- Add pom.xml to doc.
- Install unversioned jar.

* Sun Mar 2 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.1-2
- joni is MIT, not BSD.
- Require java and BuildRequire java-devel, not icedtea.

* Sun Mar 2 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.1-1
- Initial package.
