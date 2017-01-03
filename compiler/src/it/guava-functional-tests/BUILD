# Description:
#   Functional tests for Dagger that depend on Guava

package(default_visibility = ["//visibility:public"])



load("//:build_defs.bzl", "DOCLINT_HTML_AND_SYNTAX", "PRE_JAVA_8_INFERENCE_OPTS")

java_library(
    name = "code_under_test",
    testonly = 1,
    srcs = glob(["src/main/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + DOCLINT_HTML_AND_SYNTAX,
    deps = [
        "@guava//jar",
        "//:auto_value",
        "//:dagger_with_compiler",
        "@jsr330//jar",
        "@junit//jar",
    ],
)

load("//:test_defs.bzl", "GenJavaTests")

GenJavaTests(
    name = "guava_functional_tests",
    srcs = glob(["src/test/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + DOCLINT_HTML_AND_SYNTAX,
    deps = [
        ":code_under_test",
        "@guava//jar",
        "//:auto_value",
        "//:dagger_with_compiler",
        "@jsr330//jar",
        "@junit//jar",
        "@truth//jar",
    ],
)

test_suite(name = "AllTests")

