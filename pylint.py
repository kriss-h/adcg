import subprocess
import tempfile
import os
import ollama   # pip install ollama


def generate_code(prompt, model="codellama"):
    print("[+] Generating code...")
    response = ollama.generate(model=model, prompt=prompt)
    return response["response"]


def run_pylint(path):
    print("[+] Running pylint...")
    result = subprocess.run(["pylint", path], capture_output=True, text=True)
    return result.stdout


def run_pytest(test_dir):
    print("[+] Running pytest...")
    result = subprocess.run(["pytest", "-q", test_dir],
                            capture_output=True, text=True)
    return result.stdout + result.stderr


def simple_framework(code_prompt, test_prompt, model="codellama"):
    # 1. Generate code + tests
    code = generate_code(code_prompt, model)
    tests = generate_code(test_prompt, model)

    # 2. Create temp directory
    temp = tempfile.mkdtemp(prefix="simple_eval_")
    code_path = os.path.join(temp, "generated.py")
    test_dir = os.path.join(temp, "tests")
    os.makedirs(test_dir, exist_ok=True)
    test_path = os.path.join(test_dir, "test_generated.py")

    # 3. Save files
    with open(code_path, "w") as f:
        f.write(code)
    with open(test_path, "w") as f:
        f.write(tests)

    # 4. Run checks
    pylint_output = run_pylint(code_path)
    pytest_output = run_pytest(test_dir)

    # 5. Print summary
    print("\n======== CODE GENERATED ========\n")
    print(code)

    print("\n======== PYLINT REPORT ========\n")
    print(pylint_output)

    print("\n======== TEST RESULTS ========\n")
    print(pytest_output)

    print("\n======== SUMMARY ========\n")
    if "error" in pylint_output.lower():
        print("- Pylint reported issues.")
    else:
        print("- Pylint clean.")

    if "FAILED" in pytest_output:
        print("- Some tests failed.")
    else:
        print("- All tests passed.")

    print("\n[Done]")


# ------------ Example Run ------------
if __name__ == "__main__":
    simple_framework(
        "Write a Python function that checks if a number is prime.",
        "Write pytest tests for a function that checks if a number is prime.",
        model="codellama:7b"
    )