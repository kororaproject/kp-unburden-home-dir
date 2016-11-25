Name:           unburden-home-dir
Version:        0.4.0.1
Release:        1%{?dist}
Summary:        Script to move cache files in homedir to tmpfs

Group:          System Environment/Base
License:        GPLv2
URL:            https://github.com/xtaran/unburden-home-dir
Source0:        https://github.com/xtaran/unburden-home-dir/archive/%{version}.tar.gz
Patch0:         0001-reduced-dependancies.patch

BuildRequires:  rubygem-ronn
Requires:       perl-Modern-Perl
Requires:       perl-File-BaseDir
Requires:       perl-File-Which

%description
unburden-home-dir allows users to move cache files from browsers, etc.
off their home directory, i.e. on a local harddisk or tmpfs and replace
them with a symbolic link to the new location (e.g. on /tmp/ ) upon
login. Optionally the contents of the directories and files can be
removed instead of moved.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
sed -i s/sed/#sed/ Makefile
sed -i -e 's@/Xsession.d@/xinit/xinitrc.d@g' Makefile
mv README.md README
cp -R etc/ examples/

%install
%{make_install}
sed -i 's/^m D .cache cache/#m D .cache cache/g' %{buildroot}%{_sysconfdir}/unburden-home-dir.list

mkdir -p %{buildroot}%{_sysconfdir}/default
echo -e "#Enable unburden-home-dir XSession login\nUNBURDEN_HOME=yes" > %{buildroot}%{_sysconfdir}/default/unburden-home-dir

%files
%doc README examples/
%license COPYING
%{_sysconfdir}/X11/xinit/xinitrc.d/25unburden-home-dir-xdg
%{_sysconfdir}/X11/xinit/xinitrc.d/95unburden-home-dir
%config(noreplace) %{_sysconfdir}/default/unburden-home-dir
%config(noreplace) %{_sysconfdir}/unburden-home-dir
%config(noreplace) %{_sysconfdir}/unburden-home-dir.list
%{_bindir}/unburden-home-dir
%{_mandir}/man1/unburden-home-dir.1.*
%{_datadir}/unburden-home-dir/common.sh

%changelog
* Fri Nov 25 2016 Ian Firns <firnsy@kororaproject.org> - 0.4.0.1-1
- Updated to latest upstream.

* Tue Jan  5 2016 Ian Firns <firnsy@kororaproject.org> - 0.3.3-1.gitd4e2658
- Updated to latest upstream stable and reduced patch size with File::Touch
  now packaged.

* Sun Jul 19 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.3.2.3-2.git2745ccd
- spec file clean up

* Sat Jul 26 2014 Ian Firns <firnsy@kororaproject.org> - 0.3.2.3-1
- Updated to latest upstream.

* Mon Apr 14 2014 Ian Firns <firnsy@kororaproject.org> - 0.3.2.2-2
- Updated to latest upstream which drops dependancy for mbuffer.

* Thu Sep 26 2013 Ian Firns <firnsy@kororaproject.org> - 0.3.2.2-1
- Updated to upstream and tweaked patch to compile.

* Sat Feb 16 2013 Chris Smart <csmart@kororaproject.org> - 0.3.2-3
- Remove .cache for now to work around issue where terminal non-responsive if unburden disabled and not reburdened.

* Sun Feb 03 2013 Chris Smart <csmart@kororaproject.org> - 0.3.2-2
- Unburden wasn't starting due to missing config option and misplaced config file.

* Sat Jan 19 2013 Chris Smart <csmart@kororaproject.org> - 0.3.2-1
- Initial spec.
