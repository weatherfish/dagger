"""This file defines constants useful across the Dagger build."""

DOCLINT_HTML_AND_SYNTAX = ["-Xdoclint:html,syntax"]

DOCLINT_REFERENCES = ["-Xdoclint:reference"]


JAVA_6_SOURCE_LEVEL = ["-source 1.6"]

JAVA_7_SOURCE_LEVEL = ["-source 1.7"]

PRE_JAVA_8_INFERENCE_OPTS = [
    "-XDusePolyAttribution=false",
    "-XDuseStrictMethodClashCheck=false",
    "-XDuseGraphInference=false",
]
