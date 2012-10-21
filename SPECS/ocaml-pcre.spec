Name:     pcre-ocaml 
Version:  6.2.5
Release:  1
Summary:  OCAML PCRE Bindings
License:  GPLv2+
URL:      https://bitbucket.org/mmottl/pcre-ocaml/ 
Source0:  https://bitbucket.org/mmottl/pcre-ocaml/downloads/pcre-ocaml-6.2.5.tar.gz
Patch1:   pcre-ocaml-makefile.patch


BuildRequires: pcre 

%prep
%setup -q
%patch1 -p1

%build
make

%install
#%make_install 
#DESTDIR=%{buildroot}/usr/lib64/ocaml
mkdir -p %{buildroot}/usr/lib64/ocaml
make DESTDIR=%{buildroot}/usr/lib64/ocaml install

%files
/usr/lib64/ocaml/pcre/META
/usr/lib64/ocaml/pcre/dllpcre_stubs.so
/usr/lib64/ocaml/pcre/libpcre_stubs.a
/usr/lib64/ocaml/pcre/pcre.a
/usr/lib64/ocaml/pcre/pcre.cma
/usr/lib64/ocaml/pcre/pcre.cmi
/usr/lib64/ocaml/pcre/pcre.cmxa
/usr/lib64/ocaml/pcre/pcre.mli

%description
This OCaml-library interfaces the C-library PCRE (Perl-compatibility Regular Expressions). It can be used for matching regular expressions which are written in "PERL"-style.

%changelog
* Sat Oct 20 2012 Martin Konecny <martin dot konecny at gmail.com> - 1.0-2
- initial version 
