# Description:
#   An asynchronous dependency injection system that extends JSR-330.

package(default_visibility = ["//visibility:public"])



load(
    "//:build_defs.bzl",
    "DOCLINT_HTML_AND_SYNTAX",
    "DOCLINT_REFERENCES",
    "JAVA_6_SOURCE_LEVEL",
    "JAVA_7_SOURCE_LEVEL",
    "PRE_JAVA_8_INFERENCE_OPTS",
)

java_library(
    name = "producers",
    srcs = glob(["src/main/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + JAVA_6_SOURCE_LEVEL + DOCLINT_HTML_AND_SYNTAX + DOCLINT_REFERENCES,
    plugins = [
        # TODO(cgruber): Enable Beta checker.
    ],
    exports = [
        "@guava//jar",
        "@jsr330//jar",
    ],
    deps = [
        "@guava//jar",
        "@jsr_305//jar",
        "@jsr330//jar",
        "//core",
    ],
)


load("//:test_defs.bzl", "GenJavaTests")

GenJavaTests(
    name = "produces_tests",
    srcs = glob(["src/test/java/**/*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + JAVA_7_SOURCE_LEVEL,
    deps = [
        ":producers",
        "@guava//jar",
        "@junit//jar",
        "//:mockito",
        "@truth//jar",
        "@guava_testlib//jar",
    ],
)

