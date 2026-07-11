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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides some wrapper commands around LaTeX end
document hooks.

