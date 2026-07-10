%global tl_name atveryend
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.12
Release:	%{tl_revision}.1
Summary:	Hooks at the very end of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/atveryend
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atveryend.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atveryend.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atveryend.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides some wrapper commands around LaTeX end
document hooks.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/atveryend
%dir %{_datadir}/texmf-dist/source/latex/atveryend
%dir %{_datadir}/texmf-dist/tex/latex/atveryend
%doc %{_datadir}/texmf-dist/doc/latex/atveryend/README.md
%doc %{_datadir}/texmf-dist/doc/latex/atveryend/atveryend.pdf
%doc %{_datadir}/texmf-dist/source/latex/atveryend/atveryend.dtx
%{_datadir}/texmf-dist/tex/latex/atveryend/atveryend.sty
