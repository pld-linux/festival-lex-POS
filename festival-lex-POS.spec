Summary:	'Part of Speech' lexical models
Summary(pl.UTF-8):	Modele leksykalne części mowy
Name:		festival-lex-POS
Version:	0.1
Release:	4
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festlex_POSLEX.tar.gz
# Source0-md5:	742c266e4c4978fae2b5c1bf6f549eb4
# newer source (2.4) is just repacked, so tarball md5 is different (but contents are equal)
#Source0:	http://www.cstr.ed.ac.uk/downloads/festival/2.4/festlex_POSLEX.tar.gz
URL:		http://www.cstr.ed.ac.uk/projects/festival/
Requires:	festival
Requires:	festival-lex-english
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a lexicon and an ngram for English part of
speech tagging. Information in these files were derived from the Penn
Tree Bank distributed by the LDC, in tur derived from data from the
Wall Street Journal.

%description -l pl.UTF-8
Ten pakiet zawiera leksykon i n-gramy do znaczników angielskich części
mowy. Informacje umieszczone w tych plikach pochodzą z Penn Tree Bank
rozpowszechnianego przez LDC, opartego na danych pochodzących z Wall
Street Journal.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/dicts

cd festival/lib/dicts
install wsj* $RPM_BUILD_ROOT%{_datadir}/festival/lib/dicts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/dicts/COPYING.poslex
%{_datadir}/festival/lib/dicts/wsj.wp39.poslexR
%{_datadir}/festival/lib/dicts/wsj.wp39.tri.ngrambin
