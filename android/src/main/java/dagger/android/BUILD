# Description:
#   Public Dagger API for Android

package(default_visibility = ["//visibility:public"])



load(
    "//:build_defs.bzl",
    "DOCLINT_HTML_AND_SYNTAX",
    "DOCLINT_REFERENCES",
    "JAVA_6_SOURCE_LEVEL",
    "PRE_JAVA_8_INFERENCE_OPTS",
)

android_library(
    name = "android",
    srcs = glob(["*.java"]),
    javacopts = PRE_JAVA_8_INFERENCE_OPTS + JAVA_6_SOURCE_LEVEL + DOCLINT_HTML_AND_SYNTAX + DOCLINT_REFERENCES,
    deps = [
        "@androidsdk//com.android.support:support-annotations-24.2.0",
        "//:auto_value",
        "//:dagger_with_compiler",
    ],
)

