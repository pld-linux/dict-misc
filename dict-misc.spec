%define         dictname misc
Summary:	misc dictionaries for DICTD
Name:		dict-%{dictname}
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
URL:		http://www.dict.org/
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	dictzip
BuildRequires:	autoconf
Requires:	dictd 
Requires:	%{_sysconfdir}/dictd

%description 
This package contains misc dictionaries for use by the dictionary
server in the dictd package.

%package -n dict-hitchcock
Summary:	hitchcock dictionary for DICTD
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
Requires:	dictd 
Requires:	%{_sysconfdir}/dictd

%description -n dict-hitchcock
This package contains hitchcock dictionaries for use by the dicitonary
server in the dictd package

%package -n dict-world95
Summary:	world95 dictionary for DICTD
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
Requires:	dictd 
Requires:	%{_sysconfdir}/dictd

%description -n dict-world95
This package contains world95 dictionaries for use by the dicitonary
server in the dictd package

%package -n dict-foldoc
Summary:	foldoc dictionary for DICTD
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
Requires:	dictd 
Requires:	%{_sysconfdir}/dictd

%description -n dict-foldoc
This package contains foldoc dictionaries for use by the dicitonary
server in the dictd package

%package -n dict-easton
Summary:	easton dictionary for DICTD
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
Requires:	dictd 
Requires:	%{_sysconfdir}/dictd

%description -n dict-easton
This package contains easton dictionaries for use by the dicitonary
server in the dictd package

%package -n dict-elements
Summary:	elements dictionary for DICTD
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
Requires:	dictd 
Requires:	%{_sysconfdir}/dictd

%description -n dict-elements
This package contains elements dictionaries for use by the dicitonary
server in the dictd package

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

%files
%defattr(644,root,root,755)

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
