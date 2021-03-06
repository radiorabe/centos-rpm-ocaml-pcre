#!/bin/bash
#
# RPM build wrapper for ocaml-pcre, runs inside the build container on travis-ci

set -xe

OBS_OS=`source /etc/os-release; echo $ID`

case $OBS_OS in
"centos")
    OBS_DIST="CentOS_7"
    yum -y install \
        epel-release
    ;;
"fedora")
    V=`source /etc/os-release; echo $VERSION_ID`
    OBS_DIST="Fedora_${V}_standard"
    ;;
esac

curl -o /etc/yum.repos.d/liquidsoap.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/${OBS_DIST}/home:radiorabe:liquidsoap.repo"

chown root:root ocaml-pcre.spec

build-rpm-package.sh ocaml-pcre.spec
