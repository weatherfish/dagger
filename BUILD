package(default_visibility = ["//visibility:public"])

java_plugin(
    name = "auto_value_processor",
    processor_class = "com.google.auto.value.processor.AutoValueProcessor",
    deps = [
        ":auto_service",
        "@auto_common//jar",
        "@auto_value//jar",
        "@guava//jar",
    ],
)

java_plugin(
    name = "auto_annotation_processor",
    processor_class = "com.google.auto.value.processor.AutoAnnotationProcessor",
    deps = [
        ":auto_service",
        "@auto_common//jar",
        "@auto_value//jar",
        "@guava//jar",
    ],
)

java_library(
    name = "auto_value",
    exported_plugins = [
        ":auto_value_processor",
        ":auto_annotation_processor",
    ],
    exports = [
        "@auto_value//jar",
        "@jsr_250//jar",
    ],
)

java_plugin(
    name = "auto_factory_processor",
    processor_class = "com.google.auto.factory.processor.AutoFactoryProcessor",
    deps = [
        ":auto_service",
        "@auto_common//jar",
        "@auto_factory//jar",
        "@guava//jar",
        "@java_writer//jar",
    ],
)

java_library(
    name = "auto_factory",
    exported_plugins = [":auto_factory_processor"],
    exports = ["@auto_factory//jar"],
)

java_plugin(
    name = "auto_service_processor",
    processor_class = "com.google.auto.service.processor.AutoServiceProcessor",
    deps = [
        "@auto_common//jar",
        "@auto_service//jar",
        "@guava//jar",
    ],
)

java_library(
    name = "auto_service",
    exported_plugins = [":auto_service_processor"],
    exports = ["@auto_service//jar"],
)

java_library(
    name = "google_java_format",
    exports = ["@google_java_format_1_1_all//jar"],
)

java_library(
    name = "dagger_with_compiler",
    exported_plugins = ["//compiler:component-codegen"],
    exports = ["//core"],
)

java_library(
    name = "producers_with_compiler",
    exports = [
        ":dagger_with_compiler",
        "//producers",
    ],
)

java_library(
    name = "mockito",
    exports = ["@mockito//jar"],
    runtime_deps = [
        "@hamcrest_core//jar",
        "@objenesis//jar",
    ],
)

java_library(
    name = "compile_testing",
    exports = [
        "@compile_testing//jar",
    ],
    runtime_deps = [
        ":auto_value",
        "@error_prone_annotations//jar",
        "@guava//jar",
        "@jsr_305//jar",
        "@junit//jar",
        "@truth//jar",
    ],
)
