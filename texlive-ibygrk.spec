Name:		texlive-ibygrk
Version:	4.5
Release:	1
Summary:	Fonts and macros to typeset ancient Greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/ibygrk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibygrk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibygrk.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Ibycus is a Greek typeface, based on Silvio Levy's realisation
of a classic Didot cut of Greek type from around 1800. The
fonts are available both as MetaFont source and in Adobe Type 1
format. This distribution of ibycus is accompanied by a set of
macro packages to use it with Plain TeX or LaTeX, but for use
with Babel, see the ibycus-babel package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/ibygrk/fibb84.afm
%{_texmfdistdir}/fonts/afm/public/ibygrk/fibr84.afm
%{_texmfdistdir}/fonts/enc/dvips/ibygrk/IbycusHTG.enc
%{_texmfdistdir}/fonts/map/dvips/ibygrk/iby.map
%{_texmfdistdir}/fonts/source/public/ibygrk/abary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/cigma4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/digamma4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ebary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibb84.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibb848.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibb849.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibo84.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibo848.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibo849.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibr84.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibr848.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibr849.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/hbary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibyacc4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibycus4.map
%{_texmfdistdir}/fonts/source/public/ibygrk/ibycus4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibylig4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibylwr4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibypnct4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibyupr4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/koppa4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/obary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/sampi4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ubary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/version4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/wbary4.mf
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibb84.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibb848.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibb849.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibo84.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibo848.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibo849.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibr84.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibr848.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibr849.tfm
%{_texmfdistdir}/fonts/type1/public/ibygrk/fibb84.pfb
%{_texmfdistdir}/fonts/type1/public/ibygrk/fibr84.pfb
%{_texmfdistdir}/tex/generic/ibygrk/Uibycus.fd
%{_texmfdistdir}/tex/generic/ibygrk/Uibycus4.fd
%{_texmfdistdir}/tex/generic/ibygrk/iby4extr.tex
%{_texmfdistdir}/tex/generic/ibygrk/ibycus4.map
%{_texmfdistdir}/tex/generic/ibygrk/ibycus4.sty
%{_texmfdistdir}/tex/generic/ibygrk/ibycus4.tex
%{_texmfdistdir}/tex/generic/ibygrk/ibycusps.tex
%{_texmfdistdir}/tex/generic/ibygrk/psibycus.sty
%{_texmfdistdir}/tex/generic/ibygrk/pssetiby.tex
%{_texmfdistdir}/tex/generic/ibygrk/setiby4.tex
%{_texmfdistdir}/tex/generic/ibygrk/tlgsqq.tex
%{_texmfdistdir}/tex/generic/ibygrk/version4.tex
%doc %{_texmfdistdir}/doc/fonts/ibygrk/COPYING
%doc %{_texmfdistdir}/doc/fonts/ibygrk/NEWS
%doc %{_texmfdistdir}/doc/fonts/ibygrk/README
%doc %{_texmfdistdir}/doc/fonts/ibygrk/README.ibycus4
%doc %{_texmfdistdir}/doc/fonts/ibygrk/iby4text.tex
%doc %{_texmfdistdir}/doc/fonts/ibygrk/ibycus3.RME
%doc %{_texmfdistdir}/doc/fonts/ibygrk/ibycus4.ltx
%doc %{_texmfdistdir}/doc/fonts/ibygrk/psibycus.ltx
%doc %{_texmfdistdir}/doc/fonts/ibygrk/psibycus.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
