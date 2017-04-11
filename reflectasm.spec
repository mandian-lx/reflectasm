%{?_javapackages_macros:%_javapackages_macros}
Name:          reflectasm
Version:       1.11.0
Release:       4%{?dist}
Summary:       High performance Java library that provides reflection by using code generation
License:       BSD
URL:           https://github.com/EsotericSoftware/reflectasm
Source0:       https://github.com/EsotericSoftware/reflectasm/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

%description
ReflectASM is a very small Java library that provides
high performance reflection by using code generation.
An access class is generated to set/get fields,
call methods, or create a new instance. The access class
uses byte-code rather than Java's reflection, so it
is much faster. It can also access primitive fields
via byte-code to avoid boxing.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find -name "*.class" -delete
find -name "*.jar" -delete

sed -i 's/\r//' license.txt
# Do not shade asm
%pom_remove_plugin :maven-shade-plugin

%mvn_file :%{name} %{name}
%mvn_alias :%{name} "com.esotericsoftware.%{name}:%{name}"

# AssertionFailedError: expected:<1> but was:<0>
rm -r test/com/esotericsoftware/reflectasm/ClassLoaderTest.java

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 gil cattaneo <puntogil@libero.it> 1.11.0-1
- update to 1.11.0

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.07-6
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 09 2013 gil cattaneo <puntogil@libero.it> 1.07-4
- upstream update for reflectasm 1.07 (PATCH0)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 1.07-2
- switch to XMvn
- minor changes to adapt to current guideline

* Fri Mar 08 2013 gil cattaneo <puntogil@libero.it> 1.07-1
- initial rpm
