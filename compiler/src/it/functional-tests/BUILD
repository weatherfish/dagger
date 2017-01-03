# Description:
#   Functional tests for Dagger

package(default_visibility = ["//visibility:public"])



load(
    "//:build_defs.bzl",
    "DOCLINT_HTML_AND_SYNTAX",
    "DOCLINT_REFERENCES",
    "PRE_JAVA_8_INFERENCE_OPTS",
)

# Sample code to be tested in functional tests.
java_library(
    name = "code_under_test",
    testonly = 1,
    srcs = glob(
        ["src/main/java/**/*.java"],
    ),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + DOCLINT_HTML_AND_SYNTAX,
    # NOTE: This should not depend on Guava or jsr305 to ensure that Dagger can be
    # used without a Guava and jsr305 deps.
    deps = [
        "//:auto_factory",
        "//:auto_value",
        "//:dagger_with_compiler",
        "@jsr330//jar",
        "@junit//jar",
    ],
)


load("//:test_defs.bzl", "GenJavaTests")

GenJavaTests(
    name = "test_lib",
    srcs = glob(
        ["src/test/java/**/*.java"],
    ),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + DOCLINT_HTML_AND_SYNTAX + DOCLINT_REFERENCES,
    deps = [
        ":code_under_test",
        "@guava_testlib//jar",
        "@guava//jar",
        "//:auto_value",
        "//:dagger_with_compiler",
        "@jsr330//jar",
        "@junit//jar",
        "@truth//jar",
    ],
)


test_suite(name = "AllTests")

