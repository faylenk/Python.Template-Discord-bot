import os
import importlib

def loadEventHandlers(bot):
    event_path = "src.events"  
    base_dir = event_path.replace(".", "/")
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                relative_path = os.path.relpath(root, base_dir).replace("\\", ".").replace("/", ".")
                module_name = f"{event_path}{('.' + relative_path) if relative_path != '.' else ''}.{file[:-3]}"
                
                print(f"Loading module: {module_name}")
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, "setup"):
                        module.setup(bot)
                        print(f"Event Loaded: {module_name}")
                    else:
                        print(f"No setup function found in {module_name}")
                except Exception as e:
                    print(f"Error at loading {module_name}: {e}")