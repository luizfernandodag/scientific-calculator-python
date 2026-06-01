import importlib.util
import pathlib
import sys
import unittest


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str) -> unittest.TestSuite:
    project_root = pathlib.Path(__file__).resolve().parent
    sys.path.insert(0, str(project_root))

    test_file = project_root / "test" / "tests.py"
    spec = importlib.util.spec_from_file_location("project_test_module", test_file)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load test file: {test_file}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return loader.loadTestsFromModule(module)


if __name__ == "__main__":
    unittest.main()
