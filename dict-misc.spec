%define		dictname misc
Summary:	Miscellaneous dictionaries for DICTD
Summary(pl):	R騜ne s這wniki dla dictd
Name:		dict-%{dictname}
Version:	1.5
Release:	9
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
Source1:	http://dsl.org/faq/fjd/journo-1.1.tar.gz
Source2:	http://wiretap.area.com/Gopher/Library/Classic/devils.txt
Source3:	http://ptm.linux.pl/slownik
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
Ten pakiet zawiera r騜ne s這wniki do u篡wania z serwerem s這wnika
dictd.

%package -n dict-devil
Summary:	Devil's dictionary for DICTD
Summary(pl):	S這wnik Devil's Dictionary dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-devil
This package contains The Devil's Dictionary, a cynical and irreverent
dictionary of common words, formatted for use by the dictionary server
in the dictd package.

%description -n dict-devil -l pl
S這wnik The Devil's Dictionary, zawieraj帷y cyniczne i lekcewa膨ce
opisy s堯w - do u篡wania z serwerem s這wnika dictd.

%package -n dict-easton
Summary:	easton dictionary for DICTD
Summary(pl):	S這wnik easton dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-easton
This package contains Easton's 1897 Bible Dictionary, based on M.G.
Easton M.A., D.D.'s Illustrated Bible Dictionary, Third Edition,
published by Thomas Nelson, 1897, for use by the dictionary server in
the dictd package.

%description -n dict-easton -l pl
Ten pakiet zawiera s這wnik Easton's 1897 Bible Dictionary do u篡wania
z serwerem s這wnika dictd.

%package -n dict-elements
Summary:	elements dictionary for DICTD
Summary(pl):	S這wnik elements dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-elements
This package contains a freely-distributed database of elemental
information, edited by Jay Kominek, for use by the dictionary server
in the dictd package.

%description -n dict-elements -l pl
Ten pakiet zawiera baz� danych informacji o pierwiastkach,
przygotowan� przez Jaya Kominka, do u篡wania z serwerem s這wnika
dictd.

%package -n dict-foldoc
Summary:	foldoc dictionary for DICTD
Summary(pl):	S這wnik foldoc dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-foldoc
This package contains The Free On-line Dictionary of Computing for use
by the dictionary server in the dictd package.

%description -n dict-foldoc -l pl
Ten pakiet zawiera s這wnik The Free On-line Dictionary of Computing do
u篡wania z serwerem s這wnika dictd.

%package -n dict-hitchcock
Summary:	hitchcock dictionary for DICTD
Summary(pl):	S這wnik hitchcock dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-hitchcock
This package contains Hitchcock's Bible Names Dictionary, derived from
Hitchcock's New and Complete Analysis of the Holy Bible, published in
the late 1800's, for use by the dictionary server in the dictd
package.

%description -n dict-hitchcock -l pl
Ten pakiet zawiera s這wnik Hitchcock's Bible Names Dictionary do
u篡wania z serwerem s這wnika dictd.

%package -n dict-journo
Summary:	Journalism dictionary for DICTD
Summary(pl):	S這wnik Journalism dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-journo
This package contains Free Journalism Dictionary for use by the
dictionary server in the dictd package.

%description -n dict-journo -l pl
Ten pakiet zawiera s這wnik Free Journalism Dictionary do u篡wania z
serwerem s這wnika dictd.

%package -n dict-ptm
Summary:	PTM dictionary for DICTD
Summary(pl):	S這wnik PTM dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-ptm
This package contains dictionary created by Projekt Tlumaczenia
Manuali for use by the dicitonary server in the dictd package.

%description -n dict-ptm -l pl
Ten pakiet zawiera s這wnik Projektu T逝maczenia Manuali, do u篡cia z
serwerem dictd.

%package -n dict-world95
Summary:	world95 dictionary for DICTD
Summary(pl):	S這wnik world95 dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description -n dict-world95
This package contains The 1995 CIA World Factbook for use by the
dictionary server in the dictd package.

%description -n dict-world95 -l pl
Ten pakiet zawiera s這wnik The 1995 CIA World Factbook do u篡wania z
serwerem s這wnika dictd.

%prep
%setup -q -a1
cp %{SOURCE2} ./
cp %{SOURCE3} ./

%build
%{__autoconf}
%configure
%{__make} db

sed -e 's/^[[:alpha:]]\{2,\}$/:&:/' < journo-1.1/journalism.dict \
	> journalism.txt
./dictfmt -j -u "http://dsl.org/lit/" -s Journalism journo < journalism.txt
dictzip journo.dict

sed 's/^[[:upper:]]\{2,\}/:&:/' ./devils.txt | ./dictfmt \
	-j -u http://wiretap.area.com/Gopher/Library/Classic/devils.txt \
	-s "The Devil's Dictionary (1881-1906)" devil

dictzip devil.dict

egrep -v "^#" slownik > slownik.1
tr -d \[\] <slownik.1 > slownik.2
tr 膧捷鹵潭� eoaslzzcn <slownik.2 > slownik.3
sed -e 's/^\([[:alnum:]]\{2,\}\)\ \ /:\1:/' < slownik.3 > slownik.4
./dictfmt -j -u "http://ptm.linux.pl/slownik" -s "Projekt Tlumaczenia Manuali" ptm < slownik.4
dictzip ptm.dict

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd,%{_bindir}}
%{__make} install dictdir="$RPM_BUILD_ROOT%{_datadir}/dictd/"
install ptm.* journo.* devil.* $RPM_BUILD_ROOT%{_datadir}/dictd/

# jargon has separate package
rm -f $RPM_BUILD_ROOT%{_datadir}/dictd/jargon.*

for i in easton elements foldoc hitchcock world95 journo ptm devil; do
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

%post -n dict-ptm
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n dict-ptm
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
%{_datadir}/dictd/easton.*

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
%{_datadir}/dictd/hitchcock.*

%files -n dict-journo
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/journo.dictconf
%{_datadir}/dictd/journo.*

%files -n dict-ptm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/ptm.dictconf
%{_datadir}/dictd/ptm.*

%files -n dict-world95
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/world95.dictconf
%{_datadir}/dictd/world95.*
