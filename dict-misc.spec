%define         dictname misc
Summary:	misc dictionaries for DICTD
Summary(pl):	R�ne s�owniki dla dictd
Name:		dict-%{dictname}
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
URL:		http://www.dict.org/
BuildRequires:	dictzip
BuildRequires:	autoconf
Requires:	dictd
Requires:	%{_sysconfdir}/dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains misc dictionaries for use by the dictionary
server in the dictd package.

%description -l pl
Ten pakiet zawiera r�ne s�owniki do u�ywania z serwerem s�ownika
dictd.

%package -n dict-hitchcock
Summary:	hitchcock dictionary for DICTD
Summary(pl):	S�ownik hitchcock dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-hitchcock
This package contains hitchcock dictionaries for use by the dicitonary
server in the dictd package.

%description -n dict-hitchcock -l pl
Ten pakiet zawiera s�ownik hitchcock do u�ywania z serwerem s�ownika
dictd.

%package -n dict-world95
Summary:	world95 dictionary for DICTD
Summary(pl):	S�ownik world95 dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-world95
This package contains world95 dictionaries for use by the dicitonary
server in the dictd package.

%description -n dict-world95 -l pl
Ten pakiet zawiera s�ownik world95 do u�ywania z serwerem s�ownika
dictd.

%package -n dict-foldoc
Summary:	foldoc dictionary for DICTD
Summary(pl):	S�ownik foldoc dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-foldoc
This package contains foldoc dictionaries for use by the dicitonary
server in the dictd package.

%description -n dict-foldoc -l pl
Ten pakiet zawiera s�ownik foldoc do u�ywania z serwerem s�ownika
dictd.

%package -n dict-easton
Summary:	easton dictionary for DICTD
Summary(pl):	S�ownik easton dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-easton
This package contains easton dictionaries for use by the dicitonary
server in the dictd package.

%description -n dict-easton -l pl
Ten pakiet zawiera s�ownik easton do u�ywania z serwerem s�ownika
dictd.

%package -n dict-elements
Summary:	elements dictionary for DICTD
Summary(pl):	S�ownik elements dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-elements
This package contains elements dictionaries for use by the dicitonary
server in the dictd package.

%description -n dict-elements -l pl
Ten pakiet zawiera s�ownik elements do u�ywania z serwerem s�ownika
dictd.

%prep
%setup -q

%build
autoconf
%configure
%{__make} db

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd}
%{__make} install dictdir="$RPM_BUILD_ROOT%{_datadir}/dictd/"

# jargon has separate package
rm -f $RPM_BUILD_ROOT%{_datadir}/dictd/jargon.*

for i in easton elements foldoc hitchcock world95; do
dictprefix=%{_datadir}/dictd/$i
echo "# Misc Dictionaries - $i
database $i {
    data  \"$dictprefix.dict.dz\"
    index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/$i.dictconf
done;

%clean
rm -rf $RPM_BUILD_ROOT

%postun -n dict-easton
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-easton
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi


%postun -n dict-elements
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-elements
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi


%postun -n dict-foldoc
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-foldoc
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi


%postun -n dict-hitchcock
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-hitchcock
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi


%postun -n dict-world95
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-world95
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%files -n dict-hitchcock
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/hitchcock.dictconf
%{_datadir}/dictd/hitchcock*

%files -n dict-world95
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/world95.dictconf
%{_datadir}/dictd/world95.*

%files -n dict-foldoc
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/foldoc.dictconf
%{_datadir}/dictd/foldoc.*

%files -n dict-easton
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/easton.dictconf
%{_datadir}/dictd/easton*

%files -n dict-elements
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/elements.dictconf
%{_datadir}/dictd/elements.*
