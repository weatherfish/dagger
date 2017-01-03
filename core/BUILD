# Description:
#   A JSR-330 compliant dependency injection system for android and java

package(default_visibility = ["//visibility:public"])



load("//:build_defs.bzl", "DOCLINT_HTML_AND_SYNTAX", "DOCLINT_REFERENCES")
load("//:test_defs.bzl", "GenJavaTests")

java_library(
    name = "core",
    exports = ["//core/src/main/java/dagger:core"],
)


GenJavaTests(
    name = "core_tests",
    srcs = glob(["src/test/java/**/*.java"]),
    javacopts = DOCLINT_HTML_AND_SYNTAX + DOCLINT_REFERENCES,
    deps = [
        ":core",
        "@guava//jar",
        "@jsr330//jar",
        "@junit//jar",
        "@truth//jar",
    ],
)

test_suite(name = "AllTests")

