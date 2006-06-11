%define		dictname misc
Summary:	Miscellaneous dictionaries for DICTD
Summary(pl):	Ró¿ne s³owniki dla dictd
Name:		dict-%{dictname}
Version:	1.5
Release:	15
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
# Source0-md5:	74a41d916b76323482b273f8b53c31bf
Source1:	http://dsl.org/faq/fjd/journo-1.1.tar.gz
# Source1-md5:	e7ee9a7694e5640cca02da993839771a
Source2:	http://wiretap.area.com/Gopher/Library/Classic/devils.txt
# Source2-md5:	56b2918934d8f1162ec0f711df8c9669
Source3:	http://ptm.linux.pl/slownik
# Source3-md5:	7edc21ffad074041097e9f9f0e2c2b15
Source4:	http://www.prime-project.org/dict/dict-world02--2003-02-15.tar.gz
# Source4-md5:	344bd453d17536e281f1874cfd318c7d
Source5:	http://foldoc.org/foldoc/Dictionary.gz
# Source5-md5:	c93dcdd00ac3ba1436ffe3cff2a27493
URL:		http://www.dict.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dictfmt
BuildRequires:	dictzip
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains misc dictionaries for use by the dictionary
server in the dictd package.

%description -l pl
Ten pakiet zawiera ró¿ne s³owniki do u¿ywania z serwerem s³ownika
dictd.

%package -n dict-devil
Summary:	Devil's dictionary for DICTD
Summary(pl):	S³ownik Devil's Dictionary dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description -n dict-devil
This package contains The Devil's Dictionary, a cynical and irreverent
dictionary of common words, formatted for use by the dictionary server
in the dictd package.

%description -n dict-devil -l pl
S³ownik The Devil's Dictionary, zawieraj±cy cyniczne i lekcewa¿±ce
opisy s³ów - do u¿ywania z serwerem s³ownika dictd.

%package -n dict-easton
Summary:	Easton's dictionary for DICTD
Summary(pl):	S³ownik Eastona dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description -n dict-easton
This package contains Easton's 1897 Bible Dictionary, based on M.G.
Easton M.A., D.D.'s Illustrated Bible Dictionary, Third Edition,
published by Thomas Nelson, 1897, for use by the dictionary server in
the dictd package.

%description -n dict-easton -l pl
Ten pakiet zawiera s³ownik Easton's 1897 Bible Dictionary do u¿ywania
z serwerem s³ownika dictd.

%package -n dict-elements
Summary:	Elements dictionary for DICTD
Summary(pl):	S³ownik pierwiastków dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description -n dict-elements
This package contains a freely-distributed database of elemental
information, edited by Jay Kominek, for use by the dictionary server
in the dictd package.

%description -n dict-elements -l pl
Ten pakiet zawiera bazê danych informacji o pierwiastkach,
przygotowan± przez Jaya Kominka, do u¿ywania z serwerem s³ownika
dictd.

%package -n dict-foldoc
Summary:	The Free On-line Dictionary of Computing for DICTD
Summary(pl):	Darmowy s³ownik z dziedziny obliczeñ dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description -n dict-foldoc
This package contains The Free On-line Dictionary of Computing for use
by the dictionary server in the dictd package.

%description -n dict-foldoc -l pl
Ten pakiet zawiera s³ownik The Free On-line Dictionary of Computing do
u¿ywania z serwerem s³ownika dictd.

%package -n dict-hitchcock
Summary:	Hitchcock's dictionary for DICTD
Summary(pl):	S³ownik Hitchcocka dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description -n dict-hitchcock
This package contains Hitchcock's Bible Names Dictionary, derived from
Hitchcock's New and Complete Analysis of the Holy Bible, published in
the late 1800's, for use by the dictionary server in the dictd
package.

%description -n dict-hitchcock -l pl
Ten pakiet zawiera s³ownik Hitchcock's Bible Names Dictionary do
u¿ywania z serwerem s³ownika dictd.

%package -n dict-journo
Summary:	Journalism dictionary for DICTD
Summary(pl):	S³ownik Journalism dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description -n dict-journo
This package contains Free Journalism Dictionary for use by the
dictionary server in the dictd package.

%description -n dict-journo -l pl
Ten pakiet zawiera s³ownik Free Journalism Dictionary do u¿ywania z
serwerem s³ownika dictd.

%package -n dict-ptm
Summary:	PTM dictionary for DICTD
Summary(pl):	S³ownik PTM dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description -n dict-ptm
This package contains dictionary created by Projekt Tlumaczenia
Manuali for use by the dicitonary server in the dictd package.

%description -n dict-ptm -l pl
Ten pakiet zawiera s³ownik Projektu T³umaczenia Manuali, do u¿ycia z
serwerem dictd.

%package -n dict-CIAworldbook
Summary:	CIAworldbook dictionary for DICTD
Summary(pl):	S³ownik CIAworldbook dla dictd
Group:		Applications/Dictionaries
URL:		http://www.prime-project.org/dict/
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
Obsoletes:	dict-world95

%description -n dict-CIAworldbook
This package contains The 2002 CIA World Factbook for use by the
dictionary server in the dictd package.

%description -n dict-CIAworldbook -l pl
Ten pakiet zawiera s³ownik The 2002 CIA World Factbook do u¿ywania z
serwerem s³ownika dictd.

%prep
%setup -q -a1 -a4
cp %{SOURCE2} ./
cp %{SOURCE3} ./
zcat %{SOURCE5} > data/Dictionary

%build
%{__autoconf}
cp -f /usr/share/automake/install-sh .
cp -f /usr/share/automake/config.sub .
%configure
%{__make} db

sed 's/^[[:alpha:]]\{2,\}$/:&:/' fjd/journalism.dict | \
	dictfmt -j -u "http://dsl.org/lit/" -s Journalism journo
dictzip journo.dict

sed 's/^[[:upper:]]\{2,\}/:&:/' devils.txt | \
	dictfmt -j -u http://wiretap.area.com/Gopher/Library/Classic/devils.txt \
	-s "The Devil's Dictionary (1881-1906)" devil
dictzip devil.dict

#egrep -v "^#" slownik | tr -d \[\] | tr êó±¶³¿¼æñ eoaslzzcn | \
egrep -v "^#" slownik | tr -d \[\] | \
	sed 's/^\([[:alnum:]]\{2,\}\)\ \ /:\1:/' | \
	dictfmt -j -u "http://ptm.linux.pl/slownik" \
	-s "Projekt Tlumaczenia Manuali" ptm
dictzip ptm.dict

cd world02-2003-02-15
dictzip world02.dict
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd,%{_bindir}}

%{__make} install \
	dictdir=$RPM_BUILD_ROOT%{_datadir}/dictd
install ptm.* journo.* devil.* $RPM_BUILD_ROOT%{_datadir}/dictd
install world02-2003-02-15/world02.* $RPM_BUILD_ROOT%{_datadir}/dictd

# jargon has separate package
rm -f $RPM_BUILD_ROOT%{_datadir}/dictd/jargon.*

for i in easton elements foldoc hitchcock world02 journo ptm devil; do
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
%service dictd restart

%postun -n dict-devil
%service dictd restart

%post -n dict-easton
%service dictd restart

%postun -n dict-easton
%service dictd restart

%post -n dict-elements
%service dictd restart

%postun -n dict-elements
%service dictd restart

%post -n dict-foldoc
%service dictd restart

%postun -n dict-foldoc
%service dictd restart

%post -n dict-hitchcock
%service dictd restart

%postun -n dict-hitchcock
%service dictd restart

%post -n dict-journo
%service dictd restart

%postun -n dict-journo
%service dictd restart

%post -n dict-ptm
%service dictd restart

%postun -n dict-ptm
%service dictd restart

%post -n dict-CIAworldbook
%service dictd restart

%postun -n dict-CIAworldbook
%service dictd restart

%files -n dict-devil
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/devil.dictconf
%{_datadir}/dictd/devil.*

%files -n dict-easton
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/easton.dictconf
%{_datadir}/dictd/easton.*

%files -n dict-elements
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/elements.dictconf
%{_datadir}/dictd/elements.*

%files -n dict-foldoc
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/foldoc.dictconf
%{_datadir}/dictd/foldoc.*

%files -n dict-hitchcock
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/hitchcock.dictconf
%{_datadir}/dictd/hitchcock.*

%files -n dict-journo
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/journo.dictconf
%{_datadir}/dictd/journo.*

%files -n dict-ptm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/ptm.dictconf
%{_datadir}/dictd/ptm.*

%files -n dict-CIAworldbook
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/world02.dictconf
%{_datadir}/dictd/world02.*
