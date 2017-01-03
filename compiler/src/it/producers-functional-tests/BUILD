# Description:
#   Functional tests for Dagger Producers

package(default_visibility = ["//visibility:public"])



load(
    "//:build_defs.bzl",
    "DOCLINT_HTML_AND_SYNTAX",
    "DOCLINT_REFERENCES",
    "JAVA_7_SOURCE_LEVEL",
    "PRE_JAVA_8_INFERENCE_OPTS",
)

# Sample code to be tested in functional tests.
java_library(
    name = "code_under_test",
    srcs = glob(["src/main/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + JAVA_7_SOURCE_LEVEL + DOCLINT_HTML_AND_SYNTAX,
    deps = [
        "@guava//jar",
        "//:auto_value",
        "//:producers_with_compiler",
        "@jsr330//jar",
    ],
)

load("//:test_defs.bzl", "GenJavaTests")

GenJavaTests(
    name = "producers-functional-tests",
    srcs = glob(["src/test/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + JAVA_7_SOURCE_LEVEL + DOCLINT_HTML_AND_SYNTAX + DOCLINT_REFERENCES,
    deps = [
        ":code_under_test",
        "@guava//jar",
        "//:producers_with_compiler",
        "@jsr330//jar",
        "@junit//jar",
        "//:mockito",
        "@truth//jar",
    ],
)

test_suite(name = "AllTests")

