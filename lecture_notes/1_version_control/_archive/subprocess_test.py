import subprocess

magic_number_process = subprocess.run(
    ["git", "status"], check=True, capture_output=True, encoding="utf-8"
)
# print(magic_number_process.stdout)


# a = subprocess.check_output("git status", shell=True)
# print(a)
