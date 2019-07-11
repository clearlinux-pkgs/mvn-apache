#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-apache
Version  : 10
Release  : 2
URL      : https://github.com/apache/maven-apache-parent/archive/apache-10.tar.gz
Source0  : https://github.com/apache/maven-apache-parent/archive/apache-10.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/apache/10/apache-10.pom
Source2  : https://repo1.maven.org/maven2/org/apache/apache/11/apache-11.pom
Source3  : https://repo1.maven.org/maven2/org/apache/apache/12/apache-12.pom
Source4  : https://repo1.maven.org/maven2/org/apache/apache/13/apache-13.pom
Source5  : https://repo1.maven.org/maven2/org/apache/apache/14/apache-14.pom
Source6  : https://repo1.maven.org/maven2/org/apache/apache/15/apache-15.pom
Source7  : https://repo1.maven.org/maven2/org/apache/apache/16/apache-16.pom
Source8  : https://repo1.maven.org/maven2/org/apache/apache/17/apache-17.pom
Source9  : https://repo1.maven.org/maven2/org/apache/apache/18/apache-18.pom
Source10  : https://repo1.maven.org/maven2/org/apache/apache/19/apache-19.pom
Source11  : https://repo1.maven.org/maven2/org/apache/apache/2/apache-2.pom
Source12  : https://repo1.maven.org/maven2/org/apache/apache/20/apache-20.pom
Source13  : https://repo1.maven.org/maven2/org/apache/apache/21/apache-21.pom
Source14  : https://repo1.maven.org/maven2/org/apache/apache/3/apache-3.pom
Source15  : https://repo1.maven.org/maven2/org/apache/apache/4/apache-4.pom
Source16  : https://repo1.maven.org/maven2/org/apache/apache/5/apache-5.pom
Source17  : https://repo1.maven.org/maven2/org/apache/apache/6/apache-6.pom
Source18  : https://repo1.maven.org/maven2/org/apache/apache/7/apache-7.pom
Source19  : https://repo1.maven.org/maven2/org/apache/apache/9/apache-9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-apache-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-apache package.
Group: Data

%description data
data components for the mvn-apache package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/10

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/11

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/12
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/13
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/13

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/14
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/14

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/15
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/15

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/16
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/16

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/17
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/17

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/18
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/18

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/19
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/19

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/2
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/20
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/20

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/21
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/21

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/3
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/4
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/5
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/6
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/7
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/9
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache/9


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/apache/10/apache-10.pom
/usr/share/java/.m2/repository/org/apache/apache/11/apache-11.pom
/usr/share/java/.m2/repository/org/apache/apache/12/apache-12.pom
/usr/share/java/.m2/repository/org/apache/apache/13/apache-13.pom
/usr/share/java/.m2/repository/org/apache/apache/14/apache-14.pom
/usr/share/java/.m2/repository/org/apache/apache/15/apache-15.pom
/usr/share/java/.m2/repository/org/apache/apache/16/apache-16.pom
/usr/share/java/.m2/repository/org/apache/apache/17/apache-17.pom
/usr/share/java/.m2/repository/org/apache/apache/18/apache-18.pom
/usr/share/java/.m2/repository/org/apache/apache/19/apache-19.pom
/usr/share/java/.m2/repository/org/apache/apache/2/apache-2.pom
/usr/share/java/.m2/repository/org/apache/apache/20/apache-20.pom
/usr/share/java/.m2/repository/org/apache/apache/21/apache-21.pom
/usr/share/java/.m2/repository/org/apache/apache/3/apache-3.pom
/usr/share/java/.m2/repository/org/apache/apache/4/apache-4.pom
/usr/share/java/.m2/repository/org/apache/apache/5/apache-5.pom
/usr/share/java/.m2/repository/org/apache/apache/6/apache-6.pom
/usr/share/java/.m2/repository/org/apache/apache/7/apache-7.pom
/usr/share/java/.m2/repository/org/apache/apache/9/apache-9.pom
