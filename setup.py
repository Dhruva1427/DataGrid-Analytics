"""
Environment & Data Platform Initialization Script
==================================================
Configures dependencies, environment variables, initial data seeding,
and runs the transformation pipeline for initial boot.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_banner(step_title: str):
    print(f"\n{'='*50}\n{step_title}\n{'='*50}")

def check_python_version():
    print_banner("Verifying Python Runtime Environment")
    ver = sys.version_info
    print(f"Detected Python version: {sys.version}")
    if ver.major < 3 or (ver.major == 3 and ver.minor < 9):
        print("Error: Python 3.9+ runtime environment is required.")
        sys.exit(1)
    print("✅ Python environment verified")

def install_dependencies():
    print_banner("Installing Project Dependencies")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Python package requirements satisfied")
    except subprocess.CalledProcessError:
        print("❌ Failed to install required Python dependencies")
        sys.exit(1)

def setup_env_file():
    print_banner("Initializing Configuration Environment")
    env_file = Path(".env")
    if env_file.exists():
        print("✅ Environment configuration file .env present")
    else:
        print("⚠️ Environment config .env not found. Generating default template...")
        with open(".env", "w", encoding="utf-8") as handle:
            handle.write("OPENAI_API_KEY=your_key_here\n")
        print("✅ Generated .env file template. Please update with environment keys if needed.")

def run_data_generation():
    print_banner("Generating Initial Seed Dataset")
    try:
        subprocess.check_call([sys.executable, "src/ingestion/generator.py"])
        print("✅ Initial seed dataset generated")
    except subprocess.CalledProcessError:
        print("❌ Seed dataset generation encountered an error")

def run_pipeline():
    print_banner("Executing Multi-Stage Data Pipeline")
    try:
        subprocess.check_call([sys.executable, "src/transformation/pipeline.py"])
        print("✅ Data transformation pipeline finished successfully")
    except subprocess.CalledProcessError:
        print("❌ Data transformation pipeline encountered an error")

def main():
    print("🚀 Initializing Platform Environment Setup...")
    check_python_version()
    install_dependencies()
    setup_env_file()
    run_data_generation()
    run_pipeline()
    
    print_banner("Setup Complete!")
    print("To launch the platform components:")
    print("1. Backend API: python3 -m uvicorn api.main:app --reload")
    print("2. Frontend UI: cd frontend && npm install && npm run dev")

if __name__ == "__main__":
    main()

