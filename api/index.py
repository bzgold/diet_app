import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from main import app
except ImportError as e:
    print(f"Import error: {e}")
    # Fallback: try to import directly
    import importlib.util
    spec = importlib.util.spec_from_file_location("main", os.path.join(os.path.dirname(os.path.dirname(__file__)), "main.py"))
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    app = main_module.app

# Vercel serverless function handler

