# Description:
#  TCK tests for Dagger

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
    srcs = glob(["src/main/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + DOCLINT_HTML_AND_SYNTAX + [
        "-Adagger.privateMemberValidation=warning",
        "-Adagger.staticMemberValidation=warning",
        "-Adagger.ignorePrivateAndStaticInjectionForComponent=enabled",
    ],
    deps = [
        "//:dagger_with_compiler",
        "@jsr330//jar",
        "@jsr_330_tck//jar",
        "@junit//jar",
    ],
)

load("//:test_defs.bzl", "GenJavaTests")

GenJavaTests(
    name = "tck_tests",
    srcs = glob(["src/test/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + DOCLINT_HTML_AND_SYNTAX + DOCLINT_REFERENCES,
    deps = [
        ":code_under_test",
        "//:dagger_with_compiler",
        "@jsr330//jar",
        "@jsr_330_tck//jar",
        "@junit//jar",
    ],
)

test_suite(name = "AllTests")

