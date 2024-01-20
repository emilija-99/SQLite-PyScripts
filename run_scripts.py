import subprocess

# Replace these with the actual paths to your scripts
script_paths = [
    'client_tables.py',
    'package_tables.py',
    'script_for_generate_table_client.py',
    'script_for_generate_table_package.py',
    'script_for_generate_table_TV_package.py',
    'script_for_generate_table_Internet_package.py',
    'script_for_generate_table_Combine_package.py'
]

def execute_scripts():
    for script_path in script_paths:
        print(f"Executing script: {script_path}")
        try:
            # Run the script using subprocess
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {script_path}: {e}")
            break

if __name__ == "__main__":
    execute_scripts()