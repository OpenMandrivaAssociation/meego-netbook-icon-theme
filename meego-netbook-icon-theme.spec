Name: meego-netbook-icon-theme
Summary: MeeGo netbook icon theme
Version: 2.2.12
Release: %mkrel 1
Group: System/Desktop
License: Restricted
URL: http://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/netbook-icon-theme-%{version}.tar.gz
Source1: License
Requires: gtk+2
BuildRequires: hicolor-icon-theme
BuildRequires: icon-naming-utils
BuildRequires: fdupes
Obsoletes: moblin-icon-theme < 0.9

%description
MeeGo netbook icon theme.

%prep
%setup -q -n netbook-icon-theme-%{version}

%build
%configure2_5x \
  --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

fdupes %{buildroot}/%{_datadir}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor || : 
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| : 
for dir in /usr/share/icons/*; do
  if test -d "$dir"; then
    if test -f "$dir/index.theme"; then
      /usr/bin/gtk-update-icon-cache --quiet "$dir"
    fi
  fi
done

%postun
/bin/touch --no-create %{_datadir}/icons/hicolor || : 
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| : 

%files
%defattr(-,root,root,-)
%{_datadir}/icons/netbook
