# Description:
#   Functional test code for Dagger-Android

package(default_visibility = ["//visibility:public"])



load(
    "//:build_defs.bzl",
    "DOCLINT_HTML_AND_SYNTAX",
    "PRE_JAVA_8_INFERENCE_OPTS",
    "JAVA_6_SOURCE_LEVEL",
)

# Sample code to be tested in functional tests.
android_library(
    name = "android",
    testonly = 1,
    srcs = glob(["*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + JAVA_6_SOURCE_LEVEL + DOCLINT_HTML_AND_SYNTAX,
    # NOTE: This should not depend on Guava or jsr305 to ensure that Dagger can be
    # used without a Guava and jsr305 deps.
    deps = [
        "//:dagger_with_compiler",
        "//android",
    ],
)

