# Description:
#   A JSR-330 compliant dependency injection system for android and java

package(default_visibility = ["//visibility:public"])



load("//:build_defs.bzl", "DOCLINT_HTML_AND_SYNTAX", "DOCLINT_REFERENCES")

COMPILER_SRCS = glob(
    ["src/main/java/**/*.java"],
)

COMPILER_PLUGINS = [
    # TODO(cgruber): Enable Beta checker.
]

COMPILER_SHARED_DEPS = [
    "//:auto_service",
    "//:auto_value",
    "@auto_common//jar",
    "@error_prone_annotations//jar",
    "//:google_java_format",
    "@javapoet//jar",
    "@jsr_305//jar",
    "@jsr330//jar",
    "//core",
    "//producers",
    "@local_jdk//:lib/tools.jar",
]

java_library(
    name = "compiler",
    srcs = COMPILER_SRCS,
    javacopts = DOCLINT_HTML_AND_SYNTAX + DOCLINT_REFERENCES,
    plugins = COMPILER_PLUGINS,
    deps = COMPILER_SHARED_DEPS + [
        "@guava//jar"
    ],
)


java_plugin(
    name = "component-codegen",
    generates_api = 1,
    processor_class = "dagger.internal.codegen.ComponentProcessor",
    deps = [":compiler"],
)

load("//:test_defs.bzl", "GenJavaTests")

GenJavaTests(
    name = "compiler_tests",
    srcs = glob(["src/test/java/**/*.java"]),
    javacopts = DOCLINT_HTML_AND_SYNTAX,
    plugins = [":component-codegen"],
    deps = [
        ":compiler",
        "@auto_common//jar",
        "//:auto_value",
        "@compile_testing//jar",
        "@local_jdk//:lib/tools.jar",  # this is a dep for compile_testing, but bazel
        # can't recognize it in the java_library.runtime_deps
        "@javapoet//jar",
        "@jsr330//jar",
        "@junit//jar",
        "//:mockito",
        "@truth//jar",
        "//core",
        "//producers",
        "@guava//jar",
    ],
)

test_suite(name = "AllTests")

test_suite(
    name = "UnitAndFunctionalTests",
    tests = [
        ":AllTests",
        "//compiler/src/it/functional-tests:AllTests",
        "//compiler/src/it/producers-functional-tests:AllTests",
        "//compiler/src/it/tck:AllTests",
    ],
)

