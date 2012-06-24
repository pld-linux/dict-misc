%define         dictname misc
Summary:	misc dictionaries for DICTD
Summary(pl):	R�ne s�owniki dla dictd
Name:		dict-%{dictname}
Version:	1.5
Release:	3
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
Source1:	http://dsl.org/faq/fjd/journo-1.1.tar.gz
Source2:	http://wiretap.area.com/Gopher/Library/Classic/devils.txt
URL:		http://www.dict.org/
BuildRequires:	autoconf
BuildRequires:	dictzip
Requires:	dictd
Requires:	%{_sysconfdir}/dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains misc dictionaries for use by the dictionary
server in the dictd package.

%description -l pl
Ten pakiet zawiera r�ne s�owniki do u�ywania z serwerem s�ownika
dictd.

%package -n dict-devil
Summary:	Devils dictionary for DICTD
Summary(pl):	S�ownik Devils dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-devil
This package contains The Devil's Dictionary, a cynical and irreverent
dictionary of common words, formatted for use by the dictionary server
in the dictd package.

%description -n dict-devil -l pl
S�ownik The Devil's Dictionary, zawieraj�cy cyniczne i lekcewa��ce
opisy s��w - do u�ywania z serwerem s�ownika dictd.

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

%package -n dict-journo
Summary:	Journalism dictionary for DICTD
Summary(pl):	S�ownik Journalism dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-journo
This package contains journo dictionaries for use by the dicitonary
server in the dictd package.

%description -n dict-journo -l pl
Ten pakiet zawiera s�ownik journo do u�ywania z serwerem s�ownika
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

%package -n dict-fmt
Summary:	Dict file formater for DICTD
Summary(pl):	Obrabiarka plik�w dla dictda
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Provides:	dictfmt

%description -n dict-fmt
This package contains dictfmt, util for formater for files used
aferwards by the dictionary server from the dictd package.

%description -n dict-fmt -l pl
Narz�dzia do obr�bki plik�w u�ywanych p�niej przez serwer z pakietu
dictd.

%prep
%setup -q -a1
cp %{SOURCE2} ./

%build
autoconf
%configure
%{__make} db

sed  -e 's/^[[:alpha:]]\{2,\}$/:&:/' < journo-1.1/journalism.dict \
	> journalism.txt
./dictfmt -j -u "http://dsl.org/lit/" -s Journalism journo < journalism.txt
dictzip journo.dict

sed  's/^[[:upper:]]\{2,\}/:&:/' ./devils.txt | ./dictfmt  \
	-j -u http://wiretap.area.com/Gopher/Library/Classic/devils.txt \
	-s "The Devil's Dictionary (1881-1906)" devil

dictzip devil.dict

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd,%{_bindir}}
%{__make} install dictdir="$RPM_BUILD_ROOT%{_datadir}/dictd/"
install journo.* devil.* $RPM_BUILD_ROOT%{_datadir}/dictd/
install dictfmt $RPM_BUILD_ROOT%{_bindir}

# jargon has separate package
rm -f $RPM_BUILD_ROOT%{_datadir}/dictd/jargon.*

for i in easton elements foldoc hitchcock world95 journo devil; do
dictprefix=%{_datadir}/dictd/$i
echo "# Misc Dictionaries - $i
database $i {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/$i.dictconf
done;

%clean
rm -rf $RPM_BUILD_ROOT

%post -n dict-devil
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-devil
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-easton
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-easton
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-elements
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-elements
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-foldoc
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-foldoc
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-hitchcock
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-hitchcock
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n dict-journo
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-journo
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%post -n dict-world95
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-world95
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files -n dict-devil
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/devil.dictconf
%{_datadir}/dictd/devil.*

%files -n dict-easton
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/easton.dictconf
%{_datadir}/dictd/easton*

%files -n dict-elements
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/elements.dictconf
%{_datadir}/dictd/elements.*

%files -n dict-foldoc
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/foldoc.dictconf
%{_datadir}/dictd/foldoc.*

%files -n dict-hitchcock
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/hitchcock.dictconf
%{_datadir}/dictd/hitchcock*

%files -n dict-journo
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/journo.dictconf
%{_datadir}/dictd/journo.*

%files -n dict-world95
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/world95.dictconf
%{_datadir}/dictd/world95.*

%files -n dict-fmt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dictfmt
