import argparse
import subprocess

def install_packages(packages):
    for package in packages:
        subprocess.check_call(['pip', 'install', package])

def main():
    parser = argparse.ArgumentParser(description="Install required Python packages.")
    
  
    parser.add_argument(
        '-p', '--packages', 
        nargs='+', 
        required=True, 
        help='List of Python packages to install'
    )
    
    args = parser.parse_args()
    
    install_packages(args.packages)

if __name__ == "__main__":
    main()
