After pulling, make sure to run 

"mkdir -p {BUILD,RPMS,SOURCES,SPECS,SRPMS}" 

inside your git repository to create all necessary directories.

You can run 

"rpmbuild -ba SPECS/ocaml-pcre.spec" 

from the base directory to build the package. Do *not* run this as root.

Currently there is one patch file which adds support to the OCamlMakefile
for specifying the destination directory (necessary for an RPM build)
