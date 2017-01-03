# Description:
#   Functional test code for Dagger-Android

package(default_visibility = ["//visibility:public"])



load(
    "//:build_defs.bzl",
    "DOCLINT_HTML_AND_SYNTAX",
    "PRE_JAVA_8_INFERENCE_OPTS",
)

load("//:test_defs.bzl", "GenRobolectricTests")

GenRobolectricTests(
    name = "android-tests",
    srcs = glob(["*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + DOCLINT_HTML_AND_SYNTAX,
    deps = [
        "@guava//jar",
        "@guava_testlib//jar",
        "@junit//jar",
        "@truth//jar",
        "//android/src/it/functional-tests/src/main/java/test/android",
    ],
)

test_suite(name = "AllTests")

