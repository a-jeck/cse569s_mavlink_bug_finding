import argparse, pathlib, shutil, subprocess, sys, os

def run_and_move(exec_path, target_file, output_file):
    try:
        output_raw = subprocess.run(
            [str(exec_path), str(target_file)],
            text=False,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            check=False,
        )
    except FileNotFoundError as exc:
        print(f"Error launching {exec_path}: {exc}", file=sys.stderr)
        return False

    output = (output_raw.stdout + output_raw.stderr).decode("utf-8", errors="replace").lower()
    if "addresssanitizer" in output:
    #     print(f'testing {str(target_file)}')
    #     lines = output.split('\n')
    #     index = lines.index("=================================================================")
    #     print(lines[index+1])
        shutil.copy(str(target_file), os.path.join(output_file, "asan"))
    elif "undefinedbehaviorsanitizer" in output:
        print("undefined")
        shutil.copy(str(target_file), os.path.join(output_file, "ubsan"))
    else: 
        print("other")
        shutil.copy(str(target_file), os.path.join(output_file, "other"))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("exec_path", help="Path to the executable to run")
    parser.add_argument("input_folder", help="Folder containing input files")
    parser.add_argument("output_folder", help="Folder for outputs")
    args = parser.parse_args()

    exec_path = pathlib.Path(args.exec_path).expanduser().resolve()
    input_folder = pathlib.Path(args.input_folder).expanduser().resolve()
    output_folder = pathlib.Path(args.output_folder).expanduser().resolve()


    if not exec_path.is_file():
        sys.exit(f"Executable not found: {exec_path}")
    if not input_folder.is_dir():
        sys.exit(f"Input folder not found: {input_folder}")
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(os.path.join(output_folder, "asan"), exist_ok=True)
    os.makedirs(os.path.join(output_folder, "ubsan"), exist_ok=True)
    os.makedirs(os.path.join(output_folder, "other"), exist_ok=True)


    for entry in input_folder.iterdir():
        if entry.is_file():
            run_and_move(exec_path, entry, output_folder)



if __name__ == "__main__":
    main()
