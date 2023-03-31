Name:		texlive-ddphonism
Version:	52009
Release:	2
Summary:	Dodecaphonic diagrams: twelve-tone matrices, clock diagrams, etc.
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ddphonism
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ddphonism.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ddphonism.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a music-related package which is focused on notation
from the Twelve-Tone System, also called Dodecaphonism. It
provides LaTeX algorithms that produce typical dodecaphonic
notation based off a musical series, or row sequence, of
variable length. The package requires etoolbox, pgfkeys, TikZ,
xparse, and xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ddphonism
%doc %{_texmfdistdir}/doc/latex/ddphonism

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
