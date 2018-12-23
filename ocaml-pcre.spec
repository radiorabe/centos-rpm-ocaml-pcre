Name:     ocaml-pcre
Version:  7.3.4
Release:  0.1%{dist}
Summary:  OCAML PCRE Bindings

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  LGPLv2
URL:      https://github.com/mmottl/pcre-ocaml
Source0:  https://github.com/mmottl/pcre-ocaml/releases/download/%{version}/pcre-%{version}.tbz


BuildRequires: jbuilder
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-configurator-devel
BuildRequires: ocaml-sexplib0-devel
BuildRequires: ocaml-stdio-devel
BuildRequires: pcre
BuildRequires: pcre-devel

%description
This OCaml-library interfaces the C-library PCRE (Perl-compatibility
Regular Expressions). It can be used for string matching with
"PERL"-style regular expressions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

%build
pushd src
jbuilder external-lib-deps --missing --profile dev pcre.cma libpcre_stubs.a
jbuilder build --dev
popd
dune build @install

%install
install -d %{buildroot}/%{_libdir}/ocaml
pushd src
jbuilder install --libdir=%{buildroot}%{_libdir}/ocaml --prefix=%{buildroot}%{_libdir}/ocaml
popd

%files
%doc README.md
%doc %{_libdir}/ocaml/doc/%{libname}
%license LICENSE.md
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.ml
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license LICENSE.md
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Dec 23 2018 Lucas Bickel <hairmare@rabe.ch> - 7.3.4-0.1
- Fix jbuilder call for non x86_64 archs

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 7.3.4-0.0
- Onboard pcre package into LSD

* Sat Oct 20 2012 Martin Konecny <martin.konecny@gmail.com> - 1.0-2
- initial version
