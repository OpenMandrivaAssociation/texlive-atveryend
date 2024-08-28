Name:		texlive-atveryend
Version:	71991
Release:	1
Summary:	Hooks at the very end of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/atveryend
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atveryend.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atveryend.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atveryend.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX packages provides two hooks for \end{document} that
are executed after the hook of \AtEndDocument:
\AfterLastShipout can be used for code that is to be executed
right after the last \clearpage before the `.aux' file is
closed. \AtVeryEndDocument is used for code after closing and
final reading of the `.aux' file.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/atveryend
%{_texmfdistdir}/tex/latex/atveryend
%doc %{_texmfdistdir}/doc/latex/atveryend

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
