%global git fc96b59

Name:           unburden-home-dir
Version:        0.3.2
Release:        2.git%{git}%{?dist}
Summary:        Script to move cache files in homedir to tmpfs

Group:          System Environment/Base
License:        GPLv2
URL:            https://github.com/xtaran/unburden-home-dir
Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-reduced-dependancies.patch

Requires:       mbuffer, perl-Modern-Perl, perl-File-BaseDir, perl-File-Which

%description
unburden-home-dir allows users to move cache files from browsers, etc. 
off their home directory, i.e. on a local harddisk or tmpfs and replace
them with a symbolic link to the new location (e.g. on /tmp/ ) upon
login. Optionally the contents of the directories and files can be 
removed instead of moved.

%prep
%setup -q
%patch0 -p1
sed -i s/sed/#sed/ Makefile

%install
DESTDIR=%{buildroot} make install

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/examples
mkdir -p %{buildroot}%{_sysconfdir}/default
mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d
mv %{buildroot}%{_sysconfdir}/X11/Xsession.d/95unburden-home-dir %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/95unburden-home-dir
install -m 0644 README.md %{buildroot}%{_defaultdocdir}/%{name}/README
install -m 0644 debian/copyright %{buildroot}%{_defaultdocdir}/%{name}/copyright
install -m 0644 etc/* %{buildroot}%{_defaultdocdir}/%{name}/examples/
echo -e "#Enable unburden-home-dir XSession login\nUNBURDEN_HOME=yes" > %{buildroot}%{_sysconfdir}/default/unburden-home-dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc
%{_sysconfdir}/X11/xinit/xinitrc.d/95unburden-home-dir
%config(noreplace) %{_sysconfdir}/default/unburden-home-dir
%config(noreplace) %{_sysconfdir}/unburden-home-dir
%config(noreplace) %{_sysconfdir}/unburden-home-dir.list
%{_bindir}/unburden-home-dir
%{_defaultdocdir}/%{name}/README
%{_defaultdocdir}/%{name}/copyright
%{_defaultdocdir}/%{name}/examples/unburden-home-dir
%{_defaultdocdir}/%{name}/examples/unburden-home-dir.list
%{_mandir}/man1/unburden-home-dir.1.gz

%changelog
* Sun Feb 03 2013 Chris Smart <csmart@kororaproject.org> - 0.3.2-2
- Unburden wasn't starting due to missing config option and misplaced config file.

* Sat Jan 19 2013 Chris Smart <csmart@kororaproject.org> - 0.3.2-1
- Initial spec.

