Name:		
Version:	
Release:	1%{?dist}
Summary:	

Group:		
License:	
URL:		
Source0:	

BuildRequires:	
Requires:       mbuffer, perl-Modern-Perl, perl-File-BaseDir, perl-File-Which

%description


%prep
%setup -q


%install


%files
%doc
/etc/X11/Xsession.d/95unburden-home-dir
/etc/default/unburden-home-dir
/etc/unburden-home-dir
/etc/unburden-home-dir.list
/usr/bin/unburden-home-dir
/usr/share/doc/unburden-home-dir/README.Debian
/usr/share/doc/unburden-home-dir/README.gz
/usr/share/doc/unburden-home-dir/THANKS
/usr/share/doc/unburden-home-dir/changelog.gz
/usr/share/doc/unburden-home-dir/copyright
/usr/share/doc/unburden-home-dir/examples/unburden-home-dir
/usr/share/doc/unburden-home-dir/examples/unburden-home-dir.list
/usr/share/man/man1/unburden-home-dir.1.gz


%changelog

