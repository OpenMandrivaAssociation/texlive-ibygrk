%global tl_name ibygrk
%global tl_revision 15878
%global tl_version 4.5

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Fonts and macros to typeset ancient Greek
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/ibygrk
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ibygrk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ibygrk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Ibycus is a Greek typeface, based on Silvio Levy's realisation of a
classic Didot cut of Greek type from around 1800. The fonts are
available both as Metafont source and in Adobe Type 1 format. This
distribution of ibycus is accompanied by a set of macro packages to use
it with Plain TeX or LaTeX, but for use with Babel, see the ibycus-babel
package.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from ibygrk:
MixedMap iby.map
TL_DROPIN_EOF
