Summary:	'Part of Speech' lexical models
Summary(pl):	Modele leksykalne czê¶ci mowy
Name:		festival-lex-POS
Version:	0.1
Release:	1
License:	Distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festlex_POSLEX.tar.gz
Requires:	festival
Requires:	festival-lex-english
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a lexicon and an ngram for English part of speech
tagging. Information in these files were derived from the Penn Tree Bank
diustributed by the LDC, in tur derived from data from the Wall Street Journal.

%prep
%setup -q -c %{name}-%{version}

%build

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
