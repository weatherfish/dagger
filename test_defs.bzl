def GenJavaTests(name, srcs, deps, plugins = None, javacopts = None):
  _GenTests(native.java_test, name, srcs, deps, plugins, javacopts)

def GenRobolectricTests(name, srcs, deps, plugins = None, javacopts = None):
  # TODO(ronshapiro): enable these when Bazel supports robolectric tests
  pass

def _GenTests(rule_type, name, srcs, deps, plugins = None, javacopts = None):
  test_files = []
  supporting_files = []
  for src in srcs:
    if src.endswith("Test.java"):
      test_files.append(src)
    else:
      supporting_files.append(src)

  test_deps = [] + deps
  if len(supporting_files) > 0:
    supporting_files_name = name + "_supporting_files"
    test_deps.append(":" + supporting_files_name)
    native.java_library(
        name = supporting_files_name,
        deps = deps,
        srcs = supporting_files,
        plugins = plugins,
        javacopts = javacopts,
        testonly = 1,
    )

  for test_file in test_files:
    test_name = test_file.replace(".java", "")
    rule_type(
        name = test_name,
        deps = test_deps,
        srcs = [test_file],
        plugins = plugins,
        javacopts = javacopts,
        test_class = test_name.replace("src/test/java/", '').replace("/", "."),
    )
