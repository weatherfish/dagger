#!/usr/bin/env python
import sys
from subprocess import check_output
import os
from xml_formatting import generate_pom

DEVNULL = open(os.devnull)

def shell(command):
  return check_output(command, shell=True, stderr=DEVNULL).strip()

def deps_of(label):
  return shell('bazel query --output=label_kind "labels("deps", %s)"' %label)

def bazel_query_label(attr, label):
  return shell('bazel query "labels("%s", %s)"' %(attr, label))

def pom_deps(label):
  accumulated_deps = set()
  for dep_line in deps_of(label).split('\n'):
    if len(dep_line) is 0: continue
    dep = dep_line.split(' ')[2]
    if dep_line.find('//:') is not -1:
      for export in bazel_query_label("exports", dep).split('\n'):
        accumulated_deps.add(export)
        accumulated_deps.update(pom_deps(export))
    else:
      accumulated_deps.add(dep)

  return accumulated_deps

def maven_jar(name, artifact, **kwargs):
  artifacts["@%s//jar:jar" %name] = artifact

# rules in the WORKSPACE file which should be parsed but ignored
def http_jar(**kwargs): pass
def workspace(**kwargs): pass
def load(*args): pass
def android_repositories(): pass

VERSION = sys.argv[1]
if __name__ == '__main__':
  artifacts = {}
  artifacts['google_java_format_1_1_all'] = 'com.google.googlejavaformat:googlejavaformat:1.1'
  artifacts['@androidsdk//com.android.support:support-annotations-24.2.0'] = 'com.android.support:support-annotations:24.2.0'

  artifacts['//core:core'] = 'com.google.dagger:dagger:%s' % VERSION
  artifacts['//core/src/main/java/dagger:core'] = artifacts['//core:core']
  artifacts['//compiler:compiler'] = 'com.google.dagger:dagger-compiler:%s' % VERSION
  artifacts['//producers:producers'] = 'com.google.dagger:dagger-producers:%s' % VERSION
  # DO NOT SUBMIT: this needs to create an aar pom
  artifacts['//android:android'] = 'com.google.dagger:dagger-android:%s' % VERSION
  artifacts['//android/src/main/java/dagger/android:android'] = artifacts["//android:android"]

  names = {}
  names['//core:core'] = 'Dagger'
  names['//core/src/main/java/dagger:core'] = names['//core:core']
  names['//compiler:compiler'] = 'Dagger Compiler'
  names['//producers:producers'] = 'Dagger Producers'
  names['//android:android'] = 'Dagger Android'
  names['//android/src/main/java/dagger/android:android'] = names['//android:android']

  with open('WORKSPACE', 'r') as f:
    eval(compile(f.read(), 'maven_jar_parse.out', 'exec'))

  for arg in sys.argv[2:]:
    print generate_pom(artifacts[arg], names[arg], map(artifacts.get, pom_deps(arg)), VERSION)
