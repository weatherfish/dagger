# Description:
#   A JSR-330 compliant dependency injection system for android and java

package(default_visibility = ["//visibility:public"])



load(
    "//:build_defs.bzl",
    "DOCLINT_HTML_AND_SYNTAX",
    "JAVA_6_SOURCE_LEVEL",
    "PRE_JAVA_8_INFERENCE_OPTS",
)

java_library(
    name = "core",
    srcs = glob(["**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + JAVA_6_SOURCE_LEVEL + DOCLINT_HTML_AND_SYNTAX,
    exports = ["@jsr330//jar"],
    deps = ["@jsr330//jar"],
)

