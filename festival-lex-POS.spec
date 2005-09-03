Summary:	'Part of Speech' lexical models
Summary(pl):	Modele leksykalne czê¶ci mowy
Name:		festival-lex-POS
Version:	0.1
Release:	4
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festlex_POSLEX.tar.gz
# Source0-md5:	742c266e4c4978fae2b5c1bf6f549eb4
Requires:	festival
Requires:	festival-lex-english
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a lexicon and an ngram for English part of
speech tagging. Information in these files were derived from the Penn
Tree Bank distributed by the LDC, in tur derived from data from the
Wall Street Journal.

%description -l pl
Ten pakiet zawiera leksykon i n-gramy do znaczników angielskich czê¶ci
mowy. Informacje umieszczone w tych plikach pochodz± z Penn Tree Bank
rozpowszechnianego przez LDC, opartego na danych pochodz±cych z Wall
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
%{_datadir}/festival/lib/dicts/*
