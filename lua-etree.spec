Summary:	Lua Element Tree is an XML library that enables manipulation of XML documents as simple Lua data structures
Summary(hu.UTF-8):	Lua Element Tree egy XML könyvtár, amellyel XML dokumentumok módosítása lehetséges egyszerű Lua adatstruktúrákkal
Name:		lua-etree
Version:	0.1.1
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/2152/etree-%{version}.tar.gz
# Source0-md5:	848d6f4a4aadbaba6470a879bfc46094
URL:		http://luaforge.net/projects/etree/
Requires:	lua-expat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lua Element Tree is an XML library that enables manipulation of XML
documents as simple Lua data structures.

%description -l hu.UTF-8
Lua Element Tree egy XML könyvtár, amellyel XML dokumentumok
módosítása lehetséges egyszerű Lua adatstruktúrákkal.

%prep
%setup -q -n etree-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lua/5.1
install src/etree.lua $RPM_BUILD_ROOT%{_datadir}/lua/5.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/manual.html doc/manual.txt doc/style.css
%{_datadir}/lua/5.1/etree.lua
